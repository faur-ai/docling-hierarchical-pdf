import cProfile
import pstats
import json
from functools import cached_property
from io import BytesIO
from pathlib import PurePath
from pstats import SortKey
from typing import Optional, Union

from docling.datamodel.base_models import DocumentStream
from docling.datamodel.document import ConversionResult
from docling_core.types.doc.document import (
    DocItem,
    DocItemLabel,
    DoclingDocument,
    ListItem,
    NodeItem,
    RefItem,
    SectionHeaderItem,
    TextItem,
)

from hierarchical.hierarchy_builder import create_toc
from hierarchical.hierarchy_builder_metadata import HierarchyBuilderMetadata
from hierarchical.types.hierarchical_header import HierarchicalHeader


class DoclingResultNotReadyException(Exception):
    def __init__(self) -> None:
        super().__init__("It seems that the docling result has not been filled / is not ready for postprocessing.")


class ItemNotRegisteredAsChildException(Exception):
    def __init__(self, item: NodeItem):
        super().__init__(f"The item {item} does not seem to be registered as a child of its parent node!")


class ItemInconsitencyException(Exception):
    pass


def flatten_hierarchy_tree(node: HierarchicalHeader, parent_level: int = 0) -> list[tuple[HierarchicalHeader, int]]:
    children = []
    this_level = parent_level + 1
    for c in node.children:
        children.append((c, this_level))
        children.extend(flatten_hierarchy_tree(c, this_level))
    return children


def set_item_in_doc(doc: DoclingDocument, item: DocItem) -> None:
    _, path, index_str = item.self_ref.split("/")
    index = int(index_str)
    doc.__getattribute__(path)[index] = item
    item = item


class ResultPostprocessor:
    def __init__(
        self,
        result: ConversionResult,
        source: Optional[Union[PurePath, str, DocumentStream, BytesIO]] = None,
        raise_on_error: bool = False,
    ):
        self.result = result
        self.source = source
        self.raise_on_error = raise_on_error

    @cached_property
    def has_hierarchy_levels(self) -> bool:
        levels = set()
        for _, level in self.result.document.iterate_items():
            levels.add(level)

        return len(levels) > 1

    def _get_headers_result(self) -> list[dict]:
        items: list[dict] = []
        for item, _ in self.result.document.iterate_items():
            if not isinstance(item, SectionHeaderItem):
                continue
            prov = item.prov[0]
            page = self.result.pages[prov.page_no - 1]
            if page.predictions.layout is None:
                return items
            for cluster in page.predictions.layout.clusters:
                if not cluster or cluster.label != "section_header":
                    continue
                first_cell = cluster.cells[0]
                if page.size is None:
                    raise DoclingResultNotReadyException()
                if (
                    prov.bbox.intersection_area_with(
                        first_cell.rect.to_bounding_box().to_bottom_left_origin(page_height=page.size.height)
                    )
                    == first_cell.rect.to_bounding_box().area()
                ):
                    font_split = first_cell.font_name.split("-") if hasattr(first_cell, "font_name") else [""]
                    items.append({
                        "text": " ".join([cell.text for cell in cluster.cells]),
                        "font_size": first_cell.rect.height,
                        "is_bold": "Bold" in font_split[1] if len(font_split) > 1 else False,
                        "is_italic": "Italic" in font_split[1] if len(font_split) > 1 else False,
                        "top_left": first_cell.rect.r_y0,
                        "text_direction:": first_cell.text_direction,
                        "font": font_split[0],
                        "reference": item.self_ref,
                    })
                    break
        return items

    def _get_headers_document(self) -> list[dict]:
        items = []
        for item, _ in self.result.document.iterate_items():
            if isinstance(item, SectionHeaderItem):
                prov = item.prov[0]
                items.append({
                    "text": " ".join(item.text.split("\n")),
                    "font_size": prov.bbox.height,
                    "is_bold": False,
                    "is_italic": False,
                    "top_left": prov.bbox.t,
                    "text_direction:": None,
                    "font": "",
                    "reference": item.self_ref,
                })
        return items

    def get_headers(self) -> list[dict]:
        if not (items := self._get_headers_result()):
            return self._get_headers_document()
        return items

    def process(self, profile_output: Optional[str] = None) -> None:  # noqa: C901
        profile_file = open(profile_output, "w") if profile_output else None

        def write_profile(profiler: cProfile.Profile, step_name: str) -> None:
            if profile_file:
                profile_file.write(f"\n{'='*70}\n")
                profile_file.write(f"PROFILE: {step_name}\n")
                profile_file.write(f"{'='*70}\n")
                pstats.Stats(profiler, stream=profile_file).strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(10)
                profile_file.flush()

        # Step 1: HierarchyBuilderMetadata initialization
        # pr1 = cProfile.Profile()
        # pr1.enable()
        hbm = HierarchyBuilderMetadata(self.result, self.source, self.raise_on_error)
        # pr1.disable()
        # write_profile(pr1, "Step 1: HierarchyBuilderMetadata init")

        # Step 2: TOC inference or creation
        # pr2 = cProfile.Profile()
        # pr2.enable()
        header_correction = False
        if len(hbm.toc) > 0:
            root = hbm.infer()
            header_correction = True
        else:
            headings = self.get_headers()
            root = create_toc(headings)
        # pr2.disable()
        # write_profile(pr2, "Step 2: TOC inference/creation")
        with open(profile_output, "w") as f:
            f.write(str(hbm.toc))
        doc = self.result.document

        # Step 3: Flatten hierarchy tree
        # pr3 = cProfile.Profile()
        # pr3.enable()
        flat_hierarchy = flatten_hierarchy_tree(root, 0)

        with open(profile_output, "w") as f:
            json.dump(flat_hierarchy, f)
        # pr3.disable()
        # write_profile(pr3, "Step 3: flatten_hierarchy_tree")

        # Step 4: Build by_ref lookup
        # pr4 = cProfile.Profile()
        # pr4.enable()
        by_ref = {el[0].doc_ref: el for el in flat_hierarchy}
        # pr4.disable()
        # write_profile(pr4, "Step 4: by_ref lookup build")

        # Step 5: Main iteration loop (single pass for header leveling only)
        # pr5 = cProfile.Profile()
        # pr5.enable()
        current_header = root
        level = 0
        for item, _ in self.result.document.iterate_items(with_groups=True):
            # Convert SectionHeaderItem to TextItem if not in hierarchy
            if isinstance(item, SectionHeaderItem) and item.self_ref not in by_ref and header_correction:
                text_item = TextItem(
                    label=DocItemLabel.TEXT,
                    **{k: v for k, v in item.model_dump().items() if k != "label" and k in TextItem.model_fields},
                )
                set_item_in_doc(doc, text_item)
                item = text_item

            # Handle items that should be headers
            if item.self_ref in by_ref:
                if not isinstance(item, SectionHeaderItem):
                    if header_correction and isinstance(item, (TextItem, ListItem)):
                        header_item = SectionHeaderItem(**{
                            k: v
                            for k, v in item.model_dump().items()
                            if k != "label" and k in SectionHeaderItem.model_fields
                        })
                        if isinstance(item, ListItem):
                            header_item.text = header_item.orig
                        set_item_in_doc(doc, header_item)
                        item = header_item
                    else:
                        raise ItemInconsitencyException()
                current_header, level = by_ref[item.self_ref]
                item.level = level
            elif current_header.doc_ref is not None and isinstance(item, SectionHeaderItem):
                item.level = level + 1
        # pr5.disable()
        # write_profile(pr5, "Step 5: Main iteration loop")
        if profile_file:
            profile_file.close()
