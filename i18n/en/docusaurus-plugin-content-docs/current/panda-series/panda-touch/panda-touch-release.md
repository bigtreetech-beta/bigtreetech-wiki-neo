---
sidebar_position: 4
---

# Panda Touch Firmware Release History

Panda Touch Firmware Release History

### [V1.0.8.0](https://github.com/bigtreetech/PandaTouch/releases/tag/release%2Fv1.0.8.0)

#### Bug Fixes

- **Sleep / Wake Reboot Issue**: Fixed repeated reboot issues caused by sleep / wake crashes.
- **Wake / Print Start Reboot Issue**: Fixed frequent short-cycle reboot issues and reboot loops after wake or print start.
- **OTA IMG Update Issue**: Added validation to the OTA IMG update process and improved update stability.
- **AMS2 / AMS-HT Detection Issue**: Fixed AMS2 / AMS-HT search and detection logic.
- **External Spool Loading Issue**: Fixed external spool holder loading logic to ensure feed / unload operations work correctly.
- **External Spool Refresh and AMS Slot Mapping Issue**: Fixed external spool refresh and AMS slot mapping issues to ensure slot status is displayed correctly.
- **Wi-Fi Compatibility Issue**: Improved WPA2 / WPA3 Wi-Fi compatibility.
- **Cloud Account Login Reboot Issue**: Fixed a device reboot issue that could occur when logging in to a Bambu Lab cloud account.

#### Functional Optimizations

- **Print Wake Behavior**: Optimized print wake behavior so the device stays awake while a print task is running.
- **Firmware Warning Flow**: Redesigned the firmware warning flow to make the recovery path clearer.
- **Firmware Update Warning Prompts**: Optimized warning prompts during firmware updates.
- **AMS Interface**: Redesigned the AMS interface with clearer slot layout and status display.
- **Filament Management Interface**: Refactored the filament management interface and related filament management logic.
- **Printer / Group List View Modes**: Added printer and group list view modes.
- **Feed / Unload Operation Flow**: Optimized step prompts in the feed / unload operation flow.
- **Warning Popups**: Optimized warning popups.
- **Screen Saver Mode**: Added a screen saver mode during printing to help prevent accidental operation while a print is running.
- **File Manager Interface**: Refactored the file manager interface and improved file management logic and thumbnail display logic.
- **Notification Prompts**: Updated notification prompts and added new notification message content.

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

- **Increased thumbnail size**: When printing via Bambu Studio/Handy app, the home page thumbnail resolution has been increased from 128 x 128 to 280 x 306.
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
