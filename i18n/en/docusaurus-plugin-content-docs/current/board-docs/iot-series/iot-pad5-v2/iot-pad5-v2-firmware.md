---
sidebar_position: 3
description: Pad5 V2 Firmware Configuration
---

# Pad5 V2 Firmware

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Flashing the System

:::info

When using Pad5's USB OTG flash system to eMMC version hardware, please refer to the diagram below for the device's DIP switch. Turn the `nRPIBOOT` and `USB-OTG` to `ON` to enter BOOT mode. After the system is written, turn the switch back to `OFF` to start normally.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/boot.webp').default} width="60%"/>

:::

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi CM4/CM5" default>
        Download the appropriate system image based on your requirements, such as the [official Raspberry Pi image](https://www.raspberrypi.com/software/operating-systems) or the [Mainsail system image](https://github.com/mainsail-crew/MainsailOS/releases).

        :::info

        On eMMC versions, the system cannot boot from the Micro SD card. So we have to write the system into eMMC to run.

        :::
        <Tabs groupId="rpi-emmc-sd">
            <TabItem value="rpi-sd" label="SD Card Version" default>
                1. Download and install the official Raspberry Pi flashing tool from the Raspberry Pi website: https://www.raspberrypi.com/software/

                2. Insert the Micro SD card into your computer using a card reader.

                3. Set the device to `NO FILTERING`

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi1.webp').default} width="60%"/>

                4. Select the operating system.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi2.webp').default} width="60%"/>

                5. Choose `Use custom`, then select the system image file downloaded to your computer.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi3.webp').default} width="60%"/>

                6. Select the Micro SD card to be flashed, then click Next.

                    :::warning

                    Flashing the image will format the selected storage device, be careful not to select the wrong storage device.

                    :::

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi4.webp').default} width="60%"/>

                7. In the pop-up window, select `EDIT SETTINGS`.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi5.webp').default} width="60%"/>

                8. Under `General`, configure the following:

                    :::info

                    Set hostname: raspberrypi.local  // Set hostname. Default hostname: raspberrypi.local

                    Set username and password // Set username and password. Default username: pi Default password: raspberry

                    Configure wireless LAN // Set the Wi-Fi SSID and password.

                    :::

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi6.webp').default} width="60%"/>

                9. Under `Services`, configure the following:

                    :::info

                    Enable SSH

                    Use password authentication

                    :::

                    Then click `SAVE` to store the settings.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi7.webp').default} width="60%"/>

                10. Click `YES` to start flashing the system image.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi8.webp').default} width="60%"/>

                11. Wait for the flashing process to complete.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/pi9.webp').default} width="60%"/>
            </TabItem>
            <TabItem value="rpi-emmc" label="eMMC Version">
                1. Install the rpiboot Utility. Available in both [Windows](http://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) and [Mac/Linux](https://github.com/raspberrypi/usbboot#building) versions

                2. Set the nRPIBOOT and USB_OTG DIP switches to ON to enter BOOT mode.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/boot.webp').default} width="60%"/>

                3. Connect the USB OTG of the device to the computer. and run:
                    <Tabs groupId="system">
                        <TabItem value="linux" label="Mac/Linux" default>
                            ``` shell
                            sudo ./rpiboot
                            ```
                        </TabItem>
                        <TabItem value="windows" label="Windows">
                            ``` shell
                            rpiboot.exe
                            ```
                        </TabItem>
                    </Tabs>
                    Then the eMMC will then be recognized by the computer as a USB mass storage device (If rpiboot reports an error at this stage, try reconnecting the USB cable).

                    :::note

                    To avoid problems caused by insufficient USB power supply to the computer, it is best to use a USB Hub with external power supply, or use an external power source to power the device first

                    :::

                4. Use Raspberry Pi Imager to flash the system image; the procedure is the same as flashing to a Micro SD card.

                5. After flashing is complete, power off the device, switch nRPIBOOT and USB_OTG back to OFF, then power it on again to enter normal operating mode.
            </TabItem>
        </Tabs>
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        - [Refer to CB2 manual](../iot-cb2/iot-cb2-firmware)
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - [Refer to CB1 manual](../iot-cb1/iot-cb1-firmware)
    </TabItem>
</Tabs>

## System Configuration

### DSI Display

:::info

Set both 2-pin I2C DIP switches to ON; this enables the touch signal line for the DSI1 display interface.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/i2c.webp').default} width="60%"/>

:::

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi" default>
        1. Edit the `/boot/firmware/config.txt` file as follows. And restart the device after editing the configuration.

            <Tabs groupId="core-rpi">
                <TabItem value="cm5" label="CM5" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=vc4-kms-v3d
                    dtoverlay=vc4-kms-dsi-7inch
                    dtoverlay=edt-ft5406,i2c_csi_dsi
                    ```
                </TabItem>
                <TabItem value="cm4" label="CM4" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm4]
                    dtoverlay=vc4-kms-v3d
                    dtoverlay=vc4-kms-dsi-7inch
                    dtoverlay=edt-ft5406,i2c_csi_dsi0
                    ```
                </TabItem>
            </Tabs>

        2. At this point, both the built-in display and the external DSI display should function normally. However, touch input must be remapped when using multiple displays.

            1. On the display, open: `Preferences`->`Screen Configuration`

                <ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/dsi.webp').default} width="60%"/>

            2. Drag and arrange “DSI-1”, “DSI-2”, “HDMI-A-1” and “HDMI-A-2” as needed; the physical display layout will follow this arrangement, and the displays can also be fully overlapped to show identical content.

            3. Assign each touch device to its corresponding display so that, after configuration, each touch device controls only its assigned display.

            4. Apply the settings and click Apply for the configuration to take effect.
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        1. Add dsi to the `overlays` value in `/boot/armbianEnv.txt`. Separate multiple overlays with spaces.

            The system includes `hdmi` in the default configuration; to enable both screens, keep both hdmi and dsi, and to use only one screen, keep only the desired display configuration and remove the other.

            After restarting, the configuration will take effect. If both HDMI and external DSI displays are configured, both displays should show the same content. Important: The DSI touch I2C signal line on this device differs from the standard BIGTREETECH Pi2. The current system image does not yet support this touch signal, so touch functionality on the DSI display is currently unavailable.

        2. Touch input must be remapped for multi-display setups.

            1. Set the display:

                ``` shell
                export DISPLAY=:0.0
                ```

            2. Query display names:

                ``` shell
                xrandr -q
                ```

                Example output:

                ``` shell
                Screen 0: minimum 320 x 200, current 1600 x 480, maximum 16384 x 16384
                HDMI-1 connected primary 800x480+0+0 (normal left inverted right x axis y axis) 108mm x 62mm
                800x480       68.35*+  68.35
                640x480       60.00    59.94
                DSI-1 connected 800x480+800+0 (normal left inverted right x axis y axis) 0mm x 0mm
                800x480       56.06*+
                ```

                This indicates that HDMI-1 and DSI-1 are available.

            3. Query touch devices:

                ``` shell
                xinput list
                ```

                Example output:

                ``` shell
                BIQU BTT-HDMI5                     id=9    [slave  pointer  (2)]
                ```

                This indicates that the touch device BIQU BTT-HDMI5 with ID 9 is available.

            4. Run:

                ``` shell
                xinput map-to-output 9 HDMI-1
                ```

                This maps touch device ID 9 to the HDMI output. The CB2 supports mirrored dual-display output only, meaning the HDMI screen acts as the primary display while the DSI screen mirrors the HDMI output. Therefore, all touch devices should be mapped to HDMI.

            5. This command does not persist after reboot. Add it to a startup script if persistent mapping is required.
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 does not support this feature
    </TabItem>
</Tabs>

### CAM Camera

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi" default>
        1. Edit ` /boot/firmware/config.txt` as follows. And restart the device after editing the configuration. The OV5647 camera is used here as an example. If you are using a different camera model, replace the overlay with the appropriate one.

            <Tabs groupId="core-rpi">
                <TabItem value="cm5" label="CM5" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=ov5647,cam0
                    ```
                </TabItem>
                <TabItem value="cm4" label="CM4" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm4]
                    dtoverlay=ov5647
                    ```
                </TabItem>
            </Tabs>

        2. Testing the Camera

            List available cameras:

            ``` shell
            rpicam-hello --list-camera
            ```

            Set the display output:

            ``` shell
            export DISPLAY=:0.0
            ```

            Start the camera preview(do not run as root):

            ``` shell
            rpicam-hello --timeout 0 --camera 0
            ```

            For more detailed usage, refer to the Raspberry Pi Camera Software Documentation:
            https://www.raspberrypi.com/documentation/computers/camera_software.html
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        1. Add `csi ` to the `overlays` value in ` /boot/armbianEnv.txt `, separating multiple overlays with spaces, then restart the device; the current CB2 system image supports only the ` ov5647` and `imx219` CSI camera drivers, and the system will automatically detect the camera type, so no additional configuration is required.

        2. After booting, run:

            ``` shell
            dmesg | grep csi
            dmesg | grep ov5647
            dmesg | grep imx219
            ```

            Check whether the CSI camera has been detected correctly.
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 does not support this feature
    </TabItem>
</Tabs>

### RTC

:::info

The onboard RTC chip is `PCF8563`; a CR1220 coin cell battery must be installed for the RTC to continue operating when power is disconnected.

:::

<Tabs groupId="core-board">
    <TabItem value="rtc-rpi" label="Raspberry Pi" default>
        1. Edit `/boot/firmware/config.txt` as follows. And restart the device after editing the configuration.

            <Tabs groupId="core-rpi">
                <TabItem value="cm5" label="CM5" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtparam=i2c_vc=on
                    dtoverlay=i2c-rtc,pcf8563,i2c_csi_dsi0
                    ```
                </TabItem>
                <TabItem value="cm4" label="CM4" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm4]
                    dtparam=i2c_vc=on
                    dtoverlay=i2c-rtc,pcf8563,i2c_csi_dsi
                    ```
                </TabItem>
            </Tabs>

        2. After booting, run:

            ``` shell
            dmesg | grep rtc
            ```

            Check which RTC device number has been assigned; if pcf8563 is mounted as rtc0, use rtc0 in the following commands, and if it is mounted as rtc1, use rtc1 instead.

        3. RTC Test Example: Using rtc1 as an example.

            Write the system time to RTC:

            ``` shell
            sudo hwclock -w -f /dev/rtc1
            ```

            Set the system time from RTC:

            ``` shell
            sudo hwclock -s -f /dev/rtc1
            ```

            Read and display the RTC time:

            ``` shell
            sudo hwclock -r -f /dev/rtc1
            ```
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        1. Add `rtc_pcf8563` to the `overlays` value in `/boot/armbianEnv.txt`, separating multiple overlays with spaces, then restart the device.

        2. After booting, run:

            ``` shell
            dmesg | grep rtc
            ```

            Check which RTC device number has been assigned. If `pcf8563` is mounted as `rtc0`, use `rtc0` in the following commands. If it is mounted as `rtc1`, use `rtc1` instead.

        3. RTC Test Example: Using rtc0 as an example.
            Write the system time to RTC:

            ``` shell
            sudo hwclock -w -f /dev/rtc0
            ```

            Set the system time from RTC:

            ``` shell
            sudo hwclock -s -f /dev/rtc0
            ```

            Read and display the RTC time:

            ``` shell
            sudo hwclock -r -f /dev/rtc0
            ```
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 does not support this feature
    </TabItem>
</Tabs>

### CANBus

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi" default>
        1. Edit `/boot/firmware/config.txt` as follows; the same configuration applies to both CM5 and CM4.

            ``` systemd title="/boot/firmware/config.txt"
            [all]
            dtparam=spi=on
            dtoverlay=mcp2515-can0,oscillator=12000000,interrupt=24,spimaxfrequency=10000000
            ```

            Restart the device.

        2. After booting, run:

            ``` shell
            dmesg | grep -i '\(can\|spi\)'
            ```

            Check whether the MCP2515 has been initialized successfully; a normal response will look similar to:

            ``` shell
            [ 8.680446] CAN device driver interface
            [ 8.697558] mcp251x spi0.0 can0: MCP2515 successfully initialized.
            [ 9.482332] IPv6: ADDRCONF(NETDEV_CHANGE): can0: link becomes ready
            ```
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        - CB2 does not support this feature
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 does not support this feature
    </TabItem>
</Tabs>

## Notes

1. The onboard SPI-to-CAN controller uses pins from the 40-pin GPIO header, so it is not recommended to connect other devices to those same pins. SPI pins used:

    | Feature | Raspberry Pi | BIGTREETECH CB2            | BIGTREETECH CB1 | BIGTREETECH CB1 eMMC |
    | ------- | ------------ | -------------------------- | --------------- | -------------------- |
    | CS      | GPIO8        | GPIO4_A2(gpiochip4/gpio2)  | NC              | NC                   |
    | MISO    | GPIO9        | GPIO3_C2(gpiochip3/gpio18) | PH8(GPIO232)    | PH8(GPIO232)         |
    | MOSI    | GPIO10       | GPIO3_C1(gpiochip3/gpio17) | PH7(GPIO231)    | PH7(GPIO231)         |
    | SCK     | GPIO11       | GPIO3_C3(gpiochip3/gpio19) | PH6(GPIO230)    | PH6(GPIO230)         |
    | INT     | GPIO24       | GPIO4_A3(gpiochip4/gpio3)  | PC9(GPIO73)     | PI3(GPIO259)         |

2. On the Raspberry Pi CM5, both DSI and CSI can use the same pin output. Therefore, when using CM5, the onboard DSI and CAM (CSI) interfaces can be configured freely as either DSI or CSI. This means the board can be configured for either two DSI displays or two CSI cameras.
    <Tabs groupId="cm5-dphy">
        <TabItem value="cm5-dphy0" label="CAM(CSI) DPHY0 Port" default>
            <Tabs groupId="dphy0">
                <TabItem value="dphy0-dsi" label="Configure as a DSI display" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=vc4-kms-v3d
                    dtoverlay=vc4-kms-dsi-7inch,dsi0
                    dtoverlay=edt-ft5406,i2c_csi_dsi0
                    ```
                </TabItem>
                <TabItem value="dphy0-csi" label="Configure as a CSI camera">
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=ov5647,cam0
                    ```
                </TabItem>
            </Tabs>
        </TabItem>
        <TabItem value="cm5-dphy1" label="DSI DPHY1 Port">
            <Tabs groupId="dphy1">
                <TabItem value="dphy1-dsi" label="Configure as a DSI display" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=vc4-kms-v3d
                    dtoverlay=vc4-kms-dsi-7inch
                    dtoverlay=edt-ft5406,i2c_csi_dsi
                    ```
                </TabItem>
                <TabItem value="dphy1-csi" label="Configure as a CSI camera">
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=ov5647
                    ```
                </TabItem>
            </Tabs>
        </TabItem>
    </Tabs>

3. For Raspberry Pi CM4/CM5 eMMC versions, the system runs only from eMMC and does not support booting from a Micro SD card, whereas BIGTREETECH CB1/CB2 eMMC versions still support Micro SD card booting, with the Micro SD card having higher boot priority.
