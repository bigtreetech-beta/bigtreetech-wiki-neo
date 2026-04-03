# BMCU-370

<div class="div-table">

<ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-5.webp').default} width="40%" class="right-image"/>


Product Link: [Buy Here](https://biqu.equipment/products/biqu-bmcu-370-full-multi-color-feeding-system?_pos=1&_sid=25fe58e41&_ss=r)

Structural Components: [Download Here](https://makerworld.com/zh/models/2472248-bmcu-c-370-hall-effect-structural-components#profileId-2714532)

Rotary Spool Holder for BMCU-370: [Download Here](https://makerworld.com/zh/models/2472284-rotary-spool-holder-for-bmcu-370#profileId-2714571)

## Product Overview

The BMCU is a multi-material control system based on open-source designs, engineered to replicate AMS functionality. It is compatible with Bambu Lab A-series, X-series, and P-series printers (Note: The P2S is not currently supported). Designed as a 4-channel system, the BMCU utilizes a CH32 microcontroller. Please note that RFID material identification is not currently supported.

As a third-party DIY accessory, the BMCU's stability may differ from the official AMS Lite, and future official printer firmware updates may impact compatibility. The BMCU is under active development; subsequent releases of firmware or structural parts may require manual user upgrades.

The BMCU is intended for DIY enthusiasts and educational purposes. Special thanks to the original creator, 4061N. BIQU is the exclusive authorized commercial manufacturer for the BMCU project.

## Product Features

- Faster Filament Switching: Unlike the AMCU, filament unloading does not require full retraction back to the runout sensor. It only needs to retract to the 5-way connector, significantly speeding up the switching process.
- Direct Dry Box Feeding: The parallel design operates without a built-in spool holder, allowing you to feed filament directly from a sealed dry box to the printer.
- Active Filament Buffering: An integrated buffer mechanism actively feeds filament before the printer detects a tangle, preventing extrusion issues caused by excessive pulling resistance.
- Standardized Hardware: The design utilizes standardized components with unified specifications for many mechanical parts. This reduces additional costs and ensures a high success rate for one-time DIY assembly.
- Advanced Photoelectric Detection: The BMCU features a photoelectric detection system capable of sensing transparent filaments. This eliminates the drag and instability commonly associated with microswitch sensors. This photoelectric module will also be released separately under an open-source license.

</div>

## Revision History

| Version | Date           | Update          |
| ------- | -------------- | --------------- |
| v1.0.0  | March 10, 2026 | Initial release |

## Firmware Versions

| BMCU-370 Firmware Version | A1 Firmware | A1 mini Firmware | P1S Firmware | X1 Firmware | Download Link |
| --- | --- | --- | --- | --- | --- |
| BMCU-V0.1-0027 | 01.04.00.00 01.05.00.00 01.06.00.00 01.07.00.00   01.07.02.00  | 01.04.00.00 01.05.00.00 01.06.00.00 01.07.00.00 01.07.02.00 |  |  |  [BMCU-V0.1-0027-upgrade](https://github.com/bigtreetech/BMCU/releases/download/v1.0.0/BMCU-V0.1-0027-upgrade.zip) |
| BMCU-CV0.1-0020-Auto Direction 745 Retract Distance | -- | -- | 01.07.00.00 | 01.08.50.32 | [BMCU-CV0.1-0020-Auto Direction 745 Retract Distance](https://github.com/bigtreetech/BMCU/releases/download/v1.0.0/BMCU-CV0.1-0020-Auto.Direction.745.Retract.Distance.bin) |

## Product Specifications

| Product Name                     | BIQU BMCU-370 Hall Version                                                                                                                                                |
| -------------------------------- | -------------------------------- |
| Versions                         | MCU-370 Hall Version [Assembled Kit]Simple 10-minute setup, then ready to go.BMCU-370 Hall Version [DIY Kit],Requires self-printing of housing and assembly. |
| Compatible Models                | A1, A1 mini, P1P, P1S, X1C, X1E                                                                                                                                           |
| Main Controller                  | CH32V203C8T6                                                                                                                                                              |
| Power Supply                     | AC 24V                                                                                                                                |
| Number of Supported Materials    | 4 channels                                                                                                                                                                |
| Communication Interface          | 4-pin                                                                                                                                                                     |
| Housing Material [Assembled Kit] | ABS                                                                                                                                                                       |

## BMCU-370 Installation Guides (For Bambu Lab A1)

- Step 1: Prepare the Bracket: Attach the mounting bracket to the BMCU-370 housing using the included M3x8 self-tapping screws, as shown below.

    <ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-6.webp').default} width="70%"/>

-  Step 2: Mount the Unit: Mount the assembled BMCU-370 to the top of the Bambu Lab A1 gantry.

    <ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-3.webp').default} width="70%"/>

- Step 3: Connect the Cable: Connect the BMCU-370 to either of the reserved 4-pin ports on the back of the A1 using the provided 4-pin cable.

    <ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-2.webp').default} width="70%"/>

    <ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-7.webp').default} width="70%"/>

- Step 4: Power on the printer and navigate to Settings to unload any external filament, then go to AMS Options, set the type to AMS / AMS 2 Pro / AMS HT, and restart the printer to apply the changes.

:::note

The BMCU-370 does not support automatic filament loading; initial loading must be done manually.

:::

## BMCU-370 Installation Guides (For Bambu Lab A1 mini)

- Step 1: Print the Bracket: Download and print the recommended [bmcu-A1mini Rotary Mount](https://makerworld.com/zh/models/1186174-bmcu-a1mini-rotary-mount?from=search#profileId-1198642)
- Step 2: Install and Connect: Follow the tutorial images to mount the BMCU-370, then connect it to the A1 mini using the 4-pin cable.

    <ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-4.webp').default} width="70%"/>

- Step 3: Configure Printer Settings: Update the AMS Type in the printer settings, following the same procedure outlined in Step 4 of the A1 guide above.

## BMCU-370 Installation Guides (For Bambu Lab P/X Series)

- Step 1: Flash Firmware: Refer to the Firmware Flashing Guide below to flash the firmware version compatible with the P/X series.
- Step 2: Prepare a 5-Way Connector for P/X Series: We highly recommend purchasing a pre-manufactured connector. While you can find and print suitable designs from MakerWorld, 3D-printed versions often suffer from higher internal friction, which can lead to loading/unloading failures and negatively impact print quality.
- Step3: Prepare Mounting Brackets: Print the necessary mounting brackets for the P/X series (multiple community designs are available on MakerWorld).
- Step 4: Finalize Setup: Set up a filament spool rack: [Rotary Spool Holder for BMCU-370](https://makerworld.com/zh/models/2472284-rotary-spool-holder-for-bmcu-370#profileId-2714571)
- Connect the BMCU-370 to the printer via the 4-pin cable, then restart the machine.

:::note

Note: When using Bambu Studio, you must manually unload the external filament spool from the Device page after connecting to your P/X-series printer.

:::

## BMCU-370 Guide for Multi-Color Printing (2+ Colors)

You can refer to the open-source branch by author Paweł Jarczak on GitHub:[BMCU-C-PJARCZAK](https://github.com/jarczakpawel/BMCU-C-PJARCZAK)

## BMCU-370 Firmware Flashing Guide

- Wiring Preparation: You will need a flashing tool: the [**BIGTREETECH Writer V1.0 Module**](https://biqu.equipment/products/bigtreetech-btt-writer-v1-0-module-to-esp-01s-wifi-module-expansion-3d-printer-parts-for-skr-v1-4-skr-v1-4-turbo-control-board?_pos=1&_sid=62a533796&_ss=r). Connect the flashing tool to the BMCU-370 mainboard according to the pinout below:

    | BTT Writer V1.0 Interface | Mainboard Interface |
    | ------------------------- | ------------------- |
    | 3V3                       | V+                  |
    | GND                       | GND                 |
    | RXD                       | Tx                  |
    | TXD                       | Rx                  |

    <ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-1.webp').default} width="70%"/>

- Install and launch [WCHISPTool_Setup.exe](https://www.wch.cn/downloads/WCHISPTool_Setup_exe.html). If a prompt appears upon opening, click OK or close it.

    <ImageView src={require('./img/panda-bmcu370-17.webp').default} width="70%"/>

- Flashing Preparation:

    1: Select the “RISC-V MCUs CH32Vxxx”

    2: Set “Chip Serie” to “CH32V20x”

    3: Set “Chip Model” to “CH32V203C8T”

    4: Set “Dnld Port” to “SerialPort”

    5: Click “Search” to locate the flashing serial port.

    6: Then select the detected COM port number.

    7: Ensure the “Download Config” matches the default settings shown in the image below. Do not make any changes.


    <ImageView src={require('./img/panda-bmcu370-14.webp').default} width="70%"/>

- Select the file path to your target firmware file.

    <ImageView src={require('./img/panda-bmcu370-15.webp').default} width="70%"/>

- Press and hold the BOOT button, press RESET once while continuing to hold BOOT, then release the BOOT button to enter flashing mode.

    <ImageView src={require('@site/docs/panda-series/module/bmcu370/img/panda-bmcu370-8.webp').default} width="70%"/>

- Click “Deprotect”。

    <ImageView src={require('./img/panda-bmcu370-16.webp').default} width="70%"/>

- Re-enter flashing mode by holding BOOT and pressing RESET once; release the BOOT button, then click “Download” and wait for the process to complete.

    <ImageView src={require('./img/panda-bmcu370-18.webp').default} width="70%"/>
