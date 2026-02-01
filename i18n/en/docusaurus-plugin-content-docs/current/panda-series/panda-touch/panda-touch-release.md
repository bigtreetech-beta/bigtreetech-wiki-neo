---
sidebar_position: 4
---

# Panda Touch Firmware Release History

Panda Touch Firmware Release History

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

### [v1.0.7.3](https://github.com/bigtreetech/PandaTouch/releases/tag/release%2Fv1.0.7.3)

- Add firmware incompatibility warning

### [V1.0.7.1](https://github.com/bigtreetech/PandaTouch/blob/master/Firmware/1.0.7.1/panda_touch-v1.0.7.1.bin)

#### Bug Fixes

- **Panda Sense Issue**: Panda Sense temperature values occasionally fail to update
- **Part Skipping Unavailable**: Part skipping functionality is unavailable for certain print jobs
- **Reprint Functionality Anomaly**: Synchronized with Bambu Cloud's latest print request format (custom filaments not yet supported)
- **AMS Printing Anomaly**: Configurable AMS mapping (currently supports AMS-1 only; custom filaments not supported)
- **FTPS Thumbnails Missing for Other Directories**
- **SD Card File Year Information Missing**

#### Feature Enhancements
- **Increased thumbnail size**: When printing via Bambu Studio/Handy app, the home page thumbnail resolution has been increased from 128 × 128 to 280 × 306.
- **Real-time printer model updates in the background**: Printer models are synchronized in real-time from the cloud server.
- **Adjusted MQTT cache**: The MQTT buffer size has been adjusted to 40KB.

### [V1.0.7](https://github.com/bigtreetech/PandaTouch/blob/master/Firmware/1.0.7/panda_touch-v1.0.7.bin)

#### Bug Fixes

- **Fixed printer name synchronization issue**: Real-time retrieval of printer names from the server, updating them upon change.
- **Fixed axis direction error**: Resolved incorrect direction during Y-axis and Z-axis movements for controlling A1 and A1-mini.

#### New Features

- **Support for Part Skipping**: Allows users to select parts to skip during printing.
- **Support for Material Drying**: Enables users to dry materials on the P1S.  

### [V1.0.6.3](https://github.com/bigtreetech/PandaTouch/blob/master/Firmware/1.0.6.3/panda_touch-v1.0.6.3.bin)

#### Bug Fixes
- **Crash during printing**: Device crashes and reboots when printing from a USB drive.
- **Crash on OTA page**: Device crashes and reboots when tapping a Wi-Fi name on the OTA page.

#### Feature Changes
- **Stop loading thumbnails during printing**. 
