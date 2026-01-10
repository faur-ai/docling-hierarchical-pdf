[1]----------------------






<--- Start description image 1 --->

This image depicts a vast rooftop solar panel array installed on a modern urban building, with a city skyline and construction crane visible in the background under a bright, sunlit sky. The scene symbolizes the integration of renewable energy infrastructure into contemporary urban environments, highlighting sustainable development and the transition toward clean power solutions in metropolitan areas. While the image itself is not directly related to the Cisco 1000 Series router hardware guide, it visually represents the kind of modern, scalable, and networked infrastructure that such routers help power — connecting smart buildings, data centers, and city-wide energy systems. The guide’s focus on hardware installation for enterprise networking equipment underscores the foundational technology enabling the digital and physical connectivity of such sustainable urban ecosystems.

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

This panoramic image depicts a modern urban skyline viewed from a high vantage point, likely a rooftop, with the sun casting a warm, hazy glow over the scene. The foreground features a clean, tiled surface that leads the eye toward a dense cluster of skyscrapers and high-rise buildings, some under construction as indicated by visible cranes. The overall atmosphere is one of technological advancement and corporate dynamism, aligning with the context of Cisco’s enterprise networking equipment.

Given the surrounding text — which details the Cisco 1000 Series Integrated Services Routers, including chassis views, LED indicators, and specifications — this image serves as a symbolic backdrop. It visually represents the environments where Cisco’s networking solutions are deployed: large-scale, high-performance corporate, financial, or data center infrastructures. The image evokes themes of connectivity, innovation, and the digital backbone of modern business, reinforcing the professional and forward-looking nature of Cisco’s products.

In essence, the image is not literal documentation but a conceptual illustration, using the urban landscape to metaphorically convey the scale, reliability, and critical role of Cisco’s routers in powering the digital infrastructure of the modern world.

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

The image itself is a photograph of a modern city skyline viewed from a high vantage point, such as a rooftop or elevated walkway. The sun is low in the sky, creating a bright lens flare and casting long shadows, which suggests either early morning or late afternoon. The foreground is a clean, tiled surface, leading the eye towards the dense cluster of skyscrapers in the background. A construction crane is visible, symbolizing growth and development.

The significance of this image within the context of the guide is metaphorical. It represents the modern, connected, and evolving digital infrastructure that the Cisco 1000 Series routers are designed to support. The routers provide the foundational networking and security services that enable the seamless operation of the digital world depicted in the skyline — the businesses, communications, and services that power the city. The image sets a tone of innovation, scalability, and the critical role of networking technology in contemporary urban environments.

The text "CHAPTER 1" is prominently displayed at the bottom, clearly indicating the start of the guide's content. The chapter likely begins with an "Overview of Cisco 1000 Series Integrated Services Routers," as referenced in the context, providing the reader with the foundational knowledge needed before proceeding to installation procedures. The image, therefore, acts as a visual anchor, connecting the technical subject matter to its real-world application and impact.

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

This table outlines the key specifications and features of the Cisco 1000 Series Integrated Service Routers, highlighting their suitability for small and midsize businesses, enterprise branches, and managed services environments. It details hardware configurations, performance capabilities, and deployment options for both fixed and modular form factors, supporting their role as next-generation, IOS XE-based, multi-core branch routers.

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

This table provides a summary of the Cisco 1000 Series Integrated Services Routers, outlining key hardware specifications and installation considerations as detailed in the official Hardware Installation Guide. It serves as a reference for network administrators and engineers deploying or configuring these routers in enterprise or branch office environments.

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

This diagram is a front panel layout guide for the Cisco 1000 Series Integrated Services Router, illustrating the key physical components and indicator locations on the router’s front faceplate. It serves as a reference for users during installation, troubleshooting, or routine maintenance.

The diagram highlights seven labeled features:

1.  **Status Indicators (1):** A set of LED lights used to display the router’s operational state, such as power, system health, and interface activity.
2.  **VPN Indicator (2):** An indicator light that signals the status of VPN (Virtual Private Network) connections.
3.  **Wi-Fi Indicator (3):** An LED that shows the status of the built-in Wi-Fi radio.
4.  **GPS Indicator (4):** An LED that indicates the status of the GPS module, if equipped.
5.  **LTE Signal Intensity (5):** A bar graph or LED cluster that visually represents the strength of the LTE cellular signal.
6.  **LTE Data/SIM Indicator (6):** An indicator light that shows the status of LTE data connectivity and SIM card presence.
7.  **Illuminated Cisco Logo (7):** The Cisco brand logo, which is illuminated to indicate the router is powered on and operational.

This visual guide is part of the “Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router,” helping technicians quickly identify and interpret the status of critical functions at a glance. The diagram is a crucial tool for ensuring proper setup and monitoring of the router’s connectivity and operational health.

<--- End description image 7 --->



| 1 | Status | 2 | VPN |
|------|------|------|------|
| 3 | Wi-Fi | 4 | GPS |
| 5 | LTE signal intensity | 6 | LTE data/SIM |
| 7 | Illuminated Cisco logo |  |  |


<--- Start description table 2 --->

This table illustrates the placement of key hardware components—such as power and signal interfaces, interface slots, status indicators, and chassis identification labels—on the front and back panels of the Cisco 1000 Series Integrated Services Router, as referenced in the Hardware Installation Guide. The compliance label is noted to be located at the bottom of the product.

<--- End description table 2 --->



[12]----------------------




<--- Start caption image 8 --->

Figure 2: C111x-8P - I/O View

<--- End caption image 8 --->



<--- Start description image 8 --->

This diagram provides a comprehensive, labeled overview of the front panel components of a Cisco 1000 Series Integrated Services Router (ISR) chassis, serving as a critical reference for installation, configuration, and maintenance.

**Key Components and Their Functions:**

*   **Connectivity Ports (1-18):** The router offers a wide array of physical interfaces for network and service connections.
    *   **Wireless:** LTE antennas (1) for cellular connectivity.
    *   **Ethernet:** A 16-port Ethernet switch (2) for wired LAN connections, with specific ports labeled GE 0/0/0 (RJ45, 11) and GE 0/0/1 (SFP, 12) for flexible fiber or copper connections.
    *   **Serial & Console:** A serial console port (16) for initial setup and troubleshooting, and a dedicated LTE provisioning port (15) for configuring cellular services.
    *   **DSL:** A DSL port (17) for connecting to a DSL modem.
    *   **USB:** A USB 3.0 port (13) for device connectivity or firmware updates.
    *   **Power:** A 4-pin power connector (9) for supplying power to the unit.
    *   **Expansion Slots:** Lower slot0 and Upper slot1 (14) for installing service modules or line cards.
    *   **Security & Management:** A Kensington lock slot (18) for physical security, and a CLEI label (4) for device identification.

*   **System Management & Identification:**
    *   **Reset Button (7):** Used to reset the router to factory defaults.
    *   **Power Switch (8):** Controls the power state of the device.
    *   **Grounding (6):** Ensures electrical safety by connecting the chassis to ground.
    *   **Identification:** A CLEI label (4), Serial Number (5), and Product Identification Number (PID) (19) are provided for asset tracking and technical support.

**Purpose and Significance:**

This diagram is an essential technical guide for network engineers and technicians. It enables them to:
*   **Properly install** the router by connecting it to power, network, and other required services.
*   **Configure** the device by accessing the console or provisioning ports.
*   **Troubleshoot** issues by identifying which port or component might be faulty.
*   **Maintain** the device by using the reset button or grounding it correctly.
*   **Identify** the specific model and serial number for warranty, support, or inventory purposes.

In essence, this image is a foundational reference for anyone working with Cisco 1000 Series routers, ensuring correct physical setup and operational understanding.

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

This table provides a comparative overview of the chassis views available for Cisco 1000 Series Integrated Services Routers, highlighting key physical and functional distinctions to assist in identifying or selecting the appropriate router model based on deployment requirements.

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
*Front Panel Component Identification: This diagram provides a close-up view of the front bezel of a Cisco 1000 Series ISR, clearly labeling the non-illuminated Cisco logo (labeled as #1) located centrally above the router's model designation "ISR 1000 Series." The diagram serves as a reference for identifying key physical features on the device's chassis, which is part of a larger, comprehensive overview of all front-panel components including the Kensington lock slot, power switch, LAN/WAN ports, and console/USB ports. The logo is a standard branding element, and its non-illuminated state distinguishes it from models that may feature an LED-lit logo for status indication.*

<--- End description image 10 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 4 --->

This table provides a labeled overview of the front panel components on the Cisco 1000 Series Integrated Services Routers, identifying key physical features such as the Kensington lock slot, power controls, network ports (including LAN and GE WAN), USB connectivity options, and console access points for system management and security.

<--- End description table 4 --->





<--- Start caption image 11 --->

Figure 4: C1101-4P ISR - I/O View

<--- End caption image 11 --->



<--- Start description image 11 --->

This is a detailed schematic diagram of the front panel of a Cisco network device chassis, likely a router or switch, providing a labeled guide to its physical components for installation, configuration, or troubleshooting.

**Key Components and Their Functions:**

*   **1. Non-illuminated Cisco Logo:** The brand identifier for the device.
*   **2. Kensington Lock Slot:** A security feature allowing the device to be physically secured to a desk or rack using a compatible lock.
*   **3. Power Switch:** A physical toggle or button to turn the device on or off.
*   **4. 4-pin Power Connector:** The input port for connecting the device's power supply unit (PSU). The label "12 VDC = 2.5A" indicates it requires a 12-volt direct current power source with a maximum current of 2.5 amperes.
*   **5. Reset Button:** A small button used to restore the device to its factory default settings, typically in case of configuration errors or boot failures.
*   **6. LAN Ports (0-4):** A set of five Ethernet ports (labeled 0 through 4) for connecting local area network devices. These are standard RJ-45 ports for wired network connections.
*   **7. GE WAN Port:** A Gigabit Ethernet Wide Area Network port, typically used for connecting to the internet or a wide area network (WAN) link.
*   **8. Micro USB Console Port:** A port for connecting a console cable to a computer, allowing for direct command-line interface (CLI) access for initial setup, configuration, or troubleshooting.
*   **9. USB 3.0 Port:** A high-speed USB port for connecting peripherals such as flash drives or external storage devices.

**Purpose of the Diagram:**
This diagram serves as a quick-reference guide for technicians and users. It clearly identifies each component's location and function, which is essential for:
*   **Installation:** Ensuring correct cable connections and physical setup.
*   **Troubleshooting:** Quickly locating ports or switches for diagnostics.
*   **Security:** Identifying the Kensington lock slot for securing the device.
*   **Configuration:** Using the console port for initial setup or recovery.

The diagram is a standard technical illustration used in device manuals and documentation to provide clarity on the physical layout of the device's front panel.

<--- End description image 11 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Kensington lock slot | 2 | Grounding |
| 3 | Power switch | 4 | 4-pin power connector |
| 5 | Reset button | 6 | LAN: 0-4 |
| 7 | GE WAN | 8 | Micro USB console |
| 9 | USB3.0 |  |  |


<--- Start description table 5 --->

This table highlights a visual reference for the non-illuminated Cisco logo as it appears in the Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router, likely serving as an identifier or branding element within the documentation.

<--- End description table 5 --->





<--- Start caption image 12 --->

Figure 5: C1101-4PLTEP-Bezel View

<--- End caption image 12 --->



<--- Start description image 12 --->

This is a close-up diagram from the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router," specifically highlighting component #1: the non-illuminated Cisco logo.

**Description and Significance:**
The image displays the front panel of a Cisco ISR 1100 Series router, with a clear, labeled pointer indicating the Cisco logo. The logo is presented as a simple, non-illuminated (non-backlit) graphic, which is typical for this model series. This visual is part of a larger, comprehensive labeling system used in the installation guide to help technicians and users correctly identify and locate key physical components on the device.

**Contextual Relevance:**
This specific diagram is the first in a series of labeled illustrations (as indicated by the table in the surrounding context) that systematically identifies all major features on the router's front panel, including:
*   Kensington lock slot
*   Grounding points
*   Power switch
*   Power and console ports
*   LAN and WAN interfaces
*   USB ports

The purpose of this guide is to provide a clear, visual reference for hardware installation and maintenance, ensuring users can accurately identify each component for proper setup and troubleshooting. The non-illuminated logo is a standard design element, distinguishing it from models with LED-lit branding.

<--- End description image 12 --->



|  |  |
|------|------|
| 1 | Non-illuminated Cisco logo |


<--- Start description table 6 --->

This table outlines the front panel layout and component labeling of the Cisco 1000 Series Integrated Services Router, detailing key hardware features such as the Kensington lock slot, power switch, reset button, network ports, and connectivity options including USB3.0 and micro USB console for management.

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
*   **5. GE WAN Port (Labeled "5"):** A single Gigabit Ethernet port (GE WAN) for connecting to a Wide Area Network, typically the internet.
*   **6. Micro-USB Console Port (Labeled "6"):** A port for connecting a console cable to access the router's command-line interface (CLI) for configuration and troubleshooting.
*   **7. Pluggable Module Slot (Labeled "7"):** A slot for inserting a pluggable module, such as a service module or a wireless module, to expand the router's functionality.
*   **8. Grounding Terminal (Labeled "8"):** A terminal for connecting the router to a grounding wire to ensure electrical safety.
*   **9. Kensington Lock Slot (Labeled "9"):** A slot for attaching a Kensington security lock to physically secure the router in place.
*   **Non-Illuminated Cisco Logo (Labeled "1"):** The Cisco brand logo, which is not lit up on this model.
*   **Main and Diversity Antenna (Labeled "2"):** Antennas for wireless communication, designed to provide both main and diversity reception for improved signal quality.

**Purpose and Significance:**

This diagram is essential for proper installation, configuration, and maintenance of the Cisco 1000 Series ISR. It allows users to correctly connect power, network cables, and peripherals, and to perform hardware-level troubleshooting. The inclusion of the grounding and Kensington lock slots highlights the importance of physical security and electrical safety in network infrastructure. The diagram's clarity and labeling make it a valuable tool for both new users and experienced technicians working with this specific router model.

<--- End description image 13 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Power switch | 2 | 4-pin power connector |
| 3 | Reset button | 4 | LAN:0-4 |
| 5 | GE WAN | 6 | Micro-USB console port |
| 7 | Pluggable | 8 | Grounding |
| 9 | Kensington lock slot |  |  |


<--- Start description table 7 --->

This table provides a visual guide to key components of the Cisco 1000 Series Integrated Services Routers, highlighting the non-illuminated Cisco logo and the main and diversity antenna as identifiable features on the chassis.

<--- End description table 7 --->





<--- Start caption image 14 --->

Figure 7: C1109-2PLTE - Bezel View

<--- End caption image 14 --->



<--- Start description image 14 --->

This image is a close-up diagram of the front panel of a Cisco ISR 1100 Series router, specifically highlighting its physical labeling and key components. The diagram serves as a reference guide for users to identify and locate critical ports and features on the device chassis.

**Key Components and Their Significance:**

*   **Cisco Logo (1):** The central, non-illuminated Cisco logo is a brand identifier. Its non-illuminated state indicates this is likely a non-rackmount or non-optimized model, as illuminated logos are common on higher-end or rack-mounted devices.
*   **Antennas (2):** The two circular ports on either side of the logo are the main and diversity antennas. These are essential for wireless connectivity, providing robust Wi-Fi or cellular signal reception and transmission. The "2" label indicates these are the primary antenna ports for the wireless interface.
*   **Model Identification:** The text "ISR 1100 Series" is clearly visible, identifying the specific product family. This is a line of integrated services routers designed for small and medium-sized businesses, offering routing, switching, and wireless capabilities in a single device.

**Overall Purpose:**
This diagram is a technical reference for network administrators or technicians. It provides a clear, labeled view of the router's front panel to ensure correct identification and connection of antennas, which is crucial for proper wireless configuration and performance. The non-illuminated logo and antenna placement suggest this is a standard, non-rackmount model, differentiating it from other variants in the ISR 1100 series.

<--- End description image 14 --->



|  |  |
|------|------|
| 1 | Non-illuminated Cisco logo |
| 2 | Main and diversity antenna |


<--- Start description table 8 --->

This table provides a labeled diagram of the front panel ports and controls for a networking device, detailing components such as the power switch, reset button, LAN and WAN ports, USB and SIM slots, grounding, and security features like the Kensington lock slot. The layout is presented in two mirrored sections, likely to show the same components from different viewing angles or to clarify labeling.

<--- End description table 8 --->





<--- Start caption image 15 --->

Figure 8: C1109-2PLTE - I/O View

<--- End caption image 15 --->



<--- Start description image 15 --->

This image is a detailed rear-view diagram of a Cisco wireless access point, specifically the model CT100-2PLTE3, providing a comprehensive labeling of its physical ports and connectors for installation and maintenance.

**Key Components and Their Functions:**

*   **Power and Control (Left Side):**
    *   **1. Kensington Lock Slot (1):** A security feature allowing the device to be physically secured to a desk or rack using a cable lock.
    *   **2. Grounding (2):** A terminal for connecting the device to a building's electrical ground to ensure safety and reduce electromagnetic interference.
    *   **3. Reset Button (3):** A small button used to restore the device to its factory default settings, typically by holding it down for a few seconds.
    *   **4. Power Switch (4):** A physical switch to turn the device on or off.
    *   **5. 4-pin Power Connector (5):** The input for the device's power supply, rated at 12VDC, 2.5A.

*   **Network and Management (Center):**
    *   **6. LAN Ports (6):** Two Ethernet ports (labeled LAN: 0 & 1) for connecting to local network switches or other devices.
    *   **7. GE WAN Port (7):** A Gigabit Ethernet port for connecting to the Wide Area Network (e.g., the internet or a central router).
    *   **8. Micro-USB Console Port (8):** A port for direct management and configuration via a console cable, useful for initial setup or troubleshooting when the device is not connected to a network.

*   **Wireless and Identification (Right Side):**
    *   **9. Micro-SIM Slots (9):** Two slots for inserting Micro-SIM cards, which are used to enable cellular (4G/LTE) connectivity for the device.
    *   **10. USB 3.0 Port (10):** A high-speed USB port for connecting peripherals or for firmware updates.
    *   **Cisco Logo (1):** A non-illuminated Cisco logo, indicating the brand and model.

**Significance:**

This diagram is an essential reference for network administrators and technicians. It clearly identifies every physical component on the back of the device, which is crucial for:
*   **Installation:** Correctly connecting power, network cables, and SIM cards.
*   **Troubleshooting:** Locating the reset button or console port to recover from configuration issues.
*   **Security:** Using the Kensington lock slot to secure the device in a physical environment.
*   **Maintenance:** Understanding the device's connectivity options and management interfaces.

The layout is designed for clarity, with numbered labels pointing directly to each feature, making it easy to identify and use the device's various ports and controls.

<--- End description image 15 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Kensington lock slot | 2 | Grounding |
| 3 | Reset button | 4 | Power switch |
| 5 | 4-pin power connector | 6 | LAN: 0 & 1 |
| 7 | GE WAN | 8 | Micro-USB console port |
| 9 | USB 3.0 | 10 | Micro-SIM slots 0 and 1 |


<--- Start description table 9 --->

This table provides a numbered layout of the front panel components on a Cisco networking device, identifying key ports and controls such as the power switch, LAN and WAN interfaces, USB ports, antenna connections, and security features like the Kensington lock slot.

<--- End description table 9 --->







<--- Start caption image 16 --->

Figure 9: C1109-4PLTE2PWX - I/O View

<--- End caption image 16 --->



<--- Start description image 16 --->

This image presents a detailed, multi-view diagram of the Cisco C1121-4Px router, illustrating its front and rear I/O panel layouts to aid in identification and physical installation. The diagrams are labeled with numbered callouts corresponding to a legend that identifies each component’s function.

**Key Components and Their Significance:**

*   **Front Panel (Bezel View - Figure 10):** This view shows the user-accessible controls and ports on the router’s front face.
    *   **Power and Reset:** The power switch (2) and reset button (3) allow for basic system control.
    *   **Connectivity:** It features a 4-pin power connector (4), a Micro-USB console port (8) for out-of-band management, and a Kensington lock slot (10) for physical security.
    *   **Wireless and Network:** A USB 3.0 port (9) is provided for peripheral connectivity, and an LTE antenna (9) is shown for cellular connectivity. The LAN ports are labeled as 0-4 (5), indicating a multi-port Ethernet switch.
    *   **Grounding:** A grounding point (1) is included for electrical safety.

*   **Rear Panel (I/O View - Figure 11):** This view details the back of the device, which houses the primary network and power interfaces.
    *   **Power and Reset:** The reset button (1) and power switch (2) are again shown for system control.
    *   **Network Interfaces:** The rear panel features a 4-pin power connector (3), a stacked RJ-45 connector (5) for Ethernet ports, and a dedicated GE WAN port (6) with both RJ-45 and SFP (fiber) options for flexible WAN connectivity.
    *   **Management and Security:** A Micro-USB console port (8) is present for management, and a Kensington lock slot (10) is included for physical security.
    *   **Grounding:** A grounding point (11) is located on the rear panel for safety.

**Overall Purpose:**
The diagrams serve as a reference guide for technicians and administrators to correctly identify, connect, and secure the Cisco C1121-4Px router. They are essential for proper installation, troubleshooting, and physical security, ensuring that all ports and controls are correctly understood and utilized. The inclusion of both front and rear views provides a complete picture of the device’s physical interface.

<--- End description image 16 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Grounding | 2 | Power switch |
| 3 | Reset button | 4 | 4-pin power connector |
| 5 | LAN:0-4 | 6 | GE WAN |
| 7 | USB 3.0 | 8 | Micro-USB console port |
| 9 | LTE antenna | 10 | Kensington lock slot |


<--- Start description table 10 --->

This table provides a detailed labeling of the rear and front panel ports and features of a Cisco networking device, including power connections, Ethernet and WAN interfaces, USB ports, SIM card slots, console access, and security/grounding elements, with some labels repeated across different views to indicate consistent component placement.

<--- End description table 10 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 11 --->

This table provides a labeled diagram of the rear panel ports and connectors for a network device, identifying components such as the power switch, reset button, Ethernet and WAN ports, USB 3.0, console port, LTE antenna, and grounding points, with additional labels for stacked and SFP interfaces in the second section.

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

This table provides a labeled diagram of the rear and front panel ports and connectors for a Cisco networking device, identifying key components such as power, Ethernet, USB, console, and security features, along with their corresponding pin or port numbers for reference during installation or troubleshooting.

<--- End description table 12 --->







<--- Start caption image 17 --->

Figure 12: C1121-4PLTEP I/O View

<--- End caption image 17 --->



<--- Start description image 17 --->

This image is a detailed rear-view diagram of a Cisco network device, likely a router or switch model such as the C121-4G-LP, illustrating its physical ports and control interfaces for installation, configuration, and maintenance.

**Key Components and Their Purpose:**

*   **1. Non-illuminated Cisco Logo:** Identifies the manufacturer and model series.
*   **2. Reset Button:** A small button used to restore the device to factory default settings, typically by holding it down for a few seconds.
*   **3. 4-pin Power Connector:** Accepts a standard 12V-24A DC power supply to provide electrical power to the device.
*   **4. Ethernet Switch (Port 0/2/x):** A multi-port Ethernet switch module for connecting multiple devices within a local network.
*   **5. GE 0/0/1 (Gigabit Ethernet Port 0/0/1):** A standard 10/100/1000 Mbps Ethernet port for connecting to a network.
*   **6. GE WAN 0/0/0 - RJ45:** A Gigabit Ethernet WAN port, configured for use with an RJ-45 cable, typically for connecting to an internet service provider or another network.
*   **7. GE WAN 0/0/0 - SFP:** A Gigabit Ethernet WAN port that uses an SFP (Small Form-factor Pluggable) module, allowing for flexible connectivity options such as fiber optic cables.
*   **8. Micro-USB Console Port:** A port for connecting a console cable to a computer, enabling direct command-line access for initial setup, troubleshooting, and configuration.
*   **9. USB 3.0 Port:** A high-speed USB port for connecting peripherals or for firmware updates.
*   **10. Pluggable (Kensington Lock Slot):** A slot for a Kensington security lock to physically secure the device to a desk or rack.
*   **11. Grounding:** A grounding terminal to ensure electrical safety by connecting the device to a proper ground.

**Significance:**
This diagram is essential for network administrators and technicians. It provides a clear reference for identifying and connecting all necessary cables and accessories, ensuring proper installation and configuration of the device within a network infrastructure. The presence of both RJ-45 and SFP ports highlights the device's flexibility for different network environments, while the console and USB ports support direct management and maintenance.

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

This table provides a labeled diagram of the front panel ports and controls for the Cisco 1000 Series Integrated Services Router, detailing components such as power and reset buttons, Ethernet and WAN ports, USB connectivity, and security features like the Kensington lock slot.

<--- End description table 13 --->





<--- Start caption image 18 --->

Figure 13: C1121(X)-8P - Bezel View

<--- End caption image 18 --->



<--- Start description image 18 --->

This image is a detailed component label diagram from the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 10," specifically highlighting the front panel of the device.

The diagram focuses on item 1, which is the **Non-illuminated Cisco logo**. It is located centrally on the front bezel of the router, positioned directly above the model designation "Cisco 1000 Series." The logo is depicted as a simple, unlit "Cisco" text mark, indicating that it does not serve as a status indicator (unlike illuminated logos on some other devices).

The purpose of this diagram is to provide clear, numbered identification for each physical component on the router's front panel, aiding technicians and users during installation, maintenance, or troubleshooting. The accompanying table explicitly labels item 1 as the "Non-illuminated Cisco logo," confirming its identity and function as a brand identifier rather than a functional or status indicator.

This specific view is part of a larger set of diagrams (as suggested by the context table) that collectively map out all 12 front-panel components, including critical interfaces like the power switch, Ethernet ports, and console port, ensuring users can correctly identify and interact with the device.

<--- End description image 18 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 14 --->

This table provides a labeled diagram of the front panel ports and controls for the Cisco 1000 Series Integrated Services Router, detailing components such as power and reset buttons, Ethernet and WAN ports, USB connectivity, a console port, and security/grounding features to assist with hardware installation.

<--- End description table 14 --->



[17]----------------------




<--- Start caption image 19 --->

Figure 14: C1121(X)-8P I/O View

<--- End caption image 19 --->



<--- Start description image 19 --->

This is a detailed front-panel diagram of the Cisco 1000 Series Integrated Services Router, providing a clear, labeled overview of its physical components and connectivity options. The diagram is essential for network administrators and technicians to correctly install, configure, and maintain the device.

**Key Components and Their Functions:**

*   **1. Reset Button:** A physical button used to reboot the router or restore factory defaults if needed.
*   **2. Power Switch:** A toggle switch to turn the router on or off.
*   **3. 4-pin Power Connector:** Accepts the power supply unit (PSU) to provide electrical power to the router.
*   **4. Ethernet Switch (Port 4):** A 4-port Ethernet switch for connecting multiple devices within a local network.
*   **5. GE 0/0/1 (Gigabit Ethernet Port 1):** A standard RJ-45 port for connecting to a local network or another device.
*   **6. GE WAN 0/0/0 - RJ45 (Gigabit WAN Port 0/0/0 - RJ45):** A WAN (Wide Area Network) port for connecting to the internet or a remote network via an Ethernet cable.
*   **7. GE WAN 0/0/0 - SFP (Gigabit WAN Port 0/0/0 - SFP):** An SFP (Small Form-factor Pluggable) slot for inserting a fiber optic transceiver module, enabling high-speed fiber connections for WAN links.
*   **8. Micro-USB Console Port:** A port for connecting a console cable to a computer for initial configuration, troubleshooting, or direct command-line access.
*   **9. USB 3.0 Port:** A high-speed USB port for connecting peripherals like flash drives or external devices.
*   **10. Kensington Lock Slot:** A security slot for attaching a physical lock to prevent unauthorized removal of the router from its location.
*   **11. Grounding:** A grounding terminal to ensure electrical safety by connecting the device to a proper ground.

**Significance:**

This diagram is a critical reference for anyone working with the Cisco 1000 Series router. It ensures correct physical setup, helps in identifying ports for specific connections (like WAN vs. LAN), and aids in troubleshooting by clearly labeling each component. The presence of both RJ-45 and SFP ports highlights the router's flexibility for connecting to different types of networks, whether copper or fiber. The inclusion of a console port and USB port also supports various management and configuration methods.

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

This table provides a labeled overview of the front panel components on the Cisco 1000 Series Integrated Services Router chassis, identifying key ports and controls such as the power switch, Ethernet and WAN interfaces, USB ports, console access, and security features like the Kensington lock slot.

<--- End description table 15 --->





<--- Start caption image 20 --->

Figure 15: C1121-8PLTEP I/O View

<--- End caption image 20 --->



<--- Start description image 20 --->

This is a detailed hardware installation diagram for the Cisco 1000 Series Integrated Services Router, illustrating the rear panel chassis views and labeling key physical components for proper setup and maintenance.

**Key Components and Their Functions:**

*   **1. Reset Button:** A small button used to reset the router to its factory default configuration.
*   **2. Power Switch:** A toggle switch to turn the router on or off.
*   **3. 4-pin Power Connector:** Accepts a 12V-24V DC power supply (48V-57V AC or 100-240V AC) to power the device.
*   **4. Ethernet Switch:** A 4-port Ethernet switch module for connecting multiple devices locally.
*   **5. GE 0/0/1 (RJ-45):** A Gigabit Ethernet (GE) port for local network connectivity.
*   **6. GE WAN 0/0/0 - RJ45:** A Gigabit Ethernet WAN port for connecting to a wide area network (e.g., the internet) via an RJ-45 cable.
*   **7. GE WAN 0/0/0 - SFP:** A Gigabit Ethernet WAN port that supports Small Form-Factor Pluggable (SFP) transceivers for fiber optic or other high-speed connections.
*   **8. Micro-USB Console:** A port for connecting a console cable to access the router's command-line interface (CLI) for configuration and troubleshooting.
*   **9. USB 3.0:** A high-speed USB port for connecting peripherals or for firmware updates.
*   **10. Pluggable (Kensington Lock Slot):** A slot for a Kensington security lock to physically secure the router in place.
*   **11. Grounding:** A grounding terminal to ensure electrical safety by connecting the device to a proper ground.

**Significance:**
This diagram is an essential reference for network administrators and technicians installing or maintaining the Cisco 1000 Series router. It provides a clear, labeled overview of all rear-panel interfaces, helping users correctly connect power, network cables, and peripherals while ensuring proper physical security and grounding. The diagram is part of the official Hardware Installation Guide, making it a critical resource for accurate and safe deployment.

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

This table provides a labeled diagram of the front panel ports and controls for the Cisco 1000 Series Integrated Services Router, detailing components such as the power switch, Ethernet and WAN ports, USB connectors, console access, and security features like the Kensington lock slot.

<--- End description table 16 --->





<--- Start caption image 21 --->

Figure 16: C1121-8PLTEPWx Bezel View

<--- End caption image 21 --->



<--- Start description image 21 --->

This image is a schematic diagram from the “Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router,” specifically illustrating the front panel of the device. The diagram is labeled with the number “1” pointing to the Cisco logo, which is centrally located on the router’s front bezel. Above the logo, the text “Cisco 1000 Series” is printed, identifying the product family. The diagram also includes the model number “369344” in the bottom-right corner, which is likely the product’s internal or catalog identifier.

The purpose of this diagram is to provide a clear, labeled reference for users during hardware installation or maintenance, helping them identify key components and their locations on the router’s front panel. While this specific image only shows the branding area, it is part of a larger guide that includes detailed labeling for all front-panel ports and controls, such as the reset button, power switch, Ethernet ports, and USB connectors, as described in the accompanying text. This visual aid ensures accurate identification and proper handling of the device during setup or troubleshooting.

<--- End description image 21 --->



[18]----------------------


|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 17 --->

This table provides a labeled overview of the front panel components on the Cisco 1000 Series Integrated Services Routers, identifying key ports, connectors, and controls such as the power switch, Ethernet and WAN interfaces, USB ports, Wi-Fi status indicator, and security/grounding features.

<--- End description table 17 --->





<--- Start description image 22 --->

This image provides a detailed, annotated overview of the front-panel I/O interfaces for two specific models within the Cisco 1000 Series Integrated Services Routers: the C1121(X)-8PLTEPW and the C1127X-8PLTEP. The diagrams serve as essential reference guides for network administrators and technicians, clearly labeling each physical component to facilitate proper installation, configuration, and troubleshooting.

**Key Components and Their Functions:**

*   **Power & Control (Figures 17 & 19):** Both models feature a **Reset button (1)** for system reboot, a **Power switch (2)** to turn the device on or off, and a **4-pin power connector (3)** for external power supply.
*   **Network Connectivity (Figures 17 & 19):** The routers offer multiple network interfaces. The **Ethernet switch (4)** provides a local network connection. The **GE WAN 0/0/0 -RJ45 (6)** and **GE WAN 0/0/0 -SFP (7)** ports are dedicated WAN (Wide Area Network) interfaces, supporting both copper (RJ45) and fiber (SFP) connections for connecting to the internet or a wide area network. The **GE 0/0/1 (5)** port is a general-purpose Gigabit Ethernet port.
*   **Management & Expansion (Figures 17 & 19):** A **Micro-USB console (8)** port is provided for direct command-line access and initial configuration. A **USB 3.0 port (10)** allows for data transfer and peripheral connectivity. A **Pluggable (9)** slot is designed for inserting a service module or expansion card.
*   **Security & Grounding (Figures 17 & 19):** A **Kensington lock slot (11)** is included for physical security, allowing the device to be secured to a desk or rack. A **Grounding (13)** terminal ensures electrical safety by providing a path to ground.
*   **Status & Identification (Figures 17 & 19):** A **Wi-Fi status indicator (5)** provides visual feedback on the wireless radio's operational state. The **Non-illuminated Cisco logo (1)** serves as a brand identifier.

**Significance:**

These diagrams are critical for ensuring correct physical setup and preventing damage during installation. They help users identify the correct ports for power, network, and management connections, which is vital for the router to function properly in a network environment. The inclusion of both RJ45 and SFP ports highlights the router's flexibility for different network infrastructure needs. The grounding and Kensington lock features emphasize the importance of physical security and safety in network deployments.

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

This table provides a labeled overview of the front panel components on a Cisco network device chassis, identifying key ports and controls such as the reset button, power switch, Ethernet and WAN interfaces, console access, and security/grounding features.

<--- End description table 18 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 19 --->

This table provides a labeled diagram of the physical components on the rear panel of a Cisco networking device, identifying key ports and connectors such as power inputs, Ethernet and WAN interfaces, USB ports, and security/grounding features for system management and connectivity.

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

This table provides a labeled diagram of the front panel ports and controls on a Cisco networking device, identifying key components such as the power switch, Ethernet and WAN ports, Wi-Fi status indicator, USB ports, and security/grounding features, along with the non-illuminated Cisco logo.

<--- End description table 20 --->







<--- Start caption image 23 --->

Figure 20: C1128-8PLTEP Bezel View

<--- End caption image 23 --->



<--- Start description image 23 --->

This is a detailed I/O panel diagram for the Cisco C1128-8PLTEP device, illustrating the physical layout and labeling of its rear-facing ports and controls. The diagram serves as a technical reference for network administrators and technicians to identify and connect the device’s various interfaces.

**Key Components and Their Functions:**

*   **Front Panel (Top):** The device features a non-illuminated Cisco logo (1) on its front bezel, indicating the brand.
*   **Rear Panel (Main Section):** The primary interface area includes:
    *   **Power & Control (Left):** A reset button (1), a power switch (2), and a 4-pin power connector (3) for supplying power to the unit.
    *   **Network Interfaces (Center):** An Ethernet switch (4) for local network connectivity, followed by two types of WAN (Wide Area Network) ports: a GE WAN 0/0/0 port with an RJ45 connector (6) for standard Ethernet cables, and a corresponding SFP (Small Form-factor Pluggable) slot (7) for fiber optic connections.
    *   **Console & Security (Right):** A Micro-USB console port (8) for direct command-line access and troubleshooting. A pluggable port (9) is likely for an optional module or cable. A Kensington lock slot (11) is provided for physical security. The device is also grounded (12) for electrical safety.
    *   **WAN Connectivity (Right):** A dedicated port for Symmetrical High-speed Digital Subscriber Lines (SHDSL) (10), which is a type of DSL technology for high-speed data transmission over telephone lines.

**Significance:**
This diagram is crucial for proper installation, configuration, and maintenance of the Cisco C1128-8PLTEP, which is likely a router or network access server. It provides a clear visual guide to ensure correct cable connections and physical setup, helping to prevent misconfigurations and potential damage. The inclusion of both copper (RJ45) and fiber (SFP) options highlights its versatility for different network environments. The SHDSL port specifically indicates its suitability for connecting to legacy or specialized DSL-based networks.

<--- End description image 23 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 21 --->

This table provides a labeled diagram of the front panel ports and controls on a Cisco networking device, identifying key components such as the reset button, power switch, Ethernet and WAN interfaces (including SFP and RJ45 options), USB ports, DSL connectivity, console access, Kensington lock slot, and grounding points. The layout is organized for quick reference during device setup or troubleshooting.

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

This table illustrates a visual reference for the non-illuminated Cisco logo as it appears on the Cisco 1000 Series Integrated Services Router, likely used in the Hardware Installation Guide to aid in identification or documentation during setup.

<--- End description table 22 --->





<--- Start caption image 24 --->

Figure 22: C1131(X)-8PLTEPW Bezel View

<--- End caption image 24 --->



<--- Start description image 24 --->

This is a close-up diagram from the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router," specifically highlighting the front panel of the device. The image focuses on component #1, which is the non-illuminated Cisco logo, located centrally on the router's chassis.

The diagram serves as a reference guide for technicians and users during the physical installation and identification of the router. The logo, while not lit, is a key visual identifier for the device model, which is also labeled as "ISR 1100 Series" on the front panel. This component is part of a larger set of 13 labeled features on the router's front, including the reset button, power switch, various network ports (Ethernet, SFP, WAN), USB ports, and a Kensington lock slot, all of which are essential for initial setup, connectivity, and security. The diagram's purpose is to provide a clear, labeled visual aid to ensure correct identification and handling of the hardware.

<--- End description image 24 --->



|  |  |  |
|------|------|------|
| 1 | Non-illuminated Cisco logo |  |


<--- Start description table 23 --->

This table provides a labeled diagram of the front panel components of the Cisco 1000 Series Integrated Services Router, detailing key hardware elements such as the power switch, Ethernet and WAN ports, USB connectors, and security features like the Kensington lock slot, aiding in proper installation and identification.

<--- End description table 23 --->



[20]----------------------




<--- Start caption image 25 --->

Figure 23: C1131(X)-8PLTEPW I/O Panel View

<--- End caption image 25 --->



<--- Start description image 25 --->

This is a detailed schematic diagram of the front panel of a Cisco 1000 Series Integrated Services Router (model 357490), providing a comprehensive overview of its physical components and their functions. The diagram is annotated with numbered labels (1–14) to guide users in identifying each port, button, and connector.

**Key Components and Their Functions:**

*   **1. Reset Button:** A small button used to reboot the router or restore factory defaults.
*   **2. Power Switch:** A toggle switch to turn the device on or off.
*   **3. 4-pin Power Connector:** The main power input port, typically for an external power adapter.
*   **4. Ethernet Switch:** A 4-port Ethernet switch (likely 10/100/1000 Mbps) for connecting multiple devices to the local network.
*   **5. Wi-Fi Status Indicator:** A light or LED that indicates the status of the built-in wireless (Wi-Fi) functionality.
*   **6. GE WAN 0/0/1 - SFP:** A Gigabit Ethernet WAN port with an SFP (Small Form-factor Pluggable) slot for fiber optic connections.
*   **7. GE WAN 0/0/1 - RJ45:** A Gigabit Ethernet WAN port with an RJ45 connector for copper cable connections.
*   **8. GE WAN 0/0/0 - RJ45:** Another Gigabit Ethernet WAN port for copper cable connections.
*   **9. GE WAN 0/0/0 - SFP:** Another Gigabit Ethernet WAN port with an SFP slot for fiber optic connections.
*   **10. Console Port:** A serial port (typically RS-232) used for initial configuration and troubleshooting via a console cable.
*   **11. USB 2.0 Port:** A USB port for connecting peripherals or for firmware updates.
*   **12. Pluggable:** This label points to the SFP slots (ports 6 and 9), indicating they are designed to accept pluggable transceivers for fiber connectivity.
*   **13. Kensington Lock Slot:** A security slot for attaching a cable lock to prevent theft.
*   **14. Grounding:** A grounding terminal to ensure electrical safety and reduce noise.

**Purpose of the Diagram:**
This diagram serves as a quick-reference guide for network administrators and technicians. It helps them identify and troubleshoot hardware components, connect devices correctly, and understand the physical layout of the router. It is essential for installation, maintenance, and configuration tasks, ensuring that users can properly interface with the router's various ports and controls.

<--- End description image 25 --->





<--- Start caption image 26 --->

Figure 24: C1131-8PLTEPW I/O Panel View

<--- End caption image 26 --->



<--- Start description image 26 --->

This is a comprehensive front-panel diagram of the Cisco 1000 Series Integrated Services Router (specifically model G1131-8PLTBPW), serving as a quick-reference guide for users to identify and understand the physical components and LED indicators.

**Key Components and Their Purpose:**

*   **1. Reset Button:** A small button used to reboot the router or restore factory defaults.
*   **2. Power Switch:** A toggle switch to turn the device on or off.
*   **3. 4-pin Power Connector:** The input port for connecting the router's power supply.
*   **4. Ethernet Switch:** A 4-port Ethernet switch for connecting multiple devices to the local network.
*   **5. Wi-Fi Status LED:** An indicator light that shows the status of the built-in Wi-Fi radio (e.g., connected, connecting, or off).
*   **6. GE WAN 0/0/1 - SFP:** A Small Form-Factor Pluggable (SFP) port for connecting to a WAN or uplink using fiber optic cable.
*   **7. GE WAN 0/0/1 - RJ45:** A standard Ethernet port for connecting to a WAN or uplink using copper cable.
*   **8. GE WAN 0/0/0 - RJ45:** A standard Ethernet port for connecting to a WAN or uplink using copper cable.
*   **9. GE WAN 0/0/0 - SFP:** A Small Form-Factor Pluggable (SFP) port for connecting to a WAN or uplink using fiber optic cable.
*   **10. Console Port:** A serial port (typically RS-232) for direct management and configuration using a console cable and terminal emulator software.
*   **11. USB 2.0 Port:** A USB port for connecting peripherals or for firmware updates.
*   **12. Pluggable:** This label points to the SFP slots (6, 9) and the RJ45 ports (7, 8), indicating these are modular and can be used with different types of cables or modules.
*   **13. Kensington Lock Slot:** A slot for a security cable to physically secure the router to a desk or cabinet.
*   **14. Grounding:** A grounding terminal to ensure electrical safety by connecting the device to a proper ground.

**LED Indicators (Not Shown in Detail in the Diagram, but Referenced in the Context):**

The diagram references "LED Indicators" (item 14) but does not show the actual lights. In a real-world scenario, these LEDs would be located near the power switch and console port, providing visual status information for power, network activity, and system health. The diagram's purpose is to help users quickly locate and understand the physical layout of the router's front panel for installation, troubleshooting, and maintenance.

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

This table outlines the LED indicators found on the bezel or chassis of the Cisco C111x series routers, providing a quick reference for monitoring system status and operational conditions during hardware installation and maintenance.

<--- End description table 24 --->



### LED Indicators


The following figures and table summarizes the LED indicators that are located in the bezel or chassis of the C111x series.

[21]----------------------




<--- Start caption image 27 --->

Figure 25: LED Indicators - Bezel Side

<--- End caption image 27 --->



<--- Start description image 27 --->

This diagram provides a comprehensive, labeled overview of the front panel of a Cisco 1000 Series Integrated Services Router (ISR), detailing its LED indicators and physical ports for user reference.

**Top Section: LED Indicators (Status & Connectivity)**
*   **LED 1 (Status):** Indicates the overall operational status of the router.
*   **LED 2 (VPN):** Shows the status of VPN connections.
*   **LED 3 (WLAN):** Indicates the status of the wireless LAN (Wi-Fi) interface.
*   **LED 4 (GPS):** Shows the status of the GPS module (if equipped).
*   **LED 5 (LTE RSSI/mode):** Displays the signal strength (RSSI) and operating mode of the LTE cellular connection.
*   **LED 6 (LTE data/SIM):** Indicates whether LTE data is active and the status of the SIM card.
*   **LED 7 (Cisco Logo):** A status indicator located near the Cisco logo, often used for power or system health.

**Bottom Section: Physical Ports and LEDs**
*   **Port 1 (GE WAN ports):** Eight Gigabit Ethernet WAN ports (labeled 0-7), arranged in two rows (top: 0, 2, 4, 6; bottom: 1, 3, 5, 7).
*   **LED 2 (PoE LED):** Indicates Power over Ethernet status for connected devices.
*   **LED 3 (GE1 LED):** Status indicator for the GE1 port.
*   **LED 4 (GE0 LED):** Status indicator for the GE0 port.
*   **LED 5 (USB LED):** Indicates activity on the USB port.
*   **LED 6 (RJ-45 console LED):** Shows activity on the console port.
*   **Port 7 (USB console):** A USB port for console access.
*   **LED 8 (Micro USB console LED):** Indicates activity on the micro USB console port.
*   **LED 9 (CD LED):** Indicates the status of the CD drive (if present).
*   **LED 10 (DATA LED):** Indicates general data activity on the device.

This diagram is a critical reference tool for network administrators and technicians, enabling them to quickly diagnose hardware status and connectivity issues by interpreting the visual cues from the router's front panel.

<--- End description image 27 --->



|  |  |  |  |
|------|------|------|------|
| 1 | Status | 2 | VPN |
| 3 | WLAN | 4 | GPS |
| 5 | LTE RSSI/mode | 6 | LTE data/SIM |
| 7 | Cisco logo |  |  |


<--- Start description table 25 --->

This table provides a labeled layout of the front panel LED indicators and ports on the Cisco 1000 Series Integrated Services Router, detailing the location and function of each component such as GE WAN ports, PoE status, USB connections, and console interfaces, as referenced in the Hardware Installation Guide.

<--- End description table 25 --->





<--- Start caption image 28 --->

Figure 26: LED Indicators - I/O Side

<--- End caption image 28 --->



<--- Start description image 28 --->

This is a top-down schematic diagram from the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 15," illustrating the front panel layout and labeling of its physical ports and indicator lights.

**Purpose:** The diagram serves as a quick-reference guide for technicians and users to identify and understand the function of each component on the router’s front panel, facilitating proper installation, configuration, and troubleshooting.

**Key Components and Their Functions:**

*   **LED Indicators (Top Row, Labeled 1-7):** These are status lights that provide real-time feedback on the router's operational state.
    *   **1 (Status):** General system status.
    *   **2 (VPN):** Indicates VPN tunnel activity.
    *   **3 (WLAN):** Shows the status of the wireless LAN (Wi-Fi) interface.
    *   **4 (GPS):** Indicates GPS signal reception.
    *   **5 (LTE RSSI/mode):** Displays the signal strength (RSSI) and mode of the LTE cellular connection.
    *   **6 (LTE data/SIM):** Indicates LTE data activity and SIM card status.
    *   **7 (Cisco logo):** A branding indicator.

*   **Ethernet and Console Ports (Bottom Row, Labeled 1-11):** These are the physical connection points for networking and management.
    *   **1 (GE WAN ports: 0-7):** Eight Gigabit Ethernet WAN ports, arranged in two rows (top: 0, 2, 4, 6; bottom: 1, 3, 5, 7).
    *   **2 (PoE LED):** Power over Ethernet indicator light.
    *   **3 (GE1 LED):** Status light for the first Gigabit Ethernet port.
    *   **4 (GE0 LED):** Status light for the zeroth Gigabit Ethernet port.
    *   **5 (USB LED):** Indicates USB port activity.
    *   **6 (RJ-45 console LED):** Status light for the standard RJ-45 console port.
    *   **7 (USB console):** A USB port for console access.
    *   **8 (Micro USB console LED):** Status light for the micro USB console port.
    *   **9 (CD LED):** Indicates CD drive activity (if applicable).
    *   **10 (DATA LED):** General data activity indicator.

This diagram is essential for users to quickly locate and interpret the status of various services and connections on the Cisco 1000 Series router, ensuring smooth deployment and efficient network management.

<--- End description image 28 --->



|  |  |  |  |
|------|------|------|------|
| 1 | GE WAN ports: 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) | 2 | PoE LED |
| 3 | GE1 LED | 4 | GE0 LED |
| 5 | USB LED | 6 | RJ-45 console LED |
| 7 | USB console | 8 | Micro USB console LED |
| 9 | CD LED | 10 | DATA LED |


<--- Start description table 26 --->

This table outlines key hardware and connectivity indicators for the Cisco 1000 Series Integrated Services Router, including status, VPN, WLAN, GPS, LTE signal strength and mode, LTE data/SIM information, and the Cisco logo — all relevant to the router’s physical and network interface features as detailed in the Hardware Installation Guide.

<--- End description table 26 --->



[22]----------------------




<--- Start caption image 29 --->

Figure 27: Cisco 1121-4Px LED Indicators

<--- End caption image 29 --->



<--- Start description image 29 --->

This diagram provides a comprehensive, labeled overview of the front panel LED indicators for the Cisco 1000 Series Integrated Services Router (specifically model C1121-4P, as indicated on the device). It serves as a critical reference guide for network administrators and technicians to monitor the router’s operational status in real-time.

**Key Components and Their Significance:**

*   **LED Indicators (1-9):** Each numbered LED corresponds to a specific function, allowing users to quickly diagnose connectivity, power, and system health.
*   **VPN LED (1):** Indicates the status of the router's Virtual Private Network (VPN) connections. This is essential for monitoring secure remote access and site-to-site tunneling.
*   **PoE LED (2):** Shows the status of Power over Ethernet (PoE) power delivery to connected devices. This is vital for managing power consumption and ensuring connected IP phones or access points are receiving power.
*   **Status LED (3):** A general system status indicator. It typically shows power, system boot, and overall health, providing a quick glance at whether the router is operational.
*   **Ethernet Switch Ports (4):** This section includes four Ethernet switch ports (labeled 0-3). The LEDs for these ports (5, 6, 7) indicate the link and activity status for each individual port, helping to identify which devices are connected and if data is being transmitted.
*   **GE 0/0/0 RJ45 LED (5 & 7):** These are the LEDs for the two Gigabit Ethernet (GE) RJ45 ports. They provide status for the primary network interfaces, showing if they are connected and active.
*   **GE 0/0/1 LED (6):** This LED monitors the status of the second Gigabit Ethernet port, which is often used for WAN or management connections.
*   **Micro USB Console LED (8):** Indicates the status of the console port, which is used for direct command-line access and troubleshooting. This is crucial for initial setup and recovery.
*   **USB LED (9):** Shows the status of the USB port, which can be used for firmware updates, storage, or connecting peripherals.

**Purpose of the Diagram:**
The primary purpose of this diagram is to provide a clear, visual reference for interpreting the LED indicators on the Cisco 1000 Series router. By understanding what each light signifies, network engineers can rapidly identify issues such as failed connections, power problems, or system errors, enabling faster troubleshooting and minimizing downtime. This is a fundamental tool for maintaining the reliability and performance of network infrastructure.

<--- End description image 29 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet switch ports 0-3 |
| 5 | GE 0/0/0 RJ45 LED | 6 | GE 0/0/1 LED |
| 7 | GE 0/0/0 RJ45 LED | 8 | Micro USB console LED |
| 9 | USB LED |  |  |


<--- Start description table 27 --->

This table provides a clear mapping of the LED indicator locations on the Cisco 1000 Series Integrated Services Router, detailing which physical ports and components correspond to specific LED numbers—from VPN and PoE indicators to Ethernet ports, console, and USB connections—helping users identify and troubleshoot hardware status during installation or operation.

<--- End description table 27 --->





<--- Start caption image 30 --->

Figure 28: Cisco 1121-4PLTEP LED Indicators

<--- End caption image 30 --->



<--- Start description image 30 --->

This diagram is a hardware reference guide for the Cisco 1000 Series Integrated Services Router (model C1121-4PLTSP), specifically illustrating the front panel LED indicators and their corresponding ports. It serves as a quick-reference tool for network administrators and technicians to monitor the router’s operational status.

**Key Components and Their Significance:**

*   **LED Indicators (1-9):** The diagram labels nine distinct LED indicators, each providing real-time status information about the router’s functions.
    *   **1 (VPN):** Indicates the status of the router’s Virtual Private Network (VPN) connections.
    *   **2 (PoE LED):** Shows the Power over Ethernet (PoE) status, which is critical for powering connected devices like IP phones or wireless access points.
    *   **3 (Status):** A general system status indicator, typically showing power and overall health.
    *   **4 (Ethernet switch ports 0-3):** A group of LEDs that monitor the activity and link status of the four integrated Ethernet switch ports.
    *   **5 & 7 (GE 0/0/0 RJ45 LED):** These are two separate LEDs for the same Gigabit Ethernet (GE) port (0/0/0), likely indicating different states such as link/activity and speed (e.g., 10/100/1000 Mbps).
    *   **6 (GE 0/0/1 LED):** Monitors the activity and link status of the second Gigabit Ethernet port (0/0/1).
    *   **8 (Micro USB console LED):** Indicates the status of the console port, which is used for local management and configuration via a USB-to-serial adapter.
    *   **9 (USB LED):** Shows the status of the USB port, which may be used for firmware updates or connecting external storage devices.

*   **Physical Layout:** The diagram clearly shows the physical arrangement of these LEDs and ports on the router’s front panel, helping users quickly locate and interpret the status of each component.

**Purpose:**
This guide is essential for troubleshooting and routine maintenance. By observing the state of these LEDs (e.g., solid, blinking, off), technicians can quickly diagnose issues such as network connectivity problems, power failures, or configuration errors without needing to access the router’s command-line interface. It is a foundational tool for ensuring the router operates correctly within a network infrastructure.

<--- End description image 30 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet switch ports 0-3 |
| 5 | GE 0/0/0 RJ45 LED | 6 | GE 0/0/1 LED |
| 7 | GE 0/0/0 RJ45 LED | 8 | Micro USB console LED |
| 9 | USB LED |  |  |


<--- Start description table 28 --->

This table provides a pinout or component layout for the front panel of the Cisco 1000 Series Integrated Services Router, detailing labeled ports and LEDs including VPN, PoE, status indicators, Ethernet switch ports, and console/USB connectivity, as referenced in the Hardware Installation Guide.

<--- End description table 28 --->



[23]----------------------




<--- Start caption image 31 --->

Figure 29: Cisco 11x1(X)-8P/ C11x1(X)-8PLTEP LED Indicators

<--- End caption image 31 --->



<--- Start description image 31 --->

This diagram provides a detailed, labeled overview of the front panel LED indicators and ports on a Cisco 1000 Series Integrated Services Router, specifically the model C1121-SPLTPS. It serves as a quick-reference guide for network administrators and technicians to interpret the device's operational status at a glance.

**Key Components and Their Significance:**

*   **LED Indicators (1-9):** These are the primary visual status indicators for the router's health and connectivity.
    *   **1 (VPN LED):** Indicates the status of VPN (Virtual Private Network) services. A solid light typically signifies an active VPN connection.
    *   **2 (PoE LED):** Shows the status of Power over Ethernet (PoE) power delivery to connected devices. It helps confirm if the router is successfully powering devices like IP phones or wireless access points.
    *   **3 (Status LED):** A general system status indicator. It typically blinks or illuminates to show the router is powered on and operational.
    *   **4 (Ethernet Switch Ports 0-7):** This section shows the status of the 8-port Ethernet switch. Ports are arranged in two rows: top row (0, 2, 4, 6) and bottom row (1, 3, 5, 7). An illuminated LED for a port indicates that a device is connected and the link is active.
    *   **5 (GE 0/0/0 RJ45 LED):** Indicates the status of the primary Gigabit Ethernet port (GE 0/0/0) connected via an RJ45 cable. This is often the main WAN or uplink connection.
    *   **6 (GE 0/0/1 LED):** Indicates the status of the secondary Gigabit Ethernet port (GE 0/0/1). This port is often used for a secondary connection or for connecting to another network device.
    *   **7 (GE 0/0/0 RJ45 LED):** This is a duplicate label for the same port as #5, likely for redundancy or to highlight its importance.
    *   **8 (Micro USB Console LED):** Indicates the status of the Micro USB port used for console access (for configuration and troubleshooting via a terminal emulator).
    *   **9 (USB LED):** Indicates the status of the USB port, which can be used for connecting external storage or other USB devices.

**Purpose of the Diagram:**

The primary purpose of this diagram is to provide a clear, visual reference for users to quickly identify and understand the function of each LED indicator and port on the Cisco 1000 Series router. This is crucial for:
*   **Troubleshooting:** Quickly diagnosing connectivity or power issues by observing which LEDs are lit or blinking.
*   **Configuration:** Verifying that the router is properly connected to the network and powered on.
*   **Maintenance:** Ensuring that all ports and services are functioning as expected.

In summary, this diagram is an essential tool for anyone working with Cisco 1000 Series routers, enabling rapid assessment of the device's operational state through its front-panel indicators.

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

This table from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide provides a labeled diagram of the front panel LED indicators, detailing the function of each light from 1 to 10, including status LEDs for VPN, PoE, Wi-Fi, Ethernet ports, SFP modules, USB, and console connectivity.

<--- End description table 29 --->





<--- Start caption image 32 --->

Figure 30: C1121(X)-8PLTEPWx LED Indicators

<--- End caption image 32 --->



<--- Start description image 32 --->

This is a detailed front-panel diagram of the Cisco 1000 Series Integrated Services Router (model C1121-8PLTPW), serving as a hardware installation guide. The image systematically labels and identifies each component on the router’s front interface to assist technicians and users in proper setup and troubleshooting.

**Key Components and Their Functions:**

*   **1. VPN Button:** A physical button used to initiate or manage Virtual Private Network (VPN) connections.
*   **2. PoE LED (Power over Ethernet):** An indicator light that shows the status of Power over Ethernet (PoE) power delivery to connected devices.
*   **3. Status LED:** A general system status indicator, typically showing power, system health, or operational state.
*   **4. Ethernet Switch Ports (0-7):** An 8-port Ethernet switch. Ports are arranged in two rows: top row (0, 2, 4, 6) and bottom row (1, 3, 5, 7). These ports support Gigabit Ethernet (GE) connections for wired networking.
*   **5. GE 0/0/0 RJ45 LED:** An indicator light for the first Gigabit Ethernet port (GE 0/0/0) when connected via an RJ45 cable.
*   **6. GE 0/0/1 LED:** An indicator light for the second Gigabit Ethernet port (GE 0/0/1) when connected via an RJ45 cable.
*   **7. GE 0/0/0 SFP LED:** An indicator light for the first Gigabit Ethernet port (GE 0/0/0) when connected via an SFP (Small Form-factor Pluggable) transceiver module.
*   **8. Micro USB Console LED:** An indicator light for the Micro USB port, which is used for console access and configuration.
*   **9. USB LED:** An indicator light for the USB port, which may be used for storage or peripheral device connectivity.
*   **10. Wi-Fi LED:** An indicator light for the wireless (Wi-Fi) functionality of the router.

**Significance:**
This diagram is a critical reference for network administrators and installers. It enables them to:
-   Physically identify and connect devices to the correct ports.
-   Monitor the operational status of the router and its interfaces via the LED indicators.
-   Troubleshoot connectivity or power issues by observing which LEDs are lit or not.
-   Understand the router’s physical layout before beginning installation or configuration.

The diagram is part of the official "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 17," ensuring users have a standardized and accurate reference for the device’s front panel.

<--- End description image 32 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet Switch Ports 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) |
| 5 | Wi-Fi | 6 | GE 0/0/0 RJ45 LED |
| 7 | GE 0/0/1 LED | 8 | GE 0/0/0 SFP LED |
| 9 | USB LED | 10 | Micro USB console LED |


<--- Start description table 30 --->

This table provides a pinout and component labeling diagram for the front panel of the Cisco 1000 Series Integrated Services Router, detailing ports and LEDs such as VPN, PoE, Ethernet switch ports, and console/USB indicators, to assist with hardware installation and identification.

<--- End description table 30 --->



[24]----------------------




<--- Start caption image 33 --->

Figure 31: Cisco 1126(X)-8PLTEP/ C1127(X)-8PxLTEP LED Indicators

<--- End caption image 33 --->



<--- Start description image 33 --->

This diagram provides a detailed, labeled overview of the front panel of a Cisco 1000 Series Integrated Services Router, specifically the model "ISR 1000-2P-1000-2P" (as indicated by the text on the device). Its purpose is to serve as a quick-reference guide for users to identify and understand the function of each LED indicator and port, which is critical for monitoring the router's operational status, connectivity, and power.

The diagram is organized from left to right, with numbered callouts pointing to each component:

*   **LED Indicators (1-3):** These are status lights located on the left side of the device.
    *   **1 (VPN LED):** Indicates the status of VPN (Virtual Private Network) connections.
    *   **2 (PoE LED):** Indicates the status of Power over Ethernet (PoE) power delivery.
    *   **3 (Status LED):** A general system status indicator, typically showing power and overall health.

*   **Ethernet Switch Ports (4):** This is a bank of 8 Ethernet ports (labeled 0-7) for connecting network devices. The diagram shows their physical layout, with ports 0, 2, 4, and 6 positioned at the top and ports 1, 3, 5, and 7 at the bottom.

*   **GE 0/0/0 RJ45 LED (5):** An LED indicator for the first Gigabit Ethernet port (GE 0/0/0) when using an RJ45 cable connection.

*   **GE 0/0/0 SFP LED (7):** An LED indicator for the first Gigabit Ethernet port (GE 0/0/0) when using an SFP (Small Form-factor Pluggable) module.

*   **USB5 LED (6):** An LED indicator for the USB 5 port, which is typically used for connecting a USB flash drive or other USB devices.

*   **Micro USB Console LED (8):** An LED indicator for the Micro USB port, which is used for console access and debugging.

*   **CD LED (9):** An LED indicator for the CD (Compact Disc) drive, which is used for installing software or firmware.

*   **Port 10:** This is the final port shown, which is a standard RJ45 Ethernet port, likely used for management or additional connectivity.

This diagram is essential for network administrators and technicians to quickly diagnose issues by observing the state of these LEDs, ensuring the router is properly powered, connected, and functioning as expected.

<--- End description image 33 --->



|  |  |  |  |
|------|------|------|------|
| 1 | VPN | 2 | PoE LED |
| 3 | Status | 4 | Ethernet Switch Ports 0-7 (0, 2, 4, 6 at the top and 1, 3, 5, 7 at the bottom) |
| 5 | GE 0/0/0 RJ45 LED | 6 | USB5 LED |
| 7 | GE 0/0/0 SFP LED | 8 | Micro USB console LED |
| 9 | CD LED |  |  |


<--- Start description table 31 --->

This table provides a labeled layout of the LED indicators on the Cisco 1000 Series Integrated Services Routers, identifying key status lights such as VPN, PoE, Wi-Fi, Ethernet ports, SFP and RJ45 interfaces, USB, and console connectivity indicators, helping users quickly locate and interpret hardware status.

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
    *   **Ethernet Switch Ports (4):** Eight 10/100/1000 Ethernet ports (0-7) for wired network connections.
    *   **SFP Slots (6, 9):** Two slots for SFP modules, allowing for fiber optic or other high-speed connections.
    *   **RJ45 Ports (7, 8):** The physical RJ45 connectors for the Gigabit Ethernet ports.
    *   **USB Port (10):** A USB port for connecting a USB device, typically for firmware updates or console access.
    *   **Console Port (11):** A serial console port for direct management and configuration.

This diagram is essential for network administrators to quickly diagnose issues, monitor device health, and configure the switch by understanding the meaning of each LED and port.

<--- End description image 34 --->





<--- Start caption image 35 --->

Figure 33: C1131-8PW LED Indicators

<--- End caption image 35 --->



<--- Start description image 35 --->

This is a front-panel diagram of the Cisco C111x series network switch, detailing the location and function of its LED indicators and ports. The diagram serves as a quick-reference guide for users to monitor the device’s operational status and connectivity.

**Key Components and Their Significance:**

*   **LED Indicators (1-11):** These lights provide real-time status feedback for various functions:
    *   **1 (VPN):** Indicates the status of the Virtual Private Network (VPN) connection.
    *   **2 (PoE LED):** Shows the status of Power over Ethernet (PoE) power delivery to connected devices.
    *   **3 (Status):** A general system status indicator, often showing power and overall health.
    *   **4 (Ethernet Switch Ports 0-7):** This section shows the status of eight Ethernet ports, arranged in two rows (top: 0, 2, 4, 6; bottom: 1, 3, 5, 7). Each port has its own LED to indicate link/activity.
    *   **5 (GE 0/0/0 RJ45 LED):** Indicates activity and link status for the first Gigabit Ethernet port (GE 0/0/0) when using an RJ45 cable.
    *   **6 (USB5 LED):** Indicates the status of the USB 5 port, typically used for device connectivity or firmware updates.
    *   **7 (GE 0/0/0 SFP LED):** Shows the status of the first Gigabit Ethernet port (GE 0/0/0) when using an SFP (Small Form-factor Pluggable) module.
    *   **8 (Micro USB console LED):** Indicates the status of the console port, used for direct management and configuration via a USB-to-serial adapter.
    *   **9 (CD LED):** Indicates the status of the Compact Disc (CD) drive, if equipped.
    *   **10 (USB LED):** Indicates the status of the USB port, often used for connecting external storage or peripherals.
    *   **11 (Console LED):** Indicates the status of the console port, used for direct management and configuration.

*   **Ports and Interfaces:**
    *   **Ethernet Switch Ports (0-7):** Eight Gigabit Ethernet ports for connecting to other network devices.
    *   **GE 0/0/0 RJ45 & SFP:** Two interfaces for the first Gigabit Ethernet port, supporting both standard RJ45 cables and SFP modules for fiber connectivity.
    *   **GE 0/0/1 SFP:** A second Gigabit Ethernet port, also supporting SFP modules.
    *   **USB Ports:** For connecting external devices or for console access.
    *   **Console Port:** For direct management and configuration via a terminal emulator.

This diagram is essential for network administrators to quickly diagnose issues, monitor device health, and ensure proper connectivity.

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

This table provides a detailed reference for the LED indicators located on the bezel and chassis of the Cisco C111x series routers, mapping each LED’s location, color, behavior, and associated system status or control source. It covers system power, VPN connectivity, LTE/GPS/WLAN status, Ethernet port activity (including PoE), DSL line conditions, and USB/console interfaces, helping users interpret hardware status at a glance.

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

This table provides a detailed reference for the LED indicators located on the bezel or chassis of the C111x series devices, mapping each LED’s position, color, and function to help users monitor system status, network connectivity, and peripheral activity. It includes indicators for power, VPN, Ethernet ports, LTE modems, Wi-Fi, USB, and console interfaces, with descriptions of their states (e.g., off, steady on, blinking) and the control source (I/O or Bezel side).

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

This table provides a comprehensive overview of the LED indicators found on the bezel and I/O side of the C111x series routers, detailing each LED’s color, behavior, and corresponding system status or control source. It covers system power, network connectivity (including LTE, GPS, WLAN, Ethernet, and PoE), console and USB activity, and DSL status, helping users visually monitor operational health and configuration states.

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

This table outlines the interface naming convention for the Cisco 1100 series routers, using a 3-tuple format (slot/sub-slot/port) to identify each interface, where slot "0" is reserved for the motherboard and sub-slots are assigned per interface type.

<--- End description table 35 --->



### Specifications of Cisco 1000 Series Integrated Services Routers


For specifications on the Cisco 1000 Series Integrated Services Routers, refer to the Cisco 1100 Series ISR Specifications document.

## Periodic Inspection and Cleaning


We recommend that you periodically inspect and clean the external surface of the router. Removing is recommended to minimize the negative impact of environmental dust or debris. The frequency of inspection and cleaning is dependent upon the severity of the environmental conditions, but we recommend cleaning the router once every six months. Cleaning involves vacuuming router air intake and exhaust vents.



Note

Sites with ambient temperatures consistently above 25°C or 77°F and with potentially high levels of dust or debris might require periodic preventative maintenance cleaning.

[31]----------------------




<--- Start description image 37 --->

This is the chapter header image for Chapter 2 of the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 24." The image uses a professional, modern cityscape with a sun flare to convey a sense of technological advancement and enterprise-scale infrastructure.

The large, bold number "2" and the text "CHAPTER 2" clearly indicate the section's position within the guide. The surrounding context, "Prepare for Router Installation," suggests this chapter focuses on the initial setup and planning stages before physical hardware deployment.

The background image of a city skyline, complete with a construction crane, serves as a powerful metaphor. It visually represents the foundational work and infrastructure development that the guide aims to help the reader undertake. The scene implies that installing a Cisco router is a critical step in building or expanding a robust, modern network infrastructure, much like constructing the physical buildings and systems that form the backbone of a city.

In essence, the image functions as a visual anchor for the chapter, setting the tone for the preparatory work ahead and connecting the technical task of router installation to the broader, real-world context of building and maintaining critical digital infrastructure.

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

This table outlines the network cabling specifications necessary for installing the Cisco 1000 Series Integrated Services Router, including details relevant to console port configurations and other connectivity requirements.

<--- End description table 36 --->



## Network Cabling Specifications


The following sections describe the cables and the specifications required to install Cisco 1000 Series Integrated Services Router:

### Console Port Considerations


The router includes an asynchronous serial console port. The console ports provide access to the router using a console terminal connected to the console port. This section discusses important cabling information to consider before connecting the router to a console terminal or modem.

Console terminals send data at speeds slower than modems do; therefore, the console port is ideally suited for use with console terminals.

#### EIA/TIA-232


Depending on the cable and the adapter used, this port appears as a DTE or DCE device at the end of the cable. Only one port can be used at the same time.

The default parameters for the console port are 9600 baud, 8 data bits, 1 stop bit, and no parity. The console port does not support hardware flow control. For detailed information about installing a console terminal, see the Connecting to a Console Terminal or Modem section.

For cable and port pinouts, see the Cisco Modular Access Router Cable Specifications document located on Cisco.com.

#### USB Serial Console


The USB serial console port connects directly to the USB connector of a PC using a USB Type A to 5-pin micro USB Type-B cable. The USB Console supports full speed (12Mb/s) operation. The console port does not support hardware flow control.

[36]----------------------




Note

Always use shielded USB cables with a properly terminated shield.

USB Console OS Compatibility


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

### Console Port Considerations


The router includes an asynchronous serial console port. The console ports provide access to the router using a console terminal connected to the console port. This section discusses important cabling information to consider before connecting the router to a console terminal or modem.

Console terminals send data at speeds slower than modems do; therefore, the console port is ideally suited for use with console terminals.

### Prepare for Router Installation


Before you install the Cisco 1000 Series Integrated Services Routers, you must prepare your site for the installation. This chapter provides pre-installation information, such as recommendations and requirements that should be considered before installing your router.

[37]----------------------


See the following sections to prepare for installation:

#### Ethernet Connections


The IEEE has established Ethernet as standard IEEE 802.3. The routers support the following Ethernet implementations:

|  |  |
|------|------|
| 1000BASE-T—1000 Mb/s full-duplex transmission over a Category 5 or better unshielded twisted-pair (UTP) cable. | Supports the Ethernet maximum length of 328 feet (100 meters). |
| 100BASE-T—100 Mb/s full-duplex transmission over a Category 5 or better unshielded twisted-pair (UTP) cable. | Supports the Ethernet maximum length of 328 feet (100 meters). |
| 10BASE-T—10 Mb/s full-duplex transmission over a Category 5 or better unshielded twisted-pair (UTP) cable. | Supports the Ethernet maximum length of 328 feet (100 meters). |


<--- Start description table 37 --->

This table outlines the Ethernet implementations supported by the routers, referencing the IEEE 802.3 standard and directing users to Cisco’s documentation for detailed cable and connector specifications. It is part of a broader guide that also lists required tools and equipment for router installation and maintenance.

<--- End description table 37 --->



See the Cisco Modular Access Router Cable Specifications document at Cisco.com for information about Ethernet cables, connectors, and pinouts.

## Required Tools and Equipment for Installation and Maintenance


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


## Unpack the Router


Unpack the router only when you are ready to install it. If the installation site is not ready, to prevent accidental damage, keep the chassis in its shipping container until you are ready to install.

The router, accessory kit, publications, and any optional equipment you order may be shipped in more than one container. When you unpack the containers, check the packing list to ensure that you have received all the listed items.

## Set up Router on Desktop, Rack, or Wall


After unpacking, based on your requirements, you can set up a Cisco 1000 Series Integrated Services Router on a desktop, a rack, or the wall.

[40]----------------------




Note


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

This table outlines the mounting and installation options for the Cisco 1000 Series Integrated Services Router, including desktop, rack, and wall mounting configurations, along with considerations for installing external modules before or after mounting. It emphasizes the need for accessible front and back panel access when installing modules post-mounting and references additional documentation for module and FRU installation procedures.

<--- End description table 38 --->



If you choose to setup the router on a desktop, you can place the router on a desktop, bench top or on a shelf.

### Rack Mount


Secure the rack mounting brackets on the sides of the chassis. You must first secure rack mounting brackets on the chassis before you set up the chassis on the rack.

[41]----------------------




Caution

Do not stack multiple Cisco 1000 Series Integrated Services Routers when mounting the routers on a table top.

Do not put any object on the sides or on top of the routers ensuring that there is ample space for air circulation and heat removal.



Important


Periodic Inspection and Cleaning : We recommend that you periodically inspect and clean the external surface of the router. Removing is recommended to minimize the negative impact of environmental dust, debris, and liquid contamination. The frequency of inspection and cleaning is dependent upon the severity of the environmental conditions, but we recommend cleaning the router once every six months. Cleaning involves vacuuming router air intake and exhaust vents.



Note

Using the top plate on the chassis significantly helps in preventing any damages that may occur from rodent infestation.



Note

Sites with ambient temperatures consistently above 25°C or 77°F and with potentially high levels of dust or debris might require periodic preventative maintenance cleaning.



Note

Whenmounting Cisco 1000 Series Integrated Services Routers on a rack, ensure that there is ample surrounding space. This ensures more heat removal, which in turn helps the surrounding air temperature to stay within the specified operating conditions.

#### Attach the Rack Mount Brackets for C111x


This procedure describes how to attach the rack mount brackets on the router chassis:

Step 1 Secure the brackets to the router chassis (on the left) as shown in figure below:

Example:


[42]----------------------




<--- Start caption image 62 --->

Figure 34: Bracket Installation for Left-Side Mounting - C111x

<--- End caption image 62 --->



<--- Start description image 62 --->

This technical diagram illustrates Step 2 of the installation procedure for a Cisco C111x router, showing how to attach the top plate (C1110-TOP-PLATE=) to the chassis and secure the mounting brackets on the right side for desktop installation.

**Key Components and Purpose:**
*   **Router Chassis:** The main body of the Cisco C111x router, shown with its front panel ports (Ethernet, console, power, etc.) and ventilation grilles.
*   **Top Plate (C1110-TOP-PLATE=):** The cover plate that is being attached to the top of the chassis. The diagram shows it being secured with screws to the chassis' mounting points.
*   **Mounting Brackets:** The metal brackets on the left and right sides of the chassis are designed to be secured to a desktop surface or rack. The diagram specifically highlights the right-side bracket, indicating that it should be secured after the top plate is attached.
*   **Screws:** Dotted lines indicate the screw locations for attaching the top plate and brackets, providing a clear visual guide for the installation.

**Significance:**
This diagram is a critical part of the router's installation manual. It provides a clear, step-by-step visual guide to ensure the router is properly assembled and secured before powering on. Correctly attaching the top plate and brackets is essential for:
*   **Physical Stability:** Preventing the router from tipping over or becoming loose on a desktop.
*   **Proper Ventilation:** Ensuring airflow is not obstructed, which is vital for the router's cooling and longevity.
*   **Safety:** Securing the device prevents accidental damage or injury.

The diagram effectively communicates the necessary actions for this specific installation step, making it an essential reference for technicians and users following the procedure.

<--- End description image 62 --->



Step 2 Similarly, secure the brackets on the right-side of the chassis for mounting the router.


#### Attach the C111x Top Plate (C1110-TOP-PLATE=) on Desktop


This procedure describes how to attach the top plate on the router chassis:

• Step 1 Use Phillips 2 screwdriver to remove two 6-32 screws on the sides of the unit.
• Step 2 Orient the top plate with the Bezel Side arrow pointing outwards.


Example:




<--- Start caption image 63 --->

Figure 35: Removing side screws and orienting the top plate on C111x platforms

<--- End caption image 63 --->



<--- Start description image 63 --->

This technical diagram illustrates the correct orientation and installation of the top plate onto a router chassis, serving as a visual guide for the assembly procedure. The image is a schematic representation, not a photograph, designed to clearly communicate the physical relationship between components.

**Key Components and Their Purpose:**

*   **Component ① (Top Plate):** This is the primary part being installed. The diagram shows its position on top of the router chassis, with an arrow indicating its placement.
*   **Component ② (Bezel Side View):** This is an inset, magnified view that highlights the specific side of the top plate. The arrow points to the "Bezel Side," which is the side that should be oriented outward when the plate is installed. This is a critical detail to ensure the router's front panel is correctly aligned with the chassis.
*   **Component ③ (6-32 Screws):** These are the fasteners used to secure the top plate. The diagram shows their location on the sides of the chassis, indicating where they must be removed before installation (as per Step 1 of the procedure) and where they will be reinserted to secure the plate (Step 4).

**Significance and Context:**

This diagram is an essential part of the assembly instructions. It visually reinforces the textual steps provided in the context, particularly Step 2, which requires orienting the top plate with the Bezel Side pointing outwards. The diagram clarifies that the "Bezel Side" is the side with the vented, textured surface, which is the front-facing side of the router. This ensures that when the top plate is attached, the router's front panel is correctly positioned for user access and ventilation. The diagram also helps the technician identify the correct screw locations (③) for removal and reinstallation, preventing misalignment or damage during the installation process.

<--- End description image 63 --->



|  |  |
|------|------|
| 1 | Top plate |
| 2 | Bezel side view pointing outwards |
| 3 | 6-32 screws (2x) |


<--- Start description table 39 --->

This table illustrates the step-by-step procedure for assembling or disassembling a unit’s top plate, detailing the required tools, screw specifications, and torque settings to ensure proper alignment and secure fastening.

<--- End description table 39 --->





• Step 3 Lower the top plate and align side holes.
• Step 4 Use Phillips 2 screwdriver to secure the screws, torque to 6-8 in-lbs.


Example:


Figure 36: Aligning the side holes and securing the top plate with provided screws



<--- Start description image 64 --->

This technical diagram, labeled as "Figure 36" in the surrounding context, illustrates the final assembly stage of a device, specifically showing the top plate fully secured to the main unit. The image is a schematic line drawing of a rectangular electronic device, likely a network or communication appliance, viewed from an angled perspective to show its front and top surfaces.

**Key Components and Purpose:**

*   **Device Body (1):** The main chassis of the unit, which contains the internal electronics. The front panel (labeled "1") is detailed with various ports and connectors, including:
    *   **Ethernet Ports:** Standard RJ45 ports for network connectivity.
    *   **Serial/Console Port:** A DB9-style port for out-of-band management.
    *   **Power Input:** A power connector.
    *   **Status Indicators:** Small lights for power and activity.
    *   **Ventilation:** Perforated sections on the sides and top for airflow.
*   **Top Plate:** The flat, rectangular cover that is shown fully attached to the top of the chassis. This plate is the component being secured in the final step of the assembly process.
*   **Annotation (1):** The number "1" points to the main chassis, indicating it is the subject of the diagram. The diagram is likely part of a larger assembly manual, as indicated by the context mentioning "Step 5: The following figure displays the top plate fully secured to the unit."

**Significance:**

This diagram serves as a visual confirmation for technicians or users that the assembly process has been completed successfully. It shows the end result of the steps described in the preceding text: lowering the top plate and securing it with screws (Step 3 and 4). The image provides a clear, unambiguous reference point for ensuring the device is properly assembled before proceeding to testing or deployment. The part number "467962" in the corner likely identifies the specific model or component.

<--- End description image 64 --->



|  |  |
|------|------|
| 1 | Secure the side screws |


<--- Start description table 40 --->

Figure 36: Securing the top plate with provided screws after aligning the side holes — Step 5 of the Cisco 1000 Series Integrated Services Router hardware installation.

<--- End description table 40 --->



• Step 5 The following figure displays the top plate fully secured to the unit.


Example:


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
    *   Network interface ports (Ethernet, likely).
    *   Serial console port.
    *   Management/monitoring ports (e.g., USB, VGA, or other).
    *   Ventilation grilles for cooling.
*   **Chassis Design:** The illustration highlights the robust, industrial design of the router, with ventilation slots on the sides and top for heat dissipation.

**Significance:**

This diagram is a critical visual aid in the installation manual. It confirms the successful completion of the assembly steps described in the text, providing a clear reference for technicians to verify that the router is correctly configured for rack mounting. The image ensures that all components—the chassis, top plate, and mounting brackets—are properly integrated before the unit is placed into a rack environment.

<--- End description image 65 --->



#### Attach the C111x Top Plate (C1110-TOP-PLATE=) for Rack Mount


This procedure describes how to rack mount top plate on the router chassis:

• Step 1 Follow the Attach the C111x Top Plate (C1110-TOP-PLATE=) on Desktop to attach C111x Top Plate for Desktop.
• Step 2 Assemble the C111x unit with top plate to rack mount brackets according to the Rack Mount procedure.
• Step 3 The following figure shows a complete assembled C111x unit with top plate and rack mount brackets.


Example:




<--- Start caption image 66 --->

Figure 38: Fully assembled C111x unit with top plate on rack mount brackets

<--- End caption image 66 --->



<--- Start description image 66 --->

This technical illustration depicts a fully assembled Cisco 1000 Series Integrated Services Router (C111x model), showcasing the completed rack-mount configuration as described in the hardware installation guide. The image serves as a visual reference for Step 3 of the procedure, illustrating the final state after attaching the C111x top plate (C1110-TOP-PLATE=) and integrating it with the rack-mount brackets.

**Key Components and Purpose:**

*   **Rack-Mount Brackets:** The metal rails on the left and right sides of the chassis are the rack-mount brackets. These are designed to slide into standard 19-inch equipment racks, allowing the router to be securely mounted and aligned with other equipment.
*   **Top Plate:** The large, flat panel on top of the chassis is the C111x Top Plate. It provides a finished surface, protects internal components, and often serves as a mounting point for additional accessories or cables.
*   **Front Panel Interface:** The front of the unit features various ports and connectors, including what appear to be console ports, power inputs, and network interfaces, which are essential for initial setup, power, and connectivity.
*   **Ventilation Grilles:** The perforated sections on the front and sides indicate the router's cooling system, designed to dissipate heat generated by internal electronics during operation.

**Significance:**

This diagram is a critical visual aid in the installation process. It confirms the correct assembly of the router for rack mounting, ensuring that all components are properly attached and aligned. It helps technicians verify their work before powering on the device, preventing potential damage or misalignment that could occur if the unit is not securely mounted. The image provides a clear, unambiguous reference point for the end goal of the installation procedure.

<--- End description image 66 --->



[45]----------------------


#### Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) on Desktop


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


Example:


Figure 39: Removing 4 screws from C1121/C1161 unit



<--- Start description image 67 --->

This technical diagram, labeled "Figure 39" from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide, illustrates the bottom view of a router chassis, specifically highlighting the location of the four 6-32 screws that must be removed as part of the installation procedure.

**Caption:**

*Figure 39: Bottom view of the Cisco 1000 Series router chassis, showing the four 6-32 screws (indicated by arrows) located at the corners of the unit that must be removed using a Phillips #2 screwdriver, as specified in Step 2 of the hardware installation guide for applicable models (C1121, C1161 series). The diagram provides a clear visual reference for this disassembly step, which is necessary before proceeding with further installation or maintenance tasks.*

<--- End description image 67 --->



[46]----------------------


• Step 3 Orient the top plate and slide it on to the unit.


Example:


Figure 40: Installing top plate on to C1121/C1161



<--- Start description image 68 --->

This technical diagram, labeled as Figure 40 in the Cisco 1000 Series Integrated Services Router Hardware Installation Guide, illustrates Step 3 of the installation process: orienting and sliding the top plate onto the router chassis (models C1121/C1161).

**Description and Significance:**
The image is a line drawing showing the router chassis from a three-quarter perspective, highlighting the top plate being slid into place. A large black arrow points to the front edge of the chassis, indicating the direction of movement for the top plate. The diagram clearly shows the mounting holes on the top plate aligning with the corresponding holes on the chassis, which is the subject of the next step (Step 4). The front panel of the router is visible, showing ports and controls, while the rear and sides feature ventilation grilles. This visual guide is critical for technicians to ensure correct physical installation, preventing damage and ensuring proper airflow and component alignment.

<--- End description image 68 --->



• Step 4 Aligning the securing holes of top plate to C1121/C1161.


Example:

[47]----------------------




<--- Start description image 69 --->

This technical diagram, labeled "Figure 41: Aligning the securing holes of top plate to C1121/C1161," is a step-by-step visual guide from an installation manual. It illustrates the precise alignment required to attach the top plate (part number C1120-TOP-PLATE=) to the C1121 or C1161 router chassis.

**Purpose and Components:**
The diagram's purpose is to ensure the top plate is correctly positioned before fastening. It shows an isometric view of the router's underside, highlighting the mounting points. Key components depicted include:
*   **The Router Chassis:** The main body of the device, showing its ports, ventilation grilles, and mounting holes.
*   **The Top Plate:** The component being installed, shown as a flat panel that covers the top of the chassis.
*   **Securing Holes:** The diagram uses arrows and a numbered callout (1) to point to the specific holes on the router's chassis that must be aligned with the corresponding holes on the top plate. This alignment is critical to ensure the screws will fasten correctly and securely.

**Significance:**
This step is crucial for the proper assembly of the router. Misalignment could result in the top plate not seating correctly, leading to potential damage to the device or failure to secure it properly. The diagram provides a clear, unambiguous visual reference to prevent errors during installation. The accompanying text in the context, "Step 5 Use Phillips 2 screwdriver to secure screws to 6-8 in-lbs," indicates that this alignment step directly precedes the physical fastening of the plate.

<--- End description image 69 --->



|  |  |
|------|------|
| 1 | Align securing holes |


<--- Start description table 41 --->

This table provides step-by-step instructions for installing and connecting the Cisco 1000 Series Integrated Services Router, specifically detailing how to attach the top plate (C1120-TOP-PLATE=) to a desktop using a Phillips #2 screwdriver with a torque of 6–8 in-lbs.

<--- End description table 41 --->



• Step 5 Use Phillips 2 screwdriver to secure screws to 6-8 in-lbs.


Example:

[48]----------------------




<--- Start description image 70 --->

This technical diagram, labeled "Figure 42: Securing top plate of C1121/C1161 with screws," illustrates a critical step in the assembly of a network device, specifically the C1121 or C1161 model. It serves as a visual guide for technicians or users installing the top plate (part number C1120-TOP-PLATE=) onto the device's chassis.

**Diagram Components and Purpose:**
*   **Main Subject:** The diagram shows an isometric view of the C1121/C1161 device, highlighting its front panel (with ports and controls) and the top surface where the plate is being attached.
*   **Key Element:** The top plate is shown being secured by screws. Three arrows originate from a single point labeled "1" at the top of the diagram and point to three specific screw locations on the top plate's corners. This indicates that the top plate is fastened using screws at these three points.
*   **Annotation:** The label "Securing the screws" at the bottom clarifies the action being depicted. The number "1" in the diagram corresponds to this label, indicating the specific step or component being referenced.
*   **Purpose:** The diagram's purpose is to provide a clear, unambiguous visual instruction for the user to correctly position and tighten the screws to secure the top plate, ensuring the device is fully assembled and protected.

**Significance:**
This step is part of the "Install and Connect the Router" procedure. Properly securing the top plate is essential for the physical integrity of the device, protecting internal components, and ensuring the device is ready for deployment. The diagram is a standard part of the installation manual, helping to prevent errors during assembly.

<--- End description image 70 --->



|  |  |
|------|------|
| 1 | Securing the screws |


<--- Start description table 42 --->

This table illustrates the final step in assembling the Cisco 1000 Series Integrated Services Router, specifically showing the fully assembled C1121/C1161 model with the top plate securely attached, as part of the hardware installation process.

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
*   **Ventilation Grilles:** Perforated sections on the top and sides indicate the chassis is designed for active airflow to manage heat dissipation.
*   **Mounting Points:** The drawing clearly shows the locations for rack-mount brackets, which are critical for securing the unit in a standard 19-inch rack.
*   **Control Knobs:** Two rotary knobs are visible, likely for power or configuration controls.

**Significance:**
This diagram is a crucial part of the installation guide. It visually confirms the physical form factor of the router and highlights the rear panel where the top plate (C1120-TOP-PLATE=) will be attached and where the rack-mount brackets will be secured. The text specifies that the top plate must be attached before the unit is mounted in a rack, and this image provides the necessary visual context for that step. The dimensions provided (10.8in W x 7.85in D) are also relevant for ensuring the unit fits within standard rack space.

<--- End description image 71 --->



#### Attach the C1121/C1161 Top Plate (C1120-TOP-PLATE=) for Rack Mount


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


Step 4 Use Phillips 2 screwdriver to secure the screws to 6-8 in-lbs.


Example:


Figure 44: Aligning and securing C1121/C1161 with top plate to rack mount brackets



<--- Start description image 72 --->

This technical diagram, labeled as Figure 44, illustrates the precise assembly step for securing the top plate to the C1121/C1161 chassis using rack mount brackets. It visually demonstrates how the top plate is aligned and fastened with screws (indicated by dashed lines and screw heads) to the upper mounting rails of the unit. The diagram serves as a critical visual guide for technicians, showing the correct orientation and attachment points to ensure the top plate is properly secured to the chassis before proceeding to the final assembly stage (Step 5). The purpose is to ensure mechanical stability and correct mounting for rack installation, as referenced in the accompanying text which specifies using a Phillips #2 screwdriver and tightening to 6-8 in-lbs torque.

<--- End description image 72 --->



Step 5 Fully assembled C1121/C1161 secured with top plate and rack mount brackets.


Example:


Figure 45: Fully assembled C1121/C1161 with top plate and rack mount brackets



<--- Start description image 73 --->

**Caption:**

This technical diagram, labeled as Figure 45 in the Cisco 1000 Series Integrated Services Router Hardware Installation Guide, illustrates the fully assembled C1121/C1161 router chassis secured with its top plate and rack-mounting brackets. The image provides a clear, exploded-view perspective showing how the chassis is mounted within a standard 19-inch rack environment. Key components include:

- **Router Chassis:** The central unit, featuring a front panel with ports, control knobs, and ventilation grilles.
- **Top Plate:** A cover plate mounted on top of the chassis to provide structural integrity and protection.
- **Rack Mounting Brackets:** Two side-mounted brackets, one on each side of the chassis, designed to slide into a rack’s mounting rails. These brackets are secured to the chassis via screws and are essential for stable, vertical installation in a data center or network room.

This diagram serves as a visual guide for technicians during the hardware installation phase, specifically for Step 5 of the procedure: “Attach the Rack Mounting Brackets for C112x.” It ensures proper alignment and secure mounting, which is critical for airflow, physical stability, and ease of cable management in a rack environment. The clean, line-art style emphasizes component relationships without distraction, making it ideal for technical documentation.

<--- End description image 73 --->



#### Attach the Rack Mounting Brackets for C112x


This procedure describes how to attach the brackets on the router chassis:

[51]----------------------


• Step 1 Remove the 6 screws from the bottom of the chassis.
• Step 2 Place the platform into the bottom tray.
• Step 3 Secure the original screws from the bottom side of the tray.


Example:


Figure 46: Bracket Installation for C1121-4Px, C1126-8PLTEP and C1128-8PLTEP



<--- Start description image 74 --->

**Caption:**

This technical diagram, labeled “Figure 46,” illustrates the correct installation of a mounting bracket for specific router models (C1121-4Px, C1126-8PLTEP, and C1128-8PLTEP). It visually corresponds to Step 2 and Step 3 of the installation procedure, showing how to place the mounting platform into the bottom tray and secure it with screws.

**Key Components and Purpose:**
- **Mounting Platform (Top):** A perforated metal bracket designed to hold the router securely within a rack. It features multiple screw holes for adjustable mounting and cutouts for ventilation and cable management.
- **Router Chassis (Bottom):** The main unit of the router, shown with its rear I/O panel (including ports, knobs, and ventilation grilles) visible.
- **Screws and Mounting Points:** Dotted lines indicate the precise locations where screws should be inserted to fasten the platform to the chassis, ensuring a stable and secure installation.
- **Rack Mounting Compatibility:** The bracket’s design allows for standard 19-inch rack mounting, facilitating easy integration into network infrastructure.

**Significance:**
This diagram is critical for technicians to ensure proper physical installation of the router before powering it on. It directly supports the safety warning context provided in the surrounding text, emphasizing that correct mounting is a prerequisite for safe operation. The diagram’s clarity helps prevent misalignment or improper fastening, which could lead to hardware damage or operational failure.

<--- End description image 74 --->



#### Mount the Router


Before mounting the router on to the rack, refer to the following safety warning statements:



Warning

To prevent airflow restriction, allow clearance around the ventilation openings to be at least: 1.75 in. (4.4 cm). Statement 1076.

[52]----------------------




Warning


• To prevent bodily injury when mounting or servicing this unit in a rack, you must take special precautions to ensure that the system remains stable. The following guidelines are provided to ensure your safety:
• This unit should be mounted at the bottom of the rack if it is the only unit in the rack.
• When mounting this unit in a partially filled rack, load the rack from the bottom to the top with the heaviest component at the bottom of the rack.
• If the rack is provided with stabilizing devices, install the stabilizers before mounting or servicing the unit in the rack. Statement 1006.


Procedure


| Command or Action | Purpose |
|------|------|
| Step 1
To install the router, use the screws provided with the accessory kit to secure the router when you mount it on the rack. |  |


<--- Start description table 43 --->

This table outlines safety guidelines and mounting procedures for securing a router in a rack or under a desk, emphasizing stability to prevent injury during installation or servicing. It specifies rack mounting best practices—such as positioning the unit at the bottom of a rack and loading heavier components first—and notes that stabilizing devices should be installed before mounting. Additionally, it details the optional bracket kit required for under-desk mounting, including the necessary hardware and sourcing instructions.

<--- End description table 43 --->



#### Mount the Router under a Desk or a Shelf


Installing the router under a desk requires an optional bracket kit that is not included with the router. The kit contains the rack-mount brackets and screws to secure the brackets to the router and the underside of the desk. You can order these kits from your Cisco representative. This procedure describes how to mount a router under a desk or a shelf .

• Step 1 Attach a bracket to one side of the router using the flat-head screws. Follow the same steps to attach the second bracket to the opposite side.




<--- Start caption image 77 --->

Figure 47: Attaching Brackets to the Router

<--- End caption image 77 --->



<--- Start description image 77 --->

This technical diagram illustrates the hardware installation procedure for mounting a Cisco 1000 Series Integrated Services Router under a desk or shelf. It visually details the components and steps required to secure the router using an optional rack-mount bracket kit.

**Key Components and Purpose:**
*   **Router:** The central device, shown with its front panel featuring ports and the "Cisco" logo.
*   **Mounting Brackets:** Two L-shaped metal brackets are depicted, one on each side of the router. These are designed to be attached to the underside of a desk or shelf.
*   **Screws:** Dotted lines indicate the locations where flat-head screws are used to fasten the brackets to the router's chassis and then to the mounting surface.

**Significance and Context:**
This diagram is a critical part of the router's Hardware Installation Guide. It provides a clear, visual guide for technicians to properly install the router in a space-saving, under-desk configuration. The accompanying text explains that the bracket kit is sold separately and must be ordered from a Cisco representative. The diagram's purpose is to ensure the router is securely mounted, which is essential for proper airflow, cable management, and physical stability in a network environment.

<--- End description image 77 --->



[53]----------------------




<--- Start description image 78 --->

This technical diagram illustrates Step 2 of the hardware installation guide for the Cisco 1000 Series Integrated Services Router, specifically showing the router with its mounting brackets already attached, ready for wall or shelf mounting.

**Key Components and Purpose:**

*   **Figure 48 (Top Left):** Displays the type of fasteners required for installation: Flat-head Machine Screws. The diagram shows both the top view (with a cross-shaped indentation) and side view of the screws, indicating their standard machine screw profile.
*   **Figure 49 (Main Image):** Shows the router unit with the mounting brackets securely fastened to its top surface. The brackets are designed to be attached to a surface (like a desk or shelf) using the screws from Figure 48. The diagram clearly shows the mounting holes on the brackets aligning with the screw holes on the router's chassis.
*   **Router Details:** The diagram depicts the front panel of the router, showing its ports (Ethernet, USB, console, etc.) and the Cisco logo, confirming the device model.

**Significance and Context:**

This image is part of a step-by-step guide for installing the router. The instruction preceding this image (Step 2) directs the user to "drill a 2 mm hole under the desk and insert the wooden screws provided" to mount the router. This diagram visually confirms the state of the router *after* the brackets are attached, showing the final configuration before the screws are driven into the mounting surface. It serves as a visual reference to ensure the user has correctly attached the brackets before proceeding to the next step of securing the router with screws.

<--- End description image 78 --->



Step 2 After the brackets are attached, drill a 2 mm hole under the desk and insert the wooden screws provided. Mount the router under the desk or shelf using the pan-head wood screws).




<--- Start caption image 79 --->

Figure 50: Mounting the Router under a Desk or Shelf

<--- End caption image 79 --->



<--- Start description image 79 --->

This technical diagram illustrates Step 2 of the hardware installation guide for the Cisco 1000 Series Integrated Services Router, showing how to mount the device securely under a desk or shelf.

**Key Components and Purpose:**
*   **Router:** The Cisco 1000 Series router is depicted with its front panel visible, showing ports (RJ-45 Ethernet ports labeled R1-R4, and a USB port), status LEDs, and the Cisco logo.
*   **Mounting Brackets:** Two vertical mounting brackets are shown attached to the underside of the router chassis.
*   **Desk/Shelf:** A horizontal surface (representing a desk or shelf) is positioned above the router.
*   **Mounting Hardware:** The diagram implies the use of pan-head wood screws to fasten the router to the brackets, which are then secured to the underside of the desk or shelf.

**Significance:**
This step is crucial for providing a stable, organized, and space-saving installation. Mounting the router under a desk or shelf helps to:
*   Keep the device out of the way and off the floor.
*   Improve airflow around the router's cooling vents (visible on the right side).
*   Reduce cable clutter by routing cables neatly under the desk.
*   Protect the device from accidental bumps or damage.

The diagram serves as a clear, visual guide for technicians or users to correctly install the router, ensuring it is firmly and safely secured to the mounting surface.

<--- End description image 79 --->



[54]----------------------




<--- Start caption image 83 --->

Figure 51: Pan-head Wood Screws

<--- End caption image 83 --->









912290

### Mount Router using DIN Rail Brackets


The router is shipped with DIN Rail brackets that are to be secured on the bottom side of the chassis. Your chassis installation must allow unrestricted airflow for chassis cooling.

To attach the DIN Rail brackets to the router chassis, use the pan head machine screws and the plastic spacers provided for each bracket.

#### Attach Din-Rail Brackets on C112x


This procedure describes how to attach the brackets on the router chassis:

• Step 1 Remove the 3 bottom screws from the chassis.
• Step 2 Place the din-rail tray assy on the bottom side of the chassis.
• Step 3 Secure the original screw from bottom side of tray, leverage the existing chassis screws to secure the din rail mounting bracket from the bottom of the chassis.
• Step 4 Take the other two screws to secure the din-rail trail assy.


Example:


[55]----------------------




<--- Start caption image 84 --->

Figure 52: Attaching Din Rail Brackets for C1121-4Px, C1126-8PLTEP and C1128-8PLTEP

<--- End caption image 84 --->



<--- Start description image 84 --->

This technical diagram illustrates the mounting options for a Cisco 1000 Series Integrated Services Router, specifically detailing the hardware components and screw points required for wall mounting. The image serves as a visual guide for technicians, showing the router chassis from an angled rear perspective with callouts pointing to specific mounting hardware.

**Key Components and Purpose:**

*   **Mounting Brackets:** The diagram highlights two primary mounting methods mentioned in the context:
    1.  **Key-hole slots:** Located on the top and side of the chassis, these slots are designed for mounting the router using standard wall anchors or brackets that fit into the keyhole-shaped holes.
    2.  **DIN Rail Brackets:** These are the metal brackets visible on the rear of the chassis, designed to be attached to a DIN rail, which is commonly used in electrical panels and server racks for mounting equipment.

*   **Screw Points:** Numerous screw holes are indicated, showing where screws must be inserted to secure the mounting brackets to the router chassis. The diagram clearly shows the specific locations for attaching the brackets to the chassis.

*   **Router Interface:** The rear panel of the router is also visible, showing various ports and connectors (such as Ethernet ports, console ports, and power inputs), providing context for the device's functionality.

**Significance:**

This diagram is a critical part of the installation manual for the Cisco 1000 Series router. It provides precise, visual instructions to ensure the router is mounted correctly and securely, which is essential for proper ventilation, stability, and safety. The diagram directly corresponds to the text's mention of two mounting methods, helping users identify the correct hardware and attachment points for their specific router model.

<--- End description image 84 --->



### Wall Mount the Router


Depending on the models of the Cisco 1000 Series Integrated Services Router, the tasks for mounting the router chassis on the wall may vary.

There are two ways to mount a router on the wall, using Key-hole slots and DIN Rail Brackets.



Warning

Read the wall-mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation to people and damage to the system. Statement 378.

目



Note

The recommended clearance when a router is horizontally mounted is 1.5 inches on both sides for clearance and 1.75 inches on top. I/O side clearance is needed as it is required to access the cable connections. Clearance is not required on the backside (opposite side from I/O face) unless mounting on a DIN Rail. Clearance is required to attach and mount the DIN rail bracket.

[56]----------------------


#### Wall Mount Using Key-hole Slots


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
*   **Router:** The image displays the top surface of a Cisco 1000 Series router, identifiable by the "CISCO" logo and "1000 Series" text.
*   **Key-hole Slots (1):** The diagram highlights the key-hole slots, which are the elongated, oval-shaped mounting holes located on the router's top panel. These slots are designed to accommodate a single screw that passes through the slot and into a wall bracket, allowing for adjustable mounting height.
*   **Annotation:** A numbered callout (1) points to one of these key-hole slots, and a legend at the bottom explicitly labels this feature as "Key-hole slots."

**Significance:**
This diagram is a critical part of the installation process. It provides a clear, visual guide for technicians to correctly position the router on a wall mount, ensuring it is securely fastened and properly aligned. The use of key-hole slots allows for flexibility in mounting height, which is essential for optimal cable management and accessibility. The image is part of a larger, step-by-step guide, as indicated by the surrounding text "[57]---------------------- Install and Connect the Router Wall Mount Using Key-hole Slots |  |  |" and the table structure, which suggests this is step 57 in a sequential installation manual.

<--- End description image 91 --->



|  |  |
|------|------|
| 1 | Key-hole slots |


<--- Start description table 44 --->

This table outlines the hardware installation steps for mounting the Cisco 1000 Series Integrated Services Router on a wall using key-hole slots, providing a clear guide for proper setup and secure attachment.

<--- End description table 44 --->



[58]----------------------




<--- Start caption image 93 --->

Figure 54: Wall Mount Orientation-C111x

<--- End caption image 93 --->



<--- Start description image 93 --->

This technical diagram illustrates step [58] of the router installation process: installing and connecting the router wall mount using key-hole slots. The image shows a side view of the wall-mounting plate, with a label (1) pointing to a specific key-hole slot — a type of mounting hole designed with a slot rather than a single point, allowing for vertical adjustment of the mounted device. The plate features multiple mounting holes, including several key-hole slots, enabling the router to be securely fastened at various heights on the wall. This adjustability is crucial for optimal placement, ensuring the router’s antennas are positioned for the best possible signal coverage. The diagram serves as a visual guide for users to correctly align and fasten the router to the wall mount, ensuring a stable and properly configured installation.

<--- End description image 93 --->





<--- Start description image 92 --->

This technical illustration shows the Cisco 1000 Series Integrated Services Router, highlighting its physical form factor and key mounting features. The image serves as a visual reference for the hardware installation guide, specifically for the step involving the use of key-hole slots to mount the router to a wall.

**Key Components and Features Illustrated:**

*   **Router Body:** The image displays the router's rectangular chassis, showing its front and side profiles.
*   **Ventilation Grille:** A large, perforated grille is visible on the front face, indicating the router's need for airflow to maintain optimal operating temperature.
*   **Cisco Branding:** The "Cisco" logo is clearly marked on the front panel.
*   **Interface Ports:** The side of the router is detailed with various ports and connectors, including what appear to be Ethernet ports, console ports, and other service interfaces, essential for network connectivity and management.
*   **Mounting Points:** Although not explicitly labeled, the diagram implies the presence of key-hole slots on the back or sides (as referenced in the guide's title), which are standard for wall-mounting hardware using a mounting bracket.

**Purpose and Significance:**

This diagram is a crucial part of the installation guide. It provides a clear, uncluttered view of the router's physical design, helping technicians understand the device's dimensions, port layout, and mounting points before beginning the installation. It ensures that the correct mounting hardware is used and that the router is securely and correctly affixed to the wall, which is vital for both physical safety and proper ventilation. The image is a foundational step in the hardware installation process, ensuring the device is properly positioned for optimal performance and ease of access.

<--- End description image 92 --->



1

Key-hole slots

[59]----------------------




<--- Start caption image 94 --->

Figure 55: Wall mount using key-hole slots - C1101-4P

<--- End caption image 94 --->



<--- Start description image 94 --->

This technical diagram illustrates the rear panel of a network router, specifically highlighting the key-hole slots (labeled "1") for wall mounting. The diagram serves as a visual guide for the installation step described in the accompanying text: "Install and Connect the Router Wall Mount Using Key-hole Slots."

**Key Components and Purpose:**

*   **Key-hole Slots (1):** These are the primary focus of the diagram. They are the elongated, oval-shaped holes located at the bottom corners of the router's rear panel. Their purpose is to allow for adjustable mounting on a wall bracket. The slots are designed to accommodate a single screw that can be tightened at different points along the slot, enabling the router to be mounted at various heights.
*   **Mounting Screws:** The diagram shows the screw holes that align with the key-hole slots. The arrows point to the slots, indicating where the mounting hardware should be inserted.
*   **Router Rear Panel:** The diagram shows the full rear view of the router, including other ports and labels (like "10/100/1000 BASE-TX" and "WAN"), providing context for the location of the mounting hardware.

**Significance:**

This diagram is a crucial part of the router's installation manual. It provides a clear, unambiguous visual instruction for users to correctly mount the device on a wall, ensuring it is secure and positioned appropriately. The specific mention of the key-hole slots' spacing (3.024 in or 76.81 mm) in the text further emphasizes the importance of precise alignment during installation.

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

This technical diagram illustrates the mounting hardware layout for a router wall mount, specifically highlighting the key-hole slots for secure installation. The image shows the back panel of the mounting bracket, with two key-hole slots clearly marked by arrows and labeled as “1” — one at the top and one at the bottom. These slots are designed to accommodate a mounting screw or bolt, allowing for adjustable vertical positioning during installation. The diagram also indicates the horizontal spacing between the two key-hole slots as 7.302 inches (185.47 mm), which is critical for ensuring proper alignment and stability when mounting the router to a wall. The surrounding pattern of holes and screw locations suggests a standardized mounting system, likely compatible with common wall-mounting hardware. This visual guide is essential for users to correctly align and secure the router mount, ensuring a stable and level installation.

<--- End description image 96 --->



1

Horizontal spacing: 7.302 in (185.47 mm)

Key-hole slots

Vertical spacing: 7.430 in (188.72 mm)



<--- Start caption image 97 --->

Figure 58: Wall mount using key-hole slots - C1109-4PLTEP

<--- End caption image 97 --->



<--- Start description image 97 --->

This is a technical schematic from the Cisco 1000 Series Integrated Services Router 55 Hardware Installation Guide, illustrating the rear mounting bracket or chassis panel for hardware installation. The diagram provides precise dimensional guidance for mounting the router in a rack or enclosure.

Key features and details shown:

*   **Mounting Holes and Slots:** The diagram clearly marks the locations for mounting hardware. It includes key-hole slots along the top and bottom edges for adjustable rack mounting, as well as multiple screw holes for securing the unit.
*   **Ventilation Grilles:** Shaded areas indicate the locations of ventilation grilles, which are critical for airflow and thermal management of the internal components.
*   **Hardware Mounting Points:** The diagram shows the positions for mounting screws and brackets, ensuring the router is securely fastened to a rack.
*   **Dimensions:** The accompanying text provides exact measurements for spacing: 7.302 inches (185.47 mm) for horizontal spacing and 7.430 inches (188.72 mm) for vertical spacing. These dimensions are essential for ensuring proper alignment and clearance when installing the router in a standard 19-inch rack.

**Purpose:** This diagram serves as a critical reference for technicians during the physical installation of the Cisco 1000 Series router. It ensures correct and secure mounting, proper ventilation, and compliance with rack standards, which is vital for the router's performance, safety, and longevity.

<--- End description image 97 --->





<--- Start description image 98 --->

This technical diagram illustrates the rear panel of a Cisco 1000 Series Integrated Services Router, specifically highlighting the key-hole slots for hardware installation. The image serves as a visual reference from the official installation guide, showing the precise vertical spacing of 7.430 inches (188.72 mm) between the mounting slots. These slots are designed to accommodate standard mounting hardware, allowing the router to be securely fastened to a rack or enclosure. The diagram clearly depicts the router’s form factor, including the Cisco logo and the serial number 355640, providing essential information for technicians during the physical installation process.

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

*   **Mounting Plate:** The large rectangular plate is the primary mounting surface that attaches to the router's rear panel. It provides a stable base for the wall-mounting hardware.
*   **Key-hole Slots:** The diagram clearly indicates the location of key-hole slots (marked with a '+' symbol) on the mounting plate. These slots are designed to accommodate a single screw, allowing for adjustable positioning of the router on the wall. The text specifies that the horizontal spacing between these slots is 3.100 inches (78.74 mm) and the vertical spacing is 5.758 inches (146.25 mm). This spacing is crucial for aligning the router with standard wall studs or mounting brackets.
*   **Mounting Hardware:** Various holes and screw patterns are shown, including threaded holes for securing the mounting plate to the router and key-hole slots for the wall-mounting screws. The diagram also shows the orientation of the screws, indicating which side of the plate they are intended to be mounted on.
*   **Router Outline:** The overall shape and dimensions of the router are shown, providing context for the mounting plate's placement.

**Significance:**

This diagram is an essential part of the installation guide, ensuring that technicians can mount the router safely and correctly. The precise measurements for the key-hole slots are critical for achieving a secure and level installation, preventing potential damage to the device or the wall. The diagram's clarity and detail help prevent installation errors and ensure the router is properly aligned for optimal performance and ventilation.

<--- End description image 99 --->



[63]----------------------


#### Wall Mount using DIN Rail Brackets


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
*   **Router Chassis (1):** The main body of the router, shown with pre-drilled mounting holes on its top surface.
*   **DIN Rail Brackets (2):** Two metal brackets designed to be attached to the router chassis. These brackets are used to secure the router to a standard DIN rail, a common mounting system in industrial and telecommunications environments.
*   **Screws (1):** The fasteners used to attach the DIN Rail brackets to the router chassis. The diagram indicates that these are PHMS screws, which are provided with the router.

**Installation Instructions:**
The diagram visually guides the user to position the DIN Rail brackets onto the designated mounting points on the router's chassis and then secure them using the provided screws and plastic spacers (not explicitly shown but implied by the context). This mounting method allows for a secure, standardized, and space-efficient installation in rack or panel environments.

**Significance:**
This is a critical step in the router's deployment, ensuring it is properly secured for long-term, reliable operation in a network infrastructure. The use of DIN rail mounting is standard in data centers and industrial settings, facilitating easy installation, maintenance, and space management. The diagram is part of a larger hardware installation guide, ensuring technicians follow the correct procedure for the specific C111x model.

<--- End description image 101 --->



|  |  |
|------|------|
| 1 | Screws |
| 2 | DIN Rail Brackets |


<--- Start description table 45 --->

This table outlines the specific hardware requirements for mounting the Cisco 1000 Series Integrated Services Router 57 using DIN Rail brackets, noting that this mounting method is exclusive to the C111x model. It details the necessary components—PHMS screws and plastic spacers—for securing the brackets to the router chassis.

<--- End description table 45 --->



[64]----------------------




<--- Start caption image 104 --->

Figure 61: Orientation of DIN Rail Brackets

<--- End caption image 104 --->



<--- Start description image 104 --->

This technical diagram illustrates the rear panel of a network router or telecommunications device, specifically detailing the mounting hardware for installation on a DIN rail. The caption “Install and Connect the Router Wall Mount using DIN Rail Brackets” accurately describes the purpose of the image.

Key components shown in the diagram:
- **DIN Rail Mounting Brackets**: Two identical, adjustable brackets are mounted on the upper portion of the device’s rear panel. These are designed to clamp onto a standard DIN rail, which is commonly used in industrial control panels, server racks, and telecommunications equipment cabinets.
- **Mounting Holes**: Multiple threaded holes are visible around the perimeter of the device and near the brackets, allowing for secure fastening using screws.
- **Central Cutout**: A large rectangular opening is present in the center of the panel, likely intended for cable management, ventilation, or access to internal components.
- **Device Identification**: The brand name “Shuttle” is visible on the left side, and a part number “366951” is printed on the right side, indicating the specific model or component.

Purpose: This diagram serves as a visual guide for technicians or installers to properly mount the device on a DIN rail, ensuring secure, standardized installation in professional or industrial environments. The design facilitates easy integration into existing infrastructure while allowing for cable routing and maintenance access.

<--- End description image 104 --->





<--- Start description image 102 --->

This technical illustration depicts the Cisco 1000 Series Integrated Services Router, showcasing its physical form factor and key mounting interface. The image highlights the router’s rugged, industrial design with a perforated front panel for ventilation and a side panel featuring multiple connectivity ports and interfaces. The Cisco logo is clearly visible, confirming the brand. This diagram serves as a visual reference for the hardware installation guide, specifically illustrating the router’s mounting points and physical layout to assist technicians in installing it onto DIN rail brackets for wall or rack mounting in enterprise or data center environments. The purpose is to provide a clear, accurate representation of the device for proper installation and integration into network infrastructure.

<--- End description image 102 --->





<--- Start caption image 105 --->

Figure 62: DIN Rail Brackets and Mount

<--- End caption image 105 --->



<--- Start description image 105 --->

This technical diagram illustrates the hardware installation guide for mounting the Cisco 1000 Series Integrated Services Router 58 using DIN rail brackets. It provides a clear, exploded-view schematic showing how the router chassis attaches to a standard DIN rail via mounting brackets and screws.

**Key Components and Purpose:**
- **Router Chassis:** The main unit, shown with mounting holes and a cutout for the front panel.
- **DIN Rail Brackets:** Two mounting brackets are depicted—one at the top and one at the bottom—designed to clamp onto a DIN rail (a standardized rail used in electrical and electronic equipment enclosures).
- **Mounting Hardware:** The diagram indicates the precise locations for screws and fasteners to secure the brackets to the router and to the DIN rail.
- **Mounting Orientation:** The letter “L” at the bottom right corner indicates the mounting orientation, suggesting the router should be mounted with the “L” side facing down or in a specific rotational position relative to the rail.

**Significance:**
This diagram is essential for technicians and installers to ensure proper, secure, and standardized mounting of the Cisco 1000 Series router in a rack or enclosure. Correct installation using DIN rail brackets ensures stability, proper airflow, and compliance with industry standards for network equipment mounting. The schematic’s clarity helps prevent misalignment or improper fastening, which could lead to equipment damage or operational failure.

<--- End description image 105 --->





<--- Start description image 103 --->

This is a technical illustration from the “Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 58 [65]”, depicting the physical form factor of the router chassis.

**Description and Significance:**

The image shows a side-view schematic of the Cisco 1000 Series Integrated Services Router. Key features visible include:

*   **Chassis Design:** The unit has a compact, rectangular metal chassis with a perforated front panel for ventilation, which is essential for dissipating heat generated by internal components.
*   **Interface Panel:** The left side of the chassis is detailed with various ports and connectors, indicating its role as a network device. These include Ethernet ports, serial ports, and other interfaces necessary for connecting to networks, management systems, and other hardware.
*   **Mounting Points:** The top of the chassis features mounting brackets, suggesting it is designed to be rack-mounted in a data center or network closet.
*   **Branding:** The “Cisco” logo is clearly visible on the front, identifying the manufacturer.

**Purpose in the Context:**

This diagram serves as a visual reference within the installation guide. It helps technicians and engineers to:

1.  **Identify the Device:** Recognize the specific model (Cisco 1000 Series Integrated Services Router 58 [65]) by its physical appearance.
2.  **Understand Physical Layout:** Plan for installation space, rack mounting, and cable management by showing the location of ports and mounting hardware.
3.  **Prepare for Installation:** Ensure that the correct hardware and tools are available before beginning the physical installation process.

In essence, this image is a foundational visual aid that provides a clear, unambiguous representation of the router’s physical structure to support the step-by-step installation instructions provided in the guide.

<--- End description image 103 --->



[65]----------------------


Note

Do not over-torque the screws. The recommended torque is 8 to 10 inch-lbf (0.9 to 1.1 N-m).

### Chassis Grounding




Warning


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

This technical diagram, titled "Figure 64: Chassis Ground Connection-Cisco 1101-4PLTEP," provides a step-by-step visual guide for properly grounding a Cisco 1101-4PLTEP router chassis to ensure electrical safety and equipment protection.

The diagram consists of two views of the router:
1.  **Top View:** Shows the rear panel of the router, highlighting the grounding points. Two numbered callouts point to the specific components: (1) a UNC 6-32 screw and (2) a ground lug.
2.  **Side View:** Offers a clearer perspective of the grounding connection process. It illustrates how the ground lug (2) is attached to the chassis and secured with the UNC 6-32 screw (1).

**Key Components and Purpose:**
*   **Screw (UNC 6-32):** This is a Unified National Coarse thread screw, size 6-32, used to mechanically fasten the ground lug to the router's chassis. The "UNC" designation indicates a standard coarse thread, which is common for electrical and mechanical hardware.
*   **Ground Lug:** This is a metal terminal designed to connect the grounding wire from the building's electrical system to the router's chassis. It provides a low-resistance path to earth, which is critical for:
    *   **Safety:** Preventing electric shock by safely diverting fault currents.
    *   **Equipment Protection:** Protecting sensitive electronic components from voltage surges and electrostatic discharge.
    *   **Electromagnetic Interference (EMI) Shielding:** Helping to contain electromagnetic emissions and reduce susceptibility to external interference.

The diagram is a crucial part of the installation manual, emphasizing that proper grounding is a mandatory step before powering on or operating the device. The consistent labeling and clear callouts ensure technicians can accurately identify and install the correct components for a safe and reliable setup.

<--- End description image 107 --->



|  |  |
|------|------|
| 1 | Screw (UNC 6-32) |
| 2 | Ground Lug |


<--- Start description table 46 --->

This table lists the components required for grounding the router chassis, specifying two items: a UNC 6-32 screw and a ground lug, essential for proper electrical safety and installation.

<--- End description table 46 --->



|  |  |
|------|------|
| 1 | Screw (UNC 6-32) |
| 2 | Ground Lug |


<--- Start description table 47 --->

This table outlines the components used for chassis grounding, listing item number 1 as a UNC 6-32 screw and item number 2 as a ground lug, indicating the hardware required for secure electrical grounding of the chassis assembly.

<--- End description table 47 --->







<--- Start description image 108 --->

This image is a close-up of a section from an electrical wiring diagram or installation guide, specifically highlighting the second component in a list of required parts for a grounding connection.

**Caption:**

**Component 2: Ground Lug — Essential for Secure Electrical Grounding**

This diagram snippet identifies the "Ground Lug" as the second item in a list of components needed for a proper electrical ground connection. In electrical installations, a ground lug is a terminal or connector designed to securely attach a grounding wire (often from a power cable) to a grounding point, such as a metal enclosure or electrical box. It ensures a low-resistance path to earth, which is critical for safety — protecting against electrical shock and equipment damage by safely diverting fault currents. The accompanying text "Connect Power Cable" indicates that this ground lug will be used to terminate the grounding conductor from the power cable, completing the grounding circuit. The repeated listing of "Screw (UNC 6-32)" and "Ground Lug" suggests this is part of a standardized assembly or a multi-point grounding setup, where each connection point requires a specific fastener and terminal.

<--- End description image 108 --->





<--- Start caption image 109 --->

Figure 65: Chassis Ground Connection-Cisco 1121X-8PLTEP

<--- End caption image 109 --->



<--- Start description image 109 --->

This technical diagram illustrates the rear panel of a Cisco 1000 Series Integrated Services Router, highlighting key physical components for power and grounding. The image provides a clear, labeled view of the device's backside, which features a ventilation grille, the Cisco logo, and various ports and connectors.

The diagram specifically identifies two critical elements for installation and safety:
1.  **Screw (UNC 6-32)**: This is a standard coarse-threaded machine screw used to secure the router to a mounting surface or enclosure. Its inclusion in the diagram indicates that the router is designed for secure, fixed installation.
2.  **Ground Lug**: This is a terminal designed to connect the router's grounding wire to the building's electrical ground. This is a critical safety feature that protects against electrical faults and ensures the device operates within safe electrical parameters.

The accompanying text clarifies that the router uses an external AC-to-DC power adapter. The diagram's focus on the screw and ground lug underscores the importance of proper mechanical mounting and electrical grounding during installation, which are essential for the router's safe and stable operation in a network environment. The overall purpose of this diagram is to guide technicians during the physical setup and installation of the Cisco router.

<--- End description image 109 --->



|  |  |
|------|------|
| 1 | Screw (UNC 6-32) |
| 2 | Ground Lug |


<--- Start description table 48 --->

This table illustrates the power connection specifications for the Cisco 1000 Series Integrated Services Router, detailing how its external AC-to-DC power adapter interfaces with the router’s four-point DC power connector during hardware installation.

<--- End description table 48 --->



## Connect Power Cable


Power supply of the Cisco 1000 Series Intergrated Services Routers is an external AC to DC power adapter. The external DC power connector plugs into the router's 4 points power connector.

[68]----------------------




<--- Start caption image 110 --->

Figure 66: Power Cable for C111x

<--- End caption image 110 --->



<--- Start description image 110 --->

This technical illustration, labeled "Figure 68: Power Cable for 6111X," is a key visual from the hardware installation guide for the Cisco 1000 Series Integrated Services Router. It provides a clear, annotated view of the router's rear panel, specifically highlighting the correct method for connecting the power supply.

**Caption:**

**Figure 68: Power Cable Connection for the Cisco 1000 Series Router (Model 6111X)**

This diagram illustrates the first step in powering on the Cisco 1000 Series Integrated Services Router, model 6111X. It shows a side-view of the router's rear panel, which features a variety of ports including Ethernet, console, and power connectors. A numbered arrow (1) points to the power input jack, indicating where the power cable should be plugged in. The accompanying legend identifies this component as the "Power Cable." This visual is part of a step-by-step installation guide, ensuring users correctly connect the device to a power source before proceeding with further setup. The image serves as a critical instructional aid for network administrators and technicians to avoid damage from incorrect power connections.

<--- End description image 110 --->



|  |  |
|------|------|
| 1. | Power Cable |


<--- Start description table 49 --->

This table outlines the step-by-step process for installing and connecting the power cable for the Cisco 1000 Series Integrated Services Router, serving as a hardware installation guide to assist users in properly powering up the device.

<--- End description table 49 --->



[69]----------------------




<--- Start caption image 111 --->

Figure 67: Power Cable for C1127-8PLTEP

<--- End caption image 111 --->



<--- Start description image 111 --->

This technical illustration shows the rear panel of a Cisco 1000 Series Integrated Services Router, highlighting the first step in its initial setup: connecting the power cable. The image provides a clear, labeled view of the device's power input port, with a separate diagram of the power cable (labeled "1. Power Cable") shown for clarity. This step is foundational for powering on the router before proceeding to connect to the console for initial configuration. The surrounding text context confirms this is part of a larger installation guide, emphasizing that the router's asynchronous serial console port is the primary interface for administrative access once powered on. The diagram serves as a visual aid to ensure correct physical connection, a critical first step in deploying and configuring this networking device.

<--- End description image 111 --->



|  |  |
|------|------|
| 1. | Power Cable |


<--- Start description table 50 --->

This table outlines the steps for installing and connecting the Cisco 1000 Series Integrated Services Router, specifically highlighting the use of its asynchronous serial port for administrative access via a console terminal or PC.

<--- End description table 50 --->



## Connect the Router to a Console


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

This technical illustration depicts the rear panel of a Cisco 1000 Series Integrated Services Router, showcasing its hardware interface for console access. The diagram highlights the specific port where a Micro USB to RJ-45 console adapter is connected, as referenced in the accompanying installation guide. Key components visible include:

*   **RJ-45 Console Port:** The primary connection point for the adapter, used for direct command-line access to configure and manage the router.
*   **Micro USB to RJ-45 Adapter:** The cable shown is the specific hardware tool required for this installation, converting the standard Micro USB connector (common on modern devices) to the RJ-45 standard used by the router's console port.
*   **Router Interface:** The diagram shows the router's rear panel, which includes the Cisco logo, ventilation grilles, and other ports (such as Ethernet and power), providing context for the device's physical form factor.

The purpose of this image is to visually guide technicians through the initial hardware setup, specifically the connection of the console adapter, which is essential for initial configuration and troubleshooting before the router is connected to a network.

<--- End description image 113 --->



1.

Micro USB to RJ-45 console adapter

[71]----------------------


Use the USB or RJ-45 console port on the router to access the Cisco Internet Operating System (IOS-XE) command line interface (CLI) on the router and perform configuration tasks. A terminal emulation program is required to establish communication between the router and a PC.

To configure the router through the Cisco IOS CLI, you must establish a connection between the router console port and either a PC or a terminal.

Use the following cables and adapters to establish a local or remote connection.

| Port Type | Cable | Action |
|------|------|------|
| Serial (RJ-45) | C111x,C1111X: RJ-45 Serial console cable
CAB-CON-USB (Serial USB to RJ-45 serial cable) | Connecting to the Serial Port with Microsoft Windows |
| Serial (USB) | C110x: CAB-CON-USB RJ-45 |  |


<--- Start caption table 51 --->

Table 10: Local and Remote Connections

<--- End caption table 51 --->



<--- Start description table 51 --->

This table outlines the necessary cables and adapters for establishing a physical connection between a Cisco router and a PC, enabling access to the IOS-XE CLI via the console port—whether through USB or RJ-45—requiring a terminal emulation program for configuration tasks.

<--- End description table 51 --->



### Connect to the Serial Port with Microsoft Windows


To establish a physical connectivity between the router and a PC, you need to install a Microsoft Windows USB.

Use the USB Console cable plugged into the USB serial port to establish this connection.

• Connect the end of the console cable with the RJ-45 connector to the light blue console port on the router.
• OR


Connect a USB 5-pin micro USB Type-B to the USB console port. If you are using the USB serial port for the first time on a Windows-based PC, install the USB driver.



Note


You cannot use the USB port and the EIA port concurrently. When the USB port is used it takes priority over the RJ-45 EIA port.

• Connect the end of the cable with the DB-9 connector (or USB Type-A) to the terminal or PC. If your terminal or PC has a console port that does not accommodate a DB-9 connector, you must provide an appropriate adapter for that port.
• Start a terminal emulator application to communicate with the router. Configure the software with the following parameters:
• 9600 baud
• 8 data bits
• no parity
• 1 stop bit
• no flow control


[72]----------------------


### Connect to the Console Port with Mac OS X


This procedure describes how to connect a Mac OS X system USB port to the console using the built in OS X Terminal utility.

• Step 1 Use the Finder to go to Applications > Utilities > Terminal.
• Step 2 Connect the OS X USB port to the router.
• Step 3 Enter the following commands to find the OS X USB port number


Example:


macbook:user$ cd /dev macbook:user$ ls -ltr /dev/*usb* crw-rw-rw1 root wheel 9, 66 Apr 1 16:46 tty.usbmodem1a21 DT-macbook:dev user$

Step 4


Connect to the USB port with the following command followed by the router USB port speed


Example:


macbook:user$ screen /dev/tty.usbmodem1a21 9600

To disconnect the OS X USB console from the Terminal window

Enter Ctrl-a followed by Ctrl-\

### Connect to the Console Port with Linux


This procedure shows how to connect a Linux system USB port to the console using the built in Linux Terminal utility.

• Step 1 Open the Linux Terminal window.
• Step 2 Connect the Linux USB port to the router.
• Step 3 Enter the following commands to find the Linux USB port number.


Example:


root@usb-suse# cd /dev root@usb-suse /dev# ls -ltr *ACM* crw-r--r-1 root root 188, 0 Jan 14 18:02 ttyACM0 root@usb-suse /dev#

Step 4 Connect to the USB port with the following command followed by the router USB port speed


Example:


root@usb-suse /dev# screen /dev/ttyACM0 9600

[73]----------------------


To disconnect the Linux USB console from the Terminal window: Note


Enter Ctrl-a followed by : then quit.

## Install the Silicon Labs USB Device Driver


This section contains the following topics:

### Install the Silicon Labs Windows USB Device Driver


• Step 1 Go to the Silicon Labs website (www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads), and click CP210x Universal Windows Driver .
• Step 2 Unzip the downloaded folder, and select the installer for your system configuration. The Device Driver Installation Wizard begins.
• Step 3 Click Next on the Installation Wizard, then click Finish to complete installation.
• Step 4 Open the Device Manager on your system and click the Ports (COM & LPT) dropdown.
• Step 5 Insert the USB console cable and power into your system. The Device Manager refreshes and indicates the newly-detected COMport.
• Step 6 Open a terminal emulator and click the Serial connection type. Input values for the Serial Line and Speed (or Baud Rate ).
• Step 7 Click Open .
• Step 8 The terminal emulator opens. Click Enter to view the console output response.


### Install the Silicon Labs Mac USB Device Driver


• Step 1 Go to the Silicon Labs website (www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads), and click CP210x VCP Mac OSX Driver .
• Step 2 Click the Downloads folder, then click macOS_VCP_Driver folder, and double-click the SiLabsUSBDriverDisk.dmg program.
• Step 3 Click Install CP210x VCP Driver , and then click Open. The Driver Installer begins.
• Step 4 Follow installer instructions. Click Continue , scroll all the way down, then click Continue , and click Agree .
• Step 5 Click Continue , and enter your password. Then click Install Helper , and click Close .
• Step 6 Insert the USB console cable and power into your system.
• Step 7 Open a terminal and type cd/dev , and then type ls-ltr . Serial port tty.SLAB_USBtoUART appears.
• Step 8 Type screen /dev/tty.SLAB_USBtoUART <baudrate> to see console output. Console shows response upon first Enter key if there is no output.


[74]----------------------


## Connect WAN and LAN Interfaces


This section describes how to connect WAN and LAN interface cables. Before you connect the interface cables, refer to the following warning statements:



Warning


Never install telephone jacks in wet locations unless the jack is specifically designed for wet locations. Statement 1036.



Warning


Never touch uninsulated telephone wires or terminals unless the telephone line has been disconnected at the network interface. Statement 1037.



Warning


For connections outside the building where the equipment is installed, the following ports must be connected through an approved network termination unit with integral circuit protection, LAN, PoE. Statement 1044.



Warning

Avoid using or servicing any equipment that has outdoor connections during an electrical storm. There may be a risk of electric shock from lightning. Statement 1088.

### Ports and Cabling


This section summarizes typical WAN and LAN connections for Cisco 1000 Series Integrated Services Router. The connections summarized here are described in detail in the Cisco Modular Access Router Cable Specifications document on cisco.com.

| Port or Connection | Port Type, Color
1 | Connection | Cable |
|------|------|------|------|
| Ethernet | RJ-45, yellow | Ethernet hub or Ethernet switch | Category 5 or higher Ethernet |
| Gigabit Ethernet SFP, optical | LC, color according to optical wavelength | 1000BASE-SX, -LX, -LH, -ZX, -CWDM | Optical fiber as specified on applicable data sheet |
| Gigabit Ethernet SFP, copper | RJ-45 | 1000BASE-T | Category 5, 5e, 6 UTP |
| xDSL (VDSL2 / ADSL2/2+) | RJ-11 | POTS or ISDN line | RJ-11 telephone cable |


<--- Start caption table 52 --->

Table 11: WAN and LAN Connections

<--- End caption table 52 --->



<--- Start description table 52 --->

This table outlines the typical WAN and LAN connection configurations for the Cisco 1000 Series Integrated Services Router, providing a quick reference for common cabling setups. For detailed specifications, users are directed to the Cisco Modular Access Router Cable Specifications document available on cisco.com. Note: Always avoid using or servicing equipment with outdoor connections during electrical storms to prevent lightning-related electric shock.

<--- End description table 52 --->



1 Cable color codes are specific to Cisco cables.

[75]----------------------


### Connection Procedures and Precautions


After you have installed the router chassis, perform these steps to connect the WAN and LAN interfaces:

• Connect each WAN and LAN to the appropriate connector on the chassis.
• Position the cables carefully so that you do not strain the connectors.
• Organize cables in bundles so that cables do not intertwine.
• Inspect the cables to make sure that the routing and bend radius is satisfactory. If necessary, reposition the cables.
• Install cable ties in accordance with site requirements.


## Configure the Router at Startup


After installing the router and connecting the cables, you can configure the router with basic configurations. For more information on how to configure the router, see the Cisco 1100 Series Software Configuration Guide.

[76]----------------------


[77]----------------------




<--- Start description image 119 --->

This image serves as a chapter header for a technical manual, specifically Chapter 4, titled “Install and Upgrade Internal Modules and Field Replaceable Units,” from the “Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 70 [77].”

The visual content—a wide, sun-drenched urban skyline viewed from a high vantage point—functions as a thematic backdrop. It evokes a sense of scale, modern infrastructure, and technological advancement, aligning with the subject matter of enterprise networking hardware. The bright, open perspective suggests clarity, accessibility, and the ease of maintenance implied by the chapter’s title: the ability to quickly and easily replace internal components without sending the entire router for repair.

The large, bold “CHAPTER 4” text anchors the image, clearly indicating its position within the document. The overall design is clean and professional, reinforcing the technical nature of the guide while using the cityscape to subtly communicate the router’s role in powering and supporting large-scale, modern digital infrastructure.

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


## Replace the Chassis Covers for C111X and C1111x


To access the internal modules on the router, you must first remove the chassis cover. See the instructions below on how to remove and later replace the chassis cover on the routers.



Warning

Only trained and qualified personnel should be allowed to install, replace or service this equipment. Statement 1030

Cisco 1000 Series Integrated Services Routers have removable covers. Do not run the routers with the cover off. Doing so can cause the router to overheat very quickly.

Use a number-2 Phillips screw driver to perform the following tasks.

[78]----------------------


### Remove the Cover




<--- Start description image 121 --->

This technical diagram illustrates the initial step in accessing the internal components of a device, specifically showing how to remove its cover. The image is a schematic representation of a rectangular electronic unit, likely a server, network appliance, or similar hardware, with a textured top surface and ventilation grilles on the sides.

The diagram provides clear, numbered instructions for the user:
- Step 1: Points to the screws on the left side of the unit.
- Step 2: Points to the screws on the right side of the unit.

The accompanying text, “To remove the cover, do these,” confirms that the purpose of the image is to guide the user through the disassembly process. The visual clearly indicates that the first action required is to remove all 14 screws — 7 on each side — securing the cover to the chassis. This is a foundational step necessary before proceeding with the installation or upgrade of internal modules and field-replaceable units, as mentioned in the surrounding context.

The diagram’s purpose is to provide a clear, unambiguous visual guide to ensure the user correctly identifies and removes the fasteners before opening the device, thereby preventing damage and ensuring safe access to internal components.

<--- End description image 121 --->



steps:


1 and 2

Remove the 14 screws from either side of the cover.



<--- Start description image 122 --->

This technical diagram illustrates Step 1 of the hardware installation guide for the Cisco 1000 Series Integrated Services Router, showing the process of removing the device’s cover to access internal components.

**Image Description:**
The image is a two-part schematic drawing of the router:
*   **Top View (Step 1):** Shows the router with its cover in place. A large black arrow points to the left side of the device, indicating the direction to begin the removal process. The Cisco logo is visible on the front panel.
*   **Bottom View (Step 2):** Depicts the router with its cover lifted off and shown in a hinged position above the main chassis. This view reveals the internal hardware, including circuit boards, connectors, and mounting points, which are accessible for module installation or replacement.

**Significance and Context:**
This diagram is a critical visual aid for technicians performing maintenance or hardware upgrades. It directly corresponds to the instructions in the guide, which state: “Remove the 14 screws from either side of the cover.” The image visually confirms the action required — lifting the cover — and provides a clear view of the internal components that will be worked on. The diagram serves to ensure the user correctly identifies the cover and understands the orientation for safe and proper access to the router’s internals.

<--- End description image 122 --->



• Step 1 Read the Safety Warnings and disconnect the power supply before you perform any module replacement.


Step 2 Confirm the router is turned off and disconnected from the power supply.

[79]----------------------


• Step 3 Disconnect all port cables connected to the router. Ensure that you do not work on the router with cables still attached to the router in the event of lightning or surges.
• Step 4 Place the chassis on a flat surface.
• Step 5 Remove the 14 cover screws on the two sides of the router cover. See figure.
• Step 6 Slide the cover from bezel side to I/O side until it stops.
• Step 7 Pull the cover vertically to disengage from the chassis.


### Replace the Cover


To replace the cover, do these steps:



Warning


The covers are an integral part of the safety design of the product. Do not operate the unit without the covers installed. Statement 1077.



<--- Start description image 124 --->

This technical diagram illustrates the hardware installation of the cover for the Cisco 1000 Series Integrated Services Router, as detailed in the Hardware Installation Guide. It serves as a visual guide for technicians to correctly reassemble the unit’s protective cover, which is a critical safety component.

**Key Components and Purpose:**

*   **Cover (①):** The top cover, shown detached and positioned above the router chassis. It features ventilation slots and mounting points. The diagram indicates that this cover must be secured with 14 screws on each side (as referenced in Statement 1077.1 and 2).
*   **Router Chassis (②):** The main body of the router, shown below the cover. It contains the internal components and has pre-drilled holes for the screws that attach the cover. The Cisco logo is visible on the front panel.
*   **Mounting Arrows:** The arrows point to the screw locations on the cover, guiding the user to the correct attachment points.

**Significance and Safety Context:**

This diagram is part of a critical safety and installation procedure. The accompanying warning, “The covers are an integral part of the safety design of the product. Do not operate the unit without the covers installed,” underscores the importance of this step. The cover protects internal components from physical damage, dust, and accidental contact, and is essential for the safe and proper operation of the router. Failure to install the cover correctly could void the warranty and create a hazardous situation. The diagram ensures that the cover is reinstalled with the correct hardware (14 screws per side) to maintain the device’s integrity and safety.

<--- End description image 124 --->



1 and 2

Replace the 14 screws on either side of the cover.

[80]----------------------




<--- Start description image 125 --->

This technical diagram illustrates Step 5 of the installation procedure for a Cisco 1000 Series Integrated Services Router, showing the correct method for securing the chassis cover.

**Caption:**
*Step 5: Secure the Chassis Cover — Align the hooks on the router's cover with the corresponding slots on the chassis base, then lower the cover firmly onto the base. This step is critical for proper enclosure assembly and must be performed after disconnecting all power and cables (Steps 1-4) to ensure safety and prevent damage during installation.*

**Diagram Components and Purpose:**
*   **Chassis Base:** The lower, main body of the router containing the circuit boards and internal components.
*   **Router Cover:** The top lid of the chassis, which is being lowered into place. The "Cisco" logo is visible on the top surface.
*   **Alignment Hooks and Slots:** The diagram clearly shows the hooks on the cover (indicated by the arrow) that must be aligned with the slots on the chassis base for a secure fit.
*   **Arrow:** A large downward-pointing arrow indicates the direction of motion for the cover, guiding the user to lower it onto the chassis.

This diagram is part of a larger, safety-critical procedure for installing and upgrading modules in a Cisco router. It visually reinforces the mechanical step following the electrical safety precautions, ensuring the chassis is properly enclosed before proceeding to install internal or external components.

<--- End description image 125 --->



• Step 1 Read the Safety Warnings and disconnect the power supply before you perform any module replacement.
• Step 2 Confirm the router is turned off and disconnected from the power supply.
• Step 3 Disconnect all port cables connected to the router. Ensure that you do not work on the router with cables still attached to the router in the event of lightning or surges.
• Step 4 Place the chassis on a flat surface.
• Step 5 Align hooks on the cover to slots on the chassis base and lower the cover onto chassis base.
• Step 6 Slide the cover from the I/O side to the bezel side
• Step 7 Install the fourteen screws on both sides of the chassis. Torque to 6-8 in-lbs.


## External Modules


This section describes how to install external modules and FRUs in the Cisco 1000 Series Integrated Services Routers. The information is contained in the following sections:



Warning

Only trained and qualified personnel should be allowed to install, replace or service this equipment. Statement 1030.

### Locate External Slots for Modules


This section describes the locations of external modules on the router motherboard.

[81]----------------------


## Install and Remove Small Form Pluggable Modules


This section describes how to install and remove Small Form Pluggable (SFP) modules in the Cisco 1000 Series Integrated Services Routers. The information is contained in the following sections:

### Install Small Form Pluggable Module


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

### Remove Small Factor Pluggable Module


To remove a small factor pluggable (SFP) module from the chassis:

• Step 1 Disconnect all cables from the SFP.


• Step 2 Disconnect the SFP latch.


Note

SFP modules use various latch designs to secure the module in the SFP port. For information on the SFP technology type and model, see the label on the side of the SFP module.

• Tip


Use a pen, screwdriver, or other small straight tool to gently release a bale-clasp handle if you cannot reach it with your fingers.

• Step 3 Grasp the SFP on both sides and remove it from the chassis.


[82]----------------------


## Install a Pluggable Interface Module




Warning

Blank faceplates and cover panels serve three important functions: they prevent exposure to hazardous voltages and currents inside the chassis; they contain electromagnetic interference (EMI) that might disrupt other equipment; and they direct the flow of cooling air through the chassis. Do not operate the system unless all cards, faceplates, front covers, and rear covers are in place. Statement 1029.



Warning

Only trained and qualified personnel should be allowed to install, replace, or service this equipment. Statement 1030.



Warning

Pluggable optical modules comply with IEC 60825-1 Ed. 3 and 21 CFR 1040.10 and 1040.11 with or without exception for conformance with IEC 60825-1 Ed. 3 as described in Laser Notice No. 56, dated May 8, 2019. Statement 1255.

### Install a Pluggable Interface Module on a C1101-4P


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
*   **3 (Ground Lug):** This is a grounding point. Connecting a ground lug ensures the device is properly grounded, which helps to protect against electrical surges and electromagnetic interference (EMI), improving signal integrity and device safety.
*   **4 (Kensington Lock Slot):** This is a security feature. It allows the device to be physically secured to a desk or rack using a Kensington security cable, preventing theft or unauthorized removal.

**Significance:**
The diagram is crucial for network engineers and technicians installing the C1101-4P router. It provides a clear, labeled view of the rear panel to ensure correct identification of ports and connectors before inserting the pluggable module. This prevents misconnections and ensures the device is properly configured for its intended function—providing secure, time-synchronized, and cellular-connected network services. The accompanying text instructs the user to insert the module and then tighten the screw to a torque of 10-12 in-lb, which is a critical step to ensure a secure mechanical connection without damaging the module or the slot.

<--- End description image 134 --->



|  |  |
|------|------|
| 1 | GPS antenna (SMA) |
| 2 | LTE antenna (SMA) |
| 3 | Ground lug |
| 4 | Kensington lock slot |


<--- Start description table 53 --->

This table identifies the key components located on the rear panel of the C1101-4P device, including the GPS and LTE SMA antennas, a ground lug for electrical safety, and a Kensington lock slot for physical security. These elements are referenced in the preceding installation instructions, which guide users through plugging in the LTE module and securing it with the specified torque.

<--- End description table 53 --->







<--- Start caption image 135 --->

Figure 71: LTE Pluggable Interface Module - C1127X-8PLTEP

<--- End caption image 135 --->



<--- Start description image 135 --->

This is a technical diagram from the Cisco 1000 Series Integrated Services Router 77 Hardware Installation Guide, illustrating the rear panel interface and key mounting/antenna connection points.

The image provides a clear, angled view of the router's back, highlighting four critical components for installation and connectivity:

*   **1. GPS Antenna (SMA):** This is the connection point for a Global Positioning System antenna, which provides precise time synchronization and location data to the router. The SMA (Screw-on Male) connector is a standard for RF (radio frequency) connections.
*   **2. LTE Antenna (SMA):** This port is for connecting an LTE (Long-Term Evolution) cellular antenna, enabling the router to establish a wireless broadband connection via a cellular network.
*   **3. Ground Lug:** This is a grounding point, typically used to connect a grounding wire to the router's chassis. This is essential for safety, protecting against electrical surges and electromagnetic interference (EMI).
*   **4. Kensington Lock Slot:** This is a security feature that allows the router to be physically secured using a standard Kensington security cable, preventing theft or unauthorized removal.

The diagram serves as a crucial reference for technicians during the physical installation and configuration of the router, ensuring correct connections for positioning, cellular connectivity, grounding, and physical security.

<--- End description image 135 --->



|  |  |
|------|------|
| 1 | GPS antenna (SMA) |
| 2 | LTE antenna (SMA) |
| 3 | Ground lug |
| 4 | Kensington lock slot |


<--- Start description table 54 --->

This table lists key hardware components and their corresponding labels for installation on the Cisco 1000 Series Integrated Services Router, including the GPS and LTE antennas, ground lug, and Kensington lock slot, as detailed in the Hardware Installation Guide.

<--- End description table 54 --->



[84]----------------------




<--- Start caption image 136 --->

Figure 72: LTE Pluggable Interface Module - P-LTEAP18-GL

<--- End caption image 136 --->



<--- Start description image 136 --->

This is a detailed schematic diagram illustrating the pinout and component layout for installing a Pluggable Interface Module (P18-GL) on a C1101-4P device, specifically for the purpose of installing and upgrading internal modules and Field Replaceable Units (FRUs).

The diagram serves as a technical reference guide for technicians, clearly labeling each physical port and indicator on the module’s interface board. Its purpose is to ensure correct and safe installation by providing a visual map of the module’s connectivity points.

**Key Components and Their Functions:**

*   **Antenna Connectors (Ports 2, 3, 4, 5, 6):** These are SMA connectors for antenna cables. The diagram labels them as:
    *   **Main 0 (Port 2) and Main 1 (Port 6):** Primary antenna connections for the main cellular signal.
    *   **Diversity 0 (Port 5) and Diversity 1 (Port 3):** Antennas for signal diversity, which helps improve reception by using multiple paths.
    *   **LTE Indicator (Port 6):** A label indicating this port is for LTE connectivity.

*   **Micro USB Port (Port 4):** A standard USB port, likely for firmware updates, diagnostics, or power.

*   **LED Indicators (Ports 7, 8, 9):** These are status LEDs for the SIM cards:
    *   **Enable LED (Port 7):** Indicates the module’s power or operational status.
    *   **SIM 0 LED (Port 8) and SIM 1 LED (Port 9):** Show the status of the two SIM card slots.

*   **M3.5 Thumb-Screw (Port 10):** A small screw used to secure the module to the device chassis.

*   **RSSI (Received Signal Strength Indicator) LEDs (Ports 11, 12, 13, 14):** These are four LEDs that visually indicate the strength of the cellular signal for each of the four antenna channels (0, 1, 2, 3). The color coding is critical for troubleshooting:
    *   **Yellow:** Indicates a poor or very poor signal (3G).
    *   **Green:** Indicates a good or best signal (4G).
    *   This allows technicians to quickly assess signal quality and diagnose connectivity issues.

**Significance:**

This diagram is essential for field service engineers and technicians performing hardware maintenance or upgrades on the C1101-4P device. It provides a clear, unambiguous guide to avoid miswiring, which could damage the device or cause connectivity failures. The inclusion of signal strength indicators (RSSI) is particularly important for ensuring optimal network performance after installation.

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
| 2 | RSSI 1
• Yellow: Bad signal, 3G
• Green: Bad signal, 4G |
| 3 | RSSI 2
• Yellow: Good signal, 3G
• Green: Good signal, 4G |
| 4 | RSSI 3
• Yellow: Best signal, 3G
• Green: Best signal, 4G |


<--- Start description table 55 --->

This table outlines the installation and upgrade procedures for internal modules and field-replaceable units, specifically detailing the steps to install a pluggable interface module on a C1101-4P device. It also includes a signal status indicator, where “Yellow: Bad signal, 3G” denotes a warning condition related to signal integrity under 3G network conditions.

<--- End description table 55 --->







<--- Start description image 137 --->

This image displays a portion of a pinout or connector diagram for a cellular module, specifically detailing the signal quality indicators (RSSI) for multiple antenna channels. The diagram is presented in a tabular format, with each row corresponding to a specific RSSI channel (RSSI 1, RSSI 2, RSSI 3) and its associated LED color coding for signal strength under 3G and 4G network conditions.

**Key Components and Purpose:**

*   **RSSI 1 (Pin 1):** Indicates the signal strength for the first antenna channel. A yellow LED signifies a "Bad signal" for 3G networks, while a green LED indicates a "Bad signal" for 4G networks.
*   **RSSI 2 (Pin 3):** Indicates the signal strength for the second antenna channel. A yellow LED signifies a "Good signal" for 3G networks, while a green LED indicates a "Good signal" for 4G networks.
*   **RSSI 3 (Pin 4):** Indicates the signal strength for the third antenna channel. A yellow LED signifies the "Best signal" for 3G networks, while a green LED indicates the "Best signal" for 4G networks.

**Significance:**

This diagram is crucial for technicians and engineers for troubleshooting and diagnosing cellular connectivity issues. By observing the color of the corresponding RSSI LEDs, one can quickly determine the quality of the signal received by each antenna channel and whether the device is operating under 3G or 4G conditions. This information is vital for optimizing antenna placement, identifying weak signal areas, and ensuring optimal network performance. The color coding provides a clear, visual reference for signal strength, making it easier to assess the module's performance in real-time.

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

This is a schematic diagram of the P-5GS6-GL module, detailing its physical layout and pinout for a multi-antenna, multi-SIM cellular device, likely a modem or router. The diagram serves as a technical reference for installation, troubleshooting, or hardware modification.

**Key Components and Their Purpose:**

*   **Antennas (1-6):** The module features five SMA connectors for external antennas, allowing for flexible signal configuration.
    *   **Antenna 1 (SMA) (Pin 2):** Primary antenna for cellular signal reception and transmission.
    *   **GPS (SMA) (Pin 3):** Dedicated antenna for Global Positioning System signal.
    *   **Antenna 3 (SMA, reception only) (Pin 4):** A receive-only antenna, likely for a secondary or backup signal path.
    *   **Antenna 0 (SMA) (Pin 5):** Another cellular antenna, possibly for a different band or for diversity reception.
    *   **Antenna 2 (SMA) (Pin 6):** A fifth antenna, potentially for a specific band or as a backup.
*   **LED Indicators (7-10):** These provide visual status feedback.
    *   **Enable LED (Pin 7):** Indicates if the module is powered on and operational.
    *   **SIM 0 LED (Pin 8):** Indicates the status of the first SIM card (e.g., active, registered, or error).
    *   **SIM 1 LED (Pin 9):** Indicates the status of the second SIM card.
    *   **GPS LED (Pin 10):** Indicates the status of the GPS signal (e.g., locked, searching, or error).
    *   **Service LED (Pin 11):** Indicates the cellular network service status (e.g., connected, searching for network, or error).
*   **Physical Mounting (Pin 12):** A thumb-screw (Pin 1) is used to secure the module to a device or enclosure.

**Significance:**

This diagram is crucial for technicians and engineers to correctly connect antennas and interpret the status of the module's cellular, GPS, and SIM card functions. The color-coded signal indicators mentioned in the context (Yellow for 3G, Green for 4G, Yellow for best 3G) are not shown on this diagram but would be used in conjunction with the LED indicators to diagnose signal quality. The module's design suggests it is intended for applications requiring robust, multi-band cellular connectivity and GPS positioning, such as in IoT devices, ruggedized communication equipment, or mobile hotspots.

<--- End description image 138 --->



|  |  |
|------|------|
| PID |  |
| antenna 1 (SMA) |  |
| GPS (SMA) |  |
| Antenna 3 (SMA, reception only) |  |
| Antenna 0 (SMA) |  |
| Antenna 2 (SMA) |  |
| Enable LED |  |
| 8 | SIM 0 LED |
| 9 | SIM 1 LED |
| 0 | GPS LED |
| 1 | M3.5 thumb-screw |
| 2 | Service LED |


<--- Start description table 56 --->

This table provides a pinout diagram for a device’s connector, labeling each pin’s function such as antenna connections, LED indicators, and SIM card status, with additional context indicating signal quality color coding (green for 4G, yellow for 3G) for reference.

<--- End description table 56 --->







<--- Start caption image 139 --->

Figure 74: P-5GS6-R16SA-GL

<--- End caption image 139 --->



<--- Start description image 139 --->

This diagram is a detailed hardware installation guide for the Cisco 1000 Series Integrated Services Router 80, specifically illustrating the rear panel layout and component labeling for the P-5GS6-R16SA-GL module.

**Purpose:**
The diagram serves as a visual reference to help technicians correctly identify and connect the various ports, antennas, and indicator LEDs on the router’s rear panel during installation or maintenance. It ensures proper physical connection and configuration of the device’s wireless and service components.

**Key Components and Their Functions:**

*   **Antennas (Ports 2-6):** The router is equipped with five SMA connectors for antenna connections, each serving a specific purpose:
    *   **Port 2 (Main antenna 1):** The primary antenna for wireless communication.
    *   **Port 3 (GPS):** Connects to a GPS antenna for precise time synchronization.
    *   **Port 4 (Antenna 3):** A dedicated reception-only antenna, likely for passive monitoring or specific signal types.
    *   **Port 5 (Antenna 0):** A general-purpose antenna.
    *   **Port 6 (Antenna 2):** Another general-purpose antenna, often used for primary or secondary wireless links.

*   **LED Indicators (Ports 7-10):** These provide visual status feedback:
    *   **Port 7 (Enable LED):** Indicates the device’s power and operational status.
    *   **Port 8 (SIM 0 LED):** Shows the status of the first SIM card (for cellular connectivity).
    *   **Port 9 (SIM 1 LED):** Shows the status of the second SIM card.
    *   **Port 0 (GPS LED):** Indicates the status of the GPS signal reception.

*   **Physical Mounting and Service Access:**
    *   **Port 11 (M3.5 thumb-screw):** A mounting screw used to secure the module to a rack or enclosure.
    *   **Port 12 (Service LED):** An indicator for service or diagnostic purposes, often used by support personnel.

**Significance:**
This diagram is critical for ensuring correct hardware setup, which directly impacts the router’s performance, connectivity, and reliability. Misconnecting antennas or LEDs can lead to service outages or inaccurate time synchronization. The clear labeling and visual layout make it an essential tool for both initial installation and troubleshooting.

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


<--- Start description table 57 --->

This table outlines the pin assignments for hardware connections on the Cisco 1000 Series Integrated Services Router, detailing which physical components or indicators are connected to specific pins, such as antennas, LEDs, and SIM card indicators, to assist with proper installation and configuration.

<--- End description table 57 --->



[87]----------------------




<--- Start caption image 140 --->

Figure 75: P-LTEA7-NA

<--- End caption image 140 --->



<--- Start description image 140 --->

This is a detailed hardware installation diagram for the Cisco 1000 Series Integrated Services Router, specifically illustrating the pinout and component layout for the pluggable interface module **P-LTEA7-NA** (as labeled on the module). The diagram serves as a visual guide for technicians to correctly install and identify the various ports and indicators on the module.

**Key Components and Their Functions:**

*   **Antenna Connectors (1-3):** The module features three SMA connectors for antenna connections:
    *   **1 (MAIN):** Main antenna port.
    *   **2 (GPS):** GPS antenna port.
    *   **3 (DIV):** Diversity antenna port.
*   **Status LEDs (5-7):** These are indicator lights for system status:
    *   **5 (EN):** Enable LED.
    *   **6 (SIM 0 LED):** Status LED for SIM card 0.
    *   **7 (SIM 1 LED):** Status LED for SIM card 1.
    *   **8 (GPS LED):** Status LED for the GPS module.
*   **M3.5 Thumb-Screw (9):** A mounting screw used to secure the module to the router chassis.
*   **RSSI Indicators (10-13):** These are signal strength indicators for the cellular radios:
    *   **10 (RSSI 0):** Signal strength for the primary radio (0). *Yellow = Very bad signal (3G), Green = Very bad signal (4G)*.
    *   **11 (RSSI 1):** Signal strength for the secondary radio (1). *Yellow = Bad signal (3G), Green = Bad signal (4G)*.
    *   **12 (LTE):** LTE indicator light.
    *   **13 (LTE):** Another LTE indicator light, likely for redundancy or a different band.

**Purpose and Significance:**

This diagram is a critical part of the hardware installation guide for the Cisco 1000 Series router. It provides a clear, labeled reference for technicians to ensure correct physical installation and to troubleshoot connectivity issues by visually identifying which LED or port corresponds to which function. The labeling of the RSSI indicators with their color-coded signal quality thresholds (Yellow for 3G, Green for 4G) is particularly important for diagnosing cellular signal strength problems. The diagram is essential for proper deployment and maintenance of the router's wireless and cellular capabilities.

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


<--- Start description table 58 --->

This table outlines the procedures for installing and upgrading internal modules and field-replaceable units, specifically focusing on the installation of a pluggable interface module on the Cisco 1000 Series Integrated Services Router’s C1101-4P hardware platform. It serves as a reference for technicians performing hardware maintenance or expansion tasks.

<--- End description table 58 --->



[88]----------------------


RSSI 2 2 1


• Yellow: Good signal, 3G
• Green: Good signal, 4G


RSSI 3 3 1


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
    *   These are critical for receiving cellular and satellite signals.
*   **LED Indicators (5-8):** 
    *   5: Enable LED (power status)
    *   6: SIM 0 LED (status of first SIM card)
    *   7: SIM 1 LED (status of second SIM card)
    *   8: GPS LED (GPS signal status)
*   **Physical Connectors (9-14):** 
    *   9: M3.5 thumb-screw (for securing the module)
    *   10: Micro USB 2.0 port (for power and data)
    *   11-14: RSSI (Received Signal Strength Indicator) LEDs, which display signal quality for both 3G and 4G networks.

**Signal Indicator System:**
The module uses a color-coded LED system to indicate signal strength and network type:
*   **Yellow:** Indicates 3G signal quality.
*   **Green:** Indicates 4G signal quality.
*   **RSSI Levels (0-4):** The four RSSI LEDs (11-14) show signal strength from worst to best:
    *   RSSI 0: Very bad signal
    *   RSSI 1: Bad signal
    *   RSSI 2: Good signal
    *   RSSI 3: Best signal

**Significance:**
This diagram is essential for technicians and users to correctly install the module, connect antennas and power, and interpret the status of network connectivity and SIM card operation. The color-coded indicators provide a quick visual reference for diagnosing signal issues, ensuring optimal performance for LTE and 3G networks. The context provided confirms this is part of a guide for inserting a Micro-SIM card into the module, making the diagram a crucial reference for setup and troubleshooting.

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


<--- Start description table 59 --->

This table illustrates signal strength indicators for LTE connectivity, where yellow denotes the best 3G signal and green indicates the best 4G signal, serving as a visual guide for users to assess network performance when inserting a Micro-SIM card into an LTE pluggable module.

<--- End description table 59 --->





This section describes how to insert a Micro-SIM card into an LTE pluggable module.

To insert the Micro-SIM cards into an LTE Pluggable module:



Note


Ensure to use the correct tool for removing the Micro-SIM door.

• Place the pluggable module on its bottom side, remove the SIM door screw, use a #1 Philips screw driver for removing the screws, and then carefully remove the Micro-SIM cover from the pluggable module.




Caution


Do not touch any part of the exposed PCB circuit area when the Micro-SIM cover is removed.

• Slot 1 and slot 0 are the Micro-SIM slots. (see figure 5, step 2).
• Install SIM 0 and SIM 1 in their respective slots. SIM 0 or SIM 1 is marked on the pluggable interface module above the Micro-SIM cover. The SIM icons show the correct orientation required to install the SIM into each respective connector (SIM connectors are a push-push type).


To install, insert the SIM card in the connector until you feel it click, then let go and the SIM is locked to the connector. To remove the SIM card, depress the SIM in the connector slot again until you feel the

[90]----------------------


same click and let it go, the SIM connector should eject part way out of the connector. The SIM card can then be grabbed and removed).

Secure the Micro-SIM cover with a screw, use a number 1 Philips screw driver to secure the screw on the Micro-SIM cover. The recommended torque is 2.8 - 3.8 inch LBF.



Note


We recommend using industrial-grade SIM cards.

• You have now successfully inserted the Micro-SIM cards into the LTE pluggable module. The marking on the Mirco-SIM door should align with Micro-SIM 0 on the pluggable module with the arrow pointing upward.




<--- Start caption image 145 --->

Figure 77: Insert the Micro-SIM Cards

<--- End caption image 145 --->



<--- Start description image 145 --->

This diagram from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide illustrates the step-by-step procedure for inserting a Micro-SIM card into the LTE pluggable module. It is a technical illustration designed to guide network administrators or technicians during hardware installation.

The process is broken down into four clear steps:

*   **STEP 1:** The image shows the pluggable module with the SIM card tray partially open, indicating the initial state before insertion.
*   **STEP 2:** The Micro-SIM card (labeled as "Micro-SIM 0") is shown being inserted into the slot. The diagram highlights two key alignment points: (1) the arrow on the SIM card tray must point upward, and (2) the marking on the tray must align with the "0" label on the module.
*   **STEP 3:** The SIM card is fully seated in the module. The diagram uses an arrow (3) to point to the correct orientation of the card within the slot, ensuring it is properly aligned with the module's contacts.
*   **STEP 4:** The SIM card tray is closed and secured, completing the installation.

The purpose of this diagram is to ensure correct and secure installation of the SIM card, which is critical for establishing LTE connectivity. The accompanying text in the context reinforces this by recommending the use of industrial-grade SIM cards and emphasizing the importance of proper alignment to avoid connection issues.

<--- End description image 145 --->



### Configuring a Pluggable Interface Module


To insert the antenna in the Pluggable Interface Module, perform the following steps:

[91]----------------------




<--- Start caption image 146 --->

Figure 78: Attaching the Antennas

<--- End caption image 146 --->



<--- Start description image 146 --->

This instructional diagram illustrates Step 1 of installing antenna modules onto a pluggable interface module, as part of a larger procedure for configuring internal components. The image shows a hand using thumb and index finger to insert and tighten antenna 1 (labeled '1') and antenna 3 (labeled '3') into their designated middle attachment slots (indicated by arrows). The diagram also labels the EN (Enable) switch (labeled '2') and the module's mounting bracket (labeled '0') for context. This step is critical for ensuring proper antenna connection and signal integrity within the device's internal architecture.

<--- End description image 146 --->



20020

• Step 1 Use your thumb and index finger to insert and tighten antenna 1 and antenna 3 in the middle antenna attachment slots, as indicated in the figure.


Note

While installing the antennas, first install antenna 1 and antenna 3 (this instruction is for the two antenna attachments present in the middle) and secure it completely. If you install antenna 2 and antenna 0 first (this refers to the first and the last antenna attachments), there will be less space to insert your thumb and index finger and therefore, you may not be able to secure antenna 1 and 3.

• Step 2 Insert antenna 2 and antenna 0 in the first and last antenna attachment slots.
• Step 3 After installing the antennas, adjust the antenna orientation by spacing out each of them equally until they are spread out. This is important because it helps in getting higher RF performance.


[92]----------------------




<--- Start description image 147 --->

This technical line drawing illustrates the antenna assembly for the P-5GS6-GL and P-5GS6-R16SA-GL wireless communication devices, as referenced in the accompanying text regarding RF band mapping for antenna ports. The diagram shows a rectangular base unit with four distinct, vertically oriented, high-gain antenna elements mounted on top. Each antenna is connected to the base via a threaded or flanged connector, and the base unit features visible mounting holes and a connector port, indicating its design for secure installation and integration into a larger system. The image serves as a schematic representation to aid in the physical installation and upgrade of internal modules and field-replaceable units, providing a clear visual reference for technicians working with these specific models.

<--- End description image 147 --->



### RF Band Mapping for Antenna Ports (For P-5GS6-GL and P-5GS6-R16SA-GL)


The following table lists the RF band mapping for antenna ports.

RF Band Mapping for Antenna Ports for P-5GS6-GL


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


<--- Start description table 60 --->

This table outlines the RF band mapping for antenna ports in the P-5GS6-GL and P-5GS6-R16SA-GL configurations, specifying which radio access technology (RAT) bands are supported and which antenna ports (transmit, receive, and GNSS) are utilized. It includes default and alternate path antenna assignments, with transmit antennas designated as ANT0 through ANT3 and a dedicated GNSS antenna for GPS functionality.

<--- End description table 60 --->





RF Band Mapping for Antenna Ports for P-5GS6-R16SA-GL


| Radio Access Technology (RAT) | Bands | Tx Antennas | Rx Antennas | GNSS Antenna |
|------|------|------|------|------|
|  |  | Default
Alternate Path | ANT0
ANT1
ANT2
ANT3 | GPS |


<--- Start description table 61 --->

This table outlines the RF band support for each antenna port (ANT 0–3) across 3G WCDMA, LTE, and 5G NR FR1 technologies, specifying the transmit (TX) and receive (RX) frequency bands supported for the Cisco 1000 Series Integrated Services Router 87 hardware. It serves as a reference for proper antenna configuration during installation, ensuring compatibility with the specified wireless standards and frequency bands.

<--- End description table 61 --->



[94]----------------------


| Radio Access Technology (RAT) | Bands | Tx Antennas | Rx Antennas | GNSS Antenna |  |  |  |  |
|------|------|------|------|------|------|------|------|------|
| 5GNR Sub-6G | 29 | - | - | Y | - | Y | - | - |
| 5GNR Sub-6G | 38, 41 | ANT2 | ANT0 | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 48 | ANT3 | ANT1 | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 75, 76 | - | - | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 77, 78 | ANT3 | ANT1 ANT2 | Y | Y | Y | Y | - |
| 5GNR Sub-6G | 79 | ANT3 | ANT1 | Y | Y | Y | Y | - |
| LB LTE/5GNR Sub-6G | 5, 8, 12, 13, 14, 17, 18, 19, 20, 26, 28, 71 | ANT0 | - | Y | - | Y | - | - |
| MB/HB LTE/5G NR Sub-6G | 1, 2, 3, 4, 7, 25, 30, 39, 40, 66, 70 | ANT0 | - | Y | Y | Y | Y | - |
| LTE | 29 | - | - | Y | - | - | Y | - |
| LTE | 34 | ANT0 | - | Y | - | Y | - | - |
| LTE | 46 | - | - | Y | - | - | Y | - |
| LTE | 32 | - | - | Y | Y | Y | Y | - |
| LTE | 38 | ANT0 | - | Y | Y | Y | Y | - |
| LTE | 41 | ANT0 | ANT2 | Y | Y | Y | Y | - |
| LTE | 42, 43, 48 | ANT3 | ANT1 | Y | Y | Y | Y | - |
| WCDMA | 1, 2, 4, 5, 8, 19 | ANT0 | - | Y | - | Y | - | - |
| GNSS | - | - | - | - | - | - | - | L1 |


<--- Start description table 62 --->

This table outlines the RF band mapping for antenna ports on specific Cisco 1000 Series Integrated Services Router models (P-5GS6-GL and P-5GS6-R16SA-GL), providing critical information for hardware installation and module upgrades. It serves as a reference for technicians configuring or replacing internal modules and field replaceable units, ensuring proper frequency alignment during deployment.

<--- End description table 62 --->



[95]----------------------


### LED Behaviors


The following table lists the LED indicators and their behavior. The LEDs provide a visual indication of the status and the currently selected services.

LED Indicators:


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


<--- Start description table 63 --->

This table outlines the functions and visual states of the LED indicators, which convey the system’s operational status and currently active services, aiding users in monitoring device conditions at a glance.

<--- End description table 63 --->





### Attaching the Antennas


To attach the antenna in the Pluggable Interface Module, perform the following steps.

[97]----------------------




<--- Start caption image 148 --->

Figure 79: Attaching the 5G New Radio (NR) Antenna (5G-ANTM-O4-B) to P-5GS6-GL PIM

<--- End caption image 148 --->



<--- Start description image 148 --->

This technical diagram illustrates the correct physical installation and cable mapping for attaching the 5G NR Antenna (model 5G-ANTM-04-B) to the P-5GS6-GL PIM (Printed Circuit Board Module). It serves as a critical visual guide for technicians during the installation and upgrade process.

**Key Components and Purpose:**

*   **Antenna Assembly (Top):** The diagram shows the 5G NR antenna, which is a multi-element array. It features a central mounting base and multiple coaxial cables (with yellow connectors) extending downwards.
*   **P-5GS6-GL PIM (Bottom):** This is the target module, identified by its label. It has several SMA (SubMiniature version A) connector ports on its top surface.
*   **Cable Mapping:** Lines with arrows clearly indicate which antenna cable connects to which SMA port on the PIM. The diagram shows the following specific mappings:
    *   The leftmost antenna cable connects to port `φ2`.
    *   The second cable from the left connects to port `φ1`.
    *   The third cable from the left connects to port `φ3`.
    *   The fourth cable from the left connects to port `φ4`.
*   **Other Ports:** The PIM also features other ports, including an `EN` (Enable) port, a `C` port, and a `GND` (Ground) port, which are not part of the antenna cable connection but are essential for the module's operation.

**Significance and Context:**

This diagram is a crucial part of the installation procedure for 5G infrastructure. It ensures that the antenna's signal paths are correctly routed to the PIM, which is essential for the proper functioning of the 5G network. The accompanying text emphasizes the importance of attaching each SMA cable to the correct port as indicated in the table and ensuring that each cable is securely tightened into its connector to prevent signal loss or connection failure. This precise configuration is vital for maintaining the performance and reliability of the 5G NR system.

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


<--- Start caption table 64 --->

Table 12: Port Mappings for 5G-ANTM-0-4-B on P-5GS6-GL and P-LTEAP18-GL PIMs

<--- End caption table 64 --->



<--- Start description table 64 --->

This table outlines the procedures for installing and upgrading internal modules and field replaceable units, including specific instructions for inserting a Micro-SIM card into a USB LTE dongle, alongside a reference link for 5G NR antenna specifications and installation guidelines.

<--- End description table 64 --->



The following link contains the antenna specifications and installation instructions for 5G NR (5G-ANTM-O-4-B):

https://www.cisco.com/c/en/us/td/docs/routers/connectedgrid/antennas/installing-combined/ b-cisco-industrial-routers-and-industrial-wireless-access-points-antenna-guide/m-5g-antm-04b.html#Cisco_ Generic_Topic.dita_e780a6fe-fa46-4a00-bd9d-1c6a98b7bcb9

### Install a Micro-SIM Card into a USB LTE Dongle


This section describes how to insert a micro-SIM card into a USB LTE dongle in a C1101-4P router.



<--- Start caption image 150 --->

Figure 80: Micro-SIM Card Slot with Dust Cover

<--- End caption image 150 --->



<--- Start description image 150 --->

This diagram illustrates the step-by-step process for installing a micro-SIM card into a USB LTE dongle, specifically for use with a Cisco 1000 Series Integrated Services Router (such as the C1101-4P). It is a visual guide from Cisco's hardware installation documentation.

**Purpose:** To provide clear, visual instructions for users to correctly insert a micro-SIM card into the LTE dongle to enable cellular connectivity.

**Components and Steps Explained:**

1.  **Step 1 (①):** The diagram shows the USB LTE dongle with its protective cap (①) in the closed position. The cap is designed to cover the SIM card slot.
2.  **Step 2 (② → ③):** The user is instructed to tap open the protective cap (②) to expose the SIM card slot (③). The arrow indicates the action of opening the cap.
3.  **Step 3 (④):** The micro-SIM card is inserted into the slot (④). The diagram shows the card being inserted with its metal contacts facing down and aligned with the slot, ensuring proper orientation.
4.  **Step 4 (⑤):** The protective cap (⑤) is tapped back into place to secure the micro-SIM card within the dongle.

**Significance:**
This is a critical installation step for enabling cellular (LTE) connectivity on the router. The USB LTE dongle acts as a modem, allowing the router to connect to a cellular network for internet access. Correctly inserting the micro-SIM card is essential for the device to function properly. The diagram's clear, sequential visual representation helps prevent user error during hardware installation.

<--- End description image 150 --->



Step 1 To insert a micro-SIM card into a USB LTE dongle, do these steps:

• Tap open the micro-SIM protective cap on the USB dongle, gently insert the micro-SIM card with its edge oriented as shown in the figure until the SIM is seated in the socket.
• Tap close the micro-SIM protective cap on the USB to close the slot.


[99]----------------------


• Step 2 To remove a micro-SIM card into a USB LTE dongle, do these steps:
• Tap open the dust cover, and then gently push the micro-SIM card to eject the card from the SIM slot.
• Tap close the micro-SIM protective cap on the USB to close the slot.


目



Note


The antenna orientation may need to be adjusted for optimal performance.

Perform the following steps to insert the USB LTE dongle with the SIM card into a horizontal slot on the rear panel of a C110x series router:

• Ensure the micro-SIM is installed in the LTE USB dongle.
• Plug the LTE USB dongle into the magnet holder.
• Attach the magnet holder into the USB port on the metal front panel of C1101-4P.


Figure 81: LTE USB 2.0 Dongle for C1101-4P



<--- Start description image 152 --->

This technical diagram illustrates the correct installation orientation for the Cisco LTE USB 2.0 Dongle (Figure 81) when connecting it to the C1101-4P router. The image highlights four key components and their purpose:

*   **Component 1 (Supporting Ring):** A structural element on the dongle that provides rigidity and helps secure the device within the magnet holder.
*   **Component 2 (Magnet):** An integrated magnet on the underside of the dongle's housing. This magnet is designed to attach to the magnetic holder on the router's front panel, allowing for a secure, non-physical connection.
*   **Component 3 (Extend Outward 30mm):** An arrow indicates that the dongle should be extended outward from the router's front panel by 30mm to ensure proper alignment and connection to the USB port.
*   **Component 4 (Plug-in Direction):** A black arrow points to the USB connector, indicating the correct orientation for plugging the dongle into the USB port on the router's front panel.

The diagram's purpose is to provide a clear, visual guide for technicians to correctly install the LTE dongle, ensuring it is securely attached via the magnet and properly aligned for USB connection, which is essential for establishing cellular connectivity on the C1101-4P router.

<--- End description image 152 --->



| Number | Description |
|------|------|
| 1 | Supporting ring |
| 2 | Magnet |
| 3 | Extend outward 30mm |
| 4 | Plug-in direction |


<--- Start description table 65 --->

This table illustrates the step-by-step hardware installation process for the LTE USB 2.0 dongle on the Cisco 1000 Series Integrated Services Router C1101-4P, detailing the sequence of actions required to properly integrate the dongle into the router’s system.

<--- End description table 65 --->



[100]----------------------




<--- Start description image 153 --->

This technical diagram illustrates the installation of a Cisco router’s USB LTE dongle, specifically model Router-C1101-4PLTEPW, into a vertical USB port. The image serves as a visual guide for technicians during the process of installing or upgrading internal modules and field-replaceable units, as referenced in the surrounding text.

Key components shown and their purpose:

*   **(1) Supporting Ring:** This is the structural component of the router chassis that provides a secure mounting point for the dongle. The arrow indicates the correct orientation for insertion, ensuring the dongle is properly seated and aligned.
*   **(2) Dongle Holder with Magnet:** This is the mounting bracket that attaches to the router’s chassis. The magnet is designed to hold the dongle firmly in place after it is inserted into the USB port, preventing it from becoming loose or dislodged during operation.
*   **(3) Router-C1101-4PLTEPW:** This is the USB LTE dongle itself. The diagram shows it being inserted into the vertical USB port. The accompanying text clarifies that the same procedure applies to routers with a vertical USB slot, indicating this is a standard installation method for this type of hardware.

The overall significance of this image is to provide a clear, step-by-step visual reference for correctly installing the LTE dongle, ensuring a secure and functional connection for wireless data services. It is part of a larger set of instructions for maintaining and upgrading the router’s internal components.

<--- End description image 153 --->



| Number | Description |
|------|------|
| 1 | Supporting ring |
| 2 | Dongle holder with magnet |
| 3 | Router-C1101-4PLTEPW |


<--- Start description table 66 --->

This table outlines the installation and upgrade procedures for internal modules and field replaceable units, including specific instructions for mounting antennas on Cisco 1000 Series Integrated Services Routers, with guidance applicable to routers featuring vertical USB slots for LTE dongles.

<--- End description table 66 --->



Follow the same procedure to install the USB LTE dongle onto routers with a vertical USB slot.

### Antenna Mounting Instructions


This section describes how to mount the antenna on the Cisco 1000 Series Integrated Services Router. The information is contained in the following sections:

#### Rack Mount of the Antenna


To install the antenna on a rack, do these steps:

##### Option A - Rack Mount at a Different Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)
• Step 2 Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 3 Tighten the screw, the recommended torque is 10-12 in-lb.


[101]----------------------




<--- Start description image 154 --->

This technical diagram illustrates Step 1 of the installation process for mounting an internal module or Field Replaceable Unit (FRU) using R-Brackets (part number 700-121611-01) in a rack-mount configuration. The purpose is to securely attach the mounting bracket to the rack frame so that the equipment can be mounted at the same height as the platform.

**Diagram Components and Purpose:**

*   **Component ① (Rack Frame):** The vertical metal structure of the rack, which provides the mounting surface. The part number 521010 is visible, likely identifying the specific rack model or frame.
*   **Component ② (R-Bracket):** The L-shaped mounting bracket (part number 700-121611-01) that will be attached to the rack. It has pre-drilled holes to align with the rack's mounting points.
*   **Component ③ (Screw):** The fastener used to secure the R-Bracket to the rack. The diagram shows the screw being inserted through the bracket and into the rack frame.

**Key Instructions from the Context:**

The diagram visually supports the textual instructions provided in the context. It shows the initial placement of the R-Bracket (②) onto the rack frame (①) and the use of a screw (③) to fasten it. The accompanying text specifies that this is Step 1 and that the bracket should be placed at an appropriate location using two screws, with a recommended torque of 10-12 in-lb for tightening.

In summary, this diagram is a visual guide for the first step in a hardware installation procedure, showing how to correctly position and begin securing the mounting bracket to the rack before attaching the actual equipment.

<--- End description image 154 --->



##### Option A - Rack Mount at the Same Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 2 Tighten the screw, the recommended torque is 10-12 in-lb.




<--- Start description image 155 --->

This technical diagram illustrates the hardware installation procedure for mounting a Cisco 1000 Series Integrated Services Router (labeled as component ②) using a rack-mount bracket (labeled as component ①) in Option A — mounting at the same height as the platform.

**Diagram Components and Purpose:**

*   **Component ① (Rack Mount Bracket):** This is the vertical mounting rail or bracket designed to be attached to a standard 19-inch equipment rack. It provides structural support for the router.
*   **Component ② (Cisco Router):** The main device, the Cisco 1000 Series Integrated Services Router, which is to be mounted onto the bracket.
*   **Component ③ (R-Bracket):** The specific mounting bracket (part number 700-121611-01) referenced in the text. It is shown attached to the rack mount bracket (①) and is designed to clamp onto the router chassis (②).
*   **Component ④ (Screw):** The fastener used to secure the R-bracket (③) to the rack mount bracket (①). The diagram shows the screw being inserted through the bracket and into the rack mount.
*   **Component ⑤ (Screw):** The second screw, which is used to secure the R-bracket (③) to the router chassis (②). The diagram shows this screw being inserted through the bracket and into the router.
*   **Component ⑥ (Screw):** The second screw for the R-bracket (③), which is used to secure it to the rack mount bracket (①). The diagram shows this screw being inserted through the bracket and into the rack mount.
*   **Component ⑦ (Wall-Mounting Bracket):** This component (part number 700-121609-01) is shown detached and is intended for wall mounting, but the diagram is focused on the rack-mounting procedure for Option A.

**Significance and Context:**

This diagram is a visual guide from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide. It provides a clear, step-by-step visual representation of how to mount the router using the R-bracket (③) to the rack mount bracket (①). The accompanying text specifies that the R-bracket should be placed at an appropriate location on the rack and tightened with a torque of 10-12 in-lb. The diagram complements the text by showing the physical relationship between the components and the direction of the screws, ensuring the user can correctly assemble the mounting hardware before proceeding to connect the dongle, USB cable, and antenna. This is a critical step in the installation process to ensure the router is securely and correctly mounted for optimal performance and safety.

<--- End description image 155 --->



Both options - A and B should follow these remaining steps to complete the mounting procedure:

• Assemble dongle, USB, cable and antenna together in advance.
• Pick up the wall-mounting bracket (700-121609-01) and 2 SCREWS (48-0580-01).
• Align and fasten the screws.
• Plug the USB cable to the USB port on the chassis to complete the mounting procedure.


[102]----------------------




<--- Start description image 156 --->

This technical diagram from the Cisco 1000 Series Integrated Services Router Hardware Installation Guide illustrates the step-by-step process for mounting the router’s antenna on a wall. The top section provides a exploded-view diagram showing the individual components and their assembly: the antenna (2), the antenna mount bracket (1), the antenna connector (3), the mounting hardware (4), and the router’s wall-mounting bracket (5) and power cable (6). The bottom section shows the fully assembled unit, with the antenna mounted vertically on the wall bracket, which is then attached to the router’s chassis (1). This visual guide is essential for technicians to ensure proper installation, secure mounting, and optimal wireless performance for the router.

<--- End description image 156 --->



#### Wall Mount of the Antenna


To install the antenna on a wall, do these steps:

[103]----------------------


• Step 1 Pick up the C-Bracket (700-121628-01), place the bracket and then fix it on the wall using four screws.
• Step 2 Assemble the USB cable (74-122795-01), dongle and antenna (07-100470-01) together. Pick up the wall-mount bracket (700-121609-01), two SCREWS (48-0580-01). Align and fasten the screws (recommended torque is 10-12 in-lb), the wall-mount is complete.




<--- Start description image 157 --->

This technical diagram illustrates the hardware assembly and mounting procedure for a Cisco 1000 Series Integrated Services Router, specifically detailing the installation of its wireless antenna and wall-mount bracket. The image serves as a visual guide for technicians to correctly assemble and install the external antenna system.

The diagram breaks down the components and their assembly into five labeled parts:

*   **(1) Antenna:** A vertically oriented, external wireless antenna (model 07-100470-01) that connects to the router's wireless module. It is the primary component for wireless signal transmission and reception.
*   **(2) Wireless Module/Dongle:** The internal wireless module (likely the 74-122795-01 dongle) that plugs into the router. The antenna connects to this module via a standard connector.
*   **(3) Wall-Mount Bracket (C-Bracket):** The mounting hardware (model 700-121628-01) designed to be fixed to a wall. This bracket provides a secure, vertical mounting point for the entire antenna assembly.
*   **(4) Wall-Mount Bracket (700-121609-01):** A second, different wall-mount bracket (or a specific mounting plate) that is fastened to the wall using screws. This component is shown with screw holes (labeled CC1, CC2, CC3, CC4) and is intended to hold the wireless module/dongle assembly.
*   **(5) USB Cable:** The USB cable (model 74-122795-01) that connects the wireless module to the router's USB port. The diagram also implies the use of a cable clip from the kit to manage routing and prevent strain.

**Purpose and Significance:**
This diagram is a critical part of the installation guide for the Cisco 1000 Series router. It visually clarifies the physical assembly and mounting process, which is essential for ensuring proper wireless performance and physical security. The diagram complements the textual instructions by showing how the components fit together, helping technicians avoid misassembly and ensuring the antenna is correctly positioned and secured to the wall. The use of numbered parts and dotted lines clearly indicates the connection points and assembly sequence, making it an indispensable tool for field technicians during installation.

<--- End description image 157 --->



##### Connect the Antenna to the Device


• Step 1 Ensure the reserved USB cable length is sufficient to reach the device.
• Step 2 Ensure the use the cable clip within USB cable kit (74-122795-01) to manage cable routing and to hold the cable weight.
• Step 3 Ensure there are no sharp radius within the USB cable routing.


[104]----------------------




<--- Start description image 158 --->

This technical diagram illustrates the installation of a Cisco wireless access point (labeled “1”) connected to a ceiling-mounted antenna assembly (labeled “2”). The diagram is part of a larger installation guide, specifically addressing the “Install and Upgrade Internal Modules and Field Replaceable Units” for a ceiling-mounted antenna system.

**Key Components and Purpose:**
- **Component 1 (Access Point):** The main wireless device, shown with a Cisco logo and ventilation grille, which connects via a cable to the antenna assembly.
- **Component 2 (Antenna Assembly):** A ceiling-mount bracket with a vertically oriented antenna attached. This assembly is designed to be mounted to the ceiling or a rack.
- **Connection:** A cable links the access point to the antenna assembly, enabling wireless signal transmission.

**Significance and Context:**
This diagram visually supports the procedural instruction “Option A - Rack Mount at a Different Height with the Platform,” indicating that while the antenna is designed for ceiling mounting, it can also be adapted for rack mounting at a different height. The diagram serves as a clear, step-by-step visual aid for technicians to correctly install and connect the antenna to the access point, ensuring proper signal coverage and system functionality. The clean, labeled line drawing is typical of technical manuals to ensure clarity and precision during installation.

<--- End description image 158 --->



#### Ceiling Mount of the Antenna


To install the antenna on a rack, do these steps:

##### Option A - Rack Mount at a Different Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)
• Step 2 Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 3 Tighten the screw, the recommended torque is 10-12 in-lb.


[105]----------------------




<--- Start description image 159 --->

This technical diagram illustrates Step 1 of the installation process for mounting an internal module or Field Replaceable Unit (FRU) using R-Brackets (part number 700-121611-01) in a rack-mount configuration. The purpose is to securely attach the mounting bracket to the rack frame so that the equipment can be mounted at the same height as the platform.

**Diagram Components and Purpose:**

*   **Component ① (Rack Frame):** The vertical structural member of the rack, which has a series of pre-drilled holes for mounting hardware. This is the primary structure to which the bracket will be attached.
*   **Component ② (R-Bracket):** The mounting bracket (part number 700-121611-01) that will be affixed to the rack. It has a mounting flange with holes that align with the rack's holes.
*   **Component ③ (Screw):** The fastener used to secure the bracket to the rack. The diagram shows the screw being inserted through the bracket and into the rack frame.

**Key Instructions from the Context:**

The diagram visually supports the textual instructions provided in the context. It shows the correct orientation for placing the R-Bracket (②) against the rack frame (①) and indicates where the screw (③) should be inserted to fasten them together. The accompanying text specifies that this is Step 1 of the process and that the recommended torque for tightening the screw is 10-12 in-lb to ensure a secure and safe installation. This step is critical for ensuring the equipment is properly aligned and secured before proceeding to mount the actual module or FRU.

<--- End description image 159 --->



##### Option A - Rack Mount at the Same Height with the Platform


• Step 1 Pick up the R-Brackets (700-121611-01)Place and fix the bracket at an appropriate location on the rack using two screws.
• Step 2 Tighten the screw, the recommended torque is 10-12 in-lb.




<--- Start description image 160 --->

This technical diagram illustrates the hardware installation procedure for mounting a Cisco 1000 Series Integrated Services Router (labeled as component ②) using a rack-mount bracket (labeled as component ①) in Option A — mounting at the same height as the platform.

**Diagram Components and Purpose:**

*   **Component ① (Rack Mount Bracket):** This is the vertical mounting rail or bracket designed to be attached to a standard 19-inch equipment rack. It provides structural support for the router.
*   **Component ② (Cisco Router):** The main device, the Cisco 1000 Series Integrated Services Router, which is to be mounted onto the rack bracket.
*   **Component ③ (R-Bracket):** The specific mounting bracket (part number 700-121611-01) referenced in the instructions. It is shown attached to the rack bracket (①) and is designed to clamp onto the router chassis (②).
*   **Component ④ (Screw):** The fastener used to secure the R-bracket (③) to the rack bracket (①). The instructions specify using two screws and tightening them to a torque of 10-12 in-lb.
*   **Component ⑤ (Screw):** The fastener used to secure the R-bracket (③) to the router chassis (②). This step is part of the final assembly.
*   **Component ⑥ (Wall-Mounting Bracket):** This is a separate component (part number 700-121609-01) that is part of the installation process for both Option A and Option B. It is shown detached in this diagram but is used to mount the router to a wall or other surface.
*   **Component ⑦ (Screws):** The screws (part number 48-0580-01) used to attach the wall-mounting bracket (⑥) to the router chassis (②).

**Significance and Context:**

This diagram is a step-by-step visual guide from the Cisco 1000 Series Router Hardware Installation Guide. It specifically details the first step for Option A, which involves mounting the router at the same height as the rack platform. The diagram clearly shows the relationship between the rack bracket, the R-bracket, and the router, indicating where screws (④ and ⑤) should be placed to secure the router to the rack. The diagram also serves as a reference for the subsequent steps, which involve assembling the dongle, USB cable, and antenna, and then attaching the wall-mounting bracket (⑥) to the router chassis (②) using the provided screws (⑦). This ensures the router is properly secured and ready for operation.

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



## Installing a SIM Card on C111X, C1109-2PX, C1109-4P


The SIM card socket is located on the I/O side of the unit.

[107]----------------------




<--- Start description image 162 --->

This technical diagram, titled "Figure 82: Removing SIM Cover and Inserting SIMs into C111X," provides a clear, step-by-step visual guide for installing or replacing SIM cards in the Cisco C111X router. It is part of the Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router.

The diagram illustrates two key states of the device:
1.  **Top View (Labeled '1'):** Shows the router with the SIM cover (labeled '1') fully attached, covering the SIM card slots.
2.  **Bottom View (Labeled '3'):** Shows the router with the SIM cover (labeled '2') removed, revealing the two SIM card slots (labeled '3') where SIM 0 and SIM 1 are inserted.

The accompanying legend clarifies the components:
*   **1:** The SIM Cover, which is the removable panel that protects the SIM card slots.
*   **2:** SIM 0, the first SIM card slot.
*   **3:** SIM 1, the second SIM card slot.

**Purpose and Significance:**
This diagram is a critical part of the installation and maintenance procedure for the C111X router. It visually demonstrates the physical process of accessing the dual SIM card slots, which are essential for enabling cellular connectivity (e.g., for remote management or data services). The clear labeling and contrasting views help technicians accurately identify and handle the components, reducing the risk of damage during installation or replacement. This is a standard procedure for field service engineers and network administrators working with this specific Cisco router model.

<--- End description image 162 --->



|  |  |
|------|------|
| 1 | SIM Cover |
| 2 | SIM 0 |
| 3 | SIM 1 |


<--- Start description table 67 --->

This table outlines the procedure for installing and upgrading internal modules and field replaceable units, specifically detailing how to insert SIM cards into the Cisco 1000 Series Integrated Services Router models C111X, C1109-2PX, and C1109-4P, which feature dual SIM card slots accessible via a removable cover.

<--- End description table 67 --->



The unit supports dual SIM cards behind a SIM cover. To insert the SIM cards, perform the following steps:

[108]----------------------




<--- Start caption image 163 --->

Figure 83: SIMs Inserted

<--- End caption image 163 --->



<--- Start description image 163 --->

This technical diagram illustrates the process for installing and removing SIM cards in Cisco 1000 Series Integrated Services Routers (specifically models C111X, C1109-2PX, and C1109-4P), as detailed in the Hardware Installation Guide.

The image provides a clear, labeled view of the router's rear panel and a magnified cross-section of the SIM card slots to guide technicians through the procedure.

**Key Components and Their Purpose:**

*   **1. SIM Card Slot Location:** This label points to the physical location of the SIM card slots on the router's rear panel. The diagram shows two distinct slots, labeled as SIM 0 and SIM 1.
*   **2. SIM 1 Slot:** This label identifies the slot designated for the second SIM card (SIM 1). The diagram shows the physical slot and its corresponding orientation notch.
*   **3. SIM 0 Slot:** This label identifies the slot designated for the first SIM card (SIM 0). The diagram shows the physical slot and its corresponding orientation notch.
*   **4. Orientation Notch (SIM 0):** This label points to the small notch on the SIM 0 slot. This notch is a critical alignment feature that ensures the SIM card is inserted in the correct orientation. The diagram shows the notch's position relative to the slot.
*   **5. Orientation Notch (SIM 1):** This label points to the small notch on the SIM 1 slot. Like the SIM 0 notch, this is a critical alignment feature for the second SIM card.

**Significance and Context:**

This diagram is a crucial part of the installation guide for these Cisco routers. It visually communicates the precise steps for installing or removing SIM cards, which are used for cellular connectivity. The diagram emphasizes the importance of correct orientation, as indicated by the notches, and the "push-push" type connectors, which require the user to insert the SIM card until it clicks into place. The magnified view helps technicians accurately identify the slots and notches, reducing the risk of damage to the router or the SIM card. The overall purpose is to ensure a secure and correct installation, which is vital for the router's cellular functionality.

<--- End description image 163 --->



|  |  |
|------|------|
| 1 | Micro SIM slots |
| 2 | SIM 0 slot |
| 3 | SIM 1 slot |
| 4 | Orientation notch (SIM 0) |
| 5 | Orientation notch (SIM 1) |


<--- Start description table 68 --->

This table illustrates the step-by-step procedure for installing and removing SIM cards in Cisco 1000 Series routers (specifically models C111X, C1109-2PX, and C1109-4P), including instructions for proper orientation, insertion, and removal using a flat screwdriver, as well as securing the SIM cover after installation.

<--- End description table 68 --->



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

## Installing a Nano-SIM Card into a Nano-To-Micro-SIM Adapter


Step 1 Place the nano-SIM card with the electrical contacts surface facing up to position it into the micro-SIM adapter as shown below.



<--- Start description image 165 --->

This diagram illustrates the correct orientation and placement for installing a nano-SIM card into a nano-to-micro-SIM adapter, a critical step in hardware installation for devices like the Cisco 1000 Series Integrated Services Router.

The image is a technical schematic showing a top-down view of the adapter with the nano-SIM card being inserted. Each component is labeled for clarity:

*   **1. Electrical contact surface up:** This indicates the correct orientation for the nano-SIM card. The metallic contacts on the card must be facing upwards to ensure proper electrical connection with the device's reader.
*   **2. Nano-SIM card:** The small SIM card itself, which is being inserted into the adapter.
*   **3. Backing surface (cutout not open) for nano-SIM:** This refers to the part of the adapter that the nano-SIM card rests against. The cutout is designed to be closed or covered, ensuring the card is held securely and correctly aligned within the adapter.
*   **4. Nano-to-micro-SIM adapter:** The physical adapter that converts the smaller nano-SIM card to fit into a device that requires a micro-SIM slot.

The purpose of this diagram is to provide a clear, step-by-step visual guide to prevent installation errors. It emphasizes that not all adapters are designed to handle nano-SIM cards correctly, and improper placement can lead to the card being unreadable by the device. This is a crucial detail for technicians installing hardware, ensuring compatibility and functionality.

<--- End description image 165 --->



|  |  |
|------|------|
| 1 | Electrical contact surface up |
| 2 | Nano-SIM card |
| 3 | Backing surface (cutout not open) for nano-sim |
| 4 | Nano-to-micro-sim adapter |


<--- Start description table 69 --->

This table illustrates the correct orientation for inserting a nano-SIM card into a nano-to-micro-SIM adapter, as part of the hardware installation process for the Cisco 1000 Series Integrated Services Router. It visually guides users to position the card with its electrical contacts facing upward for proper alignment and secure fit.

<--- End description table 69 --->



[110]----------------------




<--- Start description image 166 --->

This technical diagram illustrates Step 2 of installing a Nano-SIM card into a Nano-to-Micro-SIM adapter, as part of the hardware installation process for Cisco 1000 Series Integrated Services Routers or Pluggable Interface Modules (PIMs).

**Diagram Components and Purpose:**
*   **Component 1 (Nano-SIM card):** The small, rectangular SIM card designed for modern smartphones and devices. It is shown being inserted into the adapter.
*   **Component 2 (Nano-to-Micro-SIM adapter):** A plastic adapter that allows a smaller Nano-SIM card to fit into a larger Micro-SIM slot. The diagram highlights the specific slot within the adapter where the Nano-SIM card should be placed.

**Significance:**
This visual guide is critical for technicians performing hardware installation. It ensures the correct orientation and placement of the SIM card within the adapter, which is a necessary step for enabling cellular connectivity in the router or PIM. The diagram is part of a larger, step-by-step procedure to install and upgrade internal modules, emphasizing precision and adherence to the manufacturer's instructions.

<--- End description image 166 --->



|  |  |
|------|------|
| 1 | Nano-SIM card |
| 2 | Nano-to-micro-sim adapter |


<--- Start description table 70 --->

This table outlines the procedure for installing a nano-SIM card into a nano-to-micro-SIM adapter, specifically for use in Cisco 1000 Series Integrated Services Routers and their Pluggable Interface Modules (PIMs). It serves as a step-by-step guide for hardware installation, ensuring compatibility and proper placement of SIM adapters within micro-SIM slots.

<--- End description table 70 --->



Step 2 Follow the instructions to install nano-SIM/adapters into micro-SIM slots of routers or Pluggable Interface Modules (PIMs).


[111]----------------------




<--- Start description image 167 --->

This is the chapter heading image for Chapter 5 of the "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 104," specifically titled "ROM Monitor Overview."

The image uses a wide, atmospheric photograph of a modern city skyline at sunrise or sunset, with the sun creating a bright lens flare on the left. The foreground features a vast, reflective rooftop or plaza, leading the viewer's eye toward the towering skyscrapers. This imagery evokes themes of technology, infrastructure, and connectivity — fitting for a networking device manual.

The text "CHAPTER 5" is prominently displayed in a bold, black, sans-serif font at the bottom center, clearly marking the section within the guide. The chapter title, "ROM Monitor Overview," is implied by the context provided in the surrounding text, indicating that this section will cover the basics of the router's ROM Monitor mode — a crucial low-level diagnostic and recovery environment used for troubleshooting and initial configuration.

The overall design suggests a professional, technical document aimed at network engineers or IT professionals, using a visually appealing background to make the technical content more engaging.

<--- End description image 167 --->



5

C H A P T E R

## ROM Monitor Overview


The ROMMONis the bootloader that initializes the hardware when the platform is powered on or reset. From the ROMMON prompt, a Cisco IOS XE image can be manually booted. There is also an autoboot option to boot a specified IOS XE image for every power-on or reset. When new features or significant defects are resolved, a newer ROMMON release is available on CCO. To determine the current ROMMON version and the location of the latest ROMMON release, these details are available in the following sections:

.

• ROM Monitor Overview, on page 105


ROM Monitor Overview


The ROMMonitor software is also known as ROMMON , boot software , boot image , or boot helper . Although it is distributed with routers that use the Cisco IOS XE software, the ROMMON is a separate program from the Cisco IOS XE software. During normal startup, ROMMON initializes the router, and then, the control passes to the Cisco IOS XE software.

Whenyouconnect a terminal to the router that is in ROMMON mode, the ROMMON command-line interface (CLI) prompt is displayed.

Access the ROMMON mode to perform these tasks:

• Specify config-register value to use for the next boot up
• Boot a valid IOS XE image
• Bypass NVRAM settings and config-register value for password recovery


目



Note

After the Cisco IOS XE software boots up, ROMMON is no longer in use.

Environmental Variables and the Configuration Register


Two primary connections exist between ROMMON and the Cisco IOS XE software: the ROMMON environment variables and the configuration register.

[112]----------------------


The ROMMON environment variables define the location of the Cisco IOS XE software and describe how to load it. After ROMMON has initialized the router, it uses the environment variables to locate and load the Cisco IOS XE software.

The configuration register is a software setting that controls how a router starts up. One of the primary uses of the configuration register setting is to control whether the router starts in ROMMON mode or Administration EXEC mode. The configuration register is set in either ROMMON mode or Administration EXEC mode as needed. You can set the configuration register using the Cisco IOS XE software prompt when you need to use ROMMONmode.Whenmaintenancein ROMMODEmodeiscomplete,change the configuration register back so that the router reboots with the Cisco IOS XE software.

Access ROMMON Mode with a Terminal Connection


When the router is in ROMMODE mode, you can access the ROMMODE software only from a terminal connected directly to the console port of the card. Because the Cisco IOS XE software (EXEC mode) is in operatiion, the nonmanagement interfaces are not accessible. Therefore, all Cisco IOS XE software resources are unavailable.

Network Management Access and ROMMON Mode


ROMMONmode is a router mode, not a mode within the Cisco IOS XE software. The ROMMON software and the Cisco IOS XE software are two separate programs that run on the same router. At any given time, the router is running one of these programs, but it never runs both at the same time.

One area that can be confusing when using ROMMON and the Cisco IOS XE software is the area that defines the IP configuration for the Management Ethernet interface. Most users are comfortable with configuring the Management Ethernet interface in the Cisco IOS XE software. When the router is in ROMMON mode, however, the router is not running the Cisco IOS XE software, therefore, Management Ethernet interface configuration is not available.

When you want to access other devices, such as a TFTP server, while in ROMMON mode on the router, you must configure the ROMMON variables with IP access information.

For more information on ROMMON and Basic Procedures, refer to the Upgrading Field-Programmable Hardware Devices for Cisco 1000 Series ISRs

[113]----------------------




<--- Start description image 169 --->

Based on the provided context, which is a text excerpt from a "Hardware Installation Guide for the Cisco 1000 Series Integrated Services Router 106," the image is not a direct visual representation of the guide's content. Instead, it appears to be a generic, thematic placeholder or cover image for a section of a document.

The image itself is a photograph of a modern city skyline viewed from a high vantage point, such as a rooftop or elevated walkway. The sun is low in the sky, creating a bright, hazy glow and long shadows, suggesting either early morning or late afternoon. The foreground consists of a tiled or paved surface, and the background is filled with a mix of contemporary high-rise buildings and a construction crane, indicating an active, developing urban environment.

The text "CHAPTER 6" is prominently displayed in the lower right corner, suggesting this image serves as the header or cover for the sixth chapter of a larger document.

**Relevant and Comprehensive Caption:**

**Chapter 6: Urban Infrastructure & Network Deployment — A Visual Introduction**

This chapter, titled "Chapter 6," is introduced by a photograph of a modern, dynamic cityscape, symbolizing the complex, interconnected infrastructure that underpins modern digital networks. The image, featuring a sun-drenched urban environment with towering buildings and a construction crane, visually represents the setting where enterprise-grade networking equipment like the Cisco 1000 Series Integrated Services Router 106 is deployed. The scene evokes themes of connectivity, growth, and technological advancement — core concepts relevant to the installation and operation of network hardware in commercial environments. The chapter likely delves into the practical aspects of installing and configuring this router within such urban or corporate settings, aligning with the regulatory and technical context provided in the preceding text regarding FCC compliance for Class A digital devices. The image serves as a thematic anchor, connecting the technical manual's content to the real-world environments where such critical network infrastructure operates.

<--- End description image 169 --->



6

# Supplier Declaration of Conformity


This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against any harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio frequency energy, and if it is not installed and used in accordance with the instruction manual, it may may cause harmful interference to radio communications.

• This device may not cause harmful interference.
• This device must accept any interference received, including interference that may cause an undesired operation.


The operation of this equipment in a residential area is likely to cause harmful interference, in which case, users are required to correct the interference at their own expense.

Radio Compliance


This system uses both licensed and licensed exempt radio frequencies. The radios are evaluated to the following regulations:

The Wi-Fi Radio is evaluated to 47 Code of Federal Regulations Part 15.247 and Part 15.407.

Part 15 Radio Systems operating outdoors in the 5150-5250 MHz band must comply with the antenna installation requirements as set forth in the FCC Part 15.407 rules.

The LTE radio is evaluated to 47 Code of Federal Regulation Part 24 and 27.

The LTE radio operates on licensed frequency bands and requires a radio license to operate. It must be operated under the control of a Licensed Service Provider or Wireless Carrier.

Modifications by User or Installer


Modifying the equipment without Cisco's authorization may result in the equipment being no longer compliant with FCC requirements for Class A digital devices. In that event, your right to use the equipment may be limited by FCC regulations, and you may be required to correct any interference to radio or television communications at your own expense.

Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

FCC RF Exposure Compliance


This product has been found to be compliant to the requirements set forth in CFR 47 Section 1.1307 addressing RF Exposure from radio frequency devices, as defined in Evaluating Compliance with FCC Guidelines for Human Exposure to Radio Frequency Electromagnetic Fields.

[114]----------------------


To maintain compliance, the minimum separation distance from the antenna to general bystander is 20 cm (8,7 inches) or more.

CANADA


This Class [*] digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [*] est conforme à la norme NMB-003 du Canada

Radio (Wi Fi)


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

Radio (Wi Fi)


This product complies with the RSS of the Industry Canada rules.

Radiation Exposure Statement


This equipment complies with IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm (7.87 in.) between the radiator and yourself.



C1109-4PLTE2P = 27 cm Note

Déclaration D'exposition Aux Radiations


Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 20 cm (7.87 in.) de distance entre la source de rayonnement et votre corps.

[115]----------------------




C1109-4PLTE2P = 27 cm Note


THAILAND


เครื่องโทรคมนาคมและอุปกรณ์นี้มีความสอดคล้องตามมาตรฐานหรือข้อกําหนดทางเทคนิค ของ กสทช

This telecommunication equipment conforms to NTC/NBTC technical requirement (optional)

Radiocommunication equipment has electromagnetic field strength in compliance with the Safety Standard for the Use of Radiocommunication Equipment on Human Health announced by the National Telecommunication Commission.

[116]----------------------
