---
sidebar_position: 3
description: CB2 Firmware
---

# CB2 Firmware

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Flash System

### Download system image

:::info[CB2 System]

CB2 System image [CB2/releases](https://github.com/bigtreetech/CB2/releases)

:::

### Write system

<Tabs groupId="cb2-emmc-sd">
    <TabItem value="cb2-sd" label="Using SD Card" default>
        1. Download [balenaEtcher](https://www.balena.io/etcher/)

        2. Insert the microSD card into your computer using a card reader.

        3. Select the image file downloaded to your computer.

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System1.webp').default} width="60%"/>

        4. Select the Micro SD card you want to flash, then click "Flash"

            :::warning

            Flashing the image will format the microSD card

            :::

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System2.webp').default} width="60%"/>

        5. Wait for the write process to complete

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System3.webp').default} width="60%"/>
    </TabItem>
    <TabItem value="cb2-emmc" label="Using eMMC">
        :::info

        We can write the system to eMMC using either the `Computer (Windows) Flashing` or `SD Card Flashing` steps. Just choose a way that suits you.

        :::
        <Tabs groupId="emmc-write">
            <TabItem value="emmc-windows" label="Computer (Windows) Flashing" default>
                :::note

                Do not insert a Micro SD card into the device.

                :::

                1. Set DIP switches `USBOTG` and `RPIBOOT` to `ON` to enter BOOT mode (as shown in the example of Pad5 V2 in the figure below).

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/boot.webp').default} width="60%"/>

                2. Connect the USB OTG of the device to the computer

                    :::note

                    To avoid problems caused by insufficient USB power supply to the computer, it is best to use a USB Hub with external power supply, or use an external power source to power the device first

                    :::

                3. If a V3.0.1 or later version of the system has already been written into eMMC, the computer will recognize eMMC as a UMS device (USB Mass Storage device). Otherwise, it will be recognized as a LOADER device. UMS has the following advantages compared to LOADER:

                    1. We can directly modify the configuration in /boot/ partition

                    2. We can directly write the system image to eMMC like a Micro SD card

                    3. All content in eMMC can be erased through software

                4. If the device is identified as a UMS device, refer to the `UMS` steps below. If it is identified as a LOADER device, refer to the `LOADER` steps below.
                <Tabs groupId="device-mode">
                    <TabItem value="ums-mode" label="UMS" default>
                        Refer to the steps in `Write system`->`Using SD Card` and use balenaEtcher software to write the system
                    </TabItem>
                    <TabItem value="loader-mode" label="LOADER">
                        1. Download [RKDevTool](https://github.com/bigtreetech/CB2) to your computer and extract it. Make sure not to insert a MicroSD card.

                        2. Install the driver

                            1. If you see "Unknown Device" in "Device Manager," it means your computer is missing the driver

                                <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System5.webp').default} width="60%"/>

                            2. Open the Driver Assistant tool in the downloaded RKDevTool, click "Uninstall Drivers" first, then click "Install Drivers." This ensures that the drivers installed are the latest versions.

                                <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System6.webp').default} width="60%"/>

                            3. Once the installation is complete, hold down the "Recovery" button and unplug and reinsert the Type-C cable. "Device Manager" will recognize "Rockusb Device," indicating that the driver has been successfully installed.

                                <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System7.webp').default} width="60%"/>

                        3. Open RKDevTool

                            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System8.webp').default} width="60%"/>

                            :::info

                            The default settings in the software are shown in the figure. Under normal circumstances, you only need to set the actual path to the .img file. If the settings in your software differ from those shown in the figure, please manually adjust them to match.

                            :::

                            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System9.webp').default} width="60%"/>

                            1. Find the path where the downloaded RKDevTool is located.

                            2. Open the RKDevTool tool.

                            3. The software will detect a device named "LOADER" or "MASKROOM"

                            4. Select the system you want to flash (the system image must be extracted to an .img file beforehand; this tool does not support flashing compressed .xz files directly)

                            5. Check the "Write by Address" box

                            6. Click "Run" to begin flashing the system

                            7. `Download image OK` indicates that the system has been successfully flashed
                    </TabItem>
                </Tabs>
            </TabItem>
            <TabItem value="emmc-micro-sd" label="SD Card Flashing">
                1. Write the system onto the MicroSD card. Then, insert the MicroSD card into the motherboard's card slot and wait for the system to boot.

                2. Connect to the system terminal via Ethernet cable, WiFi, or USB to UART, and log in to the system.

                    ```shell title="biqu User"
                    Login: biqu
                    Password: biqu
                    ```

                3. Run `sudo nand-sata-install `, Select `2 Boot From eMMC - system on eMMC`, and then select `OK`

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System36.webp').default} width="60%"/>

                4. Select `Yes`, Start erasing and writing the system to eMMC

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System37.webp').default} width="60%"/>

                5. Select `1 ext4`, and then select `OK`

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System38.webp').default} width="60%"/>

                6. Wait for the write process to complete

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System39.webp').default} width="60%"/>

                7. After writing is completed, it will prompt whether to power off. Please select `Power off`.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System40.webp').default} width="60%"/>

                8. After power off, unplug the MicroSD card and turn it back on to start from eMMC.
            </TabItem>
        </Tabs>
    </TabItem>
    <TabItem value="cb2-nvme" label="Using NVMe">

        :::info

        NVMe boot is only supported on systems V3.0.2 and later versions

        RK3566 cannot boot directly from NVMe, so we need to first write u-boot (bootloader) to eMMC. After running u-boot (bootloader) from eMMC and detecting NVMe, it can jump to the NVMe boot system.

        :::

        1. Start the system from the SD card first.

        2. Erase the entire eMMC to prevent the system from booting from eMMC, as eMMC has a higher boot priority than NVMe.

            ```shell
            sudo mkfs /dev/mmcblk1
            ```

            And then enter "y" to confirm.

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System42.webp').default} width="60%"/>

        3. Write u-boot(bootloader) to eMMC

            ```shell
            sudo armbian-install
            ```

            And then select `Install/Update the bootloader on eMMC (/dev/mmcblk1)`

        4. Poweroff the system after writing is complete

            ```shell
            sudo poweroff
            ```

        5. Refer to the steps in `Write system`->`Using eMMC`->`Computer (Windows) Flashing`, connect the device to the computer, and the u-boot (bootloader) in eMMC will mount NVMe as UMS (USB Mass Storage) on the computer.

        6. Refer to the steps in `Write system`->`Using SD Card` and use balenaEtcher software to write the system
    </TabItem>
</Tabs>

### Erasing eMMC

:::info

If your hardware is the eMMC version and you have previously written the system into eMMC, but now you do not want to boot from eMMC but prefer to boot from a MicroSD card. We need to erase the system data previously written to eMMC to prevent the device from erroneously booting from eMMC.

:::

<Tabs groupId="emmc-write">
    <TabItem value="emmc-windows" label="Using Computer to Erase (Windows)" default>
        1. Refer to the steps in `Write system`->`Using eMMC`->`Computer (Windows) Flashing`, connect the device to the computer.

        2. If the device is identified as a UMS device, refer to the `UMS` steps below. If it is identified as a LOADER device, refer to the `LOADER` steps below.
        <Tabs groupId="device-mode">
            <TabItem value="ums-mode" label="UMS (Windows)" default>
                Install [SD Card Formatter](https://www.sdcard.org/downloads/formatter/) software to format UMS devices for eMMC.

                :::info

                Please do not directly use the formatting function provided by the Windows system, as it cannot completely erase the data in eMMC

                :::
            </TabItem>
            <TabItem value="loader-mode" label="LOADER">
                1. Refer to the steps in `Computer (Windows) Flashing`->`LOADER`, download RKDevTool, install the driver, identify the device as a LOADER device.

                2. Use RKDevTool software to erase data.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System41.webp').default} width="60%"/>

                    1. Find the path where the downloaded RKDevTool is located.

                    2. Open the RKDevTool.

                    3. The software will recognize a "LOADER" device. If it recognizes "MASKROOM," it indicates there is no data in the eMMC, hence no erase operation is necessary.

                    4. Click "Advanced Function."

                    5. Click "EraseAll" to begin erasing data from the eMMC.

                    6. "Erasing sectors success" indicates the erasure is complete.
            </TabItem>
        </Tabs>
    </TabItem>
    <TabItem value="emmc-micro-sd" label="Using Micro SD Card Erase">
        1. Refer to the steps in `Write system`->`Using eMMC`->`SD Card Flashing` to log into the system terminal.

        2. Run the following command to erase data

            ```shell
            sudo mkfs /dev/mmcblk1
            ```

            And then enter "y" to confirm.

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System42.webp').default} width="60%"/>
    </TabItem>
</Tabs>

## System Configuration

### Using an Ethernet Cable

The Ethernet cable is plug-and-play and requires no additional setup.

### Setting Up Wi-Fi

After the system image has been flashed, the MicroSD card will have a FAT32 partition recognized by your computer. Within this partition, there is a configuration file named "system.cfg." Open it and replace "Your SSID" with your actual Wi-Fi network name, and replace "Your Password" with your actual password.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System17.webp').default} width="60%"/>

### Config overlays

Open the `armbianEnv.txt` file in the BOOT partition and set the value for `overlays`. The configuration file supports only one `overlays` entry at a time. If multiple `overlays` configurations are specified, only the last one will take effect. If you need to enable multiple overlays, place the configuration entries on the same line after `overlays`, separating them with a space. For example, if you need to use a DSI display, an MCP2515 SPI-to-CAN module, and I2C1 simultaneously:

```systemd title="armbianEnv.txt"
overlays=dsi mcp2515 i2c1
```

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System18.webp').default} width="60%"/>

### Configuring the Display

1. Open the armbianEnv.txt file in the BOOT partition

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System19.webp').default} width="60%"/>

2. The default setting for "overlays" is HDMI, which means the system defaults to using an HDMI display. You can change this to the display you are actually using. The available options are as follows:

    :::info[overlays Config]

    hdmi: [HDMI](https://biqu.equipment/collections/lcd/products/bigtreetech-hdmi5-v1-0-hdmi7-v1-0)

    dsi: [DSI](https://biqu.equipment/collections/lcd/products/bigtreetech-pi-tft43-v2-0-screen-board)

    tft_35: [SPI Display](https://biqu.equipment/collections/lcd/products/bigtreetech-tft35-spi-v2-1-touchscreen-io2can-module)

    :::

    In addition, "tft_35" has a parameter called "tft35_spi_rotate" that controls screen rotation at the system level. The default value of "0" means no rotation; other available values include "90", "180", and "270".

    :::info

    You can only select one screen; you cannot use multiple screens at the same time.
    
    :::

3. Configure KlipperScreen by opening the `system.cfg` file in the BOOT partition and setting the screen type `ks_src` and rotation angle `ks_angle`.

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System20.webp').default} width="60%"/>

### Using SPI to CAN

Open the armbianEnv.txt file in the BOOT partition and add "mcp2515" to the overlays configuration.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System21.webp').default} width="60%"/>

### Using CSI Cameras and Configuring Crowsnest

Whether it's the OV5647 on the Raspberry Pi V1.3 or the IMX219 on the Raspberry Pi V2, there is no need to configure overlays in the armbianEnv.txt file; they are plug-and-play.

```systemd title="crowsnest.conf"
device: /dev/video0 # The node of CSI camera is fixed as `video0`

custom_flags: --format=UYVY # The current system CSI camera does not support the default `YUYV` and needs to be set to the supported `UYVY` format
```

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System22.webp').default} width="60%"/>

### Bluetooth

1. Scan for Bluetooth devices, enter the following command, and a list of Bluetooth devices will appear, as shown in the figure below

    ```shell
    bluetoothctl --timeout 15 scan on
    ```

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System23.webp').default} width="60%"/>

2. Locate your Bluetooth device—for example, my Bluetooth device is named “HONOR xSport PRO”—and find the corresponding Bluetooth MAC ID in the device list, as shown in the image below.

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System24.webp').default} width="60%"/>

3. Connect to a Bluetooth device by entering the following command. A successful connection is shown in the image below.

    ```shell
    bluetoothctl connect E0:9D:FA:50:CD:4F
    ```

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System25.webp').default} width="60%"/>

    1. If you see the output shown below, please turn off the Bluetooth device, then follow steps 1 and 2 again to reconnect it.

        <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System26.webp').default} width="60%"/>

    2. If the output looks like the image below, enter the following command, then repeat steps 1 and 2.

        ```shell
        bluetoothctl remove E0:9D:FA:50:CD:4F # bluetooth device mac address

        rfkill block bluetooth

        sleep 3s

        rfkill unblock bluetooth

        pulseaudio -k

        pulseaudio –start
        ```

        <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System27.webp').default} width="60%"/>

4. If the audio playback function is interrupted while using Bluetooth and Bluetooth cannot be used again, you will need to manually terminate the corresponding playback process. Use the `ps` command to view the process ID of the playback process, then use `kill -9 process_id` to terminate it. As shown in the figure below

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System28.webp').default} width="60%"/>

### Audio Output Settings

```shell
aplay -l
```

Check the corresponding sound card, as shown in the figure below: (As shown in the figure, the sound card associated with the headphone jack is Card 0).

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System29.webp').default} width="60%"/>

```shll
amixer -c 0 contents # 0 refers to the “card 0” identified by the `aplay -l` command mentioned above
```

View the playback and recording channel settings, as shown in the figure below:

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System30.webp').default} width="60%"/>

```shell
amixer -c 0 cset numid=1 3
```

Configure the playback channel as shown in the figure below:

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System31.webp').default} width="60%"/>

```shell
amixer -c 0 cset numid=2 1
```

Set the recording channel as shown in the figure below

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System32.webp').default} width="60%"/>

Enter the following command to play the audio file: Replace “xxx” with the directory containing the audio file and “xxxxx.wav” with the actual filename.

```shell
aplay -D plughw:0,0 /xxx/xxxxx.wav
```

Enter the following command to record audio (where 10 indicates a 10-second recording). The recording will be saved in the xxx directory with the filename xxxx.wav:

```shell
sudo arecord -Dhw:0,0 -d 10 -f cd -r 44100 -c 2 -t wav /xxx/xxxx.wav
```

Enter the following command to play the recording:

```shell
aplay -D plughw:0,0 /xxx/xxxx.wav
```

## SSH Connect

1. Install [Mobaxterm](https://mobaxterm.mobatek.net/download-home-edition.html)

2. After powering on, wait for the system to boot up, which takes about 1–2 minutes.

3. Once the device connects to Wi-Fi or an Ethernet cable, it will be automatically assigned an IP address.

4. Go to the router's management interface and locate the device’s IP address (which should be `BIGTREETECH-CB2`/`BTT-CB2`).

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System33.webp').default} width="60%"/>

5. Open the Mobaxterm software you have installed, click "Session" then click 'SSH' in the pop-up window. Enter the device's IP address in the "Remote host" field, and click "OK" (Note: Your computer and the device must be on the same local area network).

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System34.webp').default} width="60%"/>

6. Enter your username and password to access the SSH terminal interface

    ```shell title="root Admin"
    Login: root
    Password: root
    ```

    ```shell title="biqu User"
    Login: biqu
    Password: biqu
    ```

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb2/img/CB2_System35.webp').default} width="60%"/>

## Notes

Approximately 10 seconds after power-on, the system enters the kernel phase. At this point, the power LED remains lit, and the ACT LED flashes continuously, indicating that the system is operating normally.

### Interface Usage

- The PCIe M.2 interface does not support hot-swapping; the SSD must be installed beforehand for the device to be recognized.
- Do not insert a MicroSD card when booting from eMMC. When booting from a MicroSD card, the data on the eMMC must be erased.
