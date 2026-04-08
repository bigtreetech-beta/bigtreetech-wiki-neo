---
sidebar_position: 3
description: CB1 Firmware
---

# CB1 Firmware

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Flash System

### Download system image

:::info[CB1 System]

CB1 System image [CB1/release](https://github.com/bigtreetech/CB1/releases)

:::

### Write system

<Tabs groupId="cb1-emmc-sd">
    <TabItem value="cb1-sd" label="Using SD Card" default>
        1. Download [balenaEtcher](https://www.balena.io/etcher/)

        2. Insert the microSD card into your computer using a card reader.

        3. Select the image file downloaded to your computer.

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Etcher_1.webp').default} width="600"/>

        4. Select the Micro SD card you want to flash, then click "Flash"

            :::warning

            Flashing the image will format the microSD card

            :::

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Etcher_2.webp').default} width="600"/>

        5. Wait for the burn process to complete

            <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Etcher_3.webp').default} width="600"/>
    </TabItem>
    <TabItem value="cb1-emmc" label="Using eMMC">
        :::info

        We can write the system to eMMC using either the `balanaEtcher Flashing` or `SD Card Flashing` steps. Just choose a way that suits you.

        :::
        <Tabs groupId="emmc-usage">
            <TabItem value="emmc-balena-etcher" label="balenaEtcher Flashing" default>
                1. Download [sunxi-fel tool](https://github.com/bigtreetech/sunxi-tools)(don't support Mac OS yet) and [CB1 eMMC uboot](https://github.com/bigtreetech/sunxi-tools/raw/master/u-boot-sunxi-cb1-emmc.bin) to the same path on the computer.

                2. Set DIP switches `nRPIBOOT`，`USB_OTG` to `ON` to enter BOOT mode(As shown in the figure below, taking Pad5 V2 as an example)

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/boot.webp').default} width="60%"/>

                3. Connect the USB OTG of the device to the computer

                    :::note

                    To avoid problems caused by insufficient USB power supply to the computer, it is best to use a USB Hub with external power supply, or use an external power source to power the device first

                    :::

                4. Linux systems have built-in drivers, while Windows systems require additional driver installation. Please refer to the [AllWinner official instructions](https://linux-sunxi.org/FEL/USBBoot)

                    1. Download [Zadig](https://zadig.akeo.ie/)

                    2. Enable `Options->List All Devices`

                        <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/zadig1.webp').default} width="60%"/>

                    3. Select CB1 USB device, mostly displayed as `unknown device`，the USB ID is `1F3A:EFE8`. After ensuring it's the correct USB device, click `Install Driver`

                        <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/zadig2.webp').default} width="60%"/>

                5. Open `PowerShell (Windows)` or `console terminal (Linux)` in the path of the downloaded sunxi-fel tool`

                6. Run the following command to check if USB communication is working properly.

                    <Tabs groupId="system">
                        <TabItem value="windows" label="Windows system" default>
                            ```shell
                            .\sunxi-fel.exe -v ver
                            ```
                        </TabItem>
                        <TabItem value="linux-armhf" label="linux-armhf system">
                            ``` shell
                            sudo ./sunxi-fel-armhf -v ver
                            ```
                        </TabItem>
                        <TabItem value="linux-aarch64" label="linux-aarch64 system">
                            ``` shell
                            sudo ./sunxi-fel-aarch64 -v ver
                            ```
                        </TabItem>
                    </Tabs>

                    If prompted `ERROR: Allwinner USB FEL device not found!` means that did not recognize the correct USB, please recheck if the connection and driver are installed properly.

                    If prompted `AWUSBFEX soc=00001823(H616)` means that the CB1 has been recognized normally.

                    As shown in the figure below, the result of the first command is that CB1 is not inserted, and the result of the second command is that CB1 is recognized normally.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/cb1.webp').default} width="60%"/>

                7. Run the following command to write u-boot to CB1.

                    <Tabs groupId="system">
                        <TabItem value="windows" label="Windows system" default>
                            ```shell
                            .\sunxi-fel.exe uboot .\u-boot-sunxi-cb1-emmc.bin
                            ```
                        </TabItem>
                        <TabItem value="linux-armhf" label="linux-armhf system">
                            ``` shell
                            sudo ./sunxi-fel-armhf uboot ./u-boot-sunxi-cb1-emmc.bin
                            ```
                        </TabItem>
                        <TabItem value="linux-aarch64" label="linux-aarch64 system">
                            ``` shell
                            sudo ./sunxi-fel-aarch64 uboot ./u-boot-sunxi-cb1-emmc.bin
                            ```
                        </TabItem>
                    </Tabs>

                    After u-boot writing is completed, eMMC will be mounted as a USB drive on the computer.

                8. Use balenaEtcher software to write the system image, following the same steps as writing to a MicroSD card.

                    After the CB1 eMMC version is written, additional configuration modifications are required. Open the configuration file `/BOOT/armbianEnv.txt` (or `/BOOT/BoardEnv.txt` for older versions), and change the `fdtfile` configuration from the default SD version to the eMMC version:

                    ```shell
                    fdtfile=sun50i-h616-bigtreetech-cb1-emmc.dtb
                    ```

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/emmc.webp').default} width="60%"/>

                9. After the configuration is completed, save and power off, and then turn the `nRPIBOOT` and `USB-OTG` of the dip switch back to `OFF`. After powering on again, enter normal working mode.
            </TabItem>
            <TabItem value="emmc-micro-sd" label="SD Card Flashing">
                1. Write the system onto the MicroSD card. Then, insert the MicroSD card into the motherboard's card slot and wait for the system to boot.

                2. Connect to the system terminal via Ethernet cable, WiFi, or USB to UART, and log in to the system.

                    ```shell title="biqu User"
                    Login: biqu
                    Password: biqu
                    ```

                3. The configuration of CB1 eMMC version is different from that without eMMC version, so we need to modify the configuration first before writing the system from SD card to eMMC.

                    Open the configuration file `/BOOT/armbianEnv.txt` (or `/BOOT/BoardEnv.txt` for older versions), and change the `fdtfile` configuration from the default SD version to the eMMC version:

                    ```shell
                    fdtfile=sun50i-h616-bigtreetech-cb1-emmc.dtb
                    ```

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/emmc.webp').default} width="60%"/>

                4. After configuration is complete, save and execute the command to write the system to eMMC.

                    :::info

                    Note that after changing the `fdtfile` configuration in the SD card to eMMC, restarting it again will not start unless the configuration is changed back to the SD configuration. So after modifying the configuration, please immediately write the modified system into eMMC.

                    :::

                5. Run `sudo nand-sata-install `, Select `2 Boot From eMMC - system on eMMC`, and then select `OK`

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/ok.webp').default} width="60%"/>

                6. Select `Yes`, Start erasing and writing the system to eMMC

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/yes.webp').default} width="60%"/>

                7. Select `1 ext4`, and then select `OK`

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/ext4.webp').default} width="60%"/>

                8. Wait for the write process to complete

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/wait.webp').default} width="60%"/>

                9. After writing is completed, it will prompt whether to power off. Please select `Power off`.

                    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/off.webp').default} width="60%"/>

                10. After power off, unplug the MicroSD card and turn it back on to start from eMMC.
            </TabItem>
        </Tabs>
    </TabItem>
</Tabs>

## System Configuration

### Using an Ethernet Cable

The Ethernet cable is plug-and-play and requires no additional setup.

### Setting Up Wi-Fi

Once the system image has been flashed, the Micro SD card will contain a FAT32 partition that is recognized by the computer. Within this partition, there is a configuration file named `system.cfg`.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/system.webp').default} width="60%"/>

Open it in Notepad, replace “WIFI-SSID” with your actual Wi-Fi name, and replace “PASSWORD” with your actual password.

Example: `WIFI_SSID="CB1 Tester"`

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/wifi.webp').default} width="60%"/>

### Config overlays

After the operating system is written to the SD card, there will be a FAT32 partition named `BOOT`. Open the `BoardEnv.txt` file in `VSCode`.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/BoardEnv.webp').default} width="60%"/>

Configure the settings as needed, as shown in the figure below.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/overlays.webp').default} width="60%"/>

The default value is “console=display,” which means that CB1's ‘UART0’ is used as the debug port by default. We can use “MobaXterm” to connect to CB1 via UART0 and perform debugging. If Klipper needs to use `UART0` to control the motherboard, we need to set it to `console=serial`; now Klipper can use `UART0` as `/dev/ttyS0`.

CB1 automatically detects HDMI resolutions, but if your HDMI display cannot report its resolution correctly via EDID, we can force CB1 to output a specific resolution by uncommenting `extraargs=video` and setting the actual resolution.
For example:

BTT-HDMI7 resolution = 1024x600: `extraargs=video=HDMI-A-1:1024x600-24@60`

BTT-HDMI5 resolution = 800x480: `extraargs=video=HDMI-A-1:800x480-24@60`

Uncomment `overlays=tft35_spi` to enable the tft35 SPI display.

Uncomment `overlays=mcp2515` to enable the mcp2515 SPI-to-CAN bus module.

Uncomment `overlays=tft35_spi mcp2515` if you want to use both the TFT35 SPI screen and the mcp2515 SPI-to-CAN bus module simultaneously.

Uncomment the following overlays and parameters to release `spidev1.1` to user space; note that `spidev1.1` cannot be used in conjunction with TFT35_SPI and MCP2515.

```systemd title="BoardEnv.txt"
overlays=spi-spidev
param_spidev_spi_bus=1
param_spidev_spi_cs=1
param_spidev_max_freq=1000000
```

:::note

TFT35 SPI and MCP2515 multiplex a single SPI1 bus

:::

```systemd title="BoardEnv.txt"
SPI1_CLK=PH6
SPI1_MISO=PH8
SPI1_MOSI=PH7
TFT35_SPI_CS=PC7
MCP2515_CS=PC11
MCP2515_IRQ=PC9
```

## SSH Connect

1. Install [Mobaxterm](https://mobaxterm.mobatek.net/download-home-edition.html)

2. After powering on, wait for the system to boot up, which takes about 1–2 minutes.

3. Once the device connects to Wi-Fi or an Ethernet cable, it will be automatically assigned an IP address.

4. Go to the router's management interface and locate the device’s IP address (which should be `BIGTREETECH-CB1`/`BTT-CB1`).

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Router.webp').default} width="60%"/>

    Alternatively, use [angryip](https://angryip.org) to scan all IP addresses on your network and locate the one named `BIGTREETECH-CB1`/`BTT-CB1`.

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/AngryIP.webp').default} width="60%"/>

5. Open the Mobaxterm software you have already installed, click “Session,” click ‘SSH’ in the pop-up window, enter the device's IP address in the “Remote host” field, and click “OK.”

    :::note

    Computers and devices must be on the same local area network

    :::

    <ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/MobaXterm_Login.webp').default} width="60%"/>

6. Enter your username and password to access the SSH terminal interface

    ```shell title="root Admin"
    Login: root
    Password: root
    ```

    ```shell title="biqu User"
    Login: biqu
    Password: biqu
    ```
