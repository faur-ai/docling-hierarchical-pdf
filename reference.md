[1]----------------------






<--- Start description image 1 --->

This image depicts a vast rooftop solar panel array installed on a modern urban building, with a city skyline and construction crane visible in the background under a bright, sunlit sky. The scene symbolizes the integration of renewable energy infrastructure into contemporary urban environments, highlighting sustainable development and the transition toward clean power solutions in metropolitan areas. While the image itself is not directly related to the Cisco 1000 Series router hardware guide, it visually represents the kind of modern, scalable, and networked infrastructure that such networking equipment supports — powering and connecting the smart cities and data centers of the future. The guide’s publication and updates through 2024 underscore Cisco’s ongoing role in enabling the technological backbone for these evolving, energy-conscious urban landscapes.

<--- End description image 1 --->



# Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router


First Published: 2019-06-07

Last Modified: 2024-02-26



Americas Headquarters


Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 USA

http://www.cisco.com

Tel: 408 526-4000
800 553-NETS (6387)
Fax: 408 527-0883


[2]----------------------


THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The following information is for FCC compliance of Class A devices: This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio-frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference, in which case users will be required to correct the interference at their own expense.

The following information is for FCC compliance of Class B devices: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If the equipment causes interference to radio or television reception, which can be determined by turning the equipment off and on, users are encouraged to try to correct the interference by using one or more of the following measures:

• Reorient or relocate the receiving antenna.
• Increase the separation between the equipment and receiver.
• Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
• Consult the dealer or an experienced radio/TV technician for help.


Modifications to this product not authorized by Cisco could void the FCC approval and negate your authority to operate the product.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB's public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED "AS IS" WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies of this document are considered uncontrolled. See the current online version for the latest version.

Cisco has more than 200 offices worldwide. Addresses and phone numbers are listed on the Cisco website at www.cisco.com/go/offices.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: https://www.cisco.com/c/en/us/about/legal/trademarks.html. Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R)

© 2017-2023 Cisco Systems, Inc. All rights reserved.

[3]----------------------




<--- Start description image 2 --->

This panoramic image depicts a modern urban skyline viewed from a high vantage point, likely a rooftop, with the sun casting a warm, hazy glow over the scene. The foreground features a vast, tiled surface that reflects the light, leading the eye toward a dense cluster of skyscrapers and high-rise buildings. A construction crane is visible in the distance, symbolizing ongoing development and growth. The overall atmosphere is one of technological advancement and urban dynamism, aligning with the context of Cisco — a global leader in networking and IT infrastructure — suggesting a setting where its integrated services routers and technologies power the connectivity and operations of such modern cities. The image serves as a symbolic backdrop for Cisco’s enterprise solutions, emphasizing the scale and sophistication of the digital infrastructure that underpins contemporary urban environments.

<--- End description image 2 --->



C O N T E N T S


Overview of Cisco 1000 Series Integrated Services Routers 1 C H A P T E R 1


About Cisco 1000 Series Integrated Service Routers 1
Chassis Views 5

LED Indicators 14
Reset Button 23
Power Supply 23

Slots and Interfaces 24

About Slots, Subslots, and Port Numbering 24
Specifications of Cisco 1000 Series Integrated Services Routers 24
Periodic Inspection and Cleaning 24


Prepare for Router Installation 25 C H A P T E R 2
Safety Recommendations 25

Safety With Electricity 26
Prevent Electrostatic Discharge Damage 26
General Site Requirements 26

Site Selection Guidelines 27

Rack Requirements 27
Safety Recommendations 28
Power Guidelines and Requirements 28

Network Cabling Specifications 29

Console Port Considerations 29

EIA/TIA-232 29
USB Serial Console 29
Console Port Considerations 30

Prepare for Router Installation 30



[4]----------------------


Ethernet Connections 31

Required Tools and Equipment for Installation and Maintenance 31

C H A P T E R 3


Install and Connect the Router 33


Unpack the Router 33

Set up Router on Desktop, Rack, or Wall 33

Rack Mount 34

Attach the Rack Mount Brackets for C111x 35

Attach the C111x Top Plate (C1110-TOP-PLATE=) on Desktop 36

Attach the C111x Top Plate (C1110-TOP-PLATE=) for Rack Mount 38

Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) on Desktop 39

Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) for Rack Mount 43

Attach the Rack Mounting Brackets for C112x 44

Mount the Router 45

• Mount the Router under a Desk or a Shelf 46
• Mount Router using DIN Rail Brackets 48


Attach Din-Rail Brackets on C112x 48

Wall Mount the Router 49

• Wall Mount Using Key-hole Slots 50


Wall Mount using DIN Rail Brackets 57

• Chassis Grounding 59


Connect Power Cable 61

Connect the Router to a Console 63

Connect to the Serial Port with Microsoft Windows 65

Connect to the Console Port with Mac OS X 66

Connect to the Console Port with Linux 66

• Install the Silicon Labs USB Device Driver 67


Install the Silicon Labs Windows USB Device Driver 67

Install the Silicon Labs Mac USB Device Driver 67

Connect WAN and LAN Interfaces 68

• Ports and Cabling 68


Connection Procedures and Precautions 69

Configure the Router at Startup 69

[5]----------------------


Install and Upgrade Internal Modules and Field Replaceable Units 71 C H A P T E R 4 Replace the Chassis Covers for C111X and C1111x 71 Remove the Cover 72 Replace the Cover 73 External Modules 74 Locate External Slots for Modules 74 Install and Remove Small Form Pluggable Modules 75 Install Small Form Pluggable Module 75 Remove Small Factor Pluggable Module 75 Install a Pluggable Interface Module 76 Install a Pluggable Interface Module on a C1101-4P 76 Configuring a Pluggable Interface Module 84 RF Band Mapping for Antenna Ports (For P-5GS6-GL and P-5GS6-R16SA-GL) 86 LED Behaviors 89 Attaching the Antennas 90 Install a Micro-SIM Card into a USB LTE Dongle 92 Antenna Mounting Instructions 94 Rack Mount of the Antenna 94 Wall Mount of the Antenna 96 Ceiling Mount of the Antenna 98 Installing a SIM Card on C111X, C1109-2PX, C1109-4P 100 Installing a Nano-SIM Card into a Nano-To-Micro-SIM Adapter 103 ROMMonitor Overview 105 C H A P T E R 5 ROMMonitor Overview 105 Supplier Declaration of Conformity 107 C H A P T E R 6

[6]----------------------


[7]----------------------




<--- Start description image 3 --->

Based on the provided context, which is a "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router," the image serves as the chapter opener for the first chapter of this technical manual.

The image itself is a photograph of a modern city skyline, viewed from a high vantage point like a rooftop or elevated walkway. The sun is low in the sky, creating a bright lens flare and casting long shadows, which suggests either early morning or late afternoon. The foreground is a reflective, tiled surface, and the background is filled with a mix of completed skyscrapers and a construction crane, symbolizing growth, connectivity, and the infrastructure that modern businesses and networks depend on.

The large, bold text "CHAPTER 1" at the bottom clearly indicates the start of the guide's first section.

**Comprehensive Caption:**

**Chapter 1: Introduction to the Cisco 1000 Series Integrated Services Router**

This chapter opens the Hardware Installation Guide with a powerful visual metaphor: a panoramic view of a dynamic, modern cityscape. The image, featuring towering buildings and a construction crane against a bright, sunlit sky, symbolizes the urban, high-performance environment where these routers are deployed. It visually reinforces the router's purpose as a foundational piece of infrastructure that powers and connects the digital world, enabling services like Internet access, security, and wireless connectivity for businesses and networks. The chapter will introduce the Cisco 1000 Series Integrated Services Routers, highlighting their ease of deployment and management, and setting the stage for the detailed installation procedures that follow.

<--- End description image 3 --->



# Overview of Cisco 1000 Series Integrated Services Routers


Cisco 1000 Series Integrated Services Routers with Cisco IOS XE Software are high-performance devices that are easy to deploy and manage. The routers combine Internet access, comprehensive security, and wireless services (LTE Advanced 3.0, Wireless WAN and Wireless LAN).

• About Cisco 1000 Series Integrated Service Routers, on page 1
• Periodic Inspection and Cleaning, on page 24


## About Cisco 1000 Series Integrated Service Routers


The Cisco 1000 Series Integrated Services Routers are the next generation, IOS XE-based, multi core, branch routers. They are available in both fixed and modular form factors. The Cisco 1000 Series Integrated Services Routers is best suited for small and midsize businesses, enterprise branches, and as customer premises equipment in managed services environments.

| Base Models | Front Panel Switch Ports | WAN Ports | Console Port | (Optional) POE | (Optional) WLAN | (Optional) LTE | (Optional) DSL |
|------|------|------|------|------|------|------|------|
| C111x-8P | 8 | 2 (1 Combo RJ-45/SFP + 1 RJ-45) | Serial RJ-45, Micro USB | 4PoE/2PoE+ | None | 4G LTE-Advanced (CAT6) with carrier aggregation | G.FAST, VDSL2 and ADSL2/2+ |
| C1111X-8P | 8 | 2 (1 Combo RJ-45/SFP + 1 RJ-45) | Serial RJ-45, Micro USB | 4PoE/2PoE+ | None | None | None |
| C111x-4P | 4 | 2 (1 Combo RJ-45/SFP + 1 RJ-45) | Serial RJ-45, Micro USB | 2 POE/1 POE+ | 802.11ac WAVE 2 | 4G LTE-Advanced (CAT6) with carrier aggregation | VDSL2 and ADSL2/2+ |
| C1104PLTEPWx | 4 | 1 RJ-45 | Micro USB | None | 802.11ac WAVE 2 (
C1104PLTEPWx
) | 4G pluggable LTE (CAT 4) and pluggable LTE Advanced (CAT 6) with carrier aggregation | None |
| C1101-4P | 4 | 1 RJ-45 | Micro USB | None | None | None | None |
| C1109-2PLTE | 2 | 1 RJ-45 | Micro USB | None | None | 4G LTE (CAT 4) | None |
| C1109-4PLTE2P | 4 | 1 RJ45 | Micro USB | None | 802.11ac WAVE 2 (
C1104PLTE2P
) | Dual pluggable modems - 4G pluggable LTE (CAT 4) and pluggable LTE Advanced (CAT 6) with carrier aggregation | None |
| C1121-4P | 4 | 2(1 Combo RJ45/SFP+1 RJ45 | Micro USB | 2 POE/1 POE+ | None | None | None |
| C1121-4PLTEP | 4 | 2(1 Combo RJ45/SFP+1 RJ45 | Micro USB | 2 POE/1 POE+ | None | 4G Pluggable LTE (CAT 4) and pluggable LTE Advanced (CAT 6) with carrier aggregation | None |
| C11x1(X)-8P * | 8 | 2(1 Combo RJ45/SFP+1 RJ45 | Micro USB | 4 POE/2 POE+ | None | None | None |
| C11x1(X)-8PLTEP * | 8 | 2(1 Combo RJ45/SFP+1 RJ45 | Micro USB | 4 POE/2 POE+ | None | 4G Pluggable LTE (CAT 4) and pluggable LTE Advanced (CAT 6) with carrier aggregation | VDSL2, ADSL2/2+, G.SHDSL |
| C112X8H1FWx | 8 | 2(1 Combo RJ45/SFP+1 RJ45 | Micro USB | 4 POE/2 POE+ | 802.11 AC WAVE 2 | 4G Pluggable LTE (CAT 4) and pluggable LTE Advanced (CAT 6) with carrier aggregation | None |
| C113X8H1FWx
C11318H1FWx | 8 | 2x L3 Gigabit RJ45/SFP Combo | Serial RJ45 | 4 POE/2 POE+ | 802.11 AX WiFi 6 | 5G Plugabble LTE | None |
| C1131X-8PWx
C1131-8PWx | 8 | 2x L3 Gigabit RJ45/SFP Combo | Serial RJ45 | 4 POE/2 POE+ | 802.11 AX WiFi 6 | None | None |


<--- Start caption table 0 --->

Table 1: Base Models of the Cisco 1000 Series Integrated Services Routers

<--- End caption table 0 --->



<--- Start description table 0 --->

Table caption: Overview of hardware specifications and features for the Cisco 1000 Series Integrated Services Routers, including form factors, use cases, and suitability for small to midsize businesses, enterprise branches, and managed services environments.

<--- End description table 0 --->






[10]----------------------


| Pluggable Interface Modules | Pluggable Interface Modules Technology |
|------|------|
| P-LTE-GB | CAT4 LTE Pluggable Europe SMS/GPS |
| P-LTE-GB= | CAT4 LTE Pluggable Europe SMS/GPS |
| P-LTE-IN | CAT4 LTE Pluggable India and China |
| P-LTE-IN= | CAT4 LTE Pluggable India and China |
| P-LTE-JN | CAT4 LTE Pluggable Japan |
| P-LTE-JN= | CAT4 LTE Pluggable Japan |
| P-LTE-NA | CAT4 LTE Pluggable for North America |
| P-LTE-NA= | CAT4 LTE Pluggable for North America |
| P-LTE-US | CAT4 LTE Pluggable for United States |
| P-LTE-US= | CAT4 LTE Pluggable for United States |
| P-LTE-VZ | CAT4 LTE Pluggable Verizon |
| P-LTE-VZ= | CAT4 LTE Pluggable Verizon |
| P-LTEA-EA | CAT6 LTE Advanced Pluggable for Europe and North America |
| P-LTEA-EA= | CAT6 LTE Advanced Pluggable for Europe and North America |
| P-LTEA-LA | CAT6 LTE Advanced Pluggable for APAC, LATAM, and ANZ |
| P-LTEA-LA= | CAT6 LTE Advanced Pluggable for APAC, LATAM, and ANZ |
| P-LTEAP18-GL | CAT6 LTE Advanced PRO Pluggable for ALL Global Regions |
| P-LTEAP18-GL= | CAT6 LTE Advanced PRO Pluggable for ALL Global Regions |
| P-5GS6-GL | 5G Sub-6 GHz Pluggable Interface Module |
| P-5GS6-R16SA-GL | 5G Sub-6 GHz Pluggable Interface Module |
| P-LTEA7-NA | CAT7 LTE Pluggable for North America |
| P-LTEA7-JP | CAT7 LTE Advanced PIM for Japan |
| P-LTEA7-EAL | CAT7 LTE Advanced PIM for EMEA, APAC, LATAM |


<--- Start caption table 1 --->

Table 2: Pluggable Modules of the Cisco 1000 Series Integrated Services Routers

<--- End caption table 1 --->



<--- Start description table 1 --->

Table caption: Overview of hardware specifications and features for the Cisco 1000 Series Integrated Services Routers, including key components and installation considerations.

<--- End description table 1 --->



[11]----------------------


目



Note


P-5GS6-GL is supported on C8300, C8200, C8200L, and Cisco 1000 Series Integrated Service Routers.

P-5GS6-GL is supported on Cisco 1000 Series Integrated Service Routers from the Cisco IOS XE 17.9.2 release.

目



Note


Base Models with an 'X' has 8GB of DRAM and Flash memory. Example: C1111X-8P

The C1131 models have 4GB of DRAM and 8G flash memory.

The C1131X models have 8GB of DRAM and 16G flash memory.

For the C1131 series, only the Class A statements in the Trademark notice, which is available at the beginning of this guide, is valid.

Base Models without an 'X' have 4GB of DRAM and Flash Memory. Example: C1111-8P

For base model-C11x1X-8PLTEP, 'x' represents the CPU performance level.

For more information on the features and specifications of Cisco 1000 Series Integrated Services Routers, refer to the Cisco 1000 Series Integrated Services Routers Solution Overview document and Cisco 1000 Series Integrated Services Routers datasheet.

### Chassis Views


目



Note


The compliance label is present at the bottom of the product.

This section contains front and back panel views of the Cisco 1000 Series Integrated Services Routers showing locations of the power and signal interfaces, interface slots, status indicators, and chassis identification labels.



<--- Start caption image 7 --->

Figure 1: C111x Series - Bezel View

<--- End caption image 7 --->



<--- Start description image 7 --->

This diagram is a front panel layout guide for the Cisco 1000 Series Integrated Services Router, illustrating the key physical components and indicator locations on the router’s front faceplate. It is designed to assist technicians and users in identifying and accessing critical interfaces and status indicators during installation, configuration, or troubleshooting.

**Key Components and Their Significance:**

*   **1. Status Indicators (LEDs):** A row of indicator lights that provide real-time visual feedback on the router’s operational state, including power, system health, and network activity. These are essential for diagnosing issues at a glance.
*   **2. VPN Indicator:** A dedicated LED or indicator for the Virtual Private Network (VPN) service, signaling the status of VPN connections or related services.
*   **3. Wi-Fi Indicator:** An LED that indicates the status of the built-in Wi-Fi radio, showing whether it is active and connected to a wireless network.
*   **4. GPS Indicator:** An LED that indicates the status of the Global Positioning System (GPS) module, which is used for location-based services or time synchronization.
*   **5. LTE Signal Intensity Indicator:** A visual indicator (often a bar graph) that displays the strength of the LTE cellular signal, helping users assess connectivity quality.
*   **6. LTE Data/SIM Indicator:** An LED that indicates the status of the LTE data connection and the SIM card, showing whether the cellular module is registered and active.
*   **7. Illuminated Cisco Logo:** A branded, lit-up logo that serves as a visual identifier for the device and may also function as a power-on indicator or status light in some models.

**Purpose and Context:**
This diagram is part of the *Hardware Installation Guide* for the Cisco 1000 Series router. Its purpose is to provide a clear, visual reference for users to locate and understand the functions of each front panel element. This is crucial for proper setup, maintenance, and troubleshooting, ensuring users can quickly identify the status of critical services like Wi-Fi, GPS, and LTE connectivity, as well as the overall system health. The note at the top confirms that this is a front and back panel view, and the compliance label is located at the bottom of the product, as required by regulatory standards.

<--- End description image 7 --->



| 1 | Status | 2 | VPN |
|------|------|------|------|
| 3 | Wi-Fi | 4 | GPS |
| 5 | LTE signal intensity | 6 | LTE data/SIM |
| 7 | Illuminated Cisco logo |  |  |


<--- Start description table 2 --->

This table provides front and back panel views of the Cisco 1000 Series Integrated Services Router, highlighting the locations of power and signal interfaces, interface slots, status indicators, and chassis identification labels, as part of the hardware installation guide.

<--- End description table 2 --->



[12]----------------------




<--- Start caption image 8 --->

Figure 2: C111x-8P - I/O View

<--- End caption image 8 --->



<--- Start description image 8 --->

This is a detailed front-view diagram of the Cisco 1000 Series Integrated Services Router chassis, serving as a comprehensive labeling guide for technicians and users. The image systematically identifies and numbers 18 key physical components and ports on the router's front panel, enabling accurate identification and configuration.

**Key Components and Their Functions:**

*   **Connectivity Ports (1-18):** The diagram highlights a wide array of interfaces for network and service connections, including:
    *   **Wireless:** LTE antennas (1) for cellular connectivity.
    *   **Wired Ethernet:** Multiple Gigabit Ethernet (GE) ports, including RJ45 (11) and SFP (12) slots for fiber or copper connections.
    *   **Serial & Console:** A console port (16) for initial setup and management, and a serial port (15) for LTE provisioning.
    *   **Power:** A 4-pin power connector (9) and a power switch (8) for powering the device.
    *   **Management & Debugging:** A USB 3.0 port (13) for software updates or data transfer, and a reset button (7) for factory defaults.
    *   **Security & Identification:** A Kensington lock slot (18) for physical security, and labels for the Serial Number (5), CLEI label (4), and Product Identification Number (19) for asset tracking.

*   **Chassis Structure:** The diagram also shows the physical layout, including the upper and lower slots (14) for modular expansion, and the GPS connection (3) for location-based services.

**Significance:**
This diagram is an essential reference for network administrators and engineers. It provides a clear, visual map of the router's front panel, ensuring correct cable management, troubleshooting, and hardware installation. By clearly labeling each component, it minimizes configuration errors and facilitates efficient maintenance and support for the Cisco 1000 Series routers.

<--- End description image 8 --->



|  |  |  |  |
|------|------|------|------|
| 1 | LTE antennas – main and diversity | 2 | Ethernet switch |
| 3 | GPS connection | 4 | CLEI label |
| 5 | Serial number | 6 | Grounding |
| 7 | Reset button | 8 | Power switch |
| 9 | 4-pin power connector | 10 | GE 0/0/1 |
| 11 | GE 0/0/0 - RJ45 | 12 | GE 0/0/0 - SFP |
| 13 | USB3.0 | 14 | Lower slot0
Upper slot1 |
| 15 | LTE provisioning port | 16 | RJ45/Micro USB console |
| 17 | DSL | 18 | Kensington lock slot |
| 19 | Product Identification Number (PID) |  |  |


<--- Start description table 3 --->

Caption: This table provides an overview of the chassis views for the Cisco 1000 Series Integrated Services Routers, illustrating the physical and structural components as seen from different angles.

<--- End description table 3 --->



目



Note

For more information on the Reset Button, refer to the Reset Overview section in the ISR 1000 Series Integrated Services Routers.

[13]----------------------




<--- Start caption image 10 --->

Figure 3: C1101-4P ISR - Front View

<--- End caption image 10 --->



<--- Start description image 10 --->

This is a detailed diagram illustrating the front panel of a Cisco 1000 Series Integrated Services Router (ISR), specifically highlighting component #1: the non-illuminated Cisco logo.

**Caption:**
*Front Panel Component Identification: The diagram provides a close-up view of the front bezel of a Cisco 1000 Series ISR, clearly labeling the non-illuminated Cisco logo (labeled as #1) located centrally above the model designation "ISR 1000 Series." This component serves as a brand identifier on the device's chassis. The diagram is part of a larger reference guide that systematically identifies all front-panel elements, including the Kensington lock slot, power switch, network ports, and console/USB interfaces, to assist technicians in device identification and maintenance.*

**Key Insights:**
*   **Component Focus:** The image isolates and labels the Cisco logo, which is a standard branding element on network hardware.
*   **Contextual Placement:** The logo is positioned centrally on the chassis, directly above the model name, a common design practice for clear product identification.
*   **Part of a Larger Guide:** This is not a standalone image but a specific callout from a comprehensive "Overview of Cisco 1000 Series Integrated Services Routers Chassis Views" document, which provides a complete reference for all physical components on the device's front panel.

<--- End description image 10 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 4 --->

This table provides an overview of the chassis components and features of the Cisco 1000 Series Integrated Services Routers, listing key physical elements such as the Kensington lock slot, grounding point, power switch, reset button, WAN ports, LAN ports, USB 3.0 port, and console connection via micro USB.

<--- End description table 4 --->





<--- Start caption image 11 --->

Figure 4: C1101-4P ISR - I/O View

<--- End caption image 11 --->



<--- Start description image 11 --->

This is a detailed front-view diagram of a Cisco network device chassis, likely a router or switch, serving as a reference guide for identifying key physical components and their locations.

The diagram labels nine primary features on the device's front panel:

*   **1. Non-illuminated Cisco logo:** The brand identifier, which is not lit.
*   **2. Kensington lock slot:** A security feature for physically securing the device to a desk or rack.
*   **3. Power switch:** A physical button to turn the device on or off.
*   **4. 4-pin power connector:** The input port for connecting the device's power supply.
*   **5. Reset button:** A button to restore the device to its factory default settings.
*   **6. LAN ports (0-4):** A row of five Ethernet ports for connecting to local area network devices.
*   **7. GE WAN port:** A Gigabit Ethernet port for connecting to a Wide Area Network, typically for internet or WAN connectivity.
*   **8. Micro USB console port:** A port for connecting a console cable to access the device's command-line interface (CLI) for configuration and troubleshooting.
*   **9. USB 3.0 port:** A high-speed USB port for connecting peripherals or for device management.

This diagram is essential for technicians and administrators to correctly identify and interact with the device's physical interfaces during installation, configuration, or maintenance.

<--- End description image 11 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Kensington lock slot | 2 | Grounding |
| 3 | Power switch | 4 | 4-pin power connector |
| 5 | Reset button | 6 | LAN: 0-4 |
| 7 | GE WAN | 8 | Micro USB console |
| 9 | USB3.0 |  |  |


<--- Start description table 5 --->

The table indicates the title page of the Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router, featuring a non-illuminated Cisco logo and the document identifier "1."

<--- End description table 5 --->





<--- Start caption image 12 --->

Figure 5: C1101-4PLTEP-Bezel View

<--- End caption image 12 --->



<--- Start description image 12 --->

This is a close-up diagram from the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 7," specifically highlighting component #1: the non-illuminated Cisco logo.

**Description and Significance:**
The image displays the front panel of a Cisco ISR 1100 Series router, with a clear, labeled pointer indicating the Cisco logo. The logo is presented as a simple, non-illuminated (non-backlit) graphic, which is typical for this model series. The text "ISR 1100 Series" is visible to the left of the logo, identifying the product family. The number "355586" is printed on the right side, likely serving as a model or revision identifier.

**Contextual Relevance:**
This diagram is part of a larger set of illustrations intended to guide technicians through the physical installation and identification of components on the router. While this specific image focuses only on the logo, it is the first in a numbered list (as seen in the surrounding context) that details all front-panel features, including the Kensington lock slot, power switch, network ports, and console port. The purpose is to ensure accurate identification and proper handling during setup or maintenance.

In summary, this image serves as a reference point for locating and identifying the manufacturer's branding on the router's front panel, which is essential for inventory, documentation, and technical support purposes.

<--- End description image 12 --->



|  |  |
|------|------|
| 1 | Non-illuminated Cisco logo |


<--- Start description table 6 --->

This table outlines the hardware components and their corresponding labels or identifiers for the Cisco 1000 Series Integrated Services Router 7, providing a reference for proper installation and identification of key physical features such as power, networking, and connectivity ports.

<--- End description table 6 --->



[14]----------------------




<--- Start caption image 13 --->

Figure 6: C1101-4PLTEP - I/O View

<--- End caption image 13 --->



<--- Start description image 13 --->

This diagram provides a detailed, labeled overview of the front panel components of a Cisco 1000 Series Integrated Services Router (ISR) chassis, specifically the C1000-1 model. It serves as a technical reference guide for network administrators and technicians to identify and interact with the router's physical interfaces and controls.

**Key Components and Their Functions:**

*   **1. Power Switch (Labeled "1"):** A rocker switch used to turn the router on and off.
*   **2. 4-Pin Power Connector (Labeled "2"):** The input port for the 12V DC power supply, with a current rating of 2.8A.
*   **3. Reset Button (Labeled "3"):** A small button used to reset the router to its factory default configuration.
*   **4. LAN Ports (Labeled "4"):** A set of five 10/100/1000 Ethernet ports (LAN:0-4) for connecting to local area network devices.
*   **5. GE WAN Port (Labeled "5"):** A single Gigabit Ethernet port (GE WAN) for connecting to a wide area network, such as the internet.
*   **6. Micro-USB Console Port (Labeled "6"):** A port for connecting a console cable to access the router's command-line interface (CLI) for configuration and troubleshooting.
*   **7. Pluggable Module Slot (Labeled "7"):** A slot for inserting a pluggable module, such as a service module or a wireless module, to expand the router's functionality.
*   **8. Grounding Terminal (Labeled "8"):** A terminal for connecting the router to a grounding wire to ensure electrical safety.
*   **9. Kensington Lock Slot (Labeled "9"):** A slot for attaching a Kensington security lock to physically secure the router in place.

**Significance:**

This diagram is essential for proper installation, configuration, and maintenance of the Cisco 1000 Series ISR. It allows users to correctly connect power, network cables, and peripherals, and to perform hardware-level troubleshooting. The presence of a non-illuminated Cisco logo and main/diversity antenna (as noted in the context) further confirms this is a physical device diagram, not a software interface or a chart. The diagram's purpose is to provide a clear, visual reference for the physical layout of the router's front panel.

<--- End description image 13 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Power switch | 2 | 4-pin power connector |
| 3 | Reset button | 4 | LAN:0-4 |
| 5 | GE WAN | 6 | Micro-USB console port |
| 7 | Pluggable | 8 | Grounding |
| 9 | Kensington lock slot |  |  |


<--- Start description table 7 --->

The table provides a labeled overview of the chassis views of the Cisco 1000 Series Integrated Services Routers, identifying key components such as the non-illuminated Cisco logo and the main and diversity antennas.

<--- End description table 7 --->





<--- Start caption image 14 --->

Figure 7: C1109-2PLTE - Bezel View

<--- End caption image 14 --->



<--- Start description image 14 --->

This image is a close-up diagram of the front panel of a Cisco ISR 1100 Series router, specifically highlighting its physical labeling and key components. The diagram serves as a reference guide for users to identify and locate critical ports and features on the device chassis.

**Key Components and Their Significance:**

*   **Cisco Logo (1):** The central, non-illuminated Cisco logo is a brand identifier. Its non-illuminated state indicates this is likely a non-rackmount or non-optimized model, as illuminated logos are common on higher-end or rack-mounted devices.
*   **Antenna Connectors (2):** The two circular connectors, labeled as "2" on both ends, are for the main and diversity antennas. These are essential for wireless communication, allowing the router to establish and maintain robust Wi-Fi or cellular connections. The presence of two antennas suggests support for MIMO (Multiple Input, Multiple Output) technology, which improves signal strength and data throughput.
*   **Device Identification:** The text "ISR 1100 Series" clearly identifies the product family, which is a line of integrated services routers designed for small and medium-sized businesses, offering routing, switching, and wireless capabilities in a single device.

**Overall Purpose:**
This diagram is a technical reference for network administrators or technicians. It provides a clear, labeled view of the router's front panel to ensure correct identification and connection of antennas, which is crucial for proper wireless functionality. The non-illuminated logo and antenna design suggest this is a cost-effective, entry-level model focused on core networking tasks.

<--- End description image 14 --->



|  |  |
|------|------|
| 1 | Non-illuminated Cisco logo |
| 2 | Main and diversity antenna |


<--- Start description table 8 --->

The table compares the physical ports and features of a device in two different configurations, showing how components such as the power switch, reset button, LAN ports, USB connections, and SIM slots are arranged across two layouts. It highlights variations in port placement and labeling, such as the shift from LAN:0-4 to LAN:0 & 1, and the inclusion of a USB 3.0 port in one configuration but not the other. This suggests a comparison between a standard and an updated or alternative version of the device's hardware layout.

<--- End description table 8 --->





<--- Start caption image 15 --->

Figure 8: C1109-2PLTE - I/O View

<--- End caption image 15 --->



<--- Start description image 15 --->

This image is a detailed rear-view diagram of a Cisco wireless access point, specifically the model CT100-2PLTE3, providing a comprehensive labeling of its physical ports and connectors for installation and maintenance.

**Key Components and Their Functions:**

*   **Power and Control (Left Side):**
    *   **1. Kensington Lock Slot (1):** A security slot for attaching a cable lock to prevent theft.
    *   **2. Grounding (2):** A terminal for connecting the device to a building's electrical ground for safety.
    *   **3. Reset Button (3):** A small button used to restore the device to factory default settings.
    *   **4. Power Switch (4):** A physical switch to turn the device on or off.
    *   **5. 4-pin Power Connector (5):** Accepts a 12V DC power supply (2.5A) to power the device.

*   **Network and Management (Center):**
    *   **6. LAN Ports (6):** Two Ethernet ports for connecting to local network switches or other devices.
    *   **7. GE WAN Port (7):** A Gigabit Ethernet port for connecting to the Wide Area Network (e.g., the internet or a central router).
    *   **8. Micro-USB Console Port (8):** A port for direct console access using a USB-to-serial adapter, typically for initial configuration or troubleshooting.

*   **Wireless and Expansion (Right Side):**
    *   **9. Pluggable Antennas (9):** Slots for inserting external antennas to enhance wireless signal strength and range.
    *   **10. Micro-SIM Slots (10):** Two slots for inserting SIM cards, enabling the device to connect to a cellular network for backup or remote management.

**Significance:**
This diagram is an essential reference for network administrators and technicians. It clearly identifies all physical interfaces, which is critical for:
*   **Installation:** Correctly connecting power, network cables, and antennas.
*   **Troubleshooting:** Locating the reset button or console port to recover from configuration issues.
*   **Security:** Using the Kensington lock to secure the device in a fixed location.
*   **Management:** Utilizing the console port for initial setup or the SIM slots for cellular connectivity.

The diagram's layout and labeling ensure that users can quickly and accurately identify each component, facilitating efficient deployment and maintenance of the wireless access point.

<--- End description image 15 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Kensington lock slot | 2 | Grounding |
| 3 | Reset button | 4 | Power switch |
| 5 | 4-pin power connector | 6 | LAN: 0 & 1 |
| 7 | GE WAN | 8 | Micro-USB console port |
| 9 | USB 3.0 | 10 | Micro-SIM slots 0 and 1 |


<--- Start description table 9 --->

This table outlines the physical components and labeling of a Cisco networking device, including ports and features such as grounding, power switches, reset buttons, LAN and WAN connections, USB ports, antenna placements, and physical security options like a Kensington lock slot.

<--- End description table 9 --->







<--- Start caption image 16 --->

Figure 9: C1109-4PLTE2PWX - I/O View

<--- End caption image 16 --->



<--- Start description image 16 --->

This image displays the front and rear I/O panel diagrams for the Cisco C1121-4Px, a compact, enterprise-grade wireless router or access point designed for small to medium business networks. The diagrams provide a comprehensive, labeled overview of all physical ports, buttons, and connectors, essential for installation, configuration, and maintenance.

**Front Panel (Bezel View - Figure 10):**
This view shows the user-accessible controls and connectivity ports on the device’s front face.
*   **1. Grounding:** A grounding screw terminal for connecting the device to a building’s electrical ground to ensure safety and reduce electromagnetic interference.
*   **2. Power Switch:** A physical toggle switch to turn the device on or off.
*   **3. Reset Button:** A small button used to restore the device to its factory default settings, typically required for troubleshooting or initial setup.
*   **4. 4-pin Power Connector:** A standard connector for supplying DC power to the device.
*   **5. LAN Ports (0-4):** A set of five Ethernet ports for connecting wired client devices or other network equipment.
*   **6. GE WAN:** A Gigabit Ethernet WAN port for connecting to the primary internet service provider (ISP) or upstream network.
*   **7. USB 3.0 Port:** A high-speed USB port for connecting peripherals like storage devices or for firmware updates.
*   **8. Micro-USB Console Port:** A port for connecting a console cable to access the device’s command-line interface (CLI) for advanced configuration and troubleshooting.
*   **9. LTE Antenna:** An external antenna port for connecting an LTE/4G cellular antenna to enable mobile broadband connectivity.
*   **10. Kensington Lock Slot:** A security slot to physically secure the device to a desk or rack using a standard Kensington lock.

**Rear Panel (I/O View - Figure 11):**
This view details the connectivity options on the device’s back, which are typically more extensive for network connectivity.
*   **1. Reset Button:** A second reset button, often located for easier access from the rear.
*   **2. Power Switch:** A second power switch, providing redundancy or an alternative access point.
*   **3. 4-pin Power Connector:** A second power connector, likely for redundancy or a different power source.
*   **4. Ethernet Switch:** A switch or port for managing or connecting to a network switch.
*   **5. RJ-45 Stacked Connector:** A port for stacking multiple devices together for increased capacity or redundancy.
*   **6. GE WAN 0/0/0 - RJ45:** A specific Gigabit Ethernet WAN port, likely for a dedicated connection.
*   **7. GE WAN 0/0/0 - SFP:** An SFP (Small Form-factor Pluggable) port for connecting fiber optic cables, enabling high-speed, long-distance WAN connections.
*   **8. Micro-USB Console:** A second console port, providing an alternative for CLI access.
*   **9. USB 3.0 Port:** A second USB 3.0 port, offering additional peripheral connectivity.
*   **10. Kensington Lock Slot:** A second security slot for physical protection.
*   **11. Grounding:** A second grounding terminal, ensuring safety and stability.

**Significance:**
The diagrams are critical for network administrators and technicians. They provide a clear reference for connecting cables, powering the device, accessing the console, and securing it. The presence of both wired (Ethernet, USB) and wireless (LTE) connectivity options, along with multiple WAN and LAN ports, indicates this device is designed for flexible, robust network deployment in environments requiring both wired infrastructure and mobile broadband backup. The inclusion of SFP ports suggests support for fiber optic connections, making it suitable for enterprise or campus networks. The dual front and rear views ensure that all ports are accessible and identifiable regardless of the device’s orientation.

<--- End description image 16 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Grounding | 2 | Power switch |
| 3 | Reset button | 4 | 4-pin power connector |
| 5 | LAN:0-4 | 6 | GE WAN |
| 7 | USB 3.0 | 8 | Micro-USB console port |
| 9 | LTE antenna | 10 | Kensington lock slot |


<--- Start description table 10 --->

The table compares two different configurations of a network device's physical ports and connectors, labeling each with a unique identifier. The first configuration includes components such as a Kensington lock slot, reset button, power switch, 4-pin power connector, LAN ports, GE WAN interfaces, micro-USB console port, and micro-SIM slots. The second configuration features a non-illuminated Cisco logo, reset button, power switch, 4-pin power connector, RJ-45 stacked connector, GE WAN with SFP and RJ45 options, micro-USB console port, USB 3.0, and a Kensington lock slot, along with grounding. The differences highlight variations in port assignments and connectivity options between the two setups.

<--- End description table 10 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 11 --->

The table compares two different configurations of a network device's physical ports and connectors, showing the labeling and corresponding components in two distinct setups. The first column lists numbered positions, while the second and fourth columns detail the components in each configuration. The first configuration includes items such as grounding, power switch, reset button, LAN ports, USB 3.0, LTE antenna, and Kensington lock slot. The second configuration shows variations like a 4-pin power connector, Ethernet switch, RJ-45 stacked connector, GE WAN ports with different interface types (RJ45 and SFP), and maintains the same grounding and lock slot. This comparison highlights differences in port assignments and connectivity options between two possible device configurations.

<--- End description table 11 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | RJ-45 stacked connector | 6 | GE WAN 0/0/0 -RJ45 |
| 7 | GE WAN 0/0/0 -SFP | 8 | Micro-USB console |
| 9 | USB 3.0 | 10 | Kensington lock slot |
| 11 | Grounding |  |  |


<--- Start description table 12 --->

The table presents two different configurations of port and connector labels on a network device, likely a router or switch, showing variations in labeling for components such as power, Ethernet, USB, and connectivity ports. The first section lists physical ports with their corresponding identifiers and descriptions, while the second section provides an alternative labeling scheme, including details like Ethernet interfaces, WAN connections, and physical port types. The differences highlight variations in port naming or configuration across models or versions.

<--- End description table 12 --->







<--- Start caption image 17 --->

Figure 12: C1121-4PLTEP I/O View

<--- End caption image 17 --->



<--- Start description image 17 --->

This image is a detailed rear-view diagram of a Cisco network device, likely a router or switch model C121-4G-LP, illustrating its physical interface and control components. The diagram serves as a reference guide for technicians and users to identify and connect various ports and controls.

**Key Components and Their Functions:**

*   **1. Non-illuminated Cisco Logo:** The brand identifier for the device.
*   **2. Reset Button:** A small button used to restore the device to its factory default settings, typically by holding it down for a few seconds.
*   **3. 4-pin Power Connector:** The input port for the device's power supply, accepting a 12V-24A DC power source.
*   **4. Ethernet Switch (Port 0/2/x):** A multi-port Ethernet switch module, likely for connecting multiple internal or external network devices.
*   **5. GE 0/0/1:** A Gigabit Ethernet (GE) port, typically used for connecting to a local network or another device.
*   **6. GE WAN 0/0/0 - RJ45:** A Gigabit Ethernet Wide Area Network (WAN) port, configured for RJ45 cable connection, used for connecting to an external network like the internet.
*   **7. GE WAN 0/0/0 - SFP:** An SFP (Small Form-factor Pluggable) slot, which allows for the insertion of an SFP transceiver module to support fiber optic or other high-speed connections.
*   **8. Micro-USB Console:** A port for connecting a console cable to a computer, enabling direct command-line access for configuration and troubleshooting.
*   **9. USB 3.0:** A high-speed USB port for connecting peripherals or for firmware updates.
*   **10. Pluggable (Kensington Lock Slot):** A slot for a Kensington security lock, used to physically secure the device to a desk or rack.
*   **11. Grounding:** A grounding terminal to ensure electrical safety by connecting the device to a ground wire.
*   **12. Grounding (repeated):** This label appears to be a duplicate or an error in the diagram, as it is positioned next to the same grounding terminal as item 11.

**Significance:**
This diagram is crucial for network administrators and IT professionals for proper device installation, configuration, and maintenance. It provides a clear visual map of all physical interfaces, helping users to correctly connect power, network cables, and peripherals while ensuring the device is securely installed and safely grounded. The presence of both RJ45 and SFP ports indicates the device's flexibility for connecting to different types of networks, whether copper or fiber.

<--- End description image 17 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | GE 0/0/1 | 6 | GE WAN 0/0/0 -RJ45 |
| 7 | GE WAN 0/0/0 -SFP | 8 | Micro-USB console |
| 9 | USB 3.0 | 10 | Pluggable |
| 11 | Kensington lock slot | 12 | Grounding |


<--- Start description table 13 --->

This table lists the hardware components and their corresponding identifiers found on the Cisco 1000 Series Integrated Services Router, as outlined in the Hardware Installation Guide. It includes features such as power connectors, network ports, console interfaces, and physical security elements, providing a reference for proper router setup and installation.

<--- End description table 13 --->





<--- Start caption image 18 --->

Figure 13: C1121(X)-8P - Bezel View

<--- End caption image 18 --->



<--- Start description image 18 --->

This image is a detailed component label diagram from the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 10," specifically highlighting the front panel of the device.

The diagram focuses on item 1, which is the **Non-illuminated Cisco logo**. It is shown as a simple, unlit "Cisco" brand mark located centrally on the front bezel of the router. An arrow points from the label to the logo's position on the device, which is also marked with the model identifier "Cisco 1000 Series" in the top-left corner.

This diagram serves as a reference guide for technicians or users to correctly identify and locate key physical components on the router's front panel. While the image only shows the logo, it is part of a larger, comprehensive labeling system that includes other critical elements such as the reset button, power switch, network ports (GE 0/0/1, GE WAN 0/0/0), console port, USB ports, and security features (Kensington lock slot). The purpose of this labeling is to ensure accurate hardware installation, configuration, and maintenance by providing a clear, numbered reference for each part. The non-illuminated state of the logo indicates that it does not serve as a status indicator, distinguishing it from other LEDs on the device.

<--- End description image 18 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 14 --->

This table lists various hardware components and their corresponding identifiers for the Cisco 1000 Series Integrated Services Router 10, providing a reference for proper installation and identification of physical interfaces such as power connectors, Ethernet ports, USB ports, and security features.

<--- End description table 14 --->



[17]----------------------




<--- Start caption image 19 --->

Figure 14: C1121(X)-8P I/O View

<--- End caption image 19 --->



<--- Start description image 19 --->

This is a detailed front-panel diagram of the Cisco 1000 Series Integrated Services Router, providing a comprehensive overview of its physical components and their functions. The diagram is essential for network administrators and technicians to correctly install, configure, and maintain the device.

**Key Components and Their Functions:**

*   **1. Reset Button:** A small button used to reboot the router or restore factory defaults if the device becomes unresponsive.
*   **2. Power Switch:** A toggle switch to turn the router on or off.
*   **3. 4-pin Power Connector:** Accepts the power supply unit (PSU) to provide electrical power to the router.
*   **4. Ethernet Switch (Port 0/0/1):** A 4-port Ethernet switch for connecting multiple devices within a local network.
*   **5. GE 0/0/1 (Gigabit Ethernet Port 0/0/1):** A dedicated Gigabit Ethernet port for connecting to a local network or another device.
*   **6. GE WAN 0/0/0 - RJ45 (Gigabit WAN Port 0/0/0 - RJ45):** A WAN (Wide Area Network) port for connecting to the internet or a remote network via standard Ethernet cable.
*   **7. GE WAN 0/0/0 - SFP (Gigabit WAN Port 0/0/0 - SFP):** An SFP (Small Form-factor Pluggable) slot for connecting to fiber optic networks, offering higher bandwidth and longer distances than copper cables.
*   **8. Micro-USB Console Port:** A port for connecting a console cable to a computer for initial configuration, troubleshooting, or direct command-line access.
*   **9. USB 3.0 Port:** A high-speed USB port for connecting peripherals such as flash drives or external storage devices.
*   **10. Kensington Lock Slot:** A security slot for attaching a physical lock to prevent unauthorized removal of the router from its location.
*   **11. Grounding:** A grounding terminal to ensure electrical safety by connecting the device to a proper ground.

**Significance:**

This diagram is a critical reference for anyone working with the Cisco 1000 Series router. It ensures that users can correctly identify and utilize each port and button, which is vital for proper setup, troubleshooting, and security. The inclusion of both RJ45 and SFP ports highlights the router's versatility for different network environments, from small offices to more complex enterprise setups. The presence of a console port and USB port also supports flexible management and data transfer options.

<--- End description image 19 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | RJ-45 | 6 | GE WAN 0/0/0 -RJ45 |
| 7 | GE WAN 0/0/0 -SFP | 8 | Micro-USB console |
| 9 | USB 3.0 | 10 | Kensington lock slot |
| 11 | Grounding |  |  |


<--- Start description table 15 --->

This table provides a labeled overview of the components found on the Cisco 1000 Series Integrated Services Routers, identifying key physical features such as the reset button, power switch, Ethernet and WAN ports, USB ports, console connection, and grounding options, along with their respective positions on the chassis.

<--- End description table 15 --->





<--- Start caption image 20 --->

Figure 15: C1121-8PLTEP I/O View

<--- End caption image 20 --->



<--- Start description image 20 --->

This is a detailed hardware installation diagram for the Cisco 1000 Series Integrated Services Router, illustrating the rear panel chassis views and labeling key physical components for proper setup and maintenance.

**Key Components and Their Functions:**

*   **1. Reset Button:** Used to restore the router to factory default settings, typically by holding it down for a few seconds.
*   **2. Power Switch:** A physical toggle or push-button switch to turn the device on or off.
*   **3. 4-pin Power Connector:** Accepts the power supply unit (PSU) to provide electrical power to the router.
*   **4. Ethernet Switch (Port 0/2/1):** A switch port for connecting to a local network or other devices.
*   **5. GE 0/0/1 (RJ-45):** A Gigabit Ethernet (GE) port for connecting to a local area network (LAN) using standard Ethernet cables.
*   **6. GE WAN 0/0/0 - RJ45:** A Gigabit Ethernet Wide Area Network (WAN) port for connecting to an external network, such as the internet, via an RJ-45 cable.
*   **7. GE WAN 0/0/0 - SFP:** A Gigabit Ethernet WAN port that uses a Small Form-factor Pluggable (SFP) transceiver for fiber optic or high-speed copper connections.
*   **8. Micro-USB Console:** A port for connecting a console cable to a computer for initial configuration, troubleshooting, or direct command-line access.
*   **9. USB 3.0:** A high-speed USB port for connecting peripherals like flash drives or external devices.
*   **10. Pluggable (Kensington Lock Slot):** A slot for a Kensington security lock to physically secure the router to a desk or cabinet.
*   **11. Grounding:** A grounding terminal to connect the router to a proper electrical ground for safety and to reduce electrical noise.

**Significance:**
This diagram is an essential reference for network administrators and technicians during the initial deployment, troubleshooting, or maintenance of the Cisco 1000 Series router. It ensures correct physical connections are made, prevents damage from incorrect power or cable connections, and provides a clear guide for securing the device in a physical environment. The labeling system (1-12) corresponds to the numbered list in the accompanying text, making it easy to cross-reference the diagram with the hardware installation guide.

<--- End description image 20 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | GE 0/0/1 | 6 | GE WAN 0/0/0 -RJ45 |
| 7 | GE WAN 0/0/0 -SFP | 8 | Micro-USB console |
| 9 | USB 3.0 | 10 | Pluggable |
| 11 | Kensington lock slot | 12 | Grounding |


<--- Start description table 16 --->

This table lists the hardware components and their corresponding identifiers found on the Cisco 1000 Series Integrated Services Router 11, as outlined in the Hardware Installation Guide. It includes features such as power connectors, network ports, console ports, and physical security options, helping users identify and locate specific components during installation or setup.

<--- End description table 16 --->





<--- Start caption image 21 --->

Figure 16: C1121-8PLTEPWx Bezel View

<--- End caption image 21 --->



<--- Start description image 21 --->

This image is a schematic diagram from the “Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router,” specifically illustrating the front panel of the device. The diagram is labeled with the number “1” and an arrow pointing to the Cisco logo, indicating that this is the primary identifier for the router model.

The diagram serves as a visual reference for users installing or identifying the device, highlighting the brand and model series (“Cisco 1000 Series”) located on the front bezel. While the diagram itself is minimal, it is contextually linked to a detailed table (not shown in this image) that lists and numbers all the physical ports and connectors on the device’s front panel, such as the reset button, power switch, Ethernet ports, USB ports, and Kensington lock slot.

**Significance:**
This diagram is part of a larger installation guide, helping technicians and administrators correctly identify and connect the router. The front panel layout is critical for proper hardware setup, ensuring correct cable connections (e.g., power, console, Ethernet) and physical security (e.g., Kensington lock). The Cisco logo and model designation are essential for verifying the correct device is being installed and for reference in troubleshooting or documentation.

In summary, this image is a simple, labeled schematic that identifies the Cisco 1000 Series router by its front-facing branding, serving as a foundational reference point for the more detailed component labeling provided in the accompanying hardware guide.

<--- End description image 21 --->



[18]----------------------


|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 17 --->

This table provides a labeled overview of the front and side panel components of the Cisco 1000 Series Integrated Services Routers, including key features such as reset and power buttons, Ethernet and Wi-Fi ports, WAN connections, console and USB ports, and physical security elements like the Kensington lock slot and grounding point. The layout identifies each component by number and its function, offering a clear reference for users to locate and understand the router's hardware interfaces.

<--- End description table 17 --->





<--- Start description image 22 --->

This image provides a detailed, annotated overview of the front-panel I/O interfaces for two specific models within the Cisco 1000 Series Integrated Services Routers: the C1121(X)-8PLTEPW and the C1127X-8PLTEP. The diagrams serve as essential reference guides for network administrators and technicians, clearly labeling each physical component to facilitate proper installation, configuration, and troubleshooting.

**Key Components and Their Functions:**

*   **Power and Control (Figures 17 & 19):** Both models feature a **Reset button (1)** for system reboot, a **Power switch (2)** to turn the device on or off, and a **4-pin power connector (3)** for external power supply.
*   **Network Connectivity (Figures 17 & 19):** The routers offer multiple network interfaces. The **Ethernet switch (4)** provides a local network connection. The **GE WAN 0/0/0 - RJ45 (6)** and **GE WAN 0/0/0 - SFP (7)** ports are for connecting to wide area networks, with the SFP port supporting fiber optic cables for longer distances. The **GE 0/0/1 (5)** port is a general-purpose Gigabit Ethernet port.
*   **Management and Expansion (Figures 17 & 19):** A **Micro-USB console (8)** port is provided for direct command-line access and initial configuration. A **USB 3.0 port (10)** allows for data transfer and peripheral connection. A **Pluggable (9)** slot is available for inserting optional modules to expand functionality.
*   **Security and Grounding (Figures 17 & 19):** A **Kensington lock slot (11)** is included for physical security, and a **Grounding (12)** terminal ensures electrical safety.
*   **Status Indicators (Figure 17):** A **Wi-Fi status (5)** LED indicates the operational state of the wireless radio.
*   **Branding (Figures 17 & 18):** A **Non-illuminated Cisco logo (1)** is present on the front bezel for brand identification.

**Significance:**

These diagrams are critical for ensuring correct physical setup and maintenance. They help users identify the correct ports for power, network, and management connections, preventing misconfigurations. The inclusion of both RJ45 and SFP WAN ports highlights the router's flexibility for different network environments. The presence of a console port and USB port supports both legacy and modern management methods. The grounding and Kensington lock slot emphasize the device's design for secure, professional deployment in enterprise or service provider networks.

<--- End description image 22 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | Wi-Fi status | 6 | GE 0/0/1 |
| 7 | GE WAN 0/0/0 -RJ45 | 8 | GE WAN 0/0/0 -SFP |
| 9 | Micro-USB console | 10 | USB 3.0 |
| 11 | Pluggable | 12 | Kensington lock slot |
| 13 | Grounding |  |  |


<--- Start description table 18 --->

This table outlines the components and labels found on a Cisco networking device's chassis, listing various physical features such as the logo, reset button, power switch, power connectors, Ethernet and WAN ports, SFP modules, console port, pluggable optics, DSL interface, and grounding point, along with their corresponding positions.

<--- End description table 18 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 19 --->

The table presents two different configurations of port and connector labels on a Cisco networking device, organized by position numbers. The first configuration lists components such as the reset button, power switch, Ethernet switch, Wi-Fi status, and various network interfaces (including RJ45, SFP, and USB ports), while the second configuration shows a reorganized or alternative labeling scheme with changes like "RJ-45" replacing "GE WAN 0/0/0 - RJ45" and "DSL" replacing "Pluggable." The table highlights the physical interface specifications and connectivity options available on the device, including power, network, and security features.

<--- End description table 19 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | RJ-45 | 6 | GE WAN 0/0/0 - RJ45 |
| 7 | GE WAN 0/0/0 -SFP | 8 | Micro-USB console |
| 9 | Pluggable | 10 | DSL |
| 11 | Kensington lock slot | 12 | Grounding |


<--- Start description table 20 --->

The table lists various hardware components and ports found on a Cisco networking device, including power and connectivity options such as the power switch, Ethernet and Wi-Fi status indicators, Gigabit Ethernet ports (GE), USB ports, a micro-USB console, pluggable modules, and a Kensington lock slot. It also includes a non-illuminated Cisco logo, with port numbers and descriptions organized in a structured format to help identify the physical layout and features of the device.

<--- End description table 20 --->







<--- Start caption image 23 --->

Figure 20: C1128-8PLTEP Bezel View

<--- End caption image 23 --->



<--- Start description image 23 --->

This is a detailed I/O panel diagram for the Cisco C1128-8PLTEP device, providing a comprehensive labeling of its rear-facing ports and controls. The diagram serves as a technical reference guide for network administrators and technicians to identify and utilize the device’s connectivity and management interfaces.

**Key Components and Their Functions:**

*   **Power and Control (Left Side):**
    *   **1. Reset Button:** Used to reboot the device.
    *   **2. Power Switch:** Controls the power state of the device.
    *   **3. 4-pin Power Connector:** Supplies power to the unit.
    *   **4. Ethernet Switch:** A built-in switch for connecting multiple Ethernet devices locally.

*   **Network and Management Interfaces (Center & Right):**
    *   **5. USB 3.0 Port:** For connecting external storage or management devices.
    *   **6. GE WAN 0/0/0 - RJ45:** A Gigabit Ethernet port for connecting to a Wide Area Network (WAN) via standard Ethernet cable.
    *   **7. GE WAN 0/0/0 - SFP:** A Gigabit Ethernet port that uses a Small Form-factor Pluggable (SFP) module for fiber optic or other high-speed connections.
    *   **8. Micro-USB Console:** Provides a direct console connection for initial setup, troubleshooting, and command-line interface (CLI) access.
    *   **9. Pluggable:** Refers to the SFP slot (port 7), indicating it accepts interchangeable SFP modules for different media types.
    *   **10. Symmetrical High-speed Digital Subscriber Lines (SHDSL):** A port for connecting to a DSL line, enabling broadband internet access over traditional telephone lines.
    *   **11. Kensington Lock Slot:** A security feature to physically secure the device to a desk or rack using a cable lock.
    *   **12. Grounding:** A terminal for connecting the device to a ground wire to ensure electrical safety and reduce electromagnetic interference.

**Significance:**
This diagram is essential for proper installation, configuration, and maintenance of the Cisco C1128-8PLTEP, which is likely a broadband router or access server. It clearly delineates the physical interfaces for power, network connectivity (both copper and fiber), management, and security, enabling users to correctly connect the device to their network infrastructure and perform administrative tasks. The presence of both RJ45 and SFP ports indicates its flexibility for different network environments, while the SHDSL port highlights its role in providing broadband services over existing telephone lines.

<--- End description image 23 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 21 --->

The table lists various hardware components and ports found on a network device, organized by their position (numbered labels) and type. It includes features such as the reset button, power switch, power connectors, Ethernet and WAN ports (including RJ45 and SFP), console connections, DSL options (including SHDSL), a Kensington lock slot, and grounding. The table shows two versions of the same component list, with a correction in the fifth row (USB 3.0 replacing "RJ-45") and a clarification of the DSL type to "Symmetrical High-speed Digital Subscriber Lines (SHDSL)." The final row indicates a non-illuminated Cisco logo at position 1, suggesting the device's branding.

<--- End description table 21 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | USB 3.0 | 6 | GE WAN 0/0/0 -RJ45 |
| 7 | GE WAN 0/0/0 -SFP | 8 | Micro-USB console |
| 9 | Pluggable | 10 | Symmetrical High-speed Digital Subscriber Lines (SHDSL) |
| 11 | Kensington lock slot | 12 | Grounding |


<--- Start description table 22 --->

This table serves as a header or identifier for the Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router, featuring a non-illuminated Cisco logo to indicate the document's brand and purpose.

<--- End description table 22 --->





<--- Start caption image 24 --->

Figure 22: C1131(X)-8PLTEPW Bezel View

<--- End caption image 24 --->



<--- Start description image 24 --->

This is a close-up diagram from the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router," specifically highlighting the front panel of the device. The image focuses on component #1, which is the non-illuminated Cisco logo.

**Caption:**
*Front Panel Component Identification: The non-illuminated Cisco logo (labeled #1) is prominently displayed on the front bezel of the Cisco 1000 Series Integrated Services Router. This logo, along with the "ISR 1100 Series" text to its left, serves as a brand identifier. The diagram is part of a larger labeling system that details all front-panel components, including the reset button, power switch, various network ports (Ethernet, SFP, WAN), USB ports, and physical security features like the Kensington lock slot. This visual guide is designed to assist technicians in correctly identifying and installing the router hardware.*

<--- End description image 24 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 23 --->

This table outlines the hardware components and their corresponding identifiers found on the Cisco 1000 Series Integrated Services Router. It lists various physical features such as the logo, reset and power buttons, power connectors, Ethernet and SFP ports, USB ports, console connections, and networking interfaces like SHDSL, along with their respective positions on the device. The information is part of a hardware installation guide, providing a reference for identifying and locating key components during setup or maintenance.

<--- End description table 23 --->



[20]----------------------




<--- Start caption image 25 --->

Figure 23: C1131(X)-8PLTEPW I/O Panel View

<--- End caption image 25 --->



<--- Start description image 25 --->

This is a detailed schematic diagram of the front panel of a Cisco 1000 Series Integrated Services Router (model 357490), providing a comprehensive overview of its physical components and their functions. The diagram is annotated with numbers corresponding to a legend that identifies each part, serving as a critical reference for network administrators, technicians, and users for setup, troubleshooting, and maintenance.

**Key Components and Their Functions:**

*   **1. Wi-Fi Status Indicator (LED):** A small LED light that visually indicates the status of the router's built-in Wi-Fi radio (802.11a/b/g/n/ac). It typically blinks or remains solid to show connection or activity.
*   **2. Power Switch:** A physical toggle or push-button switch used to turn the router on or off.
*   **3. 4-Pin Power Connector:** The input port for connecting the router's power supply unit (PSU). It accepts a standard 4-pin power cable.
*   **4. Ethernet Switch (Port 1):** A 10/100/1000 Ethernet port, often labeled "1" or "Port 1," used for connecting to a local network or another device via a standard Ethernet cable.
*   **5. Ethernet Switch (Port 2):** A second 10/100/1000 Ethernet port, typically labeled "2" or "Port 2," for additional network connections.
*   **6. GE WAN 0/0/1 - SFP:** A Gigabit Ethernet WAN port that supports Small Form-Factor Pluggable (SFP) transceivers for fiber optic connections. This port is labeled "GE WAN 0/0/1" and is designed for high-speed WAN links.
*   **7. GE WAN 0/0/1 - RJ45:** A second Gigabit Ethernet WAN port, labeled "GE WAN 0/0/1," which is a standard RJ45 port for copper cable connections.
*   **8. GE WAN 0/0/0 - RJ45:** A Gigabit Ethernet WAN port, labeled "GE WAN 0/0/0," for connecting to a WAN network using standard Ethernet cables.
*   **9. GE WAN 0/0/0 - SFP:** A second Gigabit Ethernet WAN port that supports SFP transceivers for fiber optic connections, labeled "GE WAN 0/0/0."
*   **10. Console Port:** A serial port (typically RS-232) used for direct, out-of-band management and configuration of the router via a console cable connected to a computer.
*   **11. USB 2.0 Port:** A USB 2.0 port for connecting peripherals such as flash drives, USB modems, or for firmware updates.
*   **12. Pluggable (SFP) Slot:** A slot for inserting SFP modules to enable fiber optic connectivity on the WAN ports.
*   **13. Kensington Lock Slot:** A security slot for attaching a physical security cable to prevent theft or unauthorized removal of the device.
*   **14. Grounding Terminal:** A terminal for connecting the router to a grounding wire to ensure electrical safety and reduce electromagnetic interference.

**Purpose of the Diagram:**

This diagram is an essential technical reference for anyone working with the Cisco 1000 Series router. It allows users to quickly identify and locate critical components for:

*   **Initial Setup:** Connecting power, network cables, and management devices.
*   **Troubleshooting:** Diagnosing issues by checking the status of LEDs and verifying physical connections.
*   **Maintenance:** Performing hardware upgrades, such as replacing SFP modules or connecting peripherals.
*   **Security:** Securing the device using the Kensington lock.

The diagram's clarity and labeling make it an indispensable tool for ensuring correct and efficient operation of the router in both enterprise and small business network environments.

<--- End description image 25 --->





<--- Start caption image 26 --->

Figure 24: C1131-8PLTEPW I/O Panel View

<--- End caption image 26 --->



<--- Start description image 26 --->

This is a comprehensive front-panel diagram of the Cisco 1000 Series Integrated Services Router (specifically model G1131-8PLTBPW), serving as a quick-reference guide for identifying and understanding its physical components and LED indicators.

**Key Components and Their Functions:**

*   **1. Reset Button:** A small button used to reboot the router or restore factory defaults.
*   **2. Power Switch:** A toggle switch to turn the device on or off.
*   **3. 4-pin Power Connector:** The input port for connecting the router's power supply.
*   **4. Ethernet Switch:** A 4-port Ethernet switch for connecting multiple devices to the local network.
*   **5. Wi-Fi Status LED:** An indicator light that shows the status of the built-in Wi-Fi radio (e.g., connected, connecting, or off).
*   **6. GE WAN 0/0/1 - SFP:** A Small Form-Factor Pluggable (SFP) port for connecting to a WAN or uplink using fiber optic cable.
*   **7. GE WAN 0/0/1 - RJ45:** A standard Ethernet (RJ45) port for connecting to a WAN or uplink using copper cable.
*   **8. GE WAN 0/0/0 - RJ45:** A standard Ethernet (RJ45) port for connecting to a WAN or uplink using copper cable.
*   **9. GE WAN 0/0/0 - SFP:** A Small Form-Factor Pluggable (SFP) port for connecting to a WAN or uplink using fiber optic cable.
*   **10. Console Port:** A serial port (typically RS-232) for direct management and configuration using a console cable and terminal emulator.
*   **11. USB 2.0 Port:** A USB port for connecting peripherals or for firmware updates.
*   **12. Pluggable:** This label points to the SFP slots (6, 9) and the RJ45 ports (7, 8), indicating these are pluggable interfaces for flexible connectivity options.
*   **13. Kensington Lock Slot:** A slot for securing the router to a desk or cabinet using a Kensington security cable.
*   **14. Grounding:** A grounding terminal to ensure electrical safety and reduce noise.

**LED Indicators (Not Shown in Detail in the Diagram, but Referenced in the Context):**

The diagram references "LED Indicators" in the context, which are typically located near the power switch and console port. These lights provide real-time status information about the router's power, network connectivity, and operational state, allowing for quick troubleshooting without needing to log into the device.

**Significance:**

This diagram is an essential tool for network administrators, technicians, and engineers. It provides a clear, labeled overview of the router's front panel, enabling them to quickly identify ports, connectors, and controls. This is critical for proper installation, configuration, maintenance, and troubleshooting of the Cisco 1000 Series router in a network environment.

<--- End description image 26 --->



1010

|  |  |  |  |
|------|------|------|------|
| 1 | Reset button | 2 | Power switch |
| 3 | 4-pin power connector | 4 | Ethernet switch |
| 5 | Wi-Fi status | 6 | GE WAN 0/0/1 - SFP |
| 7 | GE WAN 0/0/1 - RJ45 | 8 | GE WAN 0/0/0 - RJ45 |
| 9 | GE WAN 0/0/0 - SFP | 10 | Console |
| 11 | USB 2.0 | 12 | Pluggable |
| 13 | Kensington lock slot | 14 | Grounding |


<--- Start caption table 24 --->

Table 3: C1131(X)-8PLTEPW/C1131-8PLTEPW I/O Panel View

<--- End caption table 24 --->



<--- Start description table 24 --->

The table summarizes the LED indicators found in the bezel or chassis of the Cisco 1000 Series Integrated Services Router's C111x series, providing a reference for hardware installation and system status monitoring.

<--- End description table 24 --->



### LED Indicators


The following figures and table summarizes the LED indicators that are located in the bezel or chassis of the C111x series.

[21]----------------------




<--- Start caption image 27 --->

Figure 25: LED Indicators - Bezel Side

<--- End caption image 27 --->



<--- Start description image 27 --->

This diagram provides a comprehensive, labeled overview of the front panel of a Cisco 1000 Series Integrated Services Router (ISR), detailing its LED indicators and physical ports for user reference.

**Top Section: LED Indicators (Status Display)**
This section shows the router’s status lights, which provide real-time feedback on its operational state:
*   **LED 1 (Status):** Indicates the overall system health and power status.
*   **LED 2 (VPN):** Shows the status of VPN connections.
*   **LED 3 (WLAN):** Indicates the status of the wireless LAN (Wi-Fi) interface.
*   **LED 4 (GPS):** Shows the status of the GPS module (if equipped).
*   **LED 5 (LTE RSSI/mode):** Displays the signal strength (RSSI) and operational mode of the LTE cellular interface.
*   **LED 6 (LTE data/SIM):** Indicates whether LTE data is active and the status of the SIM card.
*   **LED 7 (Cisco Logo):** A status indicator light located near the Cisco logo, often used for system power or activity.

**Bottom Section: Physical Ports and LEDs**
This section details the router’s connectivity ports and their corresponding status LEDs:
*   **Port 1 (GE WAN ports):** Eight Gigabit Ethernet (GE) WAN ports, arranged in two rows (top: 0, 2, 4, 6; bottom: 1, 3, 5, 7). Each port has its own LED to indicate link and activity status.
*   **Port 2 (PoE LED):** An indicator for Power over Ethernet (PoE) status.
*   **Port 3 (GE1 LED):** Status LED for the GE1 port.
*   **Port 4 (GE0 LED):** Status LED for the GE0 port.
*   **Port 5 (USB LED):** Indicates activity on the USB port.
*   **Port 6 (RJ-45 console LED):** Shows activity on the console port.
*   **Port 7 (USB console):** A USB port for console access.
*   **Port 8 (Micro USB console LED):** A Micro USB port for console access, with its own activity LED.
*   **Port 9 (CD LED):** Indicates the status of the CD drive (if present).
*   **Port 10 (DATA LED):** Indicates data activity on the router.

This diagram is a critical reference tool for network administrators and technicians, enabling them to quickly diagnose hardware status and connectivity issues by interpreting the visual cues from the router’s front panel.

<--- End description image 27 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Status | 2 | VPN |
| 3 | WLAN | 4 | GPS |
| 5 | LTE RSSI/mode | 6 | LTE data/SIM |
| 7 | Cisco logo |  |  |


<--- Start description table 25 --->

This table provides an overview of the LED indicators located on the Cisco 1000 Series Integrated Services Router, detailing the function of each LED and its corresponding physical location on the device, such as WAN ports, PoE, Ethernet ports, USB connections, and console interfaces, to assist with hardware installation and troubleshooting.

<--- End description table 25 --->





<--- Start caption image 28 --->

Figure 26: LED Indicators - I/O Side

<--- End caption image 28 --->



<--- Start description image 28 --->

This is a detailed front-view diagram of the Cisco 1000 Series Integrated Services Router, specifically illustrating the location and function of its various LEDs and ports as described in the Hardware Installation Guide. The diagram serves as a quick-reference guide for users to identify and interpret the status of the router’s physical interfaces and operational indicators.

**Key Components and Their Significance:**

*   **LED Indicators (Top Row, Labeled 1-7):** These provide real-time status information for the router’s core connectivity and operational features.
    *   **1 (Status):** A general system status indicator.
    *   **2 (VPN):** Indicates the status of VPN connections.
    *   **3 (WLAN):** Shows the status of the wireless LAN (Wi-Fi) interface.
    *   **4 (GPS):** Indicates the status of the GPS module (if equipped).
    *   **5 (LTE RSSI/mode):** Displays the signal strength (RSSI) and operational mode of the LTE cellular connection.
    *   **6 (LTE data/SIM):** Indicates whether LTE data is active and the status of the SIM card.
    *   **7 (Cisco Logo):** A branding indicator, typically illuminated when the device is powered on.

*   **Physical Ports and LEDs (Bottom Row, Labeled 1-11):** These are the router’s physical interfaces for connecting to other devices and for console access.
    *   **1 (GE WAN ports):** Eight Gigabit Ethernet WAN ports (labeled 0-7), arranged in two rows (top: 0, 2, 4, 6; bottom: 1, 3, 5, 7). These are used for connecting to wide area networks.
    *   **2 (PoE LED):** Indicates the status of Power over Ethernet (PoE) being supplied to connected devices.
    *   **3 (GE1 LED):** Status indicator for the first Gigabit Ethernet port (GE1).
    *   **4 (GE0 LED):** Status indicator for the first Gigabit Ethernet port (GE0).
    *   **5 (USB LED):** Indicates the status of the USB port.
    *   **6 (RJ-45 console LED):** Shows the status of the RJ-45 console port.
    *   **7 (USB console):** The USB port for console access.
    *   **8 (Micro USB console LED):** Status indicator for the Micro USB console port.
    *   **9 (CD LED):** Indicates the status of the CD drive (if present).
    *   **10 (DATA LED):** Indicates data activity on the associated port or interface.

**Purpose of the Diagram:**
This diagram is an essential part of the installation and troubleshooting process. It allows network administrators and technicians to quickly diagnose issues by visually correlating the state of each LED with the router’s current operational status. For example, a blinking or solid LED can indicate a connection is active, a port is powered, or a service is running, while an unlit LED might signal a problem or that a feature is disabled. This visual guide ensures users can efficiently manage and maintain the router’s connectivity and performance.

<--- End description image 28 --->



|  |  |  |  |
|------|------|------|------|
| 1 | GE WAN ports: 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) | 2 | PoE LED |
| 3 | GE1 LED | 4 | GE0 LED |
| 5 | USB LED | 6 | RJ-45 console LED |
| 7 | USB console | 8 | Micro USB console LED |
| 9 | CD LED | 10 | DATA LED |


<--- Start description table 26 --->

This table outlines the various status indicators and hardware components available on the Cisco 1000 Series Integrated Services Router, including WLAN, LTE connectivity, GPS, VPN, and hardware-related features such as the Cisco logo and SIM data status, as part of the hardware installation guide.

<--- End description table 26 --->



[22]----------------------




<--- Start caption image 29 --->

Figure 27: Cisco 1121-4Px LED Indicators

<--- End caption image 29 --->



<--- Start description image 29 --->

This diagram provides a comprehensive, labeled overview of the front panel LED indicators for the Cisco 1000 Series Integrated Services Router (specifically model C1121-4P, as indicated on the device). It serves as a critical reference guide for network administrators and technicians to monitor the router’s operational status in real-time.

**Purpose:** The diagram’s primary purpose is to identify and explain the function of each LED indicator, enabling users to quickly diagnose connectivity, power, and system health issues.

**Key Components and Their Significance:**

*   **LED Indicator 1 (VPN):** This LED indicates the status of the router’s VPN (Virtual Private Network) functionality. It typically illuminates to show that a VPN tunnel is active or established.
*   **LED Indicator 2 (PoE LED):** This LED signifies the status of Power over Ethernet (PoE) power delivery. It helps confirm that the router is successfully supplying power to connected PoE devices.
*   **LED Indicator 3 (Status):** This is the primary system status LED. It provides a high-level overview of the router’s health. A solid green light usually indicates normal operation, while an amber or flashing light indicates a warning or error condition.
*   **LED Indicators 4 (Ethernet Switch Ports 0-3):** These four LEDs correspond to the four Ethernet switch ports (0 through 3) on the device. Each LED indicates the link and activity status of its respective port (e.g., solid light = link established, blinking = data transmission).
*   **LED Indicators 5 & 7 (GE 0/0/0 RJ45 LED):** These are the LEDs for the two Gigabit Ethernet (GE) RJ45 ports. They provide status for the physical connection and data activity on these specific ports.
*   **LED Indicator 6 (GE 0/0/1 LED):** This LED monitors the status and activity of the second Gigabit Ethernet port (GE 0/0/1).
*   **LED Indicator 8 (Micro USB Console LED):** This LED indicates the status of the Micro USB console port, which is used for direct console access and debugging.
*   **LED Indicator 9 (USB LED):** This LED indicates the status of the USB port, which may be used for device connectivity or diagnostics.

**Significance:**
This visual guide is essential for troubleshooting network issues. By observing the state of these LEDs (on, off, solid, blinking, color), technicians can rapidly identify problems such as failed connections, power issues, or system errors without needing to access the router’s command-line interface. It is a foundational tool for maintaining the reliability and performance of the Cisco 1000 Series router in enterprise or small business networks.

<--- End description image 29 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet switch ports 0-3 |
| 5 | GE 0/0/0 RJ45 LED | 6 | GE 0/0/1 LED |
| 7 | GE 0/0/0 RJ45 LED | 8 | Micro USB console LED |
| 9 | USB LED |  |  |


<--- Start description table 27 --->

This table provides a labeled overview of the LED indicators on the Cisco 1000 Series Integrated Services Router, detailing the function of each LED located on the device, including indicators for VPN, PoE, Ethernet ports, Gigabit Ethernet connections, USB, and console access, as part of the hardware installation guide.

<--- End description table 27 --->





<--- Start caption image 30 --->

Figure 28: Cisco 1121-4PLTEP LED Indicators

<--- End caption image 30 --->



<--- Start description image 30 --->

This diagram is a hardware reference guide for the Cisco 1000 Series Integrated Services Router (model C1121-4PLTSP), specifically illustrating the front panel LED indicators and their corresponding ports. It serves as a quick-reference tool for network administrators and technicians to monitor the router’s operational status.

**Key Components and Their Significance:**

*   **LED Indicators (1-9):** The diagram labels nine distinct LED indicators, each providing real-time status feedback on different router functions.
    *   **1 (VPN):** Indicates the status of the router's Virtual Private Network (VPN) connections.
    *   **2 (PoE LED):** Shows the Power over Ethernet (PoE) status, which is critical for powering connected devices like IP phones or wireless access points.
    *   **3 (Status):** A general system status indicator, typically showing if the router is powered on and operating normally.
    *   **4 (Ethernet switch ports 0-3):** A group of LEDs that monitor the activity and link status of the four integrated Ethernet switch ports.
    *   **5 & 7 (GE 0/0/0 RJ45 LED):** These are two separate LEDs for the same Gigabit Ethernet (GE) port (0/0/0), likely indicating different states such as link/activity and speed (e.g., 10/100/1000 Mbps).
    *   **6 (GE 0/0/1 LED):** Monitors the activity and link status of the second Gigabit Ethernet port (0/0/1).
    *   **8 (Micro USB console LED):** Indicates the status of the Micro USB port used for console access and debugging.
    *   **9 (USB LED):** Shows the status of the USB port, which may be used for storage or device connectivity.

*   **Physical Layout:** The diagram clearly shows the physical arrangement of these LEDs and ports on the router’s front panel, helping users quickly locate and interpret the status of their network device.

**Purpose:**
This guide is essential for troubleshooting and routine maintenance. By observing the state of these LEDs (e.g., solid, blinking, off), technicians can quickly diagnose issues such as network connectivity problems, power failures, or configuration errors without needing to access the router’s command-line interface. It is a foundational tool for ensuring the router is functioning correctly within a network infrastructure.

<--- End description image 30 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet switch ports 0-3 |
| 5 | GE 0/0/0 RJ45 LED | 6 | GE 0/0/1 LED |
| 7 | GE 0/0/0 RJ45 LED | 8 | Micro USB console LED |
| 9 | USB LED |  |  |


<--- Start description table 28 --->

This table provides a labeled overview of the hardware components and indicators on the Cisco 1000 Series Integrated Services Router 16, including ports, LEDs, and connectivity features such as PoE, Ethernet switch ports, and console access, as part of the hardware installation guide.

<--- End description table 28 --->



[23]----------------------




<--- Start caption image 31 --->

Figure 29: Cisco 11x1(X)-8P/ C11x1(X)-8PLTEP LED Indicators

<--- End caption image 31 --->



<--- Start description image 31 --->

This diagram provides a detailed, labeled overview of the front panel LED indicators and ports on a Cisco 1000 Series Integrated Services Router, specifically the model C1121-SPLTP. It serves as a quick-reference guide for network administrators and technicians to interpret the device's operational status at a glance.

**Key Components and Their Significance:**

*   **LED Indicators (1-9):** These are the primary visual status indicators for the router's health and connectivity.
    *   **1 (VPN LED):** Indicates the status of VPN (Virtual Private Network) services. A solid light typically means the VPN is active and connected.
    *   **2 (PoE LED):** Shows the status of Power over Ethernet (PoE) power delivery to connected devices. It helps confirm if the router is successfully powering devices like IP phones or wireless access points.
    *   **3 (Status LED):** A general system status indicator. It typically blinks or illuminates to show the router is powered on and operational.
    *   **4 (Ethernet Switch Ports 0-7):** This section shows the status of the 8-port Ethernet switch. Ports are arranged in two rows: top row (0, 2, 4, 6) and bottom row (1, 3, 5, 7). An illuminated LED for a port indicates that a device is connected and the link is active.
    *   **5 (GE 0/0/0 RJ45 LED):** Indicates the status of the primary Gigabit Ethernet port (GE 0/0/0) used for WAN or primary network connections.
    *   **6 (GE 0/0/1 LED):** Indicates the status of the secondary Gigabit Ethernet port (GE 0/0/1), often used for LAN or backup connections.
    *   **7 (GE 0/0/0 RJ45 LED):** This is a duplicate label for the same port as #5, likely for redundancy or clarity in the diagram.
    *   **8 (Micro USB Console LED):** Indicates the status of the console port, which is used for direct command-line access and troubleshooting.
    *   **9 (USB LED):** Shows the status of the USB port, which can be used for connecting external storage or other USB devices.

**Purpose of the Diagram:**
The primary purpose of this diagram is to provide a clear, visual reference for users to quickly identify and understand the meaning of each LED indicator and port on the Cisco 1000 Series router. This is crucial for routine monitoring, troubleshooting network issues, and ensuring the device is functioning correctly. By knowing what each light signifies, technicians can rapidly diagnose problems such as failed connections, power issues, or VPN disconnections without needing to access the router's command-line interface.

<--- End description image 31 --->



5000

|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet switch ports 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) |
| 5 | GE 0/0/0 RJ45 LED | 6 | GE 0/0/1 LED |
| 7 | GE 0/0/0 RJ45 LED | 8 | Micro USB console LED |
| 9 | USB LED |  |  |


<--- Start description table 29 --->

This table outlines the LED indicators and their corresponding functions on the Cisco 1000 Series Integrated Services Router, providing a reference for hardware installation and troubleshooting. Each LED is labeled with its position and purpose, including indicators for VPN, PoE, status, Ethernet ports, Wi-Fi, Gigabit Ethernet (GE) ports, USB, and console connectivity.

<--- End description table 29 --->





<--- Start caption image 32 --->

Figure 30: C1121(X)-8PLTEPWx LED Indicators

<--- End caption image 32 --->



<--- Start description image 32 --->

This is a detailed front-panel diagram of the Cisco 1000 Series Integrated Services Router (model C1121-8PLTPW), serving as a hardware installation guide. The image systematically labels and identifies each component on the router’s front interface to assist technicians during setup and troubleshooting.

**Key Components and Their Functions:**

*   **1. VPN Button:** A physical button used to initiate or manage Virtual Private Network (VPN) connections.
*   **2. PoE LED (Power over Ethernet):** An indicator light that shows the status of Power over Ethernet (PoE) power delivery to connected devices.
*   **3. Status LED:** A general system status indicator, typically showing power, system health, or operational state.
*   **4. Ethernet Switch Ports (0-7):** An 8-port Ethernet switch. Ports are arranged in two rows: top row (0, 2, 4, 6) and bottom row (1, 3, 5, 7). These ports support Gigabit Ethernet (GE) connections for wired networking.
*   **5. GE 0/0/0 RJ45 LED:** An indicator light for the first Gigabit Ethernet port (GE 0/0/0) using an RJ45 connector.
*   **6. GE 0/0/1 LED:** An indicator light for the second Gigabit Ethernet port (GE 0/0/1) using an RJ45 connector.
*   **7. GE 0/0/0 SFP LED:** An indicator light for the first Gigabit Ethernet port (GE 0/0/0) when using an SFP (Small Form-factor Pluggable) module for fiber or higher-speed connections.
*   **8. Micro USB Console LED:** An indicator light for the Micro USB port used to connect a console cable for command-line interface (CLI) access and configuration.
*   **9. USB LED:** An indicator light for the USB port, which may be used for device connectivity or firmware updates.
*   **10. Wi-Fi LED:** An indicator light for the wireless (Wi-Fi) functionality of the router, showing its operational status.

**Significance:**
This diagram is an essential reference for network administrators and installers. It provides a clear, visual guide to the router’s physical interface, enabling users to quickly identify ports, LEDs, and buttons. This is critical for tasks such as connecting network cables, configuring wireless settings, accessing the router’s CLI, and diagnosing hardware issues based on LED status. The labeling ensures that users can correctly map physical components to their functions, facilitating efficient and error-free deployment of the Cisco 1000 Series router.

<--- End description image 32 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet Switch Ports 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) |
| 5 | Wi-Fi | 6 | GE 0/0/0 RJ45 LED |
| 7 | GE 0/0/1 LED | 8 | GE 0/0/0 SFP LED |
| 9 | USB LED | 10 | Micro USB console LED |


<--- Start description table 30 --->

This table provides a detailed pinout and hardware component reference for the Cisco 1000 Series Integrated Services Router 17, outlining the function of various ports and LEDs, including PoE, Ethernet switch ports, RJ45 LEDs, USB, and console connections, to assist with proper hardware installation and identification.

<--- End description table 30 --->



[24]----------------------




<--- Start caption image 33 --->

Figure 31: Cisco 1126(X)-8PLTEP/ C1127(X)-8PxLTEP LED Indicators

<--- End caption image 33 --->



<--- Start description image 33 --->

This diagram provides a detailed, labeled overview of the front panel of a Cisco 1000 Series Integrated Services Router, specifically the model 1000-8P, illustrating the locations and functions of its various LED indicators and ports.

**Key Components and Their Significance:**

*   **LED Indicators (1-10):** The diagram uses numbered callouts to identify each indicator light, which is critical for network administrators to monitor the router's operational status.
    *   **1 (VPN LED):** Indicates the status of VPN connections.
    *   **2 (PoE LED):** Shows the Power over Ethernet status for connected devices.
    *   **3 (Status LED):** A general system status indicator.
    *   **4 (Ethernet Switch Ports 0-7):** This group represents the 8-port Ethernet switch. Ports are arranged in two rows: top row (0, 2, 4, 6) and bottom row (1, 3, 5, 7). Each port has its own LED to show link and activity status.
    *   **5 (GE 0/0/0 RJ45 LED):** Indicates the status of the primary Gigabit Ethernet port (RJ45 connector).
    *   **6 (USB5 LED):** Shows the status of the USB 5 port.
    *   **7 (GE 0/0/0 SFP LED):** Indicates the status of the Gigabit Ethernet port using an SFP (Small Form-factor Pluggable) module.
    *   **8 (Micro USB console LED):** Indicates the status of the console port for direct management access.
    *   **9 (CD LED):** Indicates the status of the Compact Flash (CD) card slot, often used for storage or booting.

*   **Physical Ports:**
    *   **Ethernet Switch Ports (4):** The 8-port switch is the primary interface for connecting multiple devices within a local network.
    *   **GE 0/0/0 RJ45 (5) and SFP (7):** These are the main uplink ports for connecting the router to other network devices, such as a switch or a WAN connection. The RJ45 port is for copper cables, while the SFP port is for fiber optic cables.
    *   **USB 5 (6):** A USB port for connecting peripherals or for firmware updates.
    *   **Micro USB Console (8):** A dedicated port for out-of-band management and configuration via a console cable.
    *   **Compact Flash (CD) Slot (9):** Used for installing or updating the router's operating system or for storing configuration files.

**Purpose of the Diagram:**

This diagram serves as a quick-reference guide for technicians and network administrators. It allows them to quickly identify which LED corresponds to which function, enabling them to troubleshoot network issues by visually inspecting the status of the router's indicators. Understanding the layout and function of each component is essential for the proper installation, configuration, and maintenance of the Cisco 1000 Series router.

<--- End description image 33 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet Switch Ports 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) |
| 5 | GE 0/0/0 RJ45 LED | 6 | USB5 LED |
| 7 | GE 0/0/0 SFP LED | 8 | Micro USB console LED |
| 9 | CD LED |  |  |


<--- Start description table 31 --->

This table provides a labeled overview of the LED indicators on the Cisco 1000 Series Integrated Services Routers, detailing the function of each LED by position. It includes indicators for VPN, Wi-Fi, Ethernet switch ports, Gigabit Ethernet (GE) ports, PoE, USB, and console connectivity, helping users identify the status and operational state of various router features.

<--- End description table 31 --->





<--- Start caption image 34 --->

Figure 32: C1131(X)-8PW LED Indicators

<--- End caption image 34 --->



<--- Start description image 34 --->

This is a rear-view diagram of a Cisco C1131X-8PWN network switch, providing a labeled guide to its LED indicators and physical ports for troubleshooting and configuration.

**Key Components and Their Significance:**

*   **LED Indicators (1-11):** These lights provide real-time status feedback on the device's operation.
    *   **1 (VPN):** Indicates the status of the Virtual Private Network (VPN) connection.
    *   **2 (PoE LED):** Shows the Power over Ethernet status, indicating if power is being supplied to connected devices.
    *   **3 (Status):** A general system status indicator, often showing power and overall health.
    *   **4 (Ethernet Switch Ports 0-7):** This section shows the status of the 8 Ethernet ports (0-7). The ports are arranged in two rows: top row (0, 2, 4, 6) and bottom row (1, 3, 5, 7). Each port has its own LED to indicate link/activity status.
    *   **5 (Wi-Fi):** Indicates the status of the wireless (Wi-Fi) functionality.
    *   **6 (GE 0/0/1 SFP LED):** Shows the status of the SFP (Small Form-factor Pluggable) module on the second Gigabit Ethernet port (GE 0/0/1).
    *   **7 (GE 0/0/1 RJ45 LED):** Indicates the status of the RJ45 port on the second Gigabit Ethernet port (GE 0/0/1).
    *   **8 (GE 0/0/0 RJ45 LED):** Indicates the status of the RJ45 port on the first Gigabit Ethernet port (GE 0/0/0).
    *   **9 (GE 0/0/0 SFP LED):** Shows the status of the SFP module on the first Gigabit Ethernet port (GE 0/0/0).
    *   **10 (USB LED):** Indicates the status of the USB port, often used for firmware updates or connecting a USB device.
    *   **11 (Console LED):** Indicates the status of the console port, used for direct management and configuration via a terminal.

*   **Physical Ports:**
    *   **Ethernet Switch Ports (4, 8, 7, 6):** The 8 physical Ethernet ports (labeled 0-7) are used for connecting wired devices. Ports 0, 2, 4, and 6 are on the top row, while ports 1, 3, 5, and 7 are on the bottom row.
    *   **SFP Slots (9, 6):** These are slots for pluggable SFP modules, allowing for fiber optic or other high-speed connections.
    *   **RJ45 Ports (8, 7):** These are standard Ethernet ports for copper connections.
    *   **USB Port (10):** Used for connecting a USB device, typically for firmware updates or management.
    *   **Console Port (11):** A dedicated port for direct console access using a serial cable and terminal emulator software.

This diagram is essential for network administrators to quickly diagnose issues, verify connectivity, and monitor the operational status of the switch.

<--- End description image 34 --->





<--- Start caption image 35 --->

Figure 33: C1131-8PW LED Indicators

<--- End caption image 35 --->



<--- Start description image 35 --->

This diagram provides a comprehensive front-panel layout and labeling guide for the Cisco C111x series network switch, detailing the location and function of all LED indicators and physical ports. It serves as a quick-reference manual for network administrators to monitor device status, connectivity, and power.

**Key Components and Their Significance:**

*   **LED Indicators (1-11):** These are status lights that provide real-time feedback on the switch's operational state.
    *   **1 (VPN):** Indicates the status of the Virtual Private Network (VPN) functionality.
    *   **2 (PoE LED):** Shows the status of Power over Ethernet (PoE) power delivery to connected devices.
    *   **3 (Status):** A general system status indicator, often showing power and overall health.
    *   **5 (Wi-Fi):** Indicates the status of the built-in wireless (Wi-Fi) radio.
    *   **6 (GE 0/0/1 SFP LED):** Shows the status of the SFP (Small Form-factor Pluggable) port on the second Gigabit Ethernet module.
    *   **7 (GE 0/0/1 RJ45 LED):** Indicates the status of the RJ45 port on the second Gigabit Ethernet module.
    *   **8 (GE 0/0/0 RJ45 LED):** Shows the status of the RJ45 port on the first Gigabit Ethernet module.
    *   **9 (GE 0/0/0 SFP LED):** Indicates the status of the SFP port on the first Gigabit Ethernet module.
    *   **10 (USB LED):** Indicates the status of the USB port, often used for firmware updates or device connectivity.
    *   **11 (Console LED):** Indicates the status of the console port, used for direct management and configuration.

*   **Ethernet Switch Ports (4):** The switch features 8 physical Ethernet ports (labeled 0-7) arranged in two rows. The top row contains ports 0, 2, 4, and 6, while the bottom row contains ports 1, 3, 5, and 7. These ports are used for wired network connections.

*   **Physical Ports:**
    *   **SFP Slots (7 & 9):** These are slots for pluggable SFP transceivers, allowing for fiber optic or high-speed copper connections.
    *   **RJ45 Ports (5, 7, 8):** These are standard Ethernet ports for connecting devices via twisted-pair copper cables.
    *   **USB Port (10):** Used for connecting a USB device, typically for firmware updates or management.
    *   **Console Port (11):** A dedicated port for direct, out-of-band management using a console cable and terminal emulator software.

This diagram is essential for troubleshooting, as it allows technicians to quickly identify which components are active or experiencing issues by observing the corresponding LED indicators.

<--- End description image 35 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet switch ports 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) |
| 5 | Wi-Fi | 6 | GE 0/0/1 SFP LED |
| 7 | GE 0/0/1 RJ45 LED | 8 | GE 0/0/0 RJ45 LED |
| 9 | GE 0/0/0 SFP LED | 10 | USB LED |
| 11 | Console LED |  |  |


<--- Start caption table 32 --->

Table 4: C1131(X)-8PW/C1131-8PW LED Indicators

<--- End caption table 32 --->



<--- Start description table 32 --->

The table provides a comprehensive overview of the LED indicators located on the bezel and chassis of the C111x series routers, detailing their colors, meanings, and control sources. It categorizes each LED by port, including system status, VPN, LTE, GPS, WLAN, Ethernet switch ports (with and without PoE), PoE OK, WAN, DSL, and console/USB indicators, offering clear guidance on interpreting the status of various network functions and hardware components.

<--- End description table 32 --->





The following table summarizes the LED indicators that are located in the bezel or chassis of the C111x series.

| Port | LED Color | Description | Control Source |
|------|------|------|------|
| Cisco logo | Blue | Illuminated Cisco logo. Indicates that router is powered on. | Bezel side |
| Status (System status) | Green and Amber | Steady green - System is operating normally.
Off—System is not out of reset mode or BIOS image is not loadable.
Blinking Amber — BIOS/ROMmon is booting.
Steady Amber — BIOS/ROMmon has completed booting, and the system is at the ROMmon prompt or booting the platform software. | Bezel side. All models. |
| VPN OK | Green | Off— No tunnel.
Steady On— At least one tunnel is up. | Bezel side |
| LTE RSSI/mode | Green and Amber | No LEDs On—No service
1 LED On— RSSI is under -100dBm.
2 LEDs On— Low RSSI, -99dbm <> -90dBm.
3 LEDs On— Medium RSSI -89dBm <> -70dBm.
4 LEDs On— High RSSI, >-69dBm.
Green— LTE
Amber— 3G | Bezel side |
| GPS | Green | Off: GPS not configured
On: GPS configured
Blink: GPS acquiring | Bezel side |
| WLAN | Green, Red, and Amber | Green— Normal operating condition with at least one wireless client association.
Red—Ethernet link is not operational or ethernet failure.
Amber—Software upgrade is in progress. | Bezel side |
| Ethernet switch GE LAN ports, non-PoE | Green | Off— No link
Steady On— Link
Blink— TXD/RXD data | I/O side |
| Ethernet switch GE LAN ports, with PoE | Green and Amber | Off— No link, no device powered, PD denied power, power delivery fault PoE administratively disabled.
Green steady on— link; if PoE device, power is enabled.
Green Blink— TXD/RXD data
Amber - PoE fault | I/O side |
| PoE OK | Green | Green steady on— -53.5V PoE power supply connected and all powered port operating normally.
Off — No -53.5V PoE power supply connected to router. | I/O side |
| GE WAN ports | Green | Off— No link
Steady on— link
Blink— TXD/RXD data | I/O side |
| DSL CD | Green | Off— Shut
Green blink— Training, or no shut and cable disconnected.
Green steady on— Trained | I/O side |
| DSL data | Green | Off— No data activity
Green blink— TX/RX Data | I/O side |
| Console | Green | Green on— console enabled. | I/O side |
| USB console | Green | Off— No USB device discovered.
On— USB device discovered. | I/O side |
| USB | Green | Off: No USB device discovered.
On: USB device discovered. | I/O side |


<--- Start caption table 33 --->

Table 5: LED Indicators for C111x

<--- End caption table 33 --->



<--- Start description table 33 --->

The table provides a detailed summary of the LED indicators found on the bezel or chassis of the C111x series devices, including their colors, descriptions, and control sources. It categorizes each LED by function—such as power, VPN status, Ethernet and WAN link activity, LTE modem status, WLAN, and USB connectivity—offering clear guidance on what each LED's color and behavior signify during normal operation or fault conditions.

<--- End description table 33 --->







| LED | Color | Description | Control Source |
|------|------|------|------|
| Power | Green+Amber | System power status
Off:
No power
Green steady on:
Normal operation
Green blink:
Boot up phase or in ROM monitor mode
Amber steady on or blink:
Some issues with the system. | I/O |
| VPN OK | Green | VPN Status
Off:
No tunnel
Steady on:
At least one tunnel is up | I/O |
| Ethernet switch GE LAN ports | Green | Link activity
Off:
No link
Steady on:
Link
Blink:
TXD/RXD Data | I/O |
| GE WAN ports | Green | Link activity
Off:
No link
Steady on:
Link
Blink:
TXD/RXD Data | I/O |
| LTE DATA/SIM (C1101-4PLTEPWz C1101-4PLTEPC1101-4PLTEPWx) | Green and Amber | Single LTE modem (one modem with SIM switch-over capability)
Off:
Modem not up or modem up and no SIM
Amber steady on:
Modem up, SIM installed but not active.
Green Blink:
LTE data activity. | Bezel side |
| WLAN (C1101-4PLTEPWx) | 3-color LED: Green, Red and Amber; | WLAN functions | I/O |
| USB console | Green | USB console status
OFF:
USB console not active
ON:
USB console active | I/O |
| USB 3.0 | Green | USB 3.0 status
OFF:
No USB device discovered
ON:
USB device discovered
USB activity | I/O |


<--- Start caption table 34 --->

Table 6: LED Indicators for C1101 and C1109

<--- End caption table 34 --->



<--- Start description table 34 --->

This table provides a detailed overview of the LED indicators found in the bezel and chassis of the C111x series routers, including their colors, meanings, and control sources. It describes the status of various system components such as power, system health, VPN connections, LTE signal strength, GPS, wireless operations, Ethernet and PoE ports, WAN and DSL links, and console/USB devices, helping users interpret the router's operational state.

<--- End description table 34 --->





### Reset Button


The actuation of the Reset button is only recognized during ROMmon boot, that is, as the router comes to the ROMmon prompt.

The Reset button does not require much force to be pressed. The Reset button should be pressed only with a small implement such as the tip of a pen or a paper clip. When the Reset button is pressed at startup, the system LED turns green.

For more information, see the "Reset Overview" section of the Cisco 1100 Software Configuration Guide.

### Power Supply


C111x, C1121x, and C1131 Series Integrated Services Routers support PoE and PoE+ power to endpoints. The product power specifications are as follows:

• AC input voltage: Universal 100 to 240 VAC
• Frequency: 50 to 60 Hz


[30]----------------------


• Maximum output power: Up to 66W for non-PoE supply and upto 150W for PoE supply
• Optional PoE and PoE+
• Output voltage: +12VDC for system power and -53.5VDC for PoE power


### Slots and Interfaces


#### About Slots, Subslots, and Port Numbering


The Cisco 1100 series designates its interfaces using a 3-tuple notation that lists the slot, sub slot and port in the format slot/sub-slot/port. The slot number is reserved for the mother board, which is "0". Each interface type is allocated a sub slot and the port number is a unique port on the interface.

| Subslot | Interface Type |
|------|------|
| 0 | Ethernet LAN |
| 1 | Ethernet WAN |
| 2 | LTE |
| 3 | DSL |
| 4 | Wi-Fi |


<--- Start caption table 35 --->

Table 7: Slot, Bay, and Port Numbering

<--- End caption table 35 --->



<--- Start description table 35 --->

The table provides a breakdown of slot, sub-slot, and port numbering for the Cisco 1100 series routers, using a 3-tuple format (slot/sub-slot/port), with slot 0 reserved for the motherboard and each interface assigned a unique sub-slot and port number.

<--- End description table 35 --->



### Specifications of Cisco 1000 Series Integrated Services Routers


For specifications on the Cisco 1000 Series Integrated Services Routers, refer to the Cisco 1100 Series ISR Specifications document.

## Periodic Inspection and Cleaning


We recommend that you periodically inspect and clean the external surface of the router. Removing is recommended to minimize the negative impact of environmental dust or debris. The frequency of inspection and cleaning is dependent upon the severity of the environmental conditions, but we recommend cleaning the router once every six months. Cleaning involves vacuuming router air intake and exhaust vents.



Note

Sites with ambient temperatures consistently above 25°C or 77°F and with potentially high levels of dust or debris might require periodic preventative maintenance cleaning.

[31]----------------------




<--- Start description image 37 --->

This is the chapter header image for Chapter 2 of the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 24." The image uses a wide, atmospheric photograph of a modern city skyline at sunrise or sunset, with the sun creating a bright lens flare on the left. The foreground shows a vast, empty rooftop with a tiled surface, suggesting a place of preparation and potential. The large, bold number "2" and the text "CHAPTER 2" are overlaid at the bottom, clearly marking the section. The purpose of this visual is to serve as a professional and visually engaging introduction to the chapter titled "Prepare for Router Installation," using the urban landscape to metaphorically represent the foundational setup and readiness required before deploying critical network infrastructure. The image conveys a sense of scale, modernity, and the beginning of a significant technical process.

<--- End description image 37 --->



2

C H A P T E R

# Prepare for Router Installation


Before you install the Cisco 1000 Series Integrated Services Routers, you must prepare your site for the installation. This chapter provides pre-installation information, such as recommendations and requirements that should be considered before installing your router.

See the following sections to prepare for installation:

• Safety Recommendations, on page 25
• General Site Requirements, on page 26
• Rack Requirements, on page 27
• Safety Recommendations, on page 28
• Power Guidelines and Requirements, on page 28
• Network Cabling Specifications, on page 29
• Required Tools and Equipment for Installation and Maintenance, on page 31


## Safety Recommendations




Warning

IMPORTANT SAFETY INSTRUCTIONS

This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device. Statement 1071

SAVE THESE INSTRUCTIONS



Warning

Ultimate disposal of this product should be handled according to all national laws and regulations. Statement 1040.

[32]----------------------


### Safety With Electricity




Warning

Only trained and qualified personnel should be allowed to install or replace this equipment Statement 1030



Warning

Do not locate the antenna near overhead power lines or other electric light or power circuits, or where it can come into contact with such circuits. When installing the antenna, take extreme care not to come into contact with such circuits, as they may cause serious injury or death. For proper installation and grounding of the antenna, please refer to national and local codes (for example, U.S.:NFPA 70, National Electrical Code, Article 810, Canada:Canadian Electrical Code, Section 54). Statement 1052

### Prevent Electrostatic Discharge Damage


Electrostatic discharge (ESD) can damage equipment and impair electrical circuitry. It can occur if electronic printed circuit cards are improperly handled and can cause complete or intermittent failures. Always follow ESD prevention procedures when removing and replacing modules:

• Ensure that the router chassis is electrically connected to ground.
• Wear an ESD-preventive wrist strap, ensuring that it makes good skin contact. Connect the clip to an unpainted surface of the chassis frame to channel unwanted ESD voltages safely to ground. To guard against ESD damage and shocks, the wrist strap and cord must operate effectively.
• If no wrist strap is available, ground yourself by touching a metal part of the chassis.




Caution

For the safety of your equipment, periodically check the resistance value of the anti-static strap. It should be between 1 and 10 megohms (Mohm).

## General Site Requirements


This section describes the requirements your site must meet for the safe installation and operation of your router. Ensure that the site is properly prepared before beginning installation. If you are experiencing shutdowns or unusually high errors with your existing equipment, the guidelines provided in this section can also help you isolate the cause of failures and prevent future problems.



Warning

Statement 1005 -Circuit Breaker

This product relies on the building's installation for short-circuit (overcurrent) protection. Ensure that the protective device is rated not greater than: 20 A

[33]----------------------




Warning

To prevent bodily injury when mounting or servicing this unit in a rack, you must take special precautions to ensure that the system remains stable. The following guidelines are provided to ensure your safety:

• This unit should be mounted at the bottom of the rack if it is the only unit in the rack.
• When mounting this unit in a partially filled rack, load the rack from the bottom to the top with the heaviest component at the bottom of the rack.
• If the rack is provided with stabilizing devices, install the stabilizers before mounting or servicing the unit in the rack.




Warning

Statement 1044 -Port Connections

To reduce the risk of electric shock, the following ports must be connected through an approved network termination unit with integral circuit protection if the port cabling is routed outdoors:



Warning

Statement 1047 -Overheating Prevention

To reduce the risk of fire or bodily injury, do not operate the unit in an area that exceeds the maximum recommended ambient temperature of:



Warning

Statement 1076 -Clearance Around the Ventilation Openings

To prevent airflow restriction, allow clearance around the ventilation openings to be at least: 1.75 in. (4.4 cm)

### Site Selection Guidelines


The Cisco 1000 Series Integrated Services Routers require specific environmental operating conditions. Temperature, humidity, altitude, and vibration can affect the performance and reliability of the router. The following sections provide specific information to help you plan for the proper operating environment.

The Cisco 1000 Series Integrated Services Routers are designed to meet the industry EMC, safety, and environmental standards described in the Regulatory Compliance and Safety Information for the Cisco 1000 Series Integrated Services Routers document.

## Rack Requirements


For the Cisco 1000 Series Integrated Services Router, use brackets with a 19-inch rack.



Note

Rack requirements is applicable only for Cisco 1000 Series Integrated Services Routers.

[34]----------------------


The following information can help you plan your equipment rack configuration:

• Allow clearance around the rack for maintenance.
• Allow at least one rack unit of vertical space between routers; more clearance is required when stacking multiple Cisco 1000 Series Integrated Services Routers. Provide adequate heat removal mechanism to keep the surrounding air temperature well within the specified operating temperature condition.




Note

More spacing may be required depending on the installation environment.

• Enclosed racks must have adequate ventilation. Ensure that the rack is not congested because each router generates heat. An enclosed rack should have louvered sides and a fan to provide cooling air. The heat generated by the equipment near the bottom of the rack can be drawn upward into the intake ports of the equipment above it.
• When mounting a chassis in an open rack, ensure that the rack frame does not block the intake or exhaust ports. If the chassis is installed on slides, check the position of the chassis when it is seated in the rack.


## Safety Recommendations




Warning

IMPORTANT SAFETY INSTRUCTIONS

This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device. Statement 1071

SAVE THESE INSTRUCTIONS



Warning

Ultimate disposal of this product should be handled according to all national laws and regulations. Statement 1040.

## Power Guidelines and Requirements


Check the power at your site to ensure that you are receiving power that is free of spikes and noise. Install a power conditioner, if necessary.

This section lists the power requirements for the Cisco 1000 Series Integrated Services Router.

[35]----------------------


| Power Source | Input Rated | Output Rated |
|------|------|------|
| 66W AC Power Adapter (PWR-66W-AC-V2) | 100-240V, <=2A | 12 VDC, 5.5A |
| 115W AC Power Adapter (PWR-115W-AC) | 100-240VAC, 1.8A | 12V, 4.6A, -53.5V 1.12A |
| 30W AC Power Adapter (PWR-30W-AC) | 100-240 VAC, 1A | 12V , 2.5A |
| 150W AC Power Adapter (PWR-150W-AC) | 100-240 VAC, 2.5A | 12V 6.0A, -53.5V 1.55A |


<--- Start caption table 36 --->

Table 8: Power Requirements for Cisco 1000 Series Integrated Services Router

<--- End caption table 36 --->



<--- Start description table 36 --->

This table outlines the network cabling specifications and console port considerations required for installing the Cisco 1000 Series Integrated Services Router.

<--- End description table 36 --->



# Network Cabling Specifications


The following sections describe the cables and the specifications required to install Cisco 1000 Series Integrated Services Router:

# Console Port Considerations


The router includes an asynchronous serial console port. The console ports provide access to the router using a console terminal connected to the console port. This section discusses important cabling information to consider before connecting the router to a console terminal or modem.

Console terminals send data at speeds slower than modems do; therefore, the console port is ideally suited for use with console terminals.

#### EIA/TIA-232


Depending on the cable and the adapter used, this port appears as a DTE or DCE device at the end of the cable. Only one port can be used at the same time.

The default parameters for the console port are 9600 baud, 8 data bits, 1 stop bit, and no parity. The console port does not support hardware flow control. For detailed information about installing a console terminal, see the Connecting to a Console Terminal or Modem section.

For cable and port pinouts, see the Cisco Modular Access Router Cable Specifications document located on Cisco.com.

# USB Serial Console


The USB serial console port connects directly to the USB connector of a PC using a USB Type A to 5-pin micro USB Type-B cable. The USB Console supports full speed (12Mb/s) operation. The console port does not support hardware flow control.

[36]----------------------




Note

Always use shielded USB cables with a properly terminated shield.

# USB Console OS Compatibility


• Windows 10, Windows 8, Windows 7, Windows 2000, Window XP 32 bit, Windows Vista 32 bit
• Mac OS X version 10.5.4
• Redhat / Fedora Core 10 with kernel 2.6.27.5-117
• Ubuntu 8.10 with kernel 2.6.27-11
• Debian 5.0 with kernel 2.6
• Suse 11.1 with kernel 2.6.27.7-9


The default parameters for the console port are 9600 baud, 8 data bits, no parity, and 1 stop bit. For detailed information about installing a console terminal, see the Connecting to a Console Terminal or Modem section on page 3-19.

For operation with a Microsoft Windows OS version older than Windows 7, the Cisco Windows USB Console Driver must be installed on any PC connected to the console port. If the driver is not installed, the prompts guide you through a simple installation process.

The Cisco Windows USB Console Driver allows plugging and unplugging the USB cable from the console port without affecting Windows HyperTerminal operations. No special drivers are needed for Mac OS X or Linux.

Only one console port can be active at a time. When a cable is plugged into the USB console port, the RJ-45 port becomes inactive. Conversely, when the USB cable is removed from the USB port, the RJ-45 port becomes active.

Baud rates for the USB console port are 1200, 2400, 4800, 9600, 19200, 38400, 57600, and 115200 bps.



Note

Only the 5-pin micro USB Type-B is supported.

# Console Port Considerations


The router includes an asynchronous serial console port. The console ports provide access to the router using a console terminal connected to the console port. This section discusses important cabling information to consider before connecting the router to a console terminal or modem.

Console terminals send data at speeds slower than modems do; therefore, the console port is ideally suited for use with console terminals.

# Prepare for Router Installation


Before you install the Cisco 1000 Series Integrated Services Routers, you must prepare your site for the installation. This chapter provides pre-installation information, such as recommendations and requirements that should be considered before installing your router.

[37]----------------------


See the following sections to prepare for installation:

# Ethernet Connections


The IEEE has established Ethernet as standard IEEE 802.3. The routers support the following Ethernet implementations:

|  |  |
|------|------|
| 1000BASE-T—1000 Mb/s full-duplex transmission over a Category 5 or better unshielded twisted-pair (UTP) cable. | Supports the Ethernet maximum length of 328 feet (100 meters). |
| 100BASE-T—100 Mb/s full-duplex transmission over a Category 5 or better unshielded twisted-pair (UTP) cable. | Supports the Ethernet maximum length of 328 feet (100 meters). |
| 10BASE-T—10 Mb/s full-duplex transmission over a Category 5 or better unshielded twisted-pair (UTP) cable. | Supports the Ethernet maximum length of 328 feet (100 meters). |


<--- Start description table 37 --->

Table detailing the Ethernet standards supported by the routers and the required tools and equipment for installation and maintenance.

<--- End description table 37 --->



See the Cisco Modular Access Router Cable Specifications document at Cisco.com for information about Ethernet cables, connectors, and pinouts.

# Required Tools and Equipment for Installation and Maintenance


You need the following tools and equipment to install and upgrade the router and its components:

• An ESD-preventive cord and a wrist strap
• A number 2 Phillips screwdriver
• Phillips screwdrivers: small, 3/16-in. (4 to 5 mm) and medium 1/4-in. (6 to 7 mm). You might need these when you install or remove modules, and when you remove the cover (when you upgrade the memory or other components)
• Screws that fit your rack
• A wire crimper
• A wire for connecting the chassis to an earth ground: AWG 14 (2 mm²) or larger wire
• An appropriate user-supplied UL or a CSA-certified ring terminal with an inner diameter of 1/4 in. (5 to 7 mm)


[38]----------------------


[39]----------------------




<--- Start description image 54 --->

This is the chapter opener for Chapter 3 of a technical manual, titled "Install and Connect the Router." The image uses a wide, atmospheric photograph of a modern city skyline at sunrise or sunset, with the sun creating a bright lens flare on the left. The foreground is a vast, empty rooftop or plaza, suggesting a new beginning, a blank canvas, or a place for deployment. The large, bold number "3" and the text "CHAPTER 3" are overlaid in the lower right corner, clearly marking the section.

The visual metaphor of a sprawling, modern urban environment aligns perfectly with the context: the Cisco 1000 Series Integrated Services Router is a networking device designed to connect and power enterprise and business networks. The image evokes the scale and complexity of modern infrastructure, implying that the router is a foundational component in building and connecting the digital networks that underpin such environments. The empty space suggests the potential for new connections and installations, mirroring the chapter's purpose of guiding the reader through the physical setup process for the router. The overall tone is professional, forward-looking, and aspirational, setting the stage for the technical content that follows.

<--- End description image 54 --->



C H A P T E R 3

# Install and Connect the Router


This chapter describes how to install and connect Cisco 1000 Series Integrated Services Router to LAN and WANnetworks.



Read the installation instructions before using, installing or connecting the system to the power source. Statement 1004

Installing the Cisco 1000 Series Integrated Services Router involve these tasks:

• Unpack the Router, on page 33
• Set up Router on Desktop, Rack, or Wall, on page 33
• Connect Power Cable, on page 61
• Connect the Router to a Console, on page 63
• Install the Silicon Labs USB Device Driver, on page 67
• Connect WAN and LAN Interfaces, on page 68
• Configure the Router at Startup, on page 69


# Unpack the Router


Unpack the router only when you are ready to install it. If the installation site is not ready, to prevent accidental damage, keep the chassis in its shipping container until you are ready to install.

The router, accessory kit, publications, and any optional equipment you order may be shipped in more than one container. When you unpack the containers, check the packing list to ensure that you have received all the listed items.

# Set up Router on Desktop, Rack, or Wall


After unpacking, based on your requirements, you can set up a Cisco 1000 Series Integrated Services Router on a desktop, a rack, or the wall.

[40]----------------------




# Note


You can install external modules before or after mounting a router. However, if you choose to install the external modules after mounting the router on the rack or wall, ensure that you have optimal access to the back/front panel of the router.

For information on modules and Field Replaceable Units (FRUs), see the Install and Upgrade Modules and FRUs section.

Depending on the model, the available options for mounting a Cisco 1000 Series Integrated Services Router are:

| Model | Mounting Options |
|------|------|
| C111x and C1111X | Desktop, Rack Mount, Wall Mount using Key-hole Slots, Wall Mount using-Din-Rail |
| C1101-4P | Desktop, Wall Mount using Key-hole Slots |
| C1101-4PLTEPWx | Desktop, Wall Mount using Key-Hole Slots |
| C1109-2PLTExx | Desktop, Wall Mount using Key-Hole Slots, |
| C1121-4Px | Desktop, Rack Mounting using Din-Rail Brackets, Under Desk |
| C1126(X)-8PLTEP | Desktop, Rack Mounting using Din-Rail Brackets, Under Desk |
| C1128(X)-8PLTEP | Desktop, Rack Mounting using Din-Rail Brackets, Under Desk |
| C1131(X)-8PLTEPWx | Desktop, Rack Mounting using Din-Rail Brackets, Under Desk |
| C1131(X)-8PWx | Desktop, Rack Mounting using Din-Rail Brackets, Under Desk |
| C111x | Attach the C111x Top Plate (C1110-TOP-PLATE=) on Desktop, Attach the C111x Top Plate (C1110-TOP-PLATE=) for Rack Mount |
| C1121/C1161 | Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) on Desktop, Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) for Rack Mount |


<--- Start caption table 38 --->

Table 9: Models and Mounting Options

<--- End caption table 38 --->



<--- Start description table 38 --->

This table outlines the available mounting options and installation considerations for the Cisco 1000 Series Integrated Services Router, including desktop, rack, and wall mounting, with specific instructions on securing rack brackets and ensuring adequate access to the router's front and back panels when installing external modules after mounting.

<--- End description table 38 --->



If you choose to setup the router on a desktop, you can place the router on a desktop, bench top or on a shelf.

# Rack Mount


Secure the rack mounting brackets on the sides of the chassis. You must first secure rack mounting brackets on the chassis before you set up the chassis on the rack.

[41]----------------------




Caution

Do not stack multiple Cisco 1000 Series Integrated Services Routers when mounting the routers on a table top.

Do not put any object on the sides or on top of the routers ensuring that there is ample space for air circulation and heat removal.



# Important


Periodic Inspection and Cleaning : We recommend that you periodically inspect and clean the external surface of the router. Removing is recommended to minimize the negative impact of environmental dust, debris, and liquid contamination. The frequency of inspection and cleaning is dependent upon the severity of the environmental conditions, but we recommend cleaning the router once every six months. Cleaning involves vacuuming router air intake and exhaust vents.



Note

Using the top plate on the chassis significantly helps in preventing any damages that may occur from rodent infestation.



Note

Sites with ambient temperatures consistently above 25°C or 77°F and with potentially high levels of dust or debris might require periodic preventative maintenance cleaning.



Note

Whenmounting Cisco 1000 Series Integrated Services Routers on a rack, ensure that there is ample surrounding space. This ensures more heat removal, which in turn helps the surrounding air temperature to stay within the specified operating conditions.

# Attach the Rack Mount Brackets for C111x


This procedure describes how to attach the rack mount brackets on the router chassis:

Step 1 Secure the brackets to the router chassis (on the left) as shown in figure below:

# Example:


[42]----------------------




<--- Start caption image 62 --->

Figure 34: Bracket Installation for Left-Side Mounting - C111x

<--- End caption image 62 --->



<--- Start description image 62 --->

This technical diagram illustrates Step 2 of the installation procedure for a Cisco C111x router, showing how to attach the top plate (C1110-TOP-PLATE=) to the chassis and secure the mounting brackets on the right side for desktop installation.

**Key Components and Purpose:**
*   **Router Chassis:** The main body of the Cisco C111x router, shown with its front panel ports (Ethernet, console, power, etc.) and ventilation grilles.
*   **Top Plate (C1110-TOP-PLATE=):** The cover plate that is being attached to the top of the chassis. The diagram shows it being secured with screws to the chassis' mounting points.
*   **Mounting Brackets:** The metal brackets on the left and right sides of the chassis are designed to be screwed into the desktop or rack for secure mounting. The diagram specifically highlights the right-side bracket and its mounting screws.
*   **Screws and Mounting Points:** Dotted lines indicate the screw locations for securing both the top plate and the side brackets.

**Significance:**
This diagram is a critical part of the physical assembly guide for the Cisco C111x router. It provides a clear, visual instruction for the user to properly secure the top plate and side brackets, ensuring the router is safely and stably mounted on a desktop surface before proceeding with further installation steps. Proper mounting is essential for ventilation, stability, and cable management.

<--- End description image 62 --->



Step 2 Similarly, secure the brackets on the right-side of the chassis for mounting the router.


# Attach the C111x Top Plate (C1110-TOP-PLATE=) on Desktop


This procedure describes how to attach the top plate on the router chassis:

• Step 1 Use Phillips 2 screwdriver to remove two 6-32 screws on the sides of the unit.
• Step 2 Orient the top plate with the Bezel Side arrow pointing outwards.


# Example:




<--- Start caption image 63 --->

Figure 35: Removing side screws and orienting the top plate on C111x platforms

<--- End caption image 63 --->



<--- Start description image 63 --->

This technical diagram illustrates the correct orientation and attachment method for the top plate of a router chassis, as detailed in the accompanying procedure. The image serves as a visual guide to ensure proper assembly.

**Key Components and Their Purpose:**

*   **Component ① (Top Plate):** This is the main component being installed. The diagram shows its position on top of the router chassis.
*   **Component ② (Bezel Side View):** This is an inset, magnified view that highlights the critical orientation detail. The arrow indicates that the "Bezel Side" of the top plate must be oriented pointing outwards. This ensures the plate aligns correctly with the chassis and that any bezel or mounting features are positioned as intended.
*   **Component ③ (6-32 Screws):** These are the fasteners used to secure the top plate. The diagram shows their location on the sides of the chassis, corresponding to Step 1 and Step 4 of the procedure.

**Significance and Context:**

This diagram is essential for technicians performing maintenance or assembly. It visually reinforces the critical step of orienting the top plate correctly (Step 2) before securing it. Misalignment could lead to improper fit, difficulty in securing the screws, or damage to the chassis or plate. The diagram complements the text by providing a clear, unambiguous visual reference for the part and its correct orientation, ensuring the procedure is followed accurately.

<--- End description image 63 --->



|  |  |
|------|------|
| 1 | Top plate |
| 2 | Bezel side view pointing outwards |
| 3 | 6-32 screws (2x) |


<--- Start description table 39 --->

Table showing step-by-step instructions for removing and reassembling the top plate of a device, including screw removal, proper orientation using the Bezel Side arrow, alignment of side holes, and torque specifications for reattachment.

<--- End description table 39 --->





• Step 3 Lower the top plate and align side holes.
• Step 4 Use Phillips 2 screwdriver to secure the screws, torque to 6-8 in-lbs.


# Example:


Figure 36: Aligning the side holes and securing the top plate with provided screws



<--- Start description image 64 --->

This technical diagram, labeled as "Figure 36" in the surrounding context, illustrates the final assembly stage of a network or telecommunications device. It shows the unit with its top plate fully secured, as referenced in "Step 5" of the instructions.

**Key Components and Purpose:**
*   **Device Unit (1):** The main chassis of the equipment, shown from a three-quarter rear perspective. It features a variety of ports and connectors on its rear panel, including:
    *   **Ethernet ports (RJ45):** For network connectivity.
    *   **Serial/Console ports:** For local management and configuration.
    *   **Power connectors:** For supplying power to the unit.
    *   **Other interfaces:** Likely for fiber optic, coaxial, or other specialized connections.
*   **Top Plate:** The flat, rectangular cover that has been lowered and secured over the top of the unit, as described in "Step 3" and "Step 4" (aligning side holes and securing with screws to 6-8 in-lbs torque).
*   **Labeling:** The number "1" points to the entire assembled unit, and the number "467982" is a likely part or drawing number.

**Significance:**
This diagram serves as a visual confirmation for technicians or installers that the assembly process is complete. It depicts the end result of the steps described: the top plate is correctly aligned and fastened, protecting the internal components and completing the physical installation of the device. The clean, schematic style is typical of technical manuals to clearly show the final state without unnecessary detail.

<--- End description image 64 --->



|  |  |
|------|------|
| 1 | Secure the side screws |


<--- Start description table 40 --->

Figure 36: Step-by-step assembly of the top plate, including alignment of side holes and securing with provided screws to complete the unit assembly.

<--- End description table 40 --->



• Step 5 The following figure displays the top plate fully secured to the unit.


# Example:


[44]----------------------




<--- Start caption image 65 --->

Figure 37: Fully assembled C111x unit with top plate

<--- End caption image 65 --->



<--- Start description image 65 --->

This technical illustration depicts the rear view of a C111x router chassis, specifically showing the assembled unit with its top plate and rack-mount brackets, as referenced in the installation procedure. The image serves as a visual guide for the final step of the rack-mounting process, illustrating the complete configuration before installation into a standard 19-inch equipment rack.

**Key Components and Features Shown:**

*   **Rack-Mount Brackets:** The metal brackets are visibly attached to the sides of the chassis, designed to slide into a rack's rails for secure mounting.
*   **C111x Top Plate (C1110-TOP-PLATE=):** The flat, rectangular plate is shown securely fastened to the top of the router chassis, completing the assembly.
*   **Rear I/O Panel:** The back of the unit is detailed with various ports and connectors, including:
    *   Power input jacks.
    *   Network interface ports (likely Ethernet or fiber optic).
    *   Console/management ports (e.g., serial or USB).
    *   Status indicator lights.
    *   Ventilation grilles for cooling.
*   **Chassis Design:** The illustration highlights the robust, industrial design of the router, with ventilation slots on the sides and top for heat dissipation.

**Significance:**
This diagram is a critical visual aid in the installation manual. It confirms the successful completion of the assembly steps (attaching the top plate and mounting brackets) and provides a clear reference for technicians to verify that the unit is correctly prepared for rack installation. The clean, schematic style ensures that all components are clearly identifiable without extraneous detail.

<--- End description image 65 --->



# Attach the C111x Top Plate (C1110-TOP-PLATE=) for Rack Mount


This procedure describes how to rack mount top plate on the router chassis:

• Step 1 Follow the Attach the C111x Top Plate (C1110-TOP-PLATE=) on Desktop to attach C111x Top Plate for Desktop.
• Step 2 Assemble the C111x unit with top plate to rack mount brackets according to the Rack Mount procedure.
• Step 3 The following figure shows a complete assembled C111x unit with top plate and rack mount brackets.


# Example:




<--- Start caption image 66 --->

Figure 38: Fully assembled C111x unit with top plate on rack mount brackets

<--- End caption image 66 --->



<--- Start description image 66 --->

This technical illustration depicts a fully assembled Cisco 1000 Series Integrated Services Router (C111x model), showcasing the completed rack-mount configuration as described in the hardware installation guide. The image serves as a visual reference for Step 3 of the procedure, illustrating the final state after attaching the C111x top plate (C1110-TOP-PLATE=) and integrating it with the rack-mount brackets.

**Key Components and Purpose:**

*   **Rack-Mount Brackets:** The metal rails on the left and right sides of the chassis are the rack-mount brackets. These are designed to slide into standard 19-inch equipment racks, allowing the router to be securely mounted and aligned with other equipment.
*   **Top Plate:** The large, flat panel on top of the chassis is the C111x Top Plate. It provides a finished surface, protects internal components, and often serves as a mounting point for additional accessories or cables.
*   **Front Panel Interface:** The front of the unit features various ports and controls, including what appear to be console ports, power connectors, and status indicators, which are essential for initial setup and ongoing management.
*   **Ventilation:** The perforated side panels indicate the router's need for airflow to maintain optimal operating temperature.

**Significance:**

This diagram is a critical visual aid in the installation process. It confirms the successful completion of the assembly steps, ensuring that the technician has correctly attached the top plate and integrated the rack-mount brackets. It provides a clear reference for the final physical appearance of the unit before it is installed into a rack, helping to prevent errors and ensuring proper alignment and security.

<--- End description image 66 --->



[45]----------------------


# Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) on Desktop


This procedure describes how to install the top plate on the router chassis:

• Step 1 Verify the following PIDs (10.8in W x 7.85in D) for applicability:
• C1121-4P
• C1121-4PLTEP
• C1121-8PLTEP
• C1121X-8PLTEP
• C1121-8P
• C1121X-8P
• C1161-8P
• C1161X-8P
• C1161-8PLTEP
• C1161X-8PLTEP
• Step 2 Use Phillips 2 screwdriver to remove four 6-32 screws from the bottom side of the unit.


# Example:


Figure 39: Removing 4 screws from C1121/C1161 unit



<--- Start description image 67 --->

This technical diagram, labeled "Figure 39" from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide, illustrates the bottom view of a router chassis (dimensions: 10.8in W x 7.85in D) during the hardware installation process.

**Purpose:** The diagram serves as a visual guide for Step 2 of the installation procedure, which instructs the user to remove four 6-32 screws from the bottom side of the unit using a Phillips #2 screwdriver. It specifically applies to the listed router models (C1121, C1121X, C1161, C1161X variants with 4P and 8P configurations, including LTEP versions).

**Key Components Shown:**
*   **Screw Mounts:** The diagram clearly indicates the locations of the four screws that need to be removed, marked with lines pointing to their respective screw holes on the bottom panel.
*   **Router Chassis:** The outline shows the overall rectangular form factor of the device.
*   **Front Panel Features (for context):** Although the view is from the bottom, the front panel is partially visible, showing ports (Ethernet, console, etc.) and ventilation grilles, providing context for the device's function.
*   **Part Number:** The number "467965" is visible in the bottom right corner, likely a reference or part number for this specific diagram.

This diagram is essential for technicians to accurately and safely disassemble the router, ensuring the correct screws are removed from the specified locations before proceeding with further installation or maintenance steps.

<--- End description image 67 --->



[46]----------------------


• Step 3 Orient the top plate and slide it on to the unit.


# Example:


Figure 40: Installing top plate on to C1121/C1161



<--- Start description image 68 --->

This technical diagram, labeled as Figure 40 in the Cisco 1000 Series Integrated Services Router Hardware Installation Guide, illustrates Step 3 of the installation process: orienting and sliding the top plate onto the router chassis (models C1121/C1161).

**Description and Significance:**
The image is a line drawing showing the router chassis from a three-quarter perspective, highlighting the top plate being slid into place. A large black arrow points to the front edge of the chassis, indicating the direction of movement for the top plate. The diagram clearly shows the mounting holes on the top plate aligning with the corresponding holes on the chassis, which is the subject of Step 4. The front panel of the router is visible, showing ports and controls, while the rear and sides feature ventilation grilles. This visual guide is critical for technicians to ensure correct physical installation, preventing damage and ensuring proper airflow and component alignment.

<--- End description image 68 --->



• Step 4 Aligning the securing holes of top plate to C1121/C1161.


Example:

[47]----------------------




<--- Start description image 69 --->

This technical diagram, labeled "Figure 41: Aligning the securing holes of top plate to C1121/C1161," is a step-by-step visual guide from an installation manual. It illustrates the precise alignment required to attach the top plate (part number C1120-TOP-PLATE=) to the C1121 or C1161 router chassis.

**Purpose and Components:**
The diagram's purpose is to ensure the top plate is correctly positioned before fastening. It shows an isometric view of the router's underside, highlighting the mounting points. Key components depicted include:
*   The router chassis with its ports, ventilation grilles, and mounting screw holes.
*   The top plate, shown as a flat cover that will be secured over the chassis.
*   Four arrows originating from a single point labeled "1" and pointing to the four corresponding screw holes on the router's chassis. This indicates that the user must align the holes on the top plate with these specific holes on the router.

**Significance:**
This step is critical for a proper and secure installation. Misalignment could prevent the top plate from being fastened correctly, potentially leading to instability, poor heat dissipation, or damage to the device. The diagram serves as a clear, visual reference to ensure the user performs this alignment accurately before proceeding to the next step, which involves using a Phillips #2 screwdriver to tighten the screws to a torque of 6-8 in-lbs.

<--- End description image 69 --->



|  |  |
|------|------|
| 1 | Align securing holes |


<--- Start description table 41 --->

Table showing the step-by-step hardware installation instructions for attaching the top plate of the Cisco 1000 Series Integrated Services Router, including the use of a Phillips 2 screwdriver and specified torque of 6–8 in-lbs to secure the screws.

<--- End description table 41 --->



• Step 5 Use Phillips 2 screwdriver to secure screws to 6-8 in-lbs.


Example:

[48]----------------------




<--- Start description image 70 --->

This technical diagram, labeled "Figure 42: Securing top plate of C1121/C1161 with screws," illustrates a critical step in the assembly of a network device, specifically the C1121 or C1161 model. It serves as a visual guide for technicians or users following an installation manual.

**Diagram Components and Purpose:**
*   **Main Subject:** The diagram shows an isometric view of the fully assembled C1121/C1161 device, highlighting its front panel (with ports and controls) and the top surface.
*   **Key Action:** The focus is on the top plate, which is shown being secured to the main chassis using screws. Three arrows point from a labeled "1" to the screw heads on the top plate, indicating the specific locations where screws should be inserted and tightened.
*   **Annotation:** The label "1" and the accompanying text "Securing the screws" in the legend at the bottom explicitly identify the action being depicted.
*   **Purpose:** The diagram's purpose is to provide a clear, unambiguous visual instruction for the final step of attaching the top plate, ensuring the device is properly assembled and protected.

**Significance:**
This step is crucial for the physical integrity and proper functioning of the device. Securing the top plate ensures that internal components are protected from dust and physical damage, and that the device maintains a stable and secure structure. The diagram is part of a larger assembly guide, as indicated by the surrounding text, which references "Step 6 Fully assembled C1121/C1161 with secured top plate," confirming this is the concluding step in the installation process.

<--- End description image 70 --->



|  |  |
|------|------|
| 1 | Securing the screws |


<--- Start description table 42 --->

Table showing the step-by-step hardware installation of the Cisco 1000 Series Integrated Services Router, specifically illustrating the final assembly stage with the top plate securely attached to the router unit.

<--- End description table 42 --->



Step 6 Fully assembled C1121/C1161 with secured top plate.

Example:

[49]----------------------




<--- Start caption image 71 --->

Figure 43: Fully assembled C1121/C1161 with top plate

<--- End caption image 71 --->



<--- Start description image 71 --->

This technical line drawing illustrates the rear panel of a network router chassis, specifically designed for rack mounting as part of the installation procedure outlined in the accompanying text. The image serves as a visual reference for technicians installing models such as the C1121 and C1161 series.

**Key Components Shown:**
*   **Rear I/O Panel:** The back of the unit features a comprehensive array of connectivity options, including multiple Ethernet ports (likely for WAN/LAN), a console port, and other interface connectors.
*   **Ventilation Grilles:** Perforated sections on the top and sides indicate the chassis is designed for active cooling, essential for maintaining performance in a rack environment.
*   **Mounting Points:** The drawing clearly shows the locations for rack-mount brackets, which are the focus of the installation steps described in the text.
*   **Control Knobs:** Two rotary knobs are visible, likely for power or configuration controls.

**Significance:**
This diagram is a critical part of the installation guide. It visually confirms the physical form factor of the router and highlights the rear panel where the top plate and rack-mount brackets are attached. The text specifies that the top plate (C1120-TOP-PLATE=) must be installed before the unit can be secured to a rack, making this image a key reference for ensuring correct assembly and proper mounting. The dimensions provided (10.8in W x 7.85in D) are also relevant for verifying compatibility with standard 19-inch rack spaces.

<--- End description image 71 --->



# Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) for Rack Mount


This procedure describes how to attach the top plate and rack mount the brackets on the router chassis:

• Step 1 Verify the following PIDs (10.8in W x 7.85in D) for applicability:
• C1121-4P
• C1121-4PLTEP
• C1121-8PLTEP
• C1121X-8PLTEP
• C1121-8P
• C1121X-8P
• C1161-8P
• C1161X-8P
• C1161-8PLTEP
• C1161X-8PLTEP
• Step 2 Follow the Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) on Desktop to set up the router top plate (C1120-TOP-PLATE=) to the unit.
• Step 3 Align and secure the unit with top plate to rack mount the brackets.


[50]----------------------


# Step 4 Use Phillips 2 screwdriver to secure the screws to 6-8 in-lbs.


# Example:


Figure 44: Aligning and securing C1121/C1161 with top plate to rack mount brackets



<--- Start description image 72 --->

This technical diagram, labeled as Figure 44, illustrates the precise assembly step for securing the top plate to the C1121/C1161 chassis using rack mount brackets. It visually demonstrates how the top plate is aligned and fastened with screws (indicated by dashed lines and screw heads) to the upper mounting rails of the chassis, completing the structural integration of the rack mount brackets. This step is critical for ensuring the unit is properly mounted in a standard 19-inch rack and provides mechanical stability. The diagram serves as a clear, schematic guide for technicians to follow during the physical assembly process, corresponding to Step 4 in the instructions, which specifies using a Phillips #2 screwdriver and tightening the screws to 6–8 in-lbs torque. The subsequent step (Figure 45) shows the fully assembled unit, confirming the successful completion of this mounting phase.

<--- End description image 72 --->



Step 5 Fully assembled C1121/C1161 secured with top plate and rack mount brackets.


# Example:


Figure 45: Fully assembled C1121/C1161 with top plate and rack mount brackets



<--- Start description image 73 --->

**Caption:**

This technical diagram, labeled as Figure 45 in the Cisco 1000 Series Integrated Services Router Hardware Installation Guide, illustrates the fully assembled C1121/C1161 router chassis secured with its top plate and rack-mounting brackets. The image provides a clear, exploded-view perspective showing how the chassis is mounted within a standard 19-inch rack environment. Key components include:

- **Router Chassis:** The central rectangular unit, featuring ventilation grilles on the sides and rear, and interface ports on the front panel.
- **Top Plate:** A flat cover that seals the top of the chassis, providing structural integrity and protection.
- **Rack Mounting Brackets:** Two metal brackets, one on each side of the chassis, designed to slide into a rack and secure the unit using rack screws. These brackets are pre-attached to the chassis and are critical for proper installation and stability in a data center or network room.

This diagram serves as a visual guide for technicians during Step 5 of the hardware installation process, ensuring correct and secure mounting of the C112x series router for optimal airflow, physical protection, and rack compatibility. The clean, line-art style emphasizes component relationships and mounting points without extraneous detail, making it ideal for instructional use.

<--- End description image 73 --->



# Attach the Rack Mounting Brackets for C112x


This procedure describes how to attach the brackets on the router chassis:

[51]----------------------


• Step 1 Remove the 6 screws from the bottom of the chassis.
• Step 2 Place the platform into the bottom tray.
• Step 3 Secure the original screws from the bottom side of the tray.


# Example:


Figure 46: Bracket Installation for C1121-4Px, C1126-8PLTEP and C1128-8PLTEP



<--- Start description image 74 --->

**Caption:**

This technical diagram, labeled “Figure 46,” illustrates the correct installation of a mounting bracket for specific router models (C1121-4Px, C1126-8PLTEP, and C1128-8PLTEP). It visually corresponds to Step 3 of the installation procedure, which involves securing the bracket to the bottom tray using the original screws. The diagram shows the router chassis positioned beneath the mounting bracket, with screw locations clearly indicated by dashed lines and numbered points. The bracket features multiple mounting holes and cutouts for ventilation and cable management, ensuring proper alignment and secure attachment before the router is mounted in a rack. This step is critical for stability and safety, as emphasized by the preceding safety warning in the context. The diagram serves as a precise guide to prevent misalignment or damage during installation.

<--- End description image 74 --->



# Mount the Router


Before mounting the router on to the rack, refer to the following safety warning statements:



Warning

To prevent airflow restriction, allow clearance around the ventilation openings to be at least: 1.75 in. (4.4 cm). Statement 1076.

[52]----------------------




# Warning


• To prevent bodily injury when mounting or servicing this unit in a rack, you must take special precautions to ensure that the system remains stable. The following guidelines are provided to ensure your safety:
• This unit should be mounted at the bottom of the rack if it is the only unit in the rack.
• When mounting this unit in a partially filled rack, load the rack from the bottom to the top with the heaviest component at the bottom of the rack.
• If the rack is provided with stabilizing devices, install the stabilizers before mounting or servicing the unit in the rack. Statement 1006.


# Procedure


| Command or Action | Purpose |
|------|------|
| Step 1
To install the router, use the screws provided with the accessory kit to secure the router when you mount it on the rack. |  |


<--- Start description table 43 --->

Caption: This table provides safety guidelines and step-by-step instructions for mounting a router either in a rack or under a desk/shelf, emphasizing the importance of stability, proper rack loading, and the use of optional bracket kits for desk mounting.

<--- End description table 43 --->



# Mount the Router under a Desk or a Shelf


Installing the router under a desk requires an optional bracket kit that is not included with the router. The kit contains the rack-mount brackets and screws to secure the brackets to the router and the underside of the desk. You can order these kits from your Cisco representative. This procedure describes how to mount a router under a desk or a shelf .

• Step 1 Attach a bracket to one side of the router using the flat-head screws. Follow the same steps to attach the second bracket to the opposite side.




<--- Start caption image 77 --->

Figure 47: Attaching Brackets to the Router

<--- End caption image 77 --->



<--- Start description image 77 --->

This technical diagram illustrates the hardware installation procedure for mounting a Cisco 1000 Series Integrated Services Router under a desk or shelf. It visually details the components and steps required to secure the router using an optional rack-mount bracket kit.

**Key Components and Purpose:**
*   **Router:** The central device, shown with its front panel featuring ports and the "Cisco" logo.
*   **Mounting Brackets:** Two L-shaped metal brackets are depicted, one on each side of the router. These are designed to be attached to the router's chassis and then secured to the underside of a desk or shelf.
*   **Screws:** Dotted lines indicate the locations where flat-head screws are used to fasten the brackets to the router's side panels.

**Significance and Context:**
This diagram is a critical part of the router's installation guide. It provides a clear, visual reference for technicians to understand how to properly mount the device in a standard rack or under a desk, which is a common deployment scenario in office or data center environments. The diagram complements the text instructions, which specify that the bracket kit is sold separately and must be ordered from a Cisco representative. The purpose is to ensure the router is securely and correctly installed for optimal airflow, cable management, and physical stability.

<--- End description image 77 --->



[53]----------------------




<--- Start description image 78 --->

This technical diagram illustrates Step 2 of the hardware installation guide for the Cisco 1000 Series Integrated Services Router, specifically showing the router with its mounting brackets already attached, ready for wall or shelf mounting.

**Key Components and Purpose:**

*   **Figure 48 (Top Left):** Displays the type of fasteners required for installation: Flat-head Machine Screws. The diagram shows two different types: one with a standard flat head and another with a cross-shaped (Phillips) head. These screws are used to secure the router to a surface.
*   **Figure 49 (Main Image):** Shows a top-down view of the router with the mounting brackets firmly attached to its sides. The brackets are designed to be secured to a surface (like a desk or shelf) using the screws from Figure 48. The diagram clearly shows the mounting holes on the brackets aligning with the router's chassis.
*   **Router Details:** The image depicts the router's front panel, showing its ports (Ethernet, USB, console, etc.) and the Cisco logo, confirming it is a Cisco 1000 Series device.

**Significance and Context:**

This diagram is a crucial part of the installation process. It visually confirms that the router is prepared for mounting. The next step, as described in the surrounding text, is to drill a 2mm hole under the desk or shelf and insert the provided pan-head wood screws to secure the router in place. This step ensures the router is safely and stably mounted, protecting it from accidental damage and keeping it out of the way while remaining accessible for connections.

<--- End description image 78 --->



Step 2 After the brackets are attached, drill a 2 mm hole under the desk and insert the wooden screws provided. Mount the router under the desk or shelf using the pan-head wood screws).




<--- Start caption image 79 --->

Figure 50: Mounting the Router under a Desk or Shelf

<--- End caption image 79 --->



<--- Start description image 79 --->

This technical diagram illustrates Step 2 of the hardware installation guide for the Cisco 1000 Series Integrated Services Router, showing how to mount the device securely under a desk or shelf.

**Key Components and Purpose:**
*   **Router:** The Cisco 1000 Series router is depicted with its front panel visible, showing ports (RJ-45 Ethernet, console, and other interfaces) and the Cisco logo.
*   **Mounting Brackets:** Two vertical mounting brackets are shown attached to the underside of the router chassis.
*   **Desk/Shelf:** A horizontal surface (representing a desk or shelf) is positioned above the router.
*   **Hardware:** The diagram implies the use of pan-head wood screws (as mentioned in the text) to fasten the brackets to the underside of the desk or shelf, securing the router in place.

**Significance:**
This step is crucial for proper physical installation and organization. Mounting the router under a desk or shelf helps to:
*   Keep the workspace tidy and uncluttered.
*   Protect the device from accidental bumps or damage.
*   Manage cable routing more effectively by keeping the router out of the way.
*   Save valuable floor space.

The diagram serves as a clear, visual guide to ensure the router is installed correctly and securely according to the manufacturer's specifications.

<--- End description image 79 --->



[54]----------------------




<--- Start caption image 83 --->

Figure 51: Pan-head Wood Screws

<--- End caption image 83 --->









912290

# Mount Router using DIN Rail Brackets


The router is shipped with DIN Rail brackets that are to be secured on the bottom side of the chassis. Your chassis installation must allow unrestricted airflow for chassis cooling.

To attach the DIN Rail brackets to the router chassis, use the pan head machine screws and the plastic spacers provided for each bracket.

# Attach Din-Rail Brackets on C112x


This procedure describes how to attach the brackets on the router chassis:

• Step 1 Remove the 3 bottom screws from the chassis.
• Step 2 Place the din-rail tray assy on the bottom side of the chassis.
• Step 3 Secure the original screw from bottom side of tray, leverage the existing chassis screws to secure the din rail mounting bracket from the bottom of the chassis.
• Step 4 Take the other two screws to secure the din-rail trail assy.


# Example:


[55]----------------------




<--- Start caption image 84 --->

Figure 52: Attaching Din Rail Brackets for C1121-4Px, C1126-8PLTEP and C1128-8PLTEP

<--- End caption image 84 --->



<--- Start description image 84 --->

This technical diagram illustrates the mounting options for a Cisco 1000 Series Integrated Services Router, specifically detailing the hardware components and screw points required for wall mounting. The image serves as a visual guide for technicians during the installation phase, showing two primary mounting methods:

1.  **Key-hole Slots:** Located on the top and side of the router chassis, these slots are designed to accommodate mounting screws that secure the device to a wall bracket or plate. The diagram highlights the specific screw holes and their positions for this method.

2.  **DIN Rail Brackets:** These are the metal brackets shown on the underside of the router. They are designed to be attached to a standard DIN rail, which is commonly used in electrical panels and server racks. The diagram indicates the screw points for attaching these brackets to the router chassis.

The purpose of this diagram is to provide clear, step-by-step visual instructions for mounting the router, ensuring proper and secure installation. It is a critical component of the installation guide, helping users understand the physical hardware and assembly points before proceeding with the installation. The diagram is labeled with part numbers and reference points to aid in accurate assembly.

<--- End description image 84 --->



# Wall Mount the Router


Depending on the models of the Cisco 1000 Series Integrated Services Router, the tasks for mounting the router chassis on the wall may vary.

There are two ways to mount a router on the wall, using Key-hole slots and DIN Rail Brackets.



Warning

Read the wall-mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation to people and damage to the system. Statement 378.

目



Note

The recommended clearance when a router is horizontally mounted is 1.5 inches on both sides for clearance and 1.75 inches on top. I/O side clearance is needed as it is required to access the cable connections. Clearance is not required on the backside (opposite side from I/O face) unless mounting on a DIN Rail. Clearance is required to attach and mount the DIN rail bracket.

[56]----------------------


# Wall Mount Using Key-hole Slots


The Cisco 1000 Series Integrated Services Routers have key-hole slots at the bottom of the chassis for mounting on a wall or any vertical surface.



Note

Do not mount the router with the output ports facing downwards. For the C111x series, ensure that the cables are placed on the sides.



Note

When choosing a location for wall mounting the router, consider cable limitations and wall structure.



Note

To attach a router to the wall stud, each bracket should have one number 10 wood screw (pan-head) with number 10 washers, or two number 10 washer-head screws. The screws must be long enough to penetrate at least 1.5 inches (38.1 mm) into the supporting wood or metal wall stud.



Note

For hollow-wall mounting, each bracket requires two wall anchors with washers. Wall anchors and washers must be size number 6 (pan-head). Route the cables so that they do not put a strain on the connectors or mounting hardware.

[57]----------------------




<--- Start description image 91 --->

This technical diagram, titled "Figure 53: Wall Mount Using Key-hole Slots - C111x," is a schematic from the Cisco 1000 Series Integrated Services Router 51 hardware installation guide. It visually instructs the user on how to mount the router to a wall using its key-hole slots.

**Key Components and Purpose:**
*   **Router:** The image shows the top surface of a Cisco 1000 Series router, identifiable by the "CISCO" logo and "1000 Series" text.
*   **Key-hole Slots (1):** The diagram highlights the key-hole slots, which are the elongated, oval-shaped mounting holes located on the router's top panel. These slots are designed to accommodate a single screw that passes through the slot and into a wall bracket, allowing for adjustable mounting height.
*   **Mounting Point (1):** The number "1" and an arrow point to one of these key-hole slots, indicating the specific location for mounting hardware.

**Significance:**
This diagram is a critical part of the installation process. It provides a clear, visual guide to ensure the router is mounted correctly and securely to a wall, which is essential for proper ventilation, cable management, and physical stability. The use of key-hole slots allows for flexibility in positioning the device at the desired height.

<--- End description image 91 --->



|  |  |
|------|------|
| 1 | Key-hole slots |


<--- Start description table 44 --->

Table caption: This table provides step-by-step instructions for installing and mounting the Cisco 1000 Series Integrated Services Router 51 using key-hole slots, detailing the hardware installation process for the router wall mount.

<--- End description table 44 --->



[58]----------------------




<--- Start caption image 93 --->

Figure 54: Wall Mount Orientation-C111x

<--- End caption image 93 --->



<--- Start description image 93 --->

This technical diagram illustrates step [58] of the router installation process: installing and connecting the router wall mount using key-hole slots. The image shows a side view of the wall-mounting plate, which features multiple mounting holes arranged in a grid pattern. A specific key-hole slot, labeled with the number "1" and an arrow, is highlighted to indicate the correct location for securing the router to the wall. The key-hole design allows for adjustable positioning and secure attachment, ensuring the router is mounted at the desired height and angle. The diagram serves as a visual guide for users to correctly align and fasten the mounting hardware, ensuring a stable and properly positioned installation.

<--- End description image 93 --->





<--- Start description image 92 --->

This technical illustration shows the Cisco 1000 Series Integrated Services Router, highlighting its physical form and key mounting features. The image serves as a visual reference for the hardware installation guide, specifically for the step involving the use of key-hole slots to mount the router to a wall.

**Key Components and Features Illustrated:**

*   **Router Body:** The image displays the router's rectangular chassis, showing its front and side profile.
*   **Ventilation Grille:** A large, perforated grille is visible on the front face, indicating the location of the primary cooling vents for the internal components.
*   **Cisco Branding:** The "Cisco" logo is clearly marked on the front panel.
*   **Interface Ports:** The side of the router is shown with various ports and connectors, which are essential for network connectivity and management.
*   **Mounting Points:** Although not explicitly detailed in this view, the context implies the presence of key-hole slots on the router's mounting flanges (typically on the back or sides) that align with standard wall-mount brackets.

**Purpose and Significance:**

This diagram is a crucial part of the installation guide. It provides a clear visual of the device being installed, helping technicians understand the physical dimensions and orientation of the router. By showing the router's form factor, it aids in correctly positioning the mounting hardware and ensures that the key-hole slots are properly aligned with the wall bracket for a secure and stable installation. This step is fundamental for proper physical setup and environmental management of the network device.

<--- End description image 92 --->



1

Key-hole slots

[59]----------------------




<--- Start caption image 94 --->

Figure 55: Wall mount using key-hole slots - C1101-4P

<--- End caption image 94 --->



<--- Start description image 94 --->

This technical diagram illustrates the rear panel of a network router, specifically highlighting the key-hole slots (labeled "1") for wall mounting. The diagram serves as an installation guide, showing the precise location and orientation of the mounting holes. The key-hole slots are positioned at the bottom corners of the device, with a specified spacing of 3.024 inches (76.81 mm) between them, as indicated in the accompanying text. This design allows for adjustable mounting on a wall or surface using a single screw or mounting bracket, ensuring the router is securely fastened while accommodating minor variations in wall thickness or bracket alignment. The diagram also shows other rear panel components, including ports and screws, providing a complete view of the device's mounting interface.

<--- End description image 94 --->



1

Key-hole slots

Key-hole slots-spacing: 3.024 in (76.81 mm)

[60]----------------------




<--- Start caption image 95 --->

Figure 56: Wall mount using key-hole slots - C1101-4PLTEP

<--- End caption image 95 --->



<--- Start description image 95 --->

This technical diagram from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide illustrates the key-hole slots (labeled "1") on the router’s rear panel, which are used for mounting the device to a wall. The diagram highlights the precise vertical and horizontal spacing (5.758 in / 146.25 mm vertically and 3.100 in / 78.74 mm horizontally) between the mounting holes, ensuring compatibility with standard wall-mounting hardware. The purpose of this illustration is to guide technicians in securely installing the router by aligning the key-hole slots with mounting brackets, providing a stable and properly positioned setup for network infrastructure. The diagram also shows other rear panel components, including the compliance label, ventilation grilles, and interface ports, to provide context for the router’s physical layout.

<--- End description image 95 --->



1

Key-hole slots
Horizontal spacing: 3.100 in (78.74 mm)
Vertical spacing: 5.758 in (146.25 mm)


[61]----------------------




<--- Start caption image 96 --->

Figure 57: Wall mount using key-hole slots - C1109-2P

<--- End caption image 96 --->



<--- Start description image 96 --->

This technical diagram illustrates the mounting hardware layout for a router wall mount, specifically highlighting the key-hole slots for secure installation. The image shows the back panel of the mounting bracket, with two key-hole slots clearly marked by arrows and labeled as “1” — one at the top and one at the bottom. These slots are designed to accommodate a mounting screw or bolt, allowing for adjustable vertical positioning during installation. The diagram also indicates the horizontal spacing between the two key-hole slots as 7.302 inches (185.47 mm), which is critical for ensuring proper alignment and stability when mounting the router to a wall. The surrounding pattern of holes and screw locations suggests this is part of a larger assembly guide, providing users with precise measurements and component placement to ensure a secure and correctly configured installation.

<--- End description image 96 --->



1

Horizontal spacing: 7.302 in (185.47 mm)

Key-hole slots

Vertical spacing: 7.430 in (188.72 mm)



<--- Start caption image 97 --->

Figure 58: Wall mount using key-hole slots - C1109-4PLTEP

<--- End caption image 97 --->



<--- Start description image 97 --->

This is a technical diagram from the Cisco 1000 Series Integrated Services Router 55 Hardware Installation Guide, illustrating the rear mounting bracket or chassis panel for hardware installation. The diagram provides precise dimensional guidance for mounting the router in a rack or enclosure.

Key features and details shown:

*   **Mounting Holes and Slots:** The diagram clearly indicates the locations of mounting holes and key-hole slots for rack-mounting screws. These are essential for securing the router to standard 19-inch equipment racks.
*   **Spacing Dimensions:** The text above the diagram specifies the critical spacing measurements:
    *   **Horizontal spacing:** 7.302 inches (185.47 mm) — the distance between mounting points along the width of the unit.
    *   **Vertical spacing:** 7.430 inches (188.72 mm) — the distance between mounting points along the height of the unit.
*   **Ventilation and Cooling:** The shaded areas represent perforated sections designed for airflow and heat dissipation, which are critical for the router's thermal management.
*   **Hardware Components:** The diagram also shows the positions of various hardware components, including mounting screws and possibly cable management clips or tie-down points.

**Purpose:** This diagram serves as a critical reference for technicians during the physical installation of the Cisco 1000 Series router. It ensures correct and secure mounting, proper ventilation, and alignment with standard rack configurations, which is vital for the device's safe and efficient operation.

<--- End description image 97 --->





<--- Start description image 98 --->

This technical diagram illustrates the rear panel of a Cisco 1000 Series Integrated Services Router, specifically highlighting the key-hole slots for hardware installation. The image serves as a visual reference from the installation guide, showing the precise vertical spacing of 7.430 inches (188.72 mm) between the mounting slots. These slots are designed to accommodate standard mounting hardware, allowing the router to be securely fastened to a rack or enclosure. The diagram clearly depicts the router’s form factor, including the Cisco logo and the serial number 355640, providing essential information for technicians during the physical installation process.

<--- End description image 98 --->



[62]----------------------


1

Key-hole slots
Horizontal spacing: 3.100 in (78.74 mm)
Vertical spacing: 5.758 in (146.25 mm)




<--- Start caption image 99 --->

Figure 59: Wall mount using key-hole slots - C1126-8PLTEP

<--- End caption image 99 --->



<--- Start description image 99 --->

This technical diagram illustrates the rear mounting configuration for the Cisco 1000 Series Integrated Services Router, specifically detailing the wall-mounting hardware layout. It serves as a critical reference for proper installation, ensuring the device is securely and correctly affixed to a wall.

**Key Components and Purpose:**

*   **Mounting Plate:** The large rectangular plate shown is the mounting bracket that attaches to the router's rear panel. It provides the interface for securing the device to a wall.
*   **Key-hole Slots:** The diagram highlights the key-hole slots (indicated by the circular outlines with cross-hatch patterns) on the mounting plate. These slots are designed to accommodate a single screw, allowing for adjustable positioning of the router on the wall. The text in the context confirms this: "Wall Mount Using Key-hole Slots 1 Key-hole slots".
*   **Mounting Holes:** The various circular holes on the mounting plate are for securing the bracket to the router's chassis. The diagram shows different types of holes, including those for screws and possibly for additional hardware like nuts or bolts.
*   **Router Chassis:** The outline of the router itself is shown, with mounting points indicated on its rear panel. The "Cisco" logo is visible on the side, confirming the device's identity.
*   **Hardware:** The diagram includes representations of screws and nuts, indicating the type of fasteners required for installation.

**Significance:**

This diagram is an essential part of the installation guide, providing a clear visual guide for technicians to mount the router. It ensures the device is installed correctly and securely, which is crucial for its proper operation and safety. The key-hole slots allow for minor adjustments to align the router with the wall or other equipment, while the detailed layout of mounting holes ensures a stable and robust installation. The reference number "3699513" likely corresponds to a specific part or revision in the official documentation.

<--- End description image 99 --->



[63]----------------------


# Wall Mount using DIN Rail Brackets


The router is shipped with DIN Rail brackets that are to be secured on the bottom side of the chassis. Your chassis installation must allow unrestricted airflow for chassis cooling.

目



Note

Wall mount using DIN Rail brackets is applicable only for C111x.

To attach the DIN Rail brackets to the router chassis, use the PHMS screws and the plastic spacers provided for each bracket.



<--- Start caption image 101 --->

Figure 60: DIN Rail Bracket Installation - C111x and C111X

<--- End caption image 101 --->



<--- Start description image 101 --->

This technical diagram illustrates the hardware installation process for mounting the Cisco 1000 Series Integrated Services Router 57 using DIN Rail brackets, specifically for the C111x model variant.

**Key Components and Purpose:**
*   **DIN Rail Brackets (2):** These are the mounting brackets designed to allow the router to be securely attached to a standard DIN rail, commonly found in industrial control panels and telecommunications equipment racks. The diagram shows two brackets, one for each side of the router chassis.
*   **Screws (1):** These are the PHMS screws provided in the kit. They are used to fasten the DIN Rail brackets to the router's chassis. The diagram indicates that these screws are inserted through the bracket holes and into the corresponding screw holes on the router's metal casing.

**Installation Instructions:**
The diagram visually guides the user to position the DIN Rail brackets onto the router chassis and then use the provided screws to secure them. The accompanying text clarifies that this mounting method is only applicable for the C111x model and that plastic spacers (not shown in the diagram) are also required for each bracket to ensure proper alignment and secure attachment.

**Significance:**
This diagram is a critical part of the hardware installation guide, providing a clear, visual reference for technicians to correctly mount the router in a rack or panel environment, ensuring stability and proper airflow. It emphasizes the model-specific nature of the mounting hardware, preventing incorrect installation on incompatible router models.

<--- End description image 101 --->



|  |  |
|------|------|
| 1 | Screws |
| 2 | DIN Rail Brackets |


<--- Start description table 45 --->

Table showing the hardware requirements for mounting the Cisco 1000 Series ISR router using DIN rail brackets, specifying that the mount is compatible only with the C111x model and detailing the use of PHMS screws and plastic spacers for secure attachment to the router chassis.

<--- End description table 45 --->



[64]----------------------




<--- Start caption image 104 --->

Figure 61: Orientation of DIN Rail Brackets

<--- End caption image 104 --->



<--- Start description image 104 --->

This technical diagram illustrates the rear panel of a network router or telecommunications device, specifically detailing the mounting hardware for installation via DIN rail brackets. The caption “Install and Connect the Router Wall Mount using DIN Rail Brackets” accurately describes the purpose of the image.

**Key Components and Purpose:**

*   **DIN Rail Brackets:** Two identical mounting brackets are shown mounted on the upper portion of the device’s rear panel. These are standardized metal clips designed to securely attach the device to a DIN rail, which is commonly found in electrical panels, server racks, and industrial control cabinets.
*   **Mounting Holes:** The diagram clearly indicates the precise locations of screw holes for securing the brackets to the device’s chassis and for fastening the device to the DIN rail.
*   **Device Outline:** The overall rectangular shape of the device is shown, with a large blank rectangular area in the center, likely representing a space for a label, a blank panel, or a component that is not shown in this view.
*   **Side View Indication:** The vertical line labeled “L” on the right side suggests this is a side or cross-sectional view, indicating the depth of the device and the mounting bracket’s position relative to the chassis.

**Significance:**

This diagram is a crucial part of the installation manual. It provides a clear, unambiguous visual guide for technicians to correctly position and secure the DIN rail brackets before mounting the device. Proper installation ensures the device is stable, properly aligned, and safely secured within the electrical or network enclosure, which is essential for reliable operation and safety. The part number “366951” likely identifies the specific model or revision of the mounting hardware or the device itself.

<--- End description image 104 --->





<--- Start description image 102 --->

This technical illustration depicts the Cisco 1000 Series Integrated Services Router, showcasing its physical form factor and key mounting interface. The image highlights the router’s rugged, industrial design with a perforated front panel for ventilation and a side panel featuring multiple connectivity ports and interfaces. The Cisco logo is clearly visible, confirming the brand. This diagram serves as a visual reference for the hardware installation guide, specifically illustrating the router’s mounting points and physical layout to assist technicians in properly installing and connecting it using DIN rail brackets for wall or rack mounting in network environments.

<--- End description image 102 --->





<--- Start caption image 105 --->

Figure 62: DIN Rail Brackets and Mount

<--- End caption image 105 --->



<--- Start description image 105 --->

This technical diagram illustrates the hardware installation guide for mounting the Cisco 1000 Series Integrated Services Router 58 using DIN rail brackets. It provides a clear, exploded-view schematic showing how the router chassis attaches to a standard DIN rail via mounting brackets and screws.

**Key Components and Purpose:**
- **Router Chassis:** The main unit, shown with mounting holes and a cutout for the front panel.
- **DIN Rail Brackets:** Two mounting brackets are depicted—one at the top and one at the bottom—designed to clamp onto a DIN rail (commonly used in industrial and network equipment racks).
- **Mounting Hardware:** The diagram indicates the precise locations for screws and fasteners to secure the brackets to the router and to the DIN rail.
- **Mounting Orientation:** The letter “L” at the bottom right corner indicates the mounting orientation, suggesting the router should be mounted with the “L” side facing down or in a specific rotational position relative to the rail.

**Significance:**
This diagram is essential for technicians and installers to ensure proper, secure, and standardized mounting of the Cisco 1000 Series router in a rack or enclosure. Correct installation using DIN rail brackets ensures stability, proper airflow, and easy access for maintenance, while also facilitating integration into standard network infrastructure. The schematic’s clarity helps prevent installation errors and ensures compatibility with existing DIN rail systems.

<--- End description image 105 --->





<--- Start description image 103 --->

This is a technical illustration from the “Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 58 [65]”, depicting the physical form factor of the router chassis.

**Description and Significance:**

The image shows a side-view schematic of the Cisco 1000 Series Integrated Services Router. Key features visible include:

*   **Chassis Design:** The unit has a compact, rectangular metal chassis with a perforated front panel for ventilation, which is critical for maintaining optimal operating temperatures in network environments.
*   **Interface Panel:** The left side of the chassis is detailed with various ports and connectors, indicating its role as a network device capable of connecting to different types of media and services (e.g., Ethernet, serial, console, or power inputs).
*   **Branding:** The “Cisco” logo is clearly visible on the front, identifying the manufacturer and product line.

**Purpose in Context:**

This diagram serves as a visual reference within the installation guide. It helps technicians and engineers to:

1.  **Identify the Device:** Recognize the specific model (Cisco 1000 Series Integrated Services Router 58 [65]) by its physical appearance.
2.  **Understand Physical Layout:** Plan for rack mounting, cable management, and physical space requirements.
3.  **Locate Components:** Identify where ports and connectors are located for proper cabling and configuration.
4.  **Ensure Correct Installation:** Verify that the hardware being installed matches the guide’s specifications, preventing errors during setup.

In essence, this image is a foundational visual aid for the hardware installation process, providing a clear, accurate representation of the router’s physical structure to guide users through the setup.

<--- End description image 103 --->



[65]----------------------


Note

Do not over-torque the screws. The recommended torque is 8 to 10 inch-lbf (0.9 to 1.1 N-m).

# Chassis Grounding




# Warning


Only trained and qualified personnel should be allowed to install or replace this equipment Statement 1030

After you set up the router, connect the chassis to a reliable earth ground. The ground wire must be installed in accordance with local electrical safety standards. For safety information on grounding the chassis, refer to the chassis ground connection procedures.

• For grounding the chassis, use a copper wire of size of 14 AWG (2 mm²) and the ground lug. These are not a part of the accessory kit.
• Use the UNC 6-32 screws, which have a length of about 0.25 inches.


To install the ground connection for your router, perform these steps:

• Strip one end of the ground wire to the length required for the ground lug or terminal.
• For the ground lug-approximately 0.75 inch (20 mm)
• For user-provided ring terminal-as required
• Crimp the ground wire to the ground lug or ring terminal, using a crimp tool of the appropriate size.
• Attach the ground lug or ring terminal to the chassis as shown in the below figures. The screw for the ground lug is provided. Tighten the screw; the recommended torque is 8 to 10 inch-lbf (0.9 to 1.1 N-m).


[66]----------------------




<--- Start caption image 107 --->

Figure 63: Chassis Ground Connection-Cisco 111x

<--- End caption image 107 --->



<--- Start description image 107 --->

This technical diagram, titled "Figure 64: Chassis Ground Connection-Cisco 1101-4PLTEP," provides a clear, step-by-step visual guide for installing the grounding system on a Cisco 1101-4PLTEP router chassis. The purpose is to ensure electrical safety and proper grounding for the network device.

The diagram is presented in two views:
1.  **Top View:** Shows the rear panel of the router chassis, highlighting the grounding points. It indicates that a ground lug (labeled "2") is to be connected to the chassis, and a screw (labeled "1", UNC 6-32) is used to secure this connection.
2.  **Side View:** Offers a clearer perspective of the connection point, showing the ground lug (2) being attached to the chassis and secured with the screw (1).

**Key Components and Purpose:**
*   **Screw (UNC 6-32):** This is a Unified National Coarse thread screw, size 6-32, used to fasten the ground lug securely to the chassis. The UNC standard ensures compatibility with standard threaded holes.
*   **Ground Lug (2):** This is a metal terminal designed to connect the grounding wire from the building's electrical system to the router's chassis, providing a safe path for electrical current in case of a fault.

**Significance:**
This grounding procedure is a critical safety step in the installation of network equipment. It protects against electrical shock, prevents damage to sensitive electronic components from voltage surges, and ensures the device operates reliably within the network infrastructure. The diagram is part of a larger installation manual, providing technicians with precise instructions for proper setup.

<--- End description image 107 --->



|  |  |
|------|------|
| 1 | Screw (UNC 6-32) |
| 2 | Ground Lug |


<--- Start description table 46 --->

The table lists the components required for grounding the router chassis, specifying that part 1 is a UNC 6-32 screw and part 2 is a ground lug, which are used in the installation and connection process to ensure proper electrical grounding.

<--- End description table 46 --->



|  |  |
|------|------|
| 1 | Screw (UNC 6-32) |
| 2 | Ground Lug |


<--- Start description table 47 --->

This table lists the types of fasteners and components used for chassis grounding, specifying a screw with UNC 6-32 thread specification and a ground lug as the two grounding options.

<--- End description table 47 --->







<--- Start description image 108 --->

This image is a close-up of a wiring diagram or schematic component label, specifically highlighting item #2, which is identified as a “Ground Lug.”

**Caption:**
“Ground Lug (Item #2) — A terminal connector used to secure and join the grounding wire in an electrical installation, ensuring a safe, low-resistance path to earth. Shown in context with a 6-32 UNC screw for mounting, this component is critical for grounding power cables and preventing electrical hazards.”

**Significance:**
In electrical systems, ground lugs are essential for safety. They provide a reliable connection point for grounding conductors, helping to protect equipment and personnel by diverting fault currents safely to the earth. The accompanying 6-32 UNC screw indicates the fastener size used to attach the lug to a terminal or enclosure. The repeated labeling in the surrounding context suggests this is part of a standardized wiring diagram for a power or control panel assembly.

<--- End description image 108 --->





<--- Start caption image 109 --->

Figure 65: Chassis Ground Connection-Cisco 1121X-8PLTEP

<--- End caption image 109 --->



<--- Start description image 109 --->

This technical diagram illustrates the rear panel of a Cisco 1000 Series Integrated Services Router, highlighting key physical components for power and grounding. The image provides a clear, labeled view of the device’s backside, which features the Cisco logo, ventilation grilles, and various ports. The numbered callouts identify two critical elements for proper installation and safety:

*   **1. Screw (UNC 6-32):** This is a standard Unified National Coarse thread screw, used to secure the router’s chassis or to fasten the ground lug to the chassis. It is a common fastener for mounting and grounding applications in networking equipment.
*   **2. Ground Lug:** This is a metal terminal designed to connect the router’s grounding wire to the chassis, ensuring electrical safety by providing a path to earth ground. It is typically connected to the external AC power adapter’s ground pin.

The accompanying text clarifies that the router uses an external AC-to-DC power adapter, which plugs into the router’s four-point power connector. The diagram and text together serve as a guide for technicians to correctly install and ground the device, which is essential for both operational stability and user safety. The diagram’s purpose is to provide a clear, annotated reference for physical assembly and maintenance.

<--- End description image 109 --->



|  |  |
|------|------|
| 1 | Screw (UNC 6-32) |
| 2 | Ground Lug |


<--- Start description table 48 --->

Table showing the power supply specifications for the Cisco 1000 Series Integrated Services Router, including the use of an external AC to DC power adapter and the connection method to the router's 4-point power connector.

<--- End description table 48 --->



# Connect Power Cable


Power supply of the Cisco 1000 Series Intergrated Services Routers is an external AC to DC power adapter. The external DC power connector plugs into the router's 4 points power connector.

[68]----------------------




<--- Start caption image 110 --->

Figure 66: Power Cable for C111x

<--- End caption image 110 --->



<--- Start description image 110 --->

This technical illustration, labeled "Figure 68: Power Cable for 6111X," is a step-by-step visual guide from the Cisco 1000 Series Integrated Services Router 62 hardware installation manual. It depicts the rear panel of the router, clearly showing the connection point for the power cable.

The image highlights the physical installation of the power supply, a critical first step in setting up the device. A numbered arrow (1) points to the power input jack, indicating where the power cable should be plugged in. The router's rear panel is shown with various ports and connectors, including Ethernet ports, a console port, and other interface modules, providing context for the device's connectivity options.

The purpose of this diagram is to provide clear, unambiguous visual instruction to technicians or users, ensuring the router is properly powered before proceeding with other configuration steps. It is part of a larger sequence, as indicated by the surrounding text "[68]---------------------- Install and Connect the Router Connect Power Cable |  |  | |------|------| | 1. | Power Cable | Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 62," which confirms this is step 1 of the power connection process.

<--- End description image 110 --->



|  |  |
|------|------|
| 1. | Power Cable |


<--- Start description table 49 --->

Table showing the steps and instructions for installing and connecting the Cisco 1000 Series Integrated Services Router 62, including power cable connection as part of the hardware installation process.

<--- End description table 49 --->



[69]----------------------




<--- Start caption image 111 --->

Figure 67: Power Cable for C1127-8PLTEP

<--- End caption image 111 --->



<--- Start description image 111 --->

This technical illustration shows the rear panel of a Cisco 1000 Series Integrated Services Router, highlighting the first step in its initial setup: connecting the power cable. The diagram clearly labels the power input port and the corresponding power cable (labeled "1. Power Cable"), indicating the physical connection required to supply power to the device. The surrounding text context confirms this is part of a larger installation guide, specifically step one of connecting the router to a console for initial configuration. The image serves as a visual aid to ensure proper physical setup before proceeding to administrative access via the console port.

<--- End description image 111 --->



|  |  |
|------|------|
| 1. | Power Cable |


<--- Start description table 50 --->

Table showing the steps to install and connect the Cisco 1000 Series Integrated Services Router, including connecting it to a console for administrative access via a serial port.

<--- End description table 50 --->



# Connect the Router to a Console


The Cisco 1000 Series Integrated Services Router has an asynchronous serial port. This port provides administrative access to the router through a console terminal or a PC.

[70]----------------------




<--- Start caption image 112 --->

Figure 68: Console Adapter for C1101-4PLTEP

<--- End caption image 112 --->



<--- Start description image 112 --->

This technical diagram illustrates step 1 of the initial setup for a Cisco network device, showing how to connect it to a console for configuration. The image depicts a Cisco router with a Micro USB to RJ-45 console adapter (labeled as item 1) plugged into its console port. This connection is essential for out-of-band management, allowing administrators to configure the router's settings, troubleshoot issues, and perform firmware updates before the device is connected to a network. The diagram serves as a clear, instructional guide for network engineers and technicians during the device installation and initial setup phase.

<--- End description image 112 --->



1.

Micro USB to RJ-45 console adapter



<--- Start caption image 113 --->

Figure 69: Console Adapter for C1127X-8PLTEP

<--- End caption image 113 --->



<--- Start description image 113 --->

This technical illustration depicts the rear panel of a Cisco 1000 Series Integrated Services Router, showcasing its hardware interface for console access. The diagram highlights the specific port where a Micro USB to RJ-45 console adapter is connected, as indicated by the cable linking the adapter to the router's console port. This visual guide is essential for network administrators, providing a clear, step-by-step reference for initial setup and configuration of the router via a serial console connection. The adapter allows for connectivity using standard USB cables and RJ-45 Ethernet jacks, facilitating direct communication with the router's command-line interface (CLI) for troubleshooting, firmware updates, and initial configuration. The image serves as a key component of the hardware installation guide, ensuring users correctly identify and utilize the console port for device management.

<--- End description image 113 --->



1.

Micro USB to RJ-45 console adapter

[71]----------------------


Use the USB or RJ-45 console port on the router to access the Cisco Internet Operating System (IOS-XE) command line interface (CLI) on the router and perform configuration tasks. A terminal emulation program is required to establish communication between the router and a PC.

To configure the router through the Cisco IOS CLI, you must establish a connection between the router console port and either a PC or a terminal.

Use the following cables and adapters to establish a local or remote connection.

# Table 10: Local and Remote Connections


| Port Type | Cable | Action |
|------|------|------|
| Serial (RJ-45) | C111x,C1111X: RJ-45 Serial console cable
CAB-CON-USB (Serial USB to RJ-45 serial cable) | Connecting to the Serial Port with Microsoft Windows |
| Serial (USB) | C110x: CAB-CON-USB RJ-45 |  |


<--- Start description table 51 --->

Table 10 outlines the methods and equipment required to establish local and remote connections between a Cisco router and a PC, including the use of a USB Console cable and Microsoft Windows USB drivers for physical connectivity via the router's serial port.

<--- End description table 51 --->



# Connect to the Serial Port with Microsoft Windows


To establish a physical connectivity between the router and a PC, you need to install a Microsoft Windows USB.

Use the USB Console cable plugged into the USB serial port to establish this connection.

• Connect the end of the console cable with the RJ-45 connector to the light blue console port on the router.
• OR


Connect a USB 5-pin micro USB Type-B to the USB console port. If you are using the USB serial port for the first time on a Windows-based PC, install the USB driver.



# Note


You cannot use the USB port and the EIA port concurrently. When the USB port is used it takes priority over the RJ-45 EIA port.

• Connect the end of the cable with the DB-9 connector (or USB Type-A) to the terminal or PC. If your terminal or PC has a console port that does not accommodate a DB-9 connector, you must provide an appropriate adapter for that port.
• Start a terminal emulator application to communicate with the router. Configure the software with the following parameters:
• 9600 baud
• 8 data bits
• no parity
• 1 stop bit
• no flow control


[72]----------------------


# Connect to the Console Port with Mac OS X


This procedure describes how to connect a Mac OS X system USB port to the console using the built in OS X Terminal utility.

• Step 1 Use the Finder to go to Applications > Utilities > Terminal.
• Step 2 Connect the OS X USB port to the router.
• Step 3 Enter the following commands to find the OS X USB port number


# Example:


macbook:user$ cd /dev macbook:user$ ls -ltr /dev/*usb* crw-rw-rw1 root wheel 9, 66 Apr 1 16:46 tty.usbmodem1a21 DT-macbook:dev user$

# Step 4


# Connect to the USB port with the following command followed by the router USB port speed


# Example:


macbook:user$ screen /dev/tty.usbmodem1a21 9600

To disconnect the OS X USB console from the Terminal window

Enter Ctrl-a followed by Ctrl-\

# Connect to the Console Port with Linux


This procedure shows how to connect a Linux system USB port to the console using the built in Linux Terminal utility.

• Step 1 Open the Linux Terminal window.
• Step 2 Connect the Linux USB port to the router.
• Step 3 Enter the following commands to find the Linux USB port number.


# Example:


root@usb-suse# cd /dev root@usb-suse /dev# ls -ltr *ACM* crw-r--r-1 root root 188, 0 Jan 14 18:02 ttyACM0 root@usb-suse /dev#

# Step 4 Connect to the USB port with the following command followed by the router USB port speed


# Example:


root@usb-suse /dev# screen /dev/ttyACM0 9600

[73]----------------------


# To disconnect the Linux USB console from the Terminal window: Note


Enter Ctrl-a followed by : then quit.

# Install the Silicon Labs USB Device Driver


This section contains the following topics:

# Install the Silicon Labs Windows USB Device Driver


• Step 1 Go to the Silicon Labs website (www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads), and click CP210x Universal Windows Driver .
• Step 2 Unzip the downloaded folder, and select the installer for your system configuration. The Device Driver Installation Wizard begins.
• Step 3 Click Next on the Installation Wizard, then click Finish to complete installation.
• Step 4 Open the Device Manager on your system and click the Ports (COM & LPT) dropdown.
• Step 5 Insert the USB console cable and power into your system. The Device Manager refreshes and indicates the newly-detected COMport.
• Step 6 Open a terminal emulator and click the Serial connection type. Input values for the Serial Line and Speed (or Baud Rate ).
• Step 7 Click Open .
• Step 8 The terminal emulator opens. Click Enter to view the console output response.


# Install the Silicon Labs Mac USB Device Driver


• Step 1 Go to the Silicon Labs website (www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads), and click CP210x VCP Mac OSX Driver .
• Step 2 Click the Downloads folder, then click macOS_VCP_Driver folder, and double-click the SiLabsUSBDriverDisk.dmg program.
• Step 3 Click Install CP210x VCP Driver , and then click Open. The Driver Installer begins.
• Step 4 Follow installer instructions. Click Continue , scroll all the way down, then click Continue , and click Agree .
• Step 5 Click Continue , and enter your password. Then click Install Helper , and click Close .
• Step 6 Insert the USB console cable and power into your system.
• Step 7 Open a terminal and type cd/dev , and then type ls-ltr . Serial port tty.SLAB_USBtoUART appears.
• Step 8 Type screen /dev/tty.SLAB_USBtoUART <baudrate> to see console output. Console shows response upon first Enter key if there is no output.


[74]----------------------


# Connect WAN and LAN Interfaces


This section describes how to connect WAN and LAN interface cables. Before you connect the interface cables, refer to the following warning statements:



# Warning


Never install telephone jacks in wet locations unless the jack is specifically designed for wet locations. Statement 1036.



# Warning


Never touch uninsulated telephone wires or terminals unless the telephone line has been disconnected at the network interface. Statement 1037.



# Warning


For connections outside the building where the equipment is installed, the following ports must be connected through an approved network termination unit with integral circuit protection, LAN, PoE. Statement 1044.



Warning

Avoid using or servicing any equipment that has outdoor connections during an electrical storm. There may be a risk of electric shock from lightning. Statement 1088.

# Ports and Cabling


This section summarizes typical WAN and LAN connections for Cisco 1000 Series Integrated Services Router. The connections summarized here are described in detail in the Cisco Modular Access Router Cable Specifications document on cisco.com.

# Table 11: WAN and LAN Connections


| Port or Connection | Port Type, Color
1 | Connection | Cable |
|------|------|------|------|
| Ethernet | RJ-45, yellow | Ethernet hub or Ethernet switch | Category 5 or higher Ethernet |
| Gigabit Ethernet SFP, optical | LC, color according to optical wavelength | 1000BASE-SX, -LX, -LH, -ZX, -CWDM | Optical fiber as specified on applicable data sheet |
| Gigabit Ethernet SFP, copper | RJ-45 | 1000BASE-T | Category 5, 5e, 6 UTP |
| xDSL (VDSL2 / ADSL2/2+) | RJ-11 | POTS or ISDN line | RJ-11 telephone cable |


<--- Start description table 52 --->

Table 11 displays the typical WAN and LAN connection configurations for the Cisco 1000 Series Integrated Services Router, including cable color codes specific to Cisco cables, as outlined in the Hardware Installation Guide.

<--- End description table 52 --->



1 Cable color codes are specific to Cisco cables.

[75]----------------------


# Connection Procedures and Precautions


After you have installed the router chassis, perform these steps to connect the WAN and LAN interfaces:

• Connect each WAN and LAN to the appropriate connector on the chassis.
• Position the cables carefully so that you do not strain the connectors.
• Organize cables in bundles so that cables do not intertwine.
• Inspect the cables to make sure that the routing and bend radius is satisfactory. If necessary, reposition the cables.
• Install cable ties in accordance with site requirements.


# Configure the Router at Startup


After installing the router and connecting the cables, you can configure the router with basic configurations. For more information on how to configure the router, see the Cisco 1100 Series Software Configuration Guide.

[76]----------------------


[77]----------------------




<--- Start description image 119 --->

**Caption:**

This image serves as the chapter header for **Chapter 4** of a technical manual, titled “Install and Upgrade Internal Modules and Field Replaceable Units,” from the *Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 70 [77]*. The chapter focuses on the modular design of the router, emphasizing its ease of maintenance — allowing technicians to replace internal components or field-replaceable units (FRUs) without needing to return the entire device for repair.

Visually, the header uses a wide, atmospheric photograph of a modern cityscape at sunrise or sunset, with the sun casting a warm glow over a reflective rooftop or plaza. The urban skyline, featuring tall glass and steel buildings and a construction crane, symbolizes modern infrastructure, innovation, and the dynamic, evolving nature of network technology. The large, bold “CHAPTER 4” text anchors the image, clearly marking its position within the guide.

The imagery and text together convey a message of reliability, scalability, and user-friendly design — aligning with the router’s modular architecture and the guide’s purpose of empowering IT professionals to maintain and upgrade network hardware efficiently. The chapter likely details procedures for safely installing, removing, and upgrading components such as line cards, power supplies, or other FRUs, ensuring minimal downtime and maximum operational continuity for enterprise networks.

<--- End description image 119 --->



4

# Install and Upgrade Internal Modules and Field Replaceable Units


The Cisco 1000 Series Integrated Services Routers have internal modules and field-replaceable units (FRUs) that can be quickly and easily removed and replaced without having to send the entire router for repair.

This section describes how to install the internal modules and FRUs in the Cisco 1000 Series Integrated Services Routers. The information is contained in the following sections:

• Replace the Chassis Covers for C111X and C1111x, on page 71
• External Modules, on page 74
• Install and Remove Small Form Pluggable Modules, on page 75
• Install a Pluggable Interface Module, on page 76
• Installing a SIM Card on C111X, C1109-2PX, C1109-4P, on page 100
• Installing a Nano-SIM Card into a Nano-To-Micro-SIM Adapter, on page 103


# Replace the Chassis Covers for C111X and C1111x


To access the internal modules on the router, you must first remove the chassis cover. See the instructions below on how to remove and later replace the chassis cover on the routers.



Warning

Only trained and qualified personnel should be allowed to install, replace or service this equipment. Statement 1030

Cisco 1000 Series Integrated Services Routers have removable covers. Do not run the routers with the cover off. Doing so can cause the router to overheat very quickly.

Use a number-2 Phillips screw driver to perform the following tasks.

[78]----------------------


# Remove the Cover




<--- Start description image 121 --->

This technical diagram illustrates the initial step in accessing the internal components of a device, specifically showing how to remove its cover. The image is a schematic representation of a rectangular electronic unit, likely a server, network appliance, or similar hardware, with a textured top surface and ventilation grilles on the sides.

The diagram provides clear, numbered instructions for the user:
- Step 1: Points to the screws on the left side of the unit.
- Step 2: Points to the screws on the right side of the unit.

The accompanying text, “To remove the cover, do these,” confirms that the purpose of the image is to guide the user through the disassembly process. The visual explicitly indicates that the first action is to remove the 14 screws — 7 on each side — securing the cover. This is a foundational step required before proceeding with the installation or upgrade of internal modules and field-replaceable units, as mentioned in the surrounding context.

The diagram’s purpose is to provide a clear, unambiguous visual guide to ensure the user correctly identifies and removes all necessary fasteners before opening the device, thereby preventing damage and ensuring safe access to internal components.

<--- End description image 121 --->



# steps:


1 and 2

Remove the 14 screws from either side of the cover.



<--- Start description image 122 --->

This technical diagram illustrates Step 1 of the hardware installation guide for the Cisco 1000 Series Integrated Services Router, showing the process of removing the device’s cover to access internal components.

**Image Description:**
The image is a two-part schematic drawing of the router:
*   **Top View (Step 1):** Shows the router with its cover in place. A large black arrow points to the left side of the device, indicating the direction to begin the removal process. The Cisco logo is visible on the front panel.
*   **Bottom View (Step 2):** Depicts the router with its cover lifted off and shown in a hinged position above the main chassis. This view reveals the internal hardware, including circuit boards, connectors, and mounting points. A large black arrow points upward, visually representing the action of lifting the cover off the chassis.

**Purpose and Context:**
This diagram is part of a safety and installation guide. The surrounding text emphasizes critical safety procedures: "Read the Safety Warnings and disconnect the power supply before you perform any module replacement" and "Confirm the router is turned off and disconnected from the power supply." The diagram visually supports these instructions by clearly showing the first physical action required to access the router’s internal modules — removing the cover — which is a prerequisite for any subsequent hardware installation or replacement. The image serves as a clear, visual guide to ensure technicians follow the correct procedure safely.

<--- End description image 122 --->



• Step 1 Read the Safety Warnings and disconnect the power supply before you perform any module replacement.


Step 2 Confirm the router is turned off and disconnected from the power supply.

[79]----------------------


• Step 3 Disconnect all port cables connected to the router. Ensure that you do not work on the router with cables still attached to the router in the event of lightning or surges.
• Step 4 Place the chassis on a flat surface.
• Step 5 Remove the 14 cover screws on the two sides of the router cover. See figure.
• Step 6 Slide the cover from bezel side to I/O side until it stops.
• Step 7 Pull the cover vertically to disengage from the chassis.


# Replace the Cover


To replace the cover, do these steps:



# Warning


The covers are an integral part of the safety design of the product. Do not operate the unit without the covers installed. Statement 1077.



<--- Start description image 124 --->

This technical diagram illustrates the hardware installation of the cover for the Cisco 1000 Series Integrated Services Router, specifically showing the correct orientation and attachment points for the top and bottom cover assemblies.

**Key Components and Purpose:**

*   **Cover Assembly (①):** This is the top cover, which is shown detached and positioned above the router chassis. It features ventilation slots and mounting holes for screws. The diagram indicates that this cover must be secured with 14 screws on each side, as referenced in Statement 1077.1 and 2.
*   **Router Chassis (②):** This is the main body of the router, shown with the cover removed. It contains the internal components and has pre-drilled holes for the screws that attach the cover. The Cisco logo is visible on the front panel.
*   **Dotted Lines:** These lines indicate the alignment between the cover (①) and the chassis (②), showing how they fit together.

**Significance and Context:**

This diagram is part of the Hardware Installation Guide for the Cisco 1000 Series router. It is a critical safety and operational instruction, as emphasized by the warning at the top: "The covers are an integral part of the safety design of the product. Do not operate the unit without the covers installed." The image provides a clear visual guide for technicians to correctly reassemble the router, ensuring proper ventilation, electrical safety, and physical protection for internal components.

<--- End description image 124 --->



1 and 2

Replace the 14 screws on either side of the cover.

[80]----------------------




<--- Start description image 125 --->

This technical diagram illustrates Step 5 of the installation procedure for a Cisco 1000 Series Integrated Services Router, showing the correct method for securing the chassis cover.

**Caption:**
*Illustration of Step 5: Align the hooks on the router's cover with the corresponding slots on the chassis base, then lower the cover onto the chassis. This step is critical for proper enclosure assembly before proceeding with module installation. The diagram highlights the alignment points and the downward motion required to snap the cover into place.*

**Key Details:**
*   **Action:** The cover is being lowered onto the chassis base.
*   **Mechanism:** The cover features hooks that must align precisely with slots on the chassis base to ensure a secure fit.
*   **Context:** This is part of a larger, safety-critical procedure for installing or upgrading internal and external modules. The diagram visually reinforces the instruction to place the chassis on a flat surface before this step (Step 4) and is followed by Step 6, which involves sliding the cover from the I/O side to the bezel side.

<--- End description image 125 --->



• Step 1 Read the Safety Warnings and disconnect the power supply before you perform any module replacement.
• Step 2 Confirm the router is turned off and disconnected from the power supply.
• Step 3 Disconnect all port cables connected to the router. Ensure that you do not work on the router with cables still attached to the router in the event of lightning or surges.
• Step 4 Place the chassis on a flat surface.
• Step 5 Align hooks on the cover to slots on the chassis base and lower the cover onto chassis base.
• Step 6 Slide the cover from the I/O side to the bezel side
• Step 7 Install the fourteen screws on both sides of the chassis. Torque to 6-8 in-lbs.


# External Modules


This section describes how to install external modules and FRUs in the Cisco 1000 Series Integrated Services Routers. The information is contained in the following sections:



Warning

Only trained and qualified personnel should be allowed to install, replace or service this equipment. Statement 1030.

# Locate External Slots for Modules


This section describes the locations of external modules on the router motherboard.

[81]----------------------


# Install and Remove Small Form Pluggable Modules


This section describes how to install and remove Small Form Pluggable (SFP) modules in the Cisco 1000 Series Integrated Services Routers. The information is contained in the following sections:

# Install Small Form Pluggable Module


This section describes how to install optional small-form-factor pluggable (SFP) modules in the Cisco 1000 Series Integrated Services Routers to provide optical Gigabit Ethernet connectivity.

Only SFP modules certified by Cisco and complies with IEC 60825-1:2014 are supported on these routers. For more information, refer to SFPs Supported on Cisco 1100 ISRs.



Note

The SFP module-GLC-GE-100FX V01 is not supported on the Cisco111x Series.



Note

The DSL SFP module-SFP-VADSL2+-I is supported on the Cisco 1131 Series Integrated Services Routers.



Warning

Class 1 laser product. Statement 1008.



Warning

Pluggable optical modules comply with IEC 60825-1 Ed. 3 and 21 CFR 1040.10 and 1040.11 with or without exception for conformance with IEC 60825-1 Ed. 3 as described in Laser Notice No. 56, dated May 8, 2019.

# Remove Small Factor Pluggable Module


To remove a small factor pluggable (SFP) module from the chassis:

• Step 1 Disconnect all cables from the SFP.


• Step 2 Disconnect the SFP latch.


Note

SFP modules use various latch designs to secure the module in the SFP port. For information on the SFP technology type and model, see the label on the side of the SFP module.

• Tip


Use a pen, screwdriver, or other small straight tool to gently release a bale-clasp handle if you cannot reach it with your fingers.

• Step 3 Grasp the SFP on both sides and remove it from the chassis.


[82]----------------------


# Install a Pluggable Interface Module




Warning

Blank faceplates and cover panels serve three important functions: they prevent exposure to hazardous voltages and currents inside the chassis; they contain electromagnetic interference (EMI) that might disrupt other equipment; and they direct the flow of cooling air through the chassis. Do not operate the system unless all cards, faceplates, front covers, and rear covers are in place. Statement 1029.



Warning

Only trained and qualified personnel should be allowed to install, replace, or service this equipment. Statement 1030.



Warning

Pluggable optical modules comply with IEC 60825-1 Ed. 3 and 21 CFR 1040.10 and 1040.11 with or without exception for conformance with IEC 60825-1 Ed. 3 as described in Laser Notice No. 56, dated May 8, 2019. Statement 1255.

# Install a Pluggable Interface Module on a C1101-4P


To insert the pluggable interface module into the router, follow these steps:

Insert and then gently push the LTE pluggable into the pluggable slot of C1101-4P until firmly fixed. Tighten the screw, the recommended torque is 10-12 in-lb.

• Step 1
• Step 2




<--- Start caption image 134 --->

Figure 70: LTE Pluggable Interface Module - C1101-4P

<--- End caption image 134 --->



<--- Start description image 134 --->

This technical diagram illustrates the rear panel of a Cisco C1101-4P router, specifically highlighting the pluggable interface module slot and its associated components for installation and connectivity. The image serves as a visual guide for Step 1 of the installation process, which involves inserting the LTE pluggable module.

**Key Components and Their Purpose:**

*   **1 (LTE Antenna - SMA):** This is the antenna port for the LTE (Long-Term Evolution) radio module. It is used to connect an external LTE antenna to enable cellular data connectivity.
*   **2 (GPS Antenna - SMA):** This port is for connecting an external GPS antenna, which is essential for providing precise time synchronization, a critical function for network operations and security.
*   **3 (Ground Lug):** This is a grounding point. Connecting a ground lug ensures the device is properly grounded, which helps to protect against electrical surges and electromagnetic interference, improving system stability and safety.
*   **4 (Kensington Lock Slot):** This is a security feature. It allows the device to be physically secured to a desk or rack using a Kensington security cable, preventing theft or unauthorized removal.

**Significance:**
The diagram is crucial for network engineers and technicians installing the C1101-4P router. It provides a clear, labeled view of the interface module slot and its surrounding ports, ensuring correct and safe installation. The accompanying text instructs users to insert the LTE pluggable module and then tighten the screw to a specific torque (10-12 in-lb), emphasizing the importance of following precise mechanical specifications to avoid damaging the device. This visual guide ensures that the correct antennas are connected and the device is properly secured, which is vital for the router's functionality and security.

<--- End description image 134 --->



|  |  |
|------|------|
| 1 | GPS antenna (SMA) |
| 2 | LTE antenna (SMA) |
| 3 | Ground lug |
| 4 | Kensington lock slot |


<--- Start description table 53 --->

The table lists the components of the C1101-4P device, identifying positions for the GPS antenna (SMA), LTE antenna (SMA), ground lug, and Kensington lock slot, which are used during installation and secure mounting.

<--- End description table 53 --->







<--- Start caption image 135 --->

Figure 71: LTE Pluggable Interface Module - C1127X-8PLTEP

<--- End caption image 135 --->



<--- Start description image 135 --->

This is a technical diagram from the Cisco 1000 Series Integrated Services Router 77 Hardware Installation Guide, illustrating the rear panel interface and key mounting/antenna connection points.

The image provides a clear, angled view of the router's back, highlighting four critical components labeled for installation:

*   **1. GPS Antenna (SMA):** This is the connection point for a Global Positioning System antenna, which provides precise time synchronization for the router's internal clock. The SMA (Screw-on Male) connector is a standard for RF (radio frequency) connections.
*   **2. LTE Antenna (SMA):** This port is for connecting an LTE (Long-Term Evolution) cellular antenna, enabling the router to establish a wireless broadband connection via a cellular network.
*   **3. Ground Lug:** This is a grounding point, typically used to connect a grounding wire to the router's chassis. This is essential for safety and to prevent electrical interference or damage from lightning strikes.
*   **4. Kensington Lock Slot:** This is a security feature that allows the router to be physically secured using a standard Kensington security cable, preventing theft or unauthorized removal.

The diagram serves as a visual aid for technicians during the installation and configuration of the router, ensuring correct connections are made for its wireless and security functions. The small external box shown below the router is likely a separate antenna assembly or a mounting bracket for the antennas.

<--- End description image 135 --->



|  |  |
|------|------|
| 1 | GPS antenna (SMA) |
| 2 | LTE antenna (SMA) |
| 3 | Ground lug |
| 4 | Kensington lock slot |


<--- Start description table 54 --->

This table lists the hardware components and their corresponding identifiers for installation on the Cisco 1000 Series Integrated Services Router 77, including the GPS antenna, LTE antenna, ground lug, and Kensington lock slot.

<--- End description table 54 --->



[84]----------------------




<--- Start caption image 136 --->

Figure 72: LTE Pluggable Interface Module - P-LTEAP18-GL

<--- End caption image 136 --->



<--- Start description image 136 --->

This is a detailed hardware diagram from the Cisco 1000 Series Integrated Services Router 78 installation guide, illustrating the pinout and component layout for the P-LTE-P18-GL pluggable interface module (part of the C1101-4P chassis).

**Purpose:** The diagram serves as a visual reference for technicians to correctly identify and connect the module’s physical ports and indicators during installation or maintenance.

**Key Components and Their Functions:**

*   **Antenna Connectors (Ports 1, 2, 3, 4, 5, 6):** These are SMA connectors for external antennas.
    *   **Main 0 (Port 1)** and **Main 1 (Port 6)**: Primary antennas for the LTE radio.
    *   **Diversity 0 (Port 5)** and **Diversity 1 (Port 3)**: Diversity antennas used to improve signal reception by combining signals from multiple paths.
*   **Micro USB Port (Port 4):** Used for configuration, firmware updates, or diagnostics via a USB cable.
*   **LED Indicators (Ports 7, 8, 9):** Provide status information.
    *   **Enable LED (Port 7)**: Indicates if the module is powered on and operational.
    *   **SIM 0 LED (Port 8)** and **SIM 1 LED (Port 9)**: Indicate the status of the SIM cards inserted into the module.
*   **M3.5 Thumb-Screw (Port 10):** A security screw used to secure the module to the router chassis.
*   **RSSI Indicator (Port 11):** The RSSI (Received Signal Strength Indicator) LED, which is color-coded to show signal quality:
    *   **Yellow**: Indicates a very bad signal for 3G networks.
    *   **Green**: Indicates a very bad signal for 4G networks.
*   **SIM Card Slots (Ports 12, 13, 14):** These are the physical slots for inserting the SIM cards (SIM 0 and SIM 1) to enable cellular connectivity.

This diagram is critical for ensuring correct physical installation and troubleshooting connectivity issues by allowing technicians to verify that all ports are properly connected and that the status LEDs provide the expected feedback.

<--- End description image 136 --->



|  |  |
|------|------|
| 1 | PID |
| 2 | Main 0 antenna (SMA) |
| 3 | Diversity 1 antenna (SMA) |
| 4 | Micro USB |
| 5 | Diversity 0 antenna (SMA) |
| 6 | Main 1 antenna (SMA) |
| 7 | Enable LED |
| 8 | SIM 0 LED |
| 9 | SIM 1 LED |
| 0 | M3.5 thumb-screw |
| 1 | RSSI 0
Yellow: Very bad signal, 3G
Green: Very bad signal, 4G |


<--- Start description table 55 --->

Table showing the installation steps and guidelines for pluggable interface modules on a C1101-4P hardware unit of the Cisco 1000 Series Integrated Services Router.

<--- End description table 55 --->



[85]----------------------


| 2 | RSSI 1 |
|------|------|
|  | Yellow: Bad signal, 3G
Green: Bad signal, 4G |
| 3 | RSSI 2 |
|  | Yellow: Good signal, 3G
Green: Good signal, 4G |
| 4 | RSSI 3 |
|  | Yellow: Best signal, 3G
Green: Best signal, 4G |


<--- Start description table 56 --->

The table outlines the installation and upgrade procedures for internal modules and field replaceable units on a C1101-4P system, specifically detailing the status indicators for signal quality—yellow indicating a bad signal on 3G and green indicating a bad signal on 4G.

<--- End description table 56 --->





<--- Start description image 137 --->

This image is a reference legend or key for interpreting Received Signal Strength Indicator (RSSI) status lights on a C1101-4P pluggable interface module. It explains the meaning of the color-coded LED indicators (Yellow and Green) for three different RSSI levels (RSSI 1, RSSI 2, RSSI 3), each corresponding to a different signal quality and network generation (3G or 4G).

**Key Insights:**

*   **Signal Quality Progression:** The RSSI levels are ordered from worst to best signal strength:
    *   **RSSI 1:** Indicates a "Bad" signal.
    *   **RSSI 2:** Indicates a "Good" signal.
    *   **RSSI 3:** Indicates the "Best" signal.
*   **Network Generation Differentiation:** The color coding differentiates between 3G and 4G network performance:
    *   **Yellow:** Represents the signal quality for 3G networks.
    *   **Green:** Represents the signal quality for 4G networks.
*   **Purpose:** This legend is crucial for technicians or users installing or troubleshooting the C1101-4P module. By observing the color of the corresponding RSSI LED (1, 2, or 3), they can quickly determine the current signal strength and whether it is on a 3G or 4G network, aiding in diagnosing connectivity issues or verifying proper module operation.

In essence, the image provides a clear, visual guide to interpret the module's built-in signal strength indicators, enabling users to assess network performance at a glance.

<--- End description image 137 --->



• Yellow: Bad signal, 3G


• Green: Bad signal, 4G


• Yellow: Good signal, 3G


• Green: Good signal, 4G


• Yellow: Best signal, 3G




<--- Start caption image 138 --->

Figure 73: 5G Pluggable Interface Module - P-5GS6-GL

<--- End caption image 138 --->



<--- Start description image 138 --->

This is a schematic diagram of the P-5GS6-GL module, detailing its physical layout and pinout for a multi-antenna, multi-band cellular and GPS device, likely used in a test or development environment.

**Diagram Components and Purpose:**

The diagram serves as a reference guide to identify and connect the various ports and indicators on the module's top surface. It is crucial for engineers or technicians to correctly install antennas, connect power and data lines, and interpret status LEDs during setup or troubleshooting.

**Key Components:**

*   **Antennas (Ports 2, 3, 4, 5, 6):** The module features five SMA connectors for external antennas, each designated for a specific function:
    *   **Antenna 1 (Port 2):** General-purpose antenna.
    *   **GPS (Port 3):** Dedicated GPS antenna port.
    *   **Antenna 3 (Port 4):** Reception-only antenna (likely for passive or low-power applications).
    *   **Antenna 0 (Port 5):** General-purpose antenna.
    *   **Antenna 2 (Port 6):** General-purpose antenna.
*   **LED Indicators (Ports 7, 8, 9, 10, 12):** These provide real-time status feedback:
    *   **Enable LED (Port 7):** Indicates if the module is powered on and operational.
    *   **SIM 0 LED (Port 8):** Shows the status of SIM card 0 (e.g., active, locked, or error).
    *   **SIM 1 LED (Port 9):** Shows the status of SIM card 1.
    *   **GPS LED (Port 12):** Indicates GPS signal acquisition and tracking status.
    *   **Service LED (Port 11):** This is the primary status indicator for network connectivity, which is further explained in the context provided.
*   **Service LED (Port 11):** This is the central status indicator. Based on the provided context, its color indicates the quality of the cellular signal:
    *   **Yellow:** Indicates a "Good signal" on the 3G network.
    *   **Green:** Indicates a "Good signal" on the 4G network.
    *   **Yellow (again):** Indicates the "Best signal" on the 3G network.
    This suggests the module supports both 3G and 4G networks, and the LED color helps users quickly identify which network is active and the strength of the connection.

**Significance:**

This diagram is essential for anyone working with the P-5GS6-GL module. It allows for correct hardware assembly, troubleshooting connectivity issues by observing the LED indicators, and understanding the module's multi-antenna configuration for optimal signal reception across different frequencies and services (cellular and GPS).

<--- End description image 138 --->



|  |  |
|------|------|
| 1 | PID |
| 2 | antenna 1 (SMA) |
| 3 | GPS (SMA) |
| 4 | Antenna 3 (SMA, reception only) |
| 5 | Antenna 0 (SMA) |
| 6 | Antenna 2 (SMA) |
| 7 | Enable LED |
| 8 | SIM 0 LED |
| 9 | SIM 1 LED |
| 0 | GPS LED |
| 1 | M3.5 thumb-screw |
| 2 | Service LED |


<--- Start description table 57 --->

This table lists the pin assignments and corresponding functions for a device's connector, including antenna connections, GPS, SIM card indicators, and status LEDs, with pin numbers and descriptions such as "Main antenna 1 (SMA)" and "GPS LED." The color-coded signal indicators (Green: 4G, Yellow: 3G) in the surrounding text suggest the table may also relate to signal strength and connectivity features.

<--- End description table 57 --->







<--- Start caption image 139 --->

Figure 74: P-5GS6-R16SA-GL

<--- End caption image 139 --->



<--- Start description image 139 --->

This is a detailed hardware installation diagram for the Cisco 1000 Series Integrated Services Router 80, specifically illustrating the rear panel interface and component labeling for the P-5GS6-R16SA-GL model.

The diagram serves as a visual guide for technicians to correctly identify and connect the router’s physical ports and indicators. It is divided into two main sections:

1.  **The Rear Panel Layout (Top Diagram):** This shows the physical arrangement of the ports and LEDs.
    *   **Antenna and GPS Ports (2, 3, 4, 5, 6):** Five SMA connectors are labeled for antenna connections. Port 3 is designated for the GPS signal. Port 4 is explicitly noted as "reception only," indicating it is for receiving signals only, not transmitting.
    *   **LED Indicators (7, 8, 9, 0):** Four LEDs provide status information: Enable (EN), SIM 0, SIM 1, and GPS.
    *   **Service and Mounting (1, 11, 12):** Port 11 is an M3.5 thumb-screw for securing the panel. Port 12 is the Service LED, which typically indicates service or maintenance status. Port 1 is the Product ID (PID) port, used for identification.

2.  **The Component Legend (Bottom Table):** This table provides a clear, numbered reference for each component shown in the diagram, correlating the number to its function. The numbering system is consistent between the diagram and the table, making it easy to cross-reference.

**Significance:**
This diagram is critical for proper installation and troubleshooting. It ensures that antennas, GPS signals, and SIM cards are connected to the correct ports, and that technicians can accurately interpret the status of the router’s operation through its LED indicators. The explicit labeling of "reception only" for Antenna 3 is particularly important to prevent incorrect configuration that could damage the device or compromise its functionality.

<--- End description image 139 --->



|  |  |
|------|------|
| 1 | PID |
| 2 | Main antenna 1 (SMA) |
| 3 | GPS (SMA) |
| 4 | Antenna 3 (SMA, reception only) |
| 5 | Antenna 0 (SMA) |
| 6 | Antenna 2 (SMA) |
| 7 | Enable LED |
| 8 | SIM 0 LED |
| 9 | SIM 1 LED |
| 0 | GPS LED |
| 1 | M3.5 thumb-screw |
| 2 | Service LED |


<--- Start description table 58 --->

The table lists the hardware components and their corresponding pin assignments for the Cisco 1000 Series Integrated Services Router 80, providing a reference for proper installation and connectivity of various peripherals such as antennas, GPS modules, LEDs, and SIM cards.

<--- End description table 58 --->



[87]----------------------




<--- Start caption image 140 --->

Figure 75: P-LTEA7-NA

<--- End caption image 140 --->



<--- Start description image 140 --->

This is a detailed hardware installation diagram for the Cisco 1000 Series Integrated Services Router, specifically illustrating the pinout and component layout for the pluggable interface module **P-LTEA7-NA** (a 4-port LTE module for the C1101-4P chassis).

The diagram serves as a visual guide for technicians to correctly install and identify the physical components on the module’s front panel. It is critical for ensuring proper antenna and signal connectivity during hardware deployment.

**Key Components and Their Functions:**

*   **Antenna Connectors (Ports 1, 2, 3):**
    *   **Port 1 (MAIN):** Connects to the main antenna (SMA connector).
    *   **Port 2 (GPS):** Connects to the GPS antenna (SMA connector).
    *   **Port 3 (DIV):** Connects to the diversity antenna (SMA connector).

*   **Status LEDs (Ports 5, 6, 7, 9, 10, 11, 12, 13):**
    *   **Port 5 (EN):** Enable LED — Indicates the module is powered on and operational.
    *   **Port 6 (SIM 0):** SIM 0 status LED — Indicates the status of the first SIM card.
    *   **Port 7 (SIM 1):** SIM 1 status LED — Indicates the status of the second SIM card.
    *   **Port 9 (M3.5 thumb-screw):** Indicates the location of the securing screw for the module.
    *   **Port 10 (RSSI 0):** Signal strength indicator for SIM 0. *Yellow* indicates a very bad signal (3G), *Green* indicates a very bad signal (4G).
    *   **Port 11 (RSSI 1):** Signal strength indicator for SIM 1. *Yellow* indicates a bad signal (3G), *Green* indicates a bad signal (4G).
    *   **Port 12 (LTE):** LTE status LED — Indicates LTE connectivity status.
    *   **Port 13 (GPS):** GPS status LED — Indicates GPS signal acquisition status.

*   **Physical Mounting (Port 8):**
    *   **Port 8 (M3.5 thumb-screw):** The location for the M3.5 screw used to secure the module to the router chassis.

**Significance:**
This diagram is an essential part of the hardware installation guide. It ensures that technicians correctly identify and connect the antennas and LEDs, which is crucial for the proper functioning of the LTE module. The color-coded RSSI indicators provide immediate visual feedback on signal quality, helping to diagnose connectivity issues during deployment or maintenance.

<--- End description image 140 --->



|  |  |
|------|------|
| PID | Main antenna (SMA) |
| 2 | GPS (SMA) |
| 3 | Diversity antenna (SMA) |
| 4 | Enable LED |
| 5 | SIM 0 LED |
| 6 | SIM 1 LED |
| 7 | GPS LED |
| 8 | M3.5 thumb-screw |
| 9 | RSSI 0
Yellow: Very bad signal, 3G
Green: Very bad signal, 4G |
| 0 | RSSI 1
Yellow: Bad signal, 3G
Green: Bad signal, 4G |


<--- Start description table 59 --->

Table showing the installation steps and guidelines for pluggable interface modules on a C1101-4P hardware unit of the Cisco 1000 Series Integrated Services Router.

<--- End description table 59 --->



[88]----------------------


# RSSI 2 2 1


• Yellow: Good signal, 3G
• Green: Good signal, 4G


# RSSI 3 3 1


• Yellow: Best signal, 3G
• Green: Best signal, 4G




<--- Start caption image 141 --->

Figure 76: PLTEA-LA with Micro SIM Slots

<--- End caption image 141 --->



<--- Start description image 141 --->

This is a detailed schematic diagram of the P-LTEA-LA LTE pluggable module, illustrating its physical layout, component labeling, and signal indicator system for network connectivity.

**Diagram Components and Purpose:**
The diagram serves as a user guide for identifying and interacting with the module’s ports and indicators. It clearly labels 14 key points on the module’s top surface:

*   **Antennas (1-4):** 
    *   1: Main antenna (SMA connector)
    *   2: GPS antenna (SMA connector)
    *   3: Diversity antenna (SMA connector)
    *   4: LTE antenna (SMA connector)
*   **LED Indicators (5-8):**
    *   5: Enable LED (EN)
    *   6: SIM 0 LED
    *   7: SIM 1 LED
    *   8: GPS LED
*   **Physical Connectors (9-14):**
    *   9: M3.5 thumb-screw (for securing the module)
    *   10: Micro USB 2.0 port (for power and data)
    *   11: RSSI 0 (Received Signal Strength Indicator 0)
    *   12: RSSI 1
    *   13: RSSI 2
    *   14: RSSI 3

**Signal Indicator System:**
The module features a color-coded RSSI (Received Signal Strength Indicator) system to visually communicate network signal quality. The color and the network generation (3G or 4G) are paired as follows:

*   **Yellow:** Indicates a weaker signal.
    *   Very Bad Signal (3G) / Very Bad Signal (4G) — RSSI 0
    *   Bad Signal (3G) / Bad Signal (4G) — RSSI 1
*   **Green:** Indicates a stronger signal.
    *   Good Signal (3G) / Good Signal (4G) — RSSI 2
    *   Best Signal (3G) / Best Signal (4G) — RSSI 3

This system allows users to quickly assess the quality of their 3G or 4G connection based on the color of the corresponding RSSI LED. The diagram is part of a larger guide on inserting a Micro-SIM card into the module, making it essential for proper setup and troubleshooting.

<--- End description image 141 --->



|  |  |
|------|------|
| 1 | PID |
| 2 | Main antenna (SMA) |
| 3 | GPS (SMA) |
| 4 | Diversity antenna (SMA) |
| 5 | Enable LED |
| 6 | SIM 0 LED |
| 7 | SIM 1 LED |
| 8 | GPS LED |
| 9 | M3.5 thumb-screw |
| 0 | Micro USB 2.0 |
| 1 | RSSI 0
• Yellow: Very bad signal, 3G
• Green: Very bad signal, 4G |
| 2 | RSSI 1
• Yellow: Bad signal, 3G
• Green: Bad signal, 4G |
| 3 | RSSI 2
• Yellow: Good signal, 3G
• Green: Good signal, 4G |
| 4 | RSSI 3
• Yellow: Best signal, 3G
• Green: Best signal, 4G |


<--- Start description table 60 --->

This table illustrates the RSSI (Received Signal Strength Indicator) values and their corresponding signal quality indicators for a 3G and 4G network, where "Yellow" denotes the best signal for 3G and "Green" denotes the best signal for 4G. It provides context for understanding signal strength when inserting a Micro-SIM card into an LTE pluggable module.

<--- End description table 60 --->





This section describes how to insert a Micro-SIM card into an LTE pluggable module.

To insert the Micro-SIM cards into an LTE Pluggable module:



# Note


Ensure to use the correct tool for removing the Micro-SIM door.

• Place the pluggable module on its bottom side, remove the SIM door screw, use a #1 Philips screw driver for removing the screws, and then carefully remove the Micro-SIM cover from the pluggable module.




# Caution


Do not touch any part of the exposed PCB circuit area when the Micro-SIM cover is removed.

• Slot 1 and slot 0 are the Micro-SIM slots. (see figure 5, step 2).
• Install SIM 0 and SIM 1 in their respective slots. SIM 0 or SIM 1 is marked on the pluggable interface module above the Micro-SIM cover. The SIM icons show the correct orientation required to install the SIM into each respective connector (SIM connectors are a push-push type).


To install, insert the SIM card in the connector until you feel it click, then let go and the SIM is locked to the connector. To remove the SIM card, depress the SIM in the connector slot again until you feel the

[90]----------------------


same click and let it go, the SIM connector should eject part way out of the connector. The SIM card can then be grabbed and removed).

Secure the Micro-SIM cover with a screw, use a number 1 Philips screw driver to secure the screw on the Micro-SIM cover. The recommended torque is 2.8 - 3.8 inch LBF.



# Note


We recommend using industrial-grade SIM cards.

• You have now successfully inserted the Micro-SIM cards into the LTE pluggable module. The marking on the Mirco-SIM door should align with Micro-SIM 0 on the pluggable module with the arrow pointing upward.




<--- Start caption image 145 --->

Figure 77: Insert the Micro-SIM Cards

<--- End caption image 145 --->



<--- Start description image 145 --->

This diagram from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide illustrates the step-by-step procedure for inserting a Micro-SIM card into the LTE pluggable module. It is a technical illustration designed to guide network administrators or technicians during hardware installation.

The process is broken down into four clear steps:

*   **STEP 1:** The image shows the pluggable module with the Micro-SIM card tray (labeled 4) in its closed position, indicating the starting point before insertion.
*   **STEP 2:** The tray is partially opened, revealing the slot for the Micro-SIM card. The diagram highlights the correct orientation: the marking on the tray (labeled 1) must align with the "Micro-SIM 0" slot on the module, and the arrow on the tray (labeled 2) must point upward.
*   **STEP 3:** The Micro-SIM card is shown being inserted into the slot. The diagram uses arrows (labeled 3) to indicate the correct direction for insertion, ensuring the card is seated properly.
*   **STEP 4:** The tray is fully closed, securing the Micro-SIM card in place. The final image shows the module with the tray latched, indicating the successful completion of the installation.

This visual guide is critical for ensuring correct hardware configuration, as improper insertion can lead to connectivity issues or damage to the module. It directly supports the context provided, which emphasizes using industrial-grade SIM cards and aligning the tray's marking with the module's designated slot.

<--- End description image 145 --->



# Configuring a Pluggable Interface Module


To insert the antenna in the Pluggable Interface Module, perform the following steps:

[91]----------------------




<--- Start caption image 146 --->

Figure 78: Attaching the Antennas

<--- End caption image 146 --->



<--- Start description image 146 --->

This instructional diagram illustrates Step 1 of installing antenna modules onto a pluggable interface module, as part of a larger procedure for configuring internal modules and field-replaceable units. The image provides a clear, close-up view of a hand using thumb and index finger to insert and tighten two specific antennas—labeled as Antenna 1 and Antenna 3—into their designated middle attachment slots (indicated by arrows). The diagram highlights the precise manual action required for secure installation, emphasizing the importance of proper torque to ensure reliable signal transmission. The numbered labels (1, 2, 3, 0) point to key components: Antennas 1 and 3 are the primary focus, while the other labels likely indicate surrounding hardware or connection points for context. This step is critical for the correct operation of the wireless communication system, as improper antenna installation could lead to signal degradation or device malfunction. The diagram’s clean, technical style is typical of manufacturer manuals, ensuring clarity for technicians performing field maintenance or equipment assembly.

<--- End description image 146 --->



20020

• Step 1 Use your thumb and index finger to insert and tighten antenna 1 and antenna 3 in the middle antenna attachment slots, as indicated in the figure.


Note

While installing the antennas, first install antenna 1 and antenna 3 (this instruction is for the two antenna attachments present in the middle) and secure it completely. If you install antenna 2 and antenna 0 first (this refers to the first and the last antenna attachments), there will be less space to insert your thumb and index finger and therefore, you may not be able to secure antenna 1 and 3.

• Step 2 Insert antenna 2 and antenna 0 in the first and last antenna attachment slots.
• Step 3 After installing the antennas, adjust the antenna orientation by spacing out each of them equally until they are spread out. This is important because it helps in getting higher RF performance.


[92]----------------------




<--- Start description image 147 --->

This technical line drawing illustrates the antenna assembly for the P-5GS6-GL and P-5GS6-R16SA-GL wireless communication devices, as referenced in the accompanying text about RF band mapping for antenna ports. The diagram shows a rectangular base unit with four distinct, vertically oriented, high-gain antenna elements mounted on top. Each antenna is connected to the base via a threaded coupling, and the base unit features visible mounting points and a connector port, indicating its role as a field-replaceable unit (FRU) within a larger system. The image serves as a schematic reference for installation, upgrade, or maintenance procedures, providing a clear visual of the physical form factor and mounting configuration of the antenna module. The number "3658 10" in the corner likely denotes a part number or drawing identifier.

<--- End description image 147 --->



# RF Band Mapping for Antenna Ports (For P-5GS6-GL and P-5GS6-R16SA-GL)


The following table lists the RF band mapping for antenna ports.

# RF Band Mapping for Antenna Ports for P-5GS6-GL


| Antenna Port | Technology | TX | RX |
|------|------|------|------|
| ANT 0 | 3G
WDCMA | B1, B2, B3, B4, B5, B6, B8, B9, B19 | B1, B2, B3, B4, B5, B6, B8, B9, B19 |
| ANT 0 | LTE | B1, B2, B3, B4, B5, B7, B8, B12, B13, B14, B17, B18, B19, B20, B25, B26, B28, B30, B34, B38, B39, B40, B41, B66, B71 | B1, B2, B3, B4, B5, B7, B8, B12, B13, B14, B17, B18, B19, B20, B25, B26, B28, B29, B30, B32, B34, B38, B39, B40, B41, B42, B43, B46, B48, B66, B71 |
| ANT 0 | 5G NR FR1 | n1, n2, n3, n5, n7, n8, n12, n20, n28, n38, n40, n41, n66, n71 | n1, n2, n3, n5, n7, n8, n12, n20, n25, n28, n38, n40, n41, n48, n66, n71, n77, n78, n79 |
| ANT 1 | 3G WDCMA | - | B1, B2, B3, B4, B5, B6, B8, B9, B19 |
| ANT 1 | LTE | B5, B20, B42, B43, B48, B71 | B1, B2, B3, B4, B5, B7, B8, B12, B13, B14, B17, B18, B19, B20, B25, B26, B28, B29, B30, B32, B34, B38, B39, B40, B41, B42, B43, B46, B48, B66, B71 |
| ANT 1 | 5G NR FR1 | n5, n48, n77, n78, n79 | n1, n2, n3, n5, n7, n8, n12, n20, n25, n28, n38, n40, n41, n48, n66, n71, n77, n78, n79 |
| ANT 2 | 3G WDCMA | - | - |
| ANT 2 | LTE | B1, B2, B3, B4, B7, B41, B66 | B1, B2, B3, B4, B7, B25, B30, B32, B34, B38, B39, B40, B41, B42, B43, B46, B48, B66 |
| ANT 2 | 5G NR FR1 | n1, n2, n3, n7, n25, n41, n66, n77, n78, n79 | n1, n2, n3, n7, n25, n38, n40, n41, n48, n66, n77, n78, n79 |
| ANT 3 | 3G WDCMA | - | - |
| ANT 3 | LTE | - | B1, B2, B3, B4, B7, B25, B30, B32, B34, B38, B39, B40, B41, B42, B43, B46, B48, B66 |
| ANT 3 | 5G NR FR1 | - | n1, n2, n3, n7, n25, n38, n40, n41, n48, n66, n77, n78, n79 |


<--- Start description table 61 --->

This table provides the RF band mapping for antenna ports of the P-5GS6-GL and P-5GS6-R16SA-GL devices, specifying the radio access technology, supported frequency bands, transmit and receive antenna configurations, and GNSS antenna usage, with default and alternate path options for transmit antennas.

<--- End description table 61 --->





# RF Band Mapping for Antenna Ports for P-5GS6-R16SA-GL


| Radio Access Technology (RAT) | Bands | Tx Antennas | Rx Antennas | GNSS Antenna |
|------|------|------|------|------|
|  |  | Default
Alternate Path | ANT0
ANT1
ANT2
ANT3 | GPS |


<--- Start description table 62 --->

This table provides the RF band mappings for different antenna ports (ANT 0 to ANT 3) across various wireless technologies—3G WDCMA, LTE, and 5G NR FR1—on the Cisco 1000 Series Integrated Services Router 87. It specifies the transmit (TX) and receive (RX) frequency bands (denoted by band identifiers such as B1–B9 or n1–n79) supported by each antenna port, enabling proper configuration for hardware installation and network compatibility.

<--- End description table 62 --->



[94]----------------------


| Radio Access Technology (RAT) | Bands | Tx Antennas | Rx Antennas | GNSS Antenna |  |  |  |  |
|------|------|------|------|------|------|------|------|------|
| 5GNR Sub-6G | 29 | - | - | Y | - | Y | - | - |
| 5GNR Sub-6G | 38, 41 | ANT2 | ANT0 | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 48 | ANT3 | ANT1 | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 75, 76 | - | - | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 77, 78 | ANT3 | ANT1 ANT2 | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 79 | ANT3 | ANT1 | Y | Y | Y | Y | - |
| LB LTE/ 5GNR Sub-6G | 5, 8, 12, 13, 14, 17, 18, 19, 20, 26, 28, 71 | ANT0 | - | Y | - | Y | - | - |
| MB/HB LTE/ 5G NR Sub-6G | 1, 2, 3, 4, 7, 25, 30, 39, 40, 66, 70 | ANT0 | - | Y | Y | Y | Y | - |
| LTE | 29 | - | - | Y | - | - | Y | - |
| LTE | 34 | ANT0 | - | Y | - | Y | - | - |
| LTE | 46 | - | - | Y | - | - | Y | - |
| LTE | 32 | - | - | Y | Y | Y | Y | - |
| LTE | 38 | ANT0 | - | Y | Y | Y | Y | - |
| LTE | 41 | ANT0 | ANT2 | Y | Y | Y | Y | - |
| LTE | 42, 43, 48 | ANT3 | ANT1 | Y | Y | Y | Y | - |
| WCDMA | 1, 2, 4, 5, 8, 19 | ANT0 | - | Y | - | Y | - | - |
| GNSS | - | - | - | - | - | - | - | L1 |


<--- Start description table 63 --->

Table showing the RF band mapping for antenna ports specific to the P-5GS6-GL and P-5GS6-R16SA-GL models of the Cisco 1000 Series Integrated Services Router 88, detailing hardware installation and internal module/field replaceable unit upgrades.

<--- End description table 63 --->



[95]----------------------


# LED Behaviors


The following table lists the LED indicators and their behavior. The LEDs provide a visual indication of the status and the currently selected services.

# LED Indicators:


| LED | Color | Function |
|------|------|------|
| EN | Green, Yellow | Enable LED
• Pluggable enable LED
• Off: System power is off
• Yellow: Module power is not functioning correctly
• Green: Module power is on |
| SIM0 | Green, Yellow | SIM0 LED/Activity
• SIM0 LED status and WWAN activity
• Off: SIM0 is not installed
• Yellow: SIM0 is installed, but not active
• Green: SIM0 installed and active
• Green Blink: LTE data activity |
| SIM1 | Green, Yellow | SIM1 LED/Activity
• SIM1 LED status and WWAN activity
• Off: SIM1 is not installed
• Yellow: SIM1 is installed, but not active
• Green: SIM1 installed and active
• Green Blink: LTE data activity |
| GPS | Green, Yellow | GPS LED
• Off: GPS is not configured
• Yellow: Software is defined
• Green: GPS is configured
• Green Blink: GPS is functional |
| Service | Green, Yellow, Blue | Service Indication LED (Applicable for P-5GS6-GL)
• Yellow: 3G
• Green: 4G LTE |
|  |  | Blue: 5G |
| RSSI | Green, Yellow | RSSI LED (Applicable for P-LTE-XX, P-LTEA-XX, P-LTEAP18-GL )
Green: 4G LTE
Yellow: 3G |


<--- Start description table 64 --->

The table outlines the LED indicators and their corresponding behaviors, providing visual feedback on the status and currently selected services, with a specific reference to the process of attaching antennas to the Pluggable Interface Module.

<--- End description table 64 --->





# Attaching the Antennas


To attach the antenna in the Pluggable Interface Module, perform the following steps.

[97]----------------------




<--- Start caption image 148 --->

Figure 79: Attaching the 5G New Radio (NR) Antenna (5G-ANTM-O4-B) to P-5GS6-GL PIM

<--- End caption image 148 --->



<--- Start description image 148 --->

This technical diagram illustrates the correct physical installation and cable mapping for attaching the 5G NR Antenna (model 5G-ANTM-04-B) to the P-5GS6-GL PIM (Printed Circuit Board Module). It serves as a critical visual guide for technicians during the installation and upgrade process, ensuring proper connectivity and secure attachment.

**Key Components and Purpose:**

*   **Antenna Assembly (Top):** The diagram shows the 5G NR antenna, which is a multi-port, directional antenna designed for 5G networks. It features multiple SMA (SubMiniature version A) connectors at its base.
*   **P-5GS6-GL PIM (Bottom):** This is the specific PIM model mentioned in the context. The diagram highlights its rear panel, which contains the SMA ports for antenna connection.
*   **Cable Mapping:** Lines with arrows clearly indicate which SMA cable from the antenna must be connected to which port on the P-5GS6-GL PIM. The ports are labeled as `φ1`, `φ2`, `φ3`, and `φ4`, corresponding to the antenna's ports.
*   **Security Requirement:** The diagram visually reinforces the instruction to "tighten and secure each SMA cable into the SMA connector on the PIM," ensuring a stable, low-loss connection critical for 5G signal integrity.

**Significance:**

This diagram is essential for ensuring correct hardware assembly. Incorrect cable mapping can lead to signal degradation, poor network performance, or even hardware damage. It provides a clear, unambiguous reference for technicians to follow the specific port-to-port connections required for the 5G-ANTM-04-B antenna on the P-5GS6-GL PIM, aligning with the procedural instructions provided in the surrounding text.

<--- End description image 148 --->





5G NR Antenna (5G-ANTM-04-B) is supported on both P-LTEAP18-GL and P-5GS6-GL PIMs.

• Attach each SMA cable to the ports as indicated in the table mappings.
• Ensure that you tighten and secure each SMA cable into the SMA connector on the PIM.


[98]----------------------


| 5G-ANTM-O-4-B | P-LTEAP18-GL | P-5GS6-GL |
|------|------|------|
| MAIN 0 (LTE1) | Main 0 | ANT 0 |
| MAIN 1 (LTE3) | Main 1 | ANT 1 |
| DIV 0 (LTE2) | DIV 0 | ANT 2 |
| DIV 1 (LTE4) | DIV 1 | ANT 3 |
| GNSS | No connection | GPS |


<--- Start caption table 65 --->

Table 12: Port Mappings for 5G-ANTM-0-4-B on P-5GS6-GL and P-LTEAP18-GL PIMs

<--- End caption table 65 --->



<--- Start description table 65 --->

The table provides installation instructions and antenna specifications for 5G NR (5G-ANTM-O-4-B) on Cisco industrial routers and wireless access points, including a link to the full antenna guide and a note on installing a Micro-SIM card into a USB LTE dongle.

<--- End description table 65 --->



The following link contains the antenna specifications and installation instructions for 5G NR (5G-ANTM-O-4-B):

https://www.cisco.com/c/en/us/td/docs/routers/connectedgrid/antennas/installing-combined/ b-cisco-industrial-routers-and-industrial-wireless-access-points-antenna-guide/m-5g-antm-04b.html#Cisco_ Generic_Topic.dita_e780a6fe-fa46-4a00-bd9d-1c6a98b7bcb9

# Install a Micro-SIM Card into a USB LTE Dongle


This section describes how to insert a micro-SIM card into a USB LTE dongle in a C1101-4P router.



<--- Start caption image 150 --->

Figure 80: Micro-SIM Card Slot with Dust Cover

<--- End caption image 150 --->



<--- Start description image 150 --->

This diagram illustrates the step-by-step process for installing a micro-SIM card into a USB LTE dongle, specifically for use with a Cisco 1000 Series Integrated Services Router (such as the C1101-4P). It is a hardware installation guide designed to ensure proper and secure insertion of the SIM card.

The sequence of five numbered steps is as follows:

1.  **Step 1 (①):** The diagram shows the USB LTE dongle with its micro-SIM card slot cover (labeled ①) in the open position. This is the starting point for the installation.
2.  **Step 2 (②):** The micro-SIM card (labeled ②) is shown being gently inserted into the slot. The diagram indicates the correct orientation, with the card's metallic contact edge facing down and aligned with the slot.
3.  **Step 3 (③):** The micro-SIM card (③) is shown fully seated in the slot, flush with the dongle's body.
4.  **Step 4 (④):** The protective cap (④) is shown being tapped back into place over the SIM card slot to secure the card.
5.  **Step 5 (⑤):** The final image (⑤) shows the USB LTE dongle with the protective cap securely closed, indicating the installation is complete and ready for use.

The purpose of this diagram is to provide clear, visual instructions to prevent damage to the SIM card or the dongle during installation, ensuring reliable cellular connectivity for the router. The arrows indicate the flow of the procedure from opening the slot to securing the cap.

<--- End description image 150 --->



Step 1 To insert a micro-SIM card into a USB LTE dongle, do these steps:

• Tap open the micro-SIM protective cap on the USB dongle, gently insert the micro-SIM card with its edge oriented as shown in the figure until the SIM is seated in the socket.
• Tap close the micro-SIM protective cap on the USB to close the slot.


[99]----------------------


• Step 2 To remove a micro-SIM card into a USB LTE dongle, do these steps:
• Tap open the dust cover, and then gently push the micro-SIM card to eject the card from the SIM slot.
• Tap close the micro-SIM protective cap on the USB to close the slot.


目



# Note


The antenna orientation may need to be adjusted for optimal performance.

Perform the following steps to insert the USB LTE dongle with the SIM card into a horizontal slot on the rear panel of a C110x series router:

• Ensure the micro-SIM is installed in the LTE USB dongle.
• Plug the LTE USB dongle into the magnet holder.
• Attach the magnet holder into the USB port on the metal front panel of C1101-4P.


Figure 81: LTE USB 2.0 Dongle for C1101-4P



<--- Start description image 152 --->

This technical diagram illustrates the correct installation orientation for the Cisco LTE USB 2.0 Dongle (Figure 81) when connecting it to the C1101-4P router. The image highlights four key components and their purpose:

- **1. Supporting Ring**: A structural component that provides rigidity and helps secure the dongle within the magnet holder.
- **2. Magnet**: Embedded within the holder, this magnet is designed to attach to the metal front panel of the router, enabling a secure, non-removable connection.
- **3. Extend Outward 30mm**: This dimension indicates the required extension of the magnet holder from the router’s front panel to ensure proper alignment and connection to the USB port.
- **4. Plug-in Direction**: A directional arrow clearly indicates the correct orientation for inserting the USB plug into the router’s USB port, preventing incorrect insertion.

The diagram serves as a visual guide to ensure proper hardware installation, emphasizing correct alignment and secure attachment to maintain reliable LTE connectivity for the Cisco 1000 Series Integrated Services Router.

<--- End description image 152 --->



| Number | Description |
|------|------|
| 1 | Supporting ring |
| 2 | Magnet |
| 3 | Extend outward 30mm |
| 4 | Plug-in direction |


<--- Start description table 66 --->

Figure 81 illustrates the step-by-step hardware installation of the LTE USB 2.0 dongle on the Cisco 1101-4P router, showing how to insert the micro-SIM, connect the dongle to the magnet holder, and attach the holder to the USB port on the router's metal front panel.

<--- End description table 66 --->



[100]----------------------




<--- Start description image 153 --->

This technical diagram illustrates the installation of a USB LTE dongle (model Router-C1101-4PLTEPW) into a Cisco router, specifically highlighting the components and procedure for mounting the antenna.

**Key Components and Their Purpose:**

*   **(1) Supporting Ring:** This is the structural component of the router that provides a secure mounting point for the dongle. The dongle is inserted into a slot on this ring, ensuring it is properly aligned and held in place.
*   **(2) Dongle Holder with Magnet:** This is the physical housing for the USB LTE dongle. The magnet is a critical feature that allows the dongle to be securely attached to the router's metal chassis, preventing it from becoming loose or dislodged during operation. The diagram shows the dongle's cable extending from this holder.
*   **(3) Router-C1101-4PLTEPW:** This is the specific model of the USB LTE dongle being installed. The diagram shows it inserted into the router's vertical USB port. The accompanying text instructs users to follow the same procedure for routers with a vertical USB slot, indicating this is a standard installation method for this model.

**Significance:**

This image is a crucial part of the installation and upgrade guide for internal modules and field-replaceable units. It provides a clear, visual reference for technicians to correctly install the LTE dongle, ensuring proper connectivity and secure mounting. The use of a magnetic holder is a key design feature that simplifies installation and enhances reliability in a field environment.

<--- End description image 153 --->



| Number | Description |
|------|------|
| 1 | Supporting ring |
| 2 | Dongle holder with magnet |
| 3 | Router-C1101-4PLTEPW |


<--- Start description table 67 --->

This table provides mounting instructions for the antenna on the Cisco 1000 Series Integrated Services Router, including steps for installation and guidance specific to routers with vertical USB slots, such as when installing a USB LTE dongle.

<--- End description table 67 --->



Follow the same procedure to install the USB LTE dongle onto routers with a vertical USB slot.

# Antenna Mounting Instructions


This section describes how to mount the antenna on the Cisco 1000 Series Integrated Services Router. The information is contained in the following sections:

# Rack Mount of the Antenna


To install the antenna on a rack, do these steps:

# Option A - Rack Mount at a Different Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)
• Step 2 Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 3 Tighten the screw, the recommended torque is 10-12 in-lb.


[101]----------------------




<--- Start description image 154 --->

This technical diagram illustrates Step 1 of the installation process for mounting an internal module or Field Replaceable Unit (FRU) using R-Brackets (part number 700-121611-01) in a rack-mount configuration. The purpose is to securely attach the mounting bracket to the rack frame so that the equipment can be mounted at the same height as the platform.

**Diagram Components and Purpose:**

*   **Component ① (Rack Frame):** The vertical structural member of the rack, which has a series of pre-drilled holes for mounting hardware. This is the primary structure to which the bracket will be attached.
*   **Component ② (R-Bracket):** The mounting bracket (part number 700-121611-01) that will be affixed to the rack. It has a mounting flange with holes that align with the rack's holes.
*   **Component ③ (Screw):** The fastener used to secure the bracket to the rack. The diagram shows the screw being inserted through the bracket and into the rack frame.

**Significance and Context:**

This is the first step in a procedure for installing or upgrading equipment. The diagram provides a clear, visual guide to ensure the bracket is correctly positioned and secured. The accompanying text specifies that the bracket should be placed at an "appropriate location" on the rack and that the screws should be tightened to a recommended torque of 10-12 in-lb to ensure a secure, vibration-resistant mount without damaging the components. This step is critical for proper alignment and stability of the equipment within the rack.

<--- End description image 154 --->



Option A - Rack Mount at the Same Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 2 Tighten the screw, the recommended torque is 10-12 in-lb.




<--- Start description image 155 --->

This technical diagram illustrates the hardware installation procedure for mounting a Cisco 1000 Series Integrated Services Router (labeled as component ②) using Option A: rack mounting at the same height as the platform. The image provides a clear, step-by-step visual guide for assembling and securing the mounting hardware.

**Key Components and Their Purpose:**

*   **① Rack:** The vertical metal structure (rack) provides the mounting surface for the router. The brackets are designed to attach to the standard 19-inch rack rails.
*   **② Cisco 1000 Series Router:** The main device to be mounted. The diagram shows its front panel with ports and the Cisco logo.
*   **③ R-Bracket (700-121611-01):** This is the primary mounting bracket that attaches to the rack. It is designed to hold the router at the same height as the rack's mounting platform.
*   **④ Screw (48-0580-01):** The fastener used to secure the R-Bracket to the rack. The installation guide specifies a recommended torque of 10-12 in-lb.
*   **⑤ Screw (48-0580-01):** The second screw used to secure the R-Bracket to the rack, ensuring a stable and secure mount.
*   **⑥ Wall-Mounting Bracket (700-121609-01):** This component is shown as part of the assembly but is not used in Option A. It is included in the guide for completeness, as it is also used in Option B (wall mounting).
*   **⑦ Screw (48-0580-01):** This is the second screw for the wall-mounting bracket, which is not used in this specific installation scenario.

**Significance and Context:**

This diagram is a critical part of the Cisco 1000 Series Router's Hardware Installation Guide. It visually clarifies the physical assembly required for Option A, ensuring technicians correctly mount the device in a rack environment. The diagram complements the textual instructions by showing the exact placement and orientation of the R-Bracket (③) relative to the rack (①) and the router (②). It also serves as a reference for the subsequent steps, which involve assembling the dongle, USB cable, and antenna, and then connecting the USB cable to the router's chassis to complete the installation. The diagram's clarity is essential for preventing installation errors and ensuring the router is securely and correctly mounted for optimal performance and safety.

<--- End description image 155 --->



Both options - A and B should follow these remaining steps to complete the mounting procedure:

• Assemble dongle, USB, cable and antenna together in advance.
• Pick up the wall-mounting bracket (700-121609-01) and 2 SCREWS (48-0580-01).
• Align and fasten the screws.
• Plug the USB cable to the USB port on the chassis to complete the mounting procedure.


[102]----------------------




<--- Start description image 156 --->

This technical diagram from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide illustrates the step-by-step process for mounting the antenna on a wall. It is divided into two sections:

**Top Section (Assembly View):**
This exploded-view diagram details the components and their assembly sequence:
*   **(1) Wall Mount Bracket:** The primary mounting hardware designed to be attached to a wall.
*   **(2) Antenna:** The external radio frequency antenna, which connects to the router.
*   **(3) Antenna Mounting Bracket:** A smaller bracket that attaches to the antenna's base and connects to the main wall mount.
*   **(4) Cable:** The coaxial cable that transmits the signal between the antenna and the router.
*   **(5) Router Module/Unit:** The internal module or unit that the antenna connects to.
*   **(6) Mounting Screw:** The fastener used to secure the antenna mounting bracket to the wall mount.

**Bottom Section (Assembled View):**
This shows the final installed configuration:
*   The antenna (2) is mounted vertically on the wall mount bracket (1).
*   The router (1) is positioned below the mount, with the antenna cable (4) running from the antenna down to the router's interface port.
*   The diagram highlights the physical relationship between the components, showing how the antenna is elevated above the router for optimal signal performance.

**Purpose and Significance:**
This diagram serves as a critical visual guide for technicians installing the Cisco 1000 Series router. It ensures proper and secure mounting of the antenna, which is essential for achieving optimal wireless signal strength and coverage. The exploded view clarifies the assembly order and component relationships, while the assembled view provides a clear reference for the final installation. This is part of the broader "Install and Upgrade Internal Modules and Field Replaceable Units" section, indicating that correct antenna installation is a key part of the router's setup and maintenance.

<--- End description image 156 --->



# Wall Mount of the Antenna


To install the antenna on a wall, do these steps:

[103]----------------------


• Step 1 Pick up the C-Bracket (700-121628-01), place the bracket and then fix it on the wall using four screws.
• Step 2 Assemble the USB cable (74-122795-01), dongle and antenna (07-100470-01) together. Pick up the wall-mount bracket (700-121609-01), two SCREWS (48-0580-01). Align and fasten the screws (recommended torque is 10-12 in-lb), the wall-mount is complete.




<--- Start description image 157 --->

This technical diagram illustrates the hardware assembly and mounting procedure for a Cisco 1000 Series Integrated Services Router, specifically detailing the installation of its wireless antenna and wall-mount bracket. The image serves as a visual guide for technicians to correctly assemble and install the external antenna system.

The diagram breaks down the components and their assembly into five labeled parts:

*   **(1) Antenna:** A vertically oriented, external wireless antenna (model 07-100470-01) that connects to the router's wireless module. It is the primary component for wireless signal transmission and reception.
*   **(2) Wireless Module/Dongle:** The internal wireless module (likely the USB dongle) that connects the antenna to the router's main unit. This module is the interface between the antenna and the router's internal circuitry.
*   **(3) Wall-Mount Bracket (C-Bracket):** A mounting bracket (model 700-121628-01) designed to be fixed to a wall. This component provides a secure, permanent mounting point for the entire antenna assembly.
*   **(4) Wall-Mount Bracket (Alternative/Secondary):** A second, similar wall-mount bracket (model 700-121609-01) shown with screws (48-0580-01). This is the bracket that is screwed into the wall to hold the entire assembly. The diagram indicates that this bracket is assembled with the module and antenna, and then secured to the wall.
*   **(5) USB Cable:** The USB cable (model 74-122795-01) that connects the wireless module to the router's USB port. The cable is shown with a cable clip, which is used to manage routing and prevent strain on the connection.

**Purpose and Significance:**
This diagram is a critical part of the installation guide for the Cisco 1000 Series router. It visually clarifies the physical assembly process, ensuring that technicians correctly connect the antenna to the module, attach the module to the wall-mount bracket, and secure the entire unit to the wall. The diagram complements the textual instructions by providing a clear, step-by-step visual representation of the hardware components and their relationships, which is essential for accurate and safe installation. The use of part numbers and specific assembly steps (like aligning and fastening screws with a recommended torque) ensures that the installation meets the manufacturer's specifications for optimal performance and durability.

<--- End description image 157 --->



# Connect the Antenna to the Device


• Step 1 Ensure the reserved USB cable length is sufficient to reach the device.
• Step 2 Ensure the use the cable clip within USB cable kit (74-122795-01) to manage cable routing and to hold the cable weight.
• Step 3 Ensure there are no sharp radius within the USB cable routing.


[104]----------------------




<--- Start description image 158 --->

This technical diagram illustrates the installation of a Cisco wireless access point (labeled “1”) connected to a ceiling-mounted antenna assembly (labeled “2”). The diagram is part of a larger installation guide, specifically addressing the “Install and Upgrade Internal Modules and Field Replaceable Units” for a ceiling-mounted antenna system.

**Key Components and Purpose:**
- **Component 1 (Access Point):** The main wireless device, shown with a Cisco logo and ventilation grille, which connects via a cable to the antenna assembly.
- **Component 2 (Antenna Assembly):** A ceiling-mount bracket with a vertically oriented antenna attached. This assembly is designed to be mounted to the ceiling or a rack at a different height, as indicated by the context text “Option A - Rack Mount at a Different Height with the Platform.”

**Significance:**
The diagram provides a clear visual guide for technicians to understand how the access point connects to the antenna and how the antenna assembly should be mounted. It is critical for ensuring proper signal transmission and physical installation in a wireless network environment. The reference to “Option A” suggests this is one of several mounting configurations available, allowing for flexibility in deployment based on ceiling height or rack placement requirements.

<--- End description image 158 --->



# Ceiling Mount of the Antenna


To install the antenna on a rack, do these steps:

# Option A - Rack Mount at a Different Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)
• Step 2 Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 3 Tighten the screw, the recommended torque is 10-12 in-lb.


[105]----------------------




<--- Start description image 159 --->

This technical diagram illustrates Step 1 of the installation process for mounting an internal module or Field Replaceable Unit (FRU) using R-Brackets (part number 700-121611-01) in a rack-mount configuration. The purpose is to securely attach the mounting bracket to the rack frame so that the equipment can be mounted at the same height as the platform.

**Diagram Components and Purpose:**

*   **Component ① (Rack Frame):** This is the vertical structural member of the equipment rack, featuring a series of pre-drilled holes for mounting various components. The part number 521010 is visible, likely identifying this specific rack frame or its mounting standard.
*   **Component ② (R-Bracket):** This is the mounting bracket (700-121611-01) that will be attached to the rack. It has a flange with holes to align with the rack's mounting holes and a mounting arm that will connect to the equipment.
*   **Component ③ (Screw):** This is the fastener used to secure the R-Bracket to the rack. The diagram shows the screw being inserted through the bracket and into the rack frame.

**Key Instructions from the Context:**

The diagram visually supports the textual instructions provided in the context. It shows the correct orientation for placing the R-Bracket (②) against the rack frame (①) and indicates where the screw (③) should be inserted. The accompanying text specifies that two screws are required and that the recommended torque for tightening them is 10-12 inch-pounds (in-lb) to ensure a secure, vibration-resistant mount without damaging the components.

In summary, this diagram is a critical part of the installation guide, providing a clear, visual reference for the first step in mounting equipment, ensuring proper alignment and secure attachment to the rack.

<--- End description image 159 --->



Option A - Rack Mount at the Same Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 2 Tighten the screw, the recommended torque is 10-12 in-lb.




<--- Start description image 160 --->

This technical diagram illustrates the hardware installation procedure for mounting a Cisco 1000 Series Integrated Services Router (labeled as component ②) using Option A: rack mounting at the same height as the platform. The image provides a clear, step-by-step visual guide for assembling and securing the mounting hardware.

**Key Components and Their Purpose:**

*   **① Rack:** The vertical metal structure (rack) provides the mounting surface for the router. The brackets are designed to attach to the standard 19-inch rack rails.
*   **② Cisco 1000 Series Router:** The main device to be mounted. The diagram shows its front panel with ports and the Cisco logo.
*   **③ R-Bracket (700-121611-01):** This is the primary mounting bracket that attaches to the rack. The text instructs the user to place and fix this bracket using two screws.
*   **④ Screw (48-0580-01):** One of the two screws used to fasten the R-Bracket (③) to the rack. The diagram shows the screw being inserted through the bracket and into the rack.
*   **⑤ Screw (48-0580-01):** The second screw, used to secure the R-Bracket (③) to the rack. The diagram shows the screw being inserted through the bracket and into the rack.
*   **⑥ Wall-Mounting Bracket (700-121609-01):** This component is used to attach the router (②) to the R-Bracket (③). The text indicates this bracket is used for both Option A and Option B.
*   **⑦ Screw (48-0580-01):** One of the two screws used to fasten the wall-mounting bracket (⑥) to the router (②). The diagram shows the screw being inserted through the bracket and into the router chassis.

**Installation Process (as per the text):**

1.  **Mount the R-Bracket:** Place the R-Bracket (③) onto the rack (①) and secure it with two screws (④ and ⑤). The recommended torque for these screws is 10-12 in-lb.
2.  **Attach the Router:** Align the wall-mounting bracket (⑥) with the router (②) and fasten it with two screws (⑦).
3.  **Connect Cables:** Assemble the dongle, USB cable, and antenna in advance, then plug the USB cable into the USB port on the router chassis to complete the mounting procedure.

This diagram is a critical part of the Hardware Installation Guide, providing a clear visual reference to ensure the router is mounted correctly and securely, which is essential for proper operation and safety.

<--- End description image 160 --->



Both options - A and B should follow these remaining steps to complete the mounting procedure:

• Assemble dongle, USB, cable and antenna together in advance.
• Pick up the wall-mounting bracket (700-121609-01) and 2 SCREWS (48-0580-01).
• Align and fasten the screws.
• Plug the USB cable to the USB port on the chassis to complete the mounting procedure.


[106]----------------------




<--- Start description image 161 --->

This technical diagram from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide illustrates the assembly and mounting of an external antenna system. It provides a step-by-step visual guide for installing a directional antenna (part 2) onto the router (part 1) using a mounting bracket (part 3) and a mounting plate (part 4). The diagram also shows the router's I/O side (part 5) and the rear panel (part 6) where the antenna connects, which is relevant to the context of installing SIM cards on models like the C111X, C1109-2PX, and C1109-4P. The purpose is to ensure proper physical installation for optimal wireless performance and signal integrity.

<--- End description image 161 --->



# Installing a SIM Card on C111X, C1109-2PX, C1109-4P


The SIM card socket is located on the I/O side of the unit.

[107]----------------------




<--- Start description image 162 --->

This technical diagram, titled "Figure 82: Removing SIM Cover and Inserting SIMs into C111X," provides a clear, step-by-step visual guide for installing or replacing SIM cards in the Cisco 1000 Series Integrated Services Router (specifically the C111X model). It is a crucial component of the hardware installation manual, designed to assist technicians in correctly configuring the device's cellular connectivity.

The diagram is composed of two main illustrations:
1.  **Top View:** Shows the router with the SIM cover (labeled as item 1) in its original, installed position, indicating the location of the SIM card slot.
2.  **Bottom View:** Depicts the router with the SIM cover removed, revealing the two SIM card slots (labeled as items 2 and 3, designated SIM 0 and SIM 1, respectively). This view clearly shows the physical slots where the SIM cards are inserted.

The purpose of this diagram is to ensure accurate and error-free installation. It visually confirms the location of the SIM cover and the two distinct SIM slots, which are essential for enabling dual SIM functionality. The accompanying legend explicitly identifies each numbered part, reinforcing the visual instructions for users following the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router." This is a critical step for activating cellular data services on the router.

<--- End description image 162 --->



|  |  |
|------|------|
| 1 | SIM Cover |
| 2 | SIM 0 |
| 3 | SIM 1 |


<--- Start description table 68 --->

Table caption: Steps for installing SIM cards in C111X, C1109-2PX, and C1109-4P models of the Cisco 1000 Series Integrated Services Router.

<--- End description table 68 --->



The unit supports dual SIM cards behind a SIM cover. To insert the SIM cards, perform the following steps:

[108]----------------------




<--- Start caption image 163 --->

Figure 83: SIMs Inserted

<--- End caption image 163 --->



<--- Start description image 163 --->

This diagram is a technical illustration from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide, specifically detailing the process for installing and upgrading internal modules and Field Replaceable Units (FRUs), with a focus on the SIM card installation for models C111X, C1109-2PX, and C1109-4P.

**Purpose:** The diagram serves as a visual guide to help technicians correctly identify and install SIM cards into the router's designated slots.

**Key Components and Their Significance:**

*   **1. SIM Card Slot Location (Top View):** This arrow points to the physical location of the SIM card slots on the router's rear panel. The diagram shows two distinct slots, labeled as SIM 0 and SIM 1, which are clearly marked on the unit's face for easy identification.
*   **2. SIM 1 Slot (Bottom View):** This label points to the internal connector for the second SIM card (SIM 1). The diagram shows the physical shape of the slot and the orientation notch (labeled as 5) that ensures the card is inserted correctly.
*   **3. SIM 0 Slot (Bottom View):** This label points to the internal connector for the first SIM card (SIM 0). Like SIM 1, it has a specific orientation notch (labeled as 4) to guide proper insertion.
*   **4. Orientation Notch (SIM 0):** This label indicates the small notch on the internal connector for SIM 0. This notch is a critical feature that ensures the SIM card is inserted with the correct orientation. The text in the guide confirms that the SIM icons on the unit's panel show the required orientation.
*   **5. Orientation Notch (SIM 1):** This label points to the corresponding notch on the internal connector for SIM 1, serving the same purpose as the notch for SIM 0 to prevent incorrect installation.

**Overall Significance:**
This diagram is essential for ensuring correct hardware installation. It visually reinforces the textual instructions provided in the guide, which state that SIM cards are installed using a "push-push" type connector. The diagram clarifies that the SIM card must be inserted until it clicks into place, and that the orientation notches (4 and 5) are vital for proper alignment. This prevents damage to the card or the connector and ensures the router can properly communicate with the SIM card for its intended function, such as cellular connectivity. The guide also notes that the SIM location (0 or 1) is marked on the unit's panel face, which the diagram helps to visually confirm.

<--- End description image 163 --->



|  |  |
|------|------|
| 1 | Micro SIM slots |
| 2 | SIM 0 slot |
| 3 | SIM 1 slot |
| 4 | Orientation notch (SIM 0) |
| 5 | Orientation notch (SIM 1) |


<--- Start description table 69 --->

Table caption: Steps for installing and removing SIM cards in Cisco 1000 Series ISR routers (C111X, C1109-2PX, C1109-4P), including SIM cover removal, proper orientation, insertion, and ejection procedures.

<--- End description table 69 --->



• Use a flat screw driver to pry and remove the SIM cover.
• Install SIM 0 or SIM 1 in their respective slots. SIM location (0 or 1) is marked on both the unit panel face (visible when the SIM cover is removed). The SIM icons show the correct orientation required to install the SIM into each respective connector (SIM connectors are a push-push type).
• To install, insert the SIM card into the connector until you feel it click, and then let go. The SIM is locked into the connector.
• To remove the SIM card, depress the SIM in the connector slot until you feel the same click and let it go. The SIM connector should get ejected part way out of the connector. You can then grab the SIM and remove it.
• When SIM cards are installed, replace the SIM-cover and secure using a flat screw-driver.


[109]----------------------




Important


• For accurate readings of the SIM-card in the micro-SIM slots, we recommend using the native industrial-grade micro-SIM cards.
• If a nano-SIM (4FF) card is used, we recommend to use the cisco nano-to-micro-sim adapter - pid: Nano-micro-adpt=


Not all off-the-shelf adapters are robust in positioning the nano-SIM card to be read accurately.

# Installing a Nano-SIM Card into a Nano-To-Micro-SIM Adapter


Step 1 Place the nano-SIM card with the electrical contacts surface facing up to position it into the micro-SIM adapter as shown below.



<--- Start description image 165 --->

This technical diagram illustrates the correct orientation and placement for installing a nano-SIM card into a nano-to-micro-SIM adapter, a critical step in hardware setup for devices like the Cisco 1000 Series Integrated Services Router.

The diagram is a labeled, exploded-view schematic showing the key components and their proper alignment:

*   **1. Electrical contact surface up:** This indicates the orientation of the nano-SIM card. The metallic contacts, which must make direct contact with the device's reader, must be facing upwards to ensure a reliable connection.
*   **2. Nano-SIM card:** The small, standard-sized SIM card that needs to be inserted.
*   **3. Backing surface (cutout not open) for nano-SIM:** This refers to the specific cutout or slot within the adapter designed to hold the nano-SIM card. The diagram shows the card should be placed so that its backing surface (the non-contact side) aligns with the adapter's cutout, ensuring it is seated correctly and not inverted.
*   **4. Nano-to-micro-SIM adapter:** The physical adapter that converts the smaller nano-SIM card to fit into a device that requires a micro-SIM slot. The diagram shows the adapter's shape and how the nano-SIM card fits inside it.

The purpose of this diagram is to provide a clear, visual guide to prevent installation errors. Incorrect placement can lead to the device failing to recognize the SIM card, which is why the guide emphasizes the importance of the electrical contacts facing up and the card being seated properly within the adapter's designated cutout. This is particularly relevant for users installing SIM cards in routers or other devices that may not have a native nano-SIM slot.

<--- End description image 165 --->



|  |  |
|------|------|
| 1 | Electrical contact surface up |
| 2 | Nano-SIM card |
| 3 | Backing surface (cutout not open) for nano-sim |
| 4 | Nano-to-micro-sim adapter |


<--- Start description table 70 --->

Caption: Step-by-step instructions for installing a Nano-SIM card into a Nano-to-Micro-SIM adapter, as part of the hardware setup for the Cisco 1000 Series Integrated Services Router.

<--- End description table 70 --->



[110]----------------------




<--- Start description image 166 --->

This technical diagram illustrates Step 2 of installing a Nano-SIM card into a Nano-to-Micro-SIM adapter, as part of the hardware installation process for Cisco 1000 Series Integrated Services Routers or Pluggable Interface Modules (PIMs).

**Diagram Components and Purpose:**
- **Component 1 (Nano-SIM card):** The small, rectangular SIM card designed for modern smartphones and devices. It is shown being inserted into the adapter.
- **Component 2 (Nano-to-Micro-SIM adapter):** A plastic adapter that allows a smaller Nano-SIM card to fit into a larger Micro-SIM slot. The diagram highlights the adapter's shape and the slot where the Nano-SIM card is placed.

**Significance:**
This visual guide is critical for technicians performing hardware installation, ensuring the correct orientation and secure placement of the SIM card within the adapter. Proper installation is necessary for the router or PIM to establish cellular connectivity via the SIM card. The diagram is part of a larger procedure for installing and upgrading internal modules and field-replaceable units, emphasizing precision and adherence to the Cisco Hardware Installation Guide.

<--- End description image 166 --->



|  |  |
|------|------|
| 1 | Nano-SIM card |
| 2 | Nano-to-micro-sim adapter |


<--- Start description table 71 --->

Table showing step-by-step instructions for installing a nano-SIM card into a nano-to-micro-SIM adapter for use in Cisco 1000 Series routers or Pluggable Interface Modules (PIMs).

<--- End description table 71 --->



Step 2 Follow the instructions to install nano-SIM/adapters into micro-SIM slots of routers or Pluggable Interface Modules (PIMs).


[111]----------------------




<--- Start description image 167 --->

This is the chapter heading image for Chapter 5 of the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 104," specifically titled "ROM Monitor Overview."

The image uses a wide, atmospheric photograph of a modern city skyline at sunrise or sunset, with the sun creating a bright lens flare on the left. The foreground features a vast, reflective rooftop or plaza, leading the viewer's eye toward the towering skyscrapers. This visual metaphorically represents the foundational and critical nature of the ROM Monitor — a core, low-level system that boots and initializes the router, much like the ground floor of a building that supports the entire structure above.

The text "CHAPTER 5" is prominently displayed in a bold, black, sans-serif font at the bottom center, clearly marking the section within the technical manual. The chapter's title, "ROM Monitor Overview," is implied by the context provided in the surrounding text, indicating that this section will cover the essential functions, access methods, and operational principles of the router's ROM Monitor, which is a crucial component for troubleshooting, recovery, and initial configuration. The image serves as a visual divider and thematic anchor for this important technical chapter.

<--- End description image 167 --->



5

C H A P T E R

# ROM Monitor Overview


The ROMMONis the bootloader that initializes the hardware when the platform is powered on or reset. From the ROMMON prompt, a Cisco IOS XE image can be manually booted. There is also an autoboot option to boot a specified IOS XE image for every power-on or reset. When new features or significant defects are resolved, a newer ROMMON release is available on CCO. To determine the current ROMMON version and the location of the latest ROMMON release, these details are available in the following sections:

.

• ROM Monitor Overview, on page 105


# ROM Monitor Overview


The ROMMonitor software is also known as ROMMON , boot software , boot image , or boot helper . Although it is distributed with routers that use the Cisco IOS XE software, the ROMMON is a separate program from the Cisco IOS XE software. During normal startup, ROMMON initializes the router, and then, the control passes to the Cisco IOS XE software.

Whenyouconnect a terminal to the router that is in ROMMON mode, the ROMMON command-line interface (CLI) prompt is displayed.

Access the ROMMON mode to perform these tasks:

• Specify config-register value to use for the next boot up
• Boot a valid IOS XE image
• Bypass NVRAM settings and config-register value for password recovery


目



Note

After the Cisco IOS XE software boots up, ROMMON is no longer in use.

# Environmental Variables and the Configuration Register


Two primary connections exist between ROMMON and the Cisco IOS XE software: the ROMMON environment variables and the configuration register.

[112]----------------------


The ROMMON environment variables define the location of the Cisco IOS XE software and describe how to load it. After ROMMON has initialized the router, it uses the environment variables to locate and load the Cisco IOS XE software.

The configuration register is a software setting that controls how a router starts up. One of the primary uses of the configuration register setting is to control whether the router starts in ROMMON mode or Administration EXEC mode. The configuration register is set in either ROMMON mode or Administration EXEC mode as needed. You can set the configuration register using the Cisco IOS XE software prompt when you need to use ROMMONmode.Whenmaintenancein ROMMODEmodeiscomplete,change the configuration register back so that the router reboots with the Cisco IOS XE software.

# Access ROMMON Mode with a Terminal Connection


When the router is in ROMMODE mode, you can access the ROMMODE software only from a terminal connected directly to the console port of the card. Because the Cisco IOS XE software (EXEC mode) is in operatiion, the nonmanagement interfaces are not accessible. Therefore, all Cisco IOS XE software resources are unavailable.

# Network Management Access and ROMMON Mode


ROMMONmode is a router mode, not a mode within the Cisco IOS XE software. The ROMMON software and the Cisco IOS XE software are two separate programs that run on the same router. At any given time, the router is running one of these programs, but it never runs both at the same time.

One area that can be confusing when using ROMMON and the Cisco IOS XE software is the area that defines the IP configuration for the Management Ethernet interface. Most users are comfortable with configuring the Management Ethernet interface in the Cisco IOS XE software. When the router is in ROMMON mode, however, the router is not running the Cisco IOS XE software, therefore, Management Ethernet interface configuration is not available.

When you want to access other devices, such as a TFTP server, while in ROMMON mode on the router, you must configure the ROMMON variables with IP access information.

For more information on ROMMON and Basic Procedures, refer to the Upgrading Field-Programmable Hardware Devices for Cisco 1000 Series ISRs

[113]----------------------




<--- Start description image 169 --->

Based on the provided context, which is a text excerpt from a "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 106," the image is not a direct visual representation of the guide's content. Instead, it appears to be a generic, thematic placeholder or cover image for a section titled "Chapter 6."

The image depicts a wide, elevated view of a modern cityscape, likely taken from a rooftop or overpass during sunrise or sunset. The sun is low on the horizon, casting a warm, hazy glow and creating lens flare. The foreground consists of a reflective, tiled surface, possibly a rooftop or walkway, leading the viewer's eye toward the dense cluster of skyscrapers and high-rise buildings in the background. A construction crane is visible on the right, suggesting ongoing development.

**Relevant and Comprehensive Caption:**

**Chapter 6: Infrastructure Foundations — A View from the Top**

This chapter, set against the backdrop of a dynamic, evolving urban landscape, introduces the foundational aspects of deploying enterprise-grade networking hardware. The image symbolizes the critical infrastructure that underpins modern digital connectivity — the physical and architectural environment where network devices like the Cisco 1000 Series Router are installed and integrated. The rising sun and construction crane represent the dawn of new connectivity solutions and the continuous evolution of the digital infrastructure that powers commerce and communication. This chapter will guide you through the physical installation and compliance considerations necessary to deploy this critical equipment within a commercial environment, ensuring it operates reliably and in harmony with the surrounding technological ecosystem.

<--- End description image 169 --->



6

# Supplier Declaration of Conformity


This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against any harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio frequency energy, and if it is not installed and used in accordance with the instruction manual, it may may cause harmful interference to radio communications.

• This device may not cause harmful interference.
• This device must accept any interference received, including interference that may cause an undesired operation.


The operation of this equipment in a residential area is likely to cause harmful interference, in which case, users are required to correct the interference at their own expense.

# Radio Compliance


This system uses both licensed and licensed exempt radio frequencies. The radios are evaluated to the following regulations:

The Wi-Fi Radio is evaluated to 47 Code of Federal Regulations Part 15.247 and Part 15.407.

Part 15 Radio Systems operating outdoors in the 5150-5250 MHz band must comply with the antenna installation requirements as set forth in the FCC Part 15.407 rules.

The LTE radio is evaluated to 47 Code of Federal Regulation Part 24 and 27.

The LTE radio operates on licensed frequency bands and requires a radio license to operate. It must be operated under the control of a Licensed Service Provider or Wireless Carrier.

# Modifications by User or Installer


Modifying the equipment without Cisco's authorization may result in the equipment being no longer compliant with FCC requirements for Class A digital devices. In that event, your right to use the equipment may be limited by FCC regulations, and you may be required to correct any interference to radio or television communications at your own expense.

Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

# FCC RF Exposure Compliance


This product has been found to be compliant to the requirements set forth in CFR 47 Section 1.1307 addressing RF Exposure from radio frequency devices, as defined in Evaluating Compliance with FCC Guidelines for Human Exposure to Radio Frequency Electromagnetic Fields.

[114]----------------------


To maintain compliance, the minimum separation distance from the antenna to general bystander is 20 cm (8,7 inches) or more.

# CANADA


This Class [*] digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [*] est conforme à la norme NMB-003 du Canada

# Radio (Wi Fi)


This product complies with RSS-247 of the Industry Canada Rules. Its operation is subject to the following two conditions:

• This device may not cause harmful interference.
• This device must accept any interference received, including interference that may cause an undesired operation.


Ce dispositif est conforme à la norme RSS-247 d'Industrie Canada applicable aux appareils radio exempts de licence. Son fonctionnement est sujet aux deux conditions suivantes:

• le dispositif ne doit pas produire de brouillage préjudiciable
• ce dispositif doit accepter tout brouillage reçu, y compris un brouillage susceptible de provoquer un fonctionnement indésirable


The device for operation in the band 5150-5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite system.

For devices with detachable antenna(s), the maximum antenna gain permitted for devices in the bands 5250-5350 MHz and 5470-5725 MHz must be such that the equipment still complies with the e.i.r.p. limit.

For devices with detachable antenna(s), the maximum antenna gain permitted for devices in the band 5725-5850 MHz must be such that the equipment still complies with the e.i.r.p. limits as appropriate.

For systems that are capable of operating outdoors or with antennas mounted outdoors (where applicable antenna type(s), antenna models(s), and worst-case tilt angle(s)) are necessaryto remain compliant with the e.i.r.p, therefore, the elevation mask requirement set forth in section 6.2.2.3 should be clearly indicated.

# Radio (Wi Fi)


This product complies with the RSS of the Industry Canada rules.

# Radiation Exposure Statement


This equipment complies with IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm (7.87 in.) between the radiator and yourself.



C1109-4PLTE2P = 27 cm Note

# Déclaration D'exposition Aux Radiations


Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 20 cm (7.87 in.) de distance entre la source de rayonnement et votre corps.

[115]----------------------




# C1109-4PLTE2P = 27 cm Note


# THAILAND


เครื่องโทรคมนาคมและอุปกรณ์นี้มีความสอดคล้องตามมาตรฐานหรือข้อกําหนดทางเทคนิค ของ กสทช

This telecommunication equipment conforms to NTC/NBTC technical requirement (optional)

Radiocommunication equipment has electromagnetic field strength in compliance with the Safety Standard for the Use of Radiocommunication Equipment on Human Health announced by the National Telecommunication Commission.

[116]----------------------
