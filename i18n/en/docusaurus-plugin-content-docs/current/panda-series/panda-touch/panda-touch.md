---
sidebar_position: 1
---

# Panda Touch

Panda Touch intro

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

:::warning[Known firmware compatibility issues]

Bambu Lab may release a firmware version in the future that affects the usable functionality of the Panda Touch. Bigtreetech will monitor all beta firmware versions and if we find a firmware version that affects the functionality of the Panda Touch, we will send an alert via email, Sizzle Chat, and our social channels. Purchasers can then decide if they want to risk losing functionality by performing the update. Please note that the Panda Touch warranty does not cover loss of functionality due to performing a Bambu Lab firmware update.

It is expected that some of the functions of the Panda Touch (e.g. initiating prints, controlling the motion system, adjusting the temperature, fan, AMS setup and calibration) will not be available due to the authorization and authentication mechanism in the new firmware recently announced by Bambu Lab (currently in beta for the X1 series), however, the ability to obtain printer status information such as print progress, nozzle temperature, hotbed temperature, etc. will not be affected. However, the ability to obtain printer status information such as print progress, nozzle temperature, thermal bed temperature, etc. is not affected, and you will still be able to utilize the full functionality of the Panda Touch by manually enabling Developer Mode in LAN Mode on printers with the new firmware.

https://bigtree-tech.com/blogs/news/announcement-on-bambu-lab-security-firmware-update 
https://blog.bambulab.com/firmware-update-introducing-new-authorization-control-system-2/ 
https://blog.bambulab.com/updates-and-third-party-integration-with-bambu-connect/

Panda Touch is currently compatible with all Bambu Lab printer firmware versions until.

P1P/S: 01.07.00.00

X1C: 01.08.02.00

X1E: 01.01.02.00

A1: 01.04.00.00

A1 Mini: 01.04.00.00

:::

:::warning[important information]

When the P1P or P1S is in LAN Only mode, all printer functions are available from the Panda Touch without connecting the Panda Touch to a cloud account.

When the printer is set to connect to the cloud, you will need to enable the Cloud Mode feature on the Panda Touch to retain the ability to control the heater and print functions.

Check the firmware listing in the product page description to ensure that your printer firmware is compatible with the Panda Touch. Updating the printer firmware to an incompatible version that may limit the functionality of the Panda Touch is not covered under warranty.

Currently, MicroSD card and USB drive files can only be read from the root directory and are only recognized when slicing the model to build plate #1 in Bambu Studio and the file is in 3mf format. Folder browsing and thumbnail previews will be available in a future firmware release.

When running on its internal lithium battery, Panda Touch has a battery life of approximately 20 to 30 minutes, depending on screen brightness. To maintain the battery and extend the life of the product, it is recommended that the Panda Touch be charged or powered off when the battery is depleted.

When the lithium battery is low, the screen may flicker. This flickering is normal and warns the user that the battery is almost depleted. The user should then immediately charge the battery or turn off the Panda Touch.

If you plan to turn the printer on and off frequently, we recommend that you run the Panda Touch in DC5V mode. this bypasses the battery and prevents it from going through multiple charge/discharge cycles. If you want to use battery power, simply switch the switch on the back of the 
Panda Touch to battery power mode.

The maximum supported USB drive capacity is 8GB.

:::

## Specifications

| Panda Touch | Specifications |
| -----| ---- | 
| Microprocessor | Xtensa 32-bit LX7 Dual-Core ESP32S3R8<br/> Clock speed up to 240MHz. | 
| Memory | PSRAM-8MB, Flash-16MB | 
| Screen Size | 5" | 
| Resolution | 800 x 480 | 
| Viewing Angle | IPS Full View | 
| Display Color | 16.7M | 
| Communication Mode | 2.4G Wi-Fi (IEEE 802.11 b/g/n) | 
| Operating Temperature | 0-60°C | 
| Operating Current (Fully Charged) | Screen Activated: 0.6A, Screen Inactivated: 0.2A | 
| Operating Current (Charging) | Screen Activated: 1.25A, (0.95A 2024 After May) Screen inactive: 0.85A | 
| Logic Voltage | 3.3V | 
| Built-in Battery | Allows up to 30 minutes of portable use of the Panda Touch. | 
| Charging time | 1.2 hours | 
| Expansion Interfaces | I2C (for temperature/humidity sensors that will be supported in future firmware, etc.)<br/>USB drive (for reading 3mf files from USB drive - FAT32 only) |
