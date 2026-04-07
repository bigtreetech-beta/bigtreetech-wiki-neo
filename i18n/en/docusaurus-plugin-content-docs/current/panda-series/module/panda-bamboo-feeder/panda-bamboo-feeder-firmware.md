---
sidebar_position: 3
description: Panda Bamboo Feeder Firmware
---

# Panda Bamboo Feeder Firmware Config

## Initial Setup

:::info[Note]

In Follower or Leader mode, you only need to bind the printer to the Leader unit. Before binding, ensure the Leader has completed its network setup.

:::

### Network Configuration

- When the network is not configured, the screen will display the Hotspot name "XXXXXXXXXXXXPanda_Bamboo_Feeder"

    <ImageView src={require('./img/ap-name.webp').default} width="256"/>

- Connect to this Hotspot using a smartphone or computer. Default password: `987654321`

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/ap-select.webp').default} width="256"/>

- If the Web UI does not open automatically after connecting, manually enter `http://192.168.254.1/` in your browser.

- Select Language.

    <ImageView src={require('./img/select-lang.webp').default} width="256"/>

- After scanning for WiFi, select the desired network, enter the WiFi password, and tap Connect.

    <ImageView src={require('./img/ap-connect.webp').default} width="256"/>

### Binding the Printer

- Tap Scan, enter the Access Code, and tap Bind.

    <ImageView src={require('./img/bind-printer.webp').default} width="256"/>

- Once bound successfully, the printer name will appear on the display.

    <ImageView src={require('./img/printer-name.webp').default} width="256"/>

## Operation Modes

Long-press the Retract button to enter the mode selection interface. Use the Retract button to toggle options and the Load button to confirm.

<ImageView src={require('./img/select-mode.webp').default} width="256"/>

### Independent Mode

In this mode, a single Panda Bamboo Feeder is used with an additional spool connected through the "Ext" labeled inlet on the filament hub.

### Follower/Leader Mode

#### Follower

In this mode, the unit works with a unit set to "Leader" mode. The Leader unit manages the printer binding.

#### Leader

In this mode, the unit works in conjunction with one or two Follower units. The Leader unit is responsible for binding with the printer.

## Leader Follower Binding

### How to Bind to a Leader

- Using at least two Panda Bamboo Feeders, set one as Leader and the other as Follower.

- On the Follower unit, long-press the Load button to enter Binding state.

    <ImageView src={require('./img/follower-binding.webp').default} width="256"/>

- When the Leader unit receives the binding request, press Yes.

    <ImageView src={require('./img/leader-bind-remind.webp').default} width="256"/>

### Unbinding

#### Leader

- Long-press the Load button to enter the unbinding interface, then select the Follower you wish to unbind.

    <ImageView src={require('./img/unbind-follower-step1.webp').default} width="256"/>

- Confirm unbinding.

    <ImageView src={require('./img/unbind-follower-step2.webp').default} width="256"/>

#### Follower

- Long-press the Load button to enter the unbinding interface and confirm unbinding.

    <ImageView src={require('./img/unbind-leader.webp').default} width="256"/>

## Factory Reset

- Long-press the Retract button for approximately 8 seconds to perform a factory reset.

    <ImageView src={require('./img/factory.webp').default} width="256"/>

## Status Display

### Sensor Status

The display features on-screen status circles on the right side that indicate the trigger status of each sensor.

- Filament Hub Sensor

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/sensor-5way.webp').default} width="70"/>

- Outlet 2

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/sensor-out2.webp').default} width="70"/>

    - Triggered when the buffer is full.

- Outlet 1

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/sensor-out1.webp').default} width="70"/>

- Inlet 2

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/sensor-in2.webp').default} width="70"/>

    - In "Waiting" status, feeding stops when this sensor is triggered.

- Inlet 1

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/sensor-in1.webp').default} width="70"/>

    - When this sensor changes from triggered to untriggered, the system enters "Filament Runout" status.

    - When it changes from untriggered to triggered, the system enters "Waiting" or "Loading" status.

### Operation Status or Alerts

Displays current operation status such as Loading, Unloading, Waiting, Filament Runout, etc., as well as alert messages when applicable.

<ImageView src={require('./img/running-status.webp').default} width="256"/>

### Working Status or Mode

Displays the current device status or active work mode.

<ImageView src={require('./img/work-follower.webp').default} width="256"/>

## Parameter Configuration

- Printer Type

    Select between Bambu Lab or Klipper printers.

- Buzzer Switch

    When disabled, the buzzer will not sound during alerts.

- Pressure Level

    The feeding pressure value determines the positive pressure applied by the Panda Bamboo Feeder to the filament. Use the "Auto-Calibration" button to automatically determine the appropriate level. If the auto-calibrated value is insufficient for reliable filament refilling, manually adjust to a higher pressure.

    When printing softer materials like TPU, we recommend recalibrating the Pressure Level or manually decreasing the pressure value.

    The system supports TPU with a shore hardness as low as 60A, which helps mitigate jamming and breakage issues common with flexible filaments. Please note that the actual compatible hardness depends on your specific filament path; the more complex the routing, the lower the success rate for ultra-soft materials.

- Hostname

    Enter `http://pandabamboofeeder.local` in your browser to access the Web UI.

- Hotspot Name

    The hotspot name can be modified via the Web UI.

## Calibration

Resistance exists within the filament feeding path. If this resistance exceeds the currently set calibration level, the filament may jam. Calibration should be performed whenever switching filaments or replacing PTFE tubes.

:::info[Note]

Excessive pressure may cause brittle materials to break in the filament path or cause soft materials to buckle. Please exercise caution when manually setting feeding pressure values.

:::

### Calibration Modes

- Quick Calibration: Performed by the Leader unit. Upon completion, all pressure levels are set to the same value.

- Calibrate All: The Leader and Follower units are calibrated separately. Upon completion, pressure levels are independent of each other.

### Starting Calibration

- Open the Settings page.

- Tap Auto-Calibration.

    <ImageView src={require('./img/auto-calibration.webp').default} width="256"/>

- Tap Start Calibration.

    <ImageView src={require('./img/start-calibration.webp').default} width="256"/>

## Klipper Configuration

Automatic Loading or Unloading Filament via Custom Macros

- Download the configuration file [feeder.cfg](https://github.com/bigtreetech/Panda_Bamboo_Feeder/blob/master/klipper/feeder.cfg)

- Upload and add it to printer.cfg.

    ```systemd title="printer.cfg"
    [include feeder.cfg]
    ```

## Troubleshooting

#### Q: Filament jammed in PTFE tube, not reaching the extruder

- Excessive resistance in the tube.

    - Use the PTFE tubes provided with the machine or by Panda Bamboo Feeder. Keep tubes as short as possible. Ensure the entire filament path has smooth curvature without sharp bends or kinks. Excessive resistance may exceed the maximum positive pressure provided by the Panda Bamboo Feeder.

    - Use the reserved mounting points on the filament hub to secure it, but ensure the PTFE tube (connecting to the printer) has a clean, flat cut and is fully inserted into the quick connector. Avoid bending the PTFE tube near the connector.

- Attempt to manually set a higher pressure level.

#### Q: The filament hub sensor is triggered with filament present, but filament is stuck inside the filament hub

- The filament hub sensor may be damaged, leading to false reports. Check the following statuses on the screen:

    - After removing the filament hub, the screen should only show 4 sensor circles.

    - When the filament hub is connected but empty, the screen should show it as untriggered.

    - When the filament hub contains filament, the screen should show it as triggered.

    - When the external channel contains filament inserted to the correct depth, the screen should show it as triggered.

- Possible wear at the outlet end of the filament hub (the inlet end of the printer's own PTFE tube).

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/ptfe-broken.webp').default} width="256"/>


## Firmware

### Feature Requests

If you have feature requests for future Panda Bamboo Feeder firmware releases, please submit a request on the [official Panda Bamboo Feeder GitHub repository](https://github.com/bigtreetech/Panda_Bamboo_Feeder/issues).

### OTA (Over-The-Air)

- [Download](./panda-bamboo-feeder-release.md) the Latest Firmware

- Access via Smartphone or Computer Browser

    - Connect to the Panda Bamboo Feeder's AP (Default: xxxxxxxxxxxxPanda_Bamboo_Feeder). Enter the address `http://192.168.254.1` in your browser.

    - If the unit is already connected to a router (Example IP: 192.168.3.161). Enter the IP address shown on the screen (e.g., `http://192.168.3.161`) in your browser.

- Navigate to the Settings Page

    - Tap to select the `.bin` file.

        <ImageView src={require('./img/select-bin.webp').default} width="256"/>

    - Update Successful.

        <ImageView src={require('./img/update_ok.webp').default} width="256"/>

### flash_download_tool (Type-C Wired Flash)

:::info[Note]

The Panda Bamboo Feeder is designed for OTA updates. This step should only be used if OTA is unavailable.

:::

- If your computer lacks the CH340 driver, please download and install it first: [CH341SER.EXE](https://www.wch-ic.com/downloads/CH341SER_EXE.html)

- Download [Flash Download Tool](https://www.espressif.com/en/support/download/other-tools)

    <ImageView src={require('./img/download_esp_tool.webp').default} width="70%"/>

- Download the [Panda Bamboo Feeder Flashable Firmware](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/recovery_tool/flash)

- Connect the Panda Bamboo Feeder to your computer via `Type-C`. A new COM port should appear in the Device Manager.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/typec.webp').default} width="35%"/>

- Open `flash_download_tool_3.x.x.exe`and configure as follows in the popup:

    ChipType: `ESP32-S3`

    WorkMode: `Develop`

    LoadMode: `UART`

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/download.webp').default} width="200"/>

- Configure the flashing software as shown below:

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/esp_tool_config.webp').default} width="400"/>

    1. Set the flashing address for the .bin file and ensure the checkbox is ticked:

        - Flash `panda_bamboo_feeder_flash.bin` at address `0x0000`

    2. Set the COM port to the actual port (check `Device Manager` -> `Ports`). We recommend a Baud rate of `460800`

    3. Click `START` to begin flashing. Once complete, power cycle the device.
