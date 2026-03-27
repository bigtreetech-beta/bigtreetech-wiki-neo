---
sidebar_position: 3
description: CB1 固件配置
---

# CB1 Firmware

## Config Network

### Use Network Cable

The Ethernet cable is plug-and-play and requires no additional setup.

### Use WiFi

Once the system image has been flashed, the Micro SD card will contain a FAT32 partition that is recognized by the computer. Within this partition, there is a configuration file named `system.cfg`.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/system.webp').default} width="60%"/>

Open it in Notepad, replace “WIFI-SSID” with your actual Wi-Fi name, and replace “PASSWORD” with your actual password.

Example: `WIFI_SSID="CB1 Tester"`

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/wifi.webp').default} width="60%"/>

## Overlays Settings

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

:::info

ssh software [mobaxterm](https://mobaxterm.mobatek.net/download-home-edition.html)

:::

Insert the Micro SD card (containing the installed operating system) into the motherboard and wait for the system to boot up. This takes 1–2 minutes. The ACT LED on the motherboard will flash continuously after a successful boot.

Once the device connects to Wi-Fi or an Ethernet cable, it will be automatically assigned an IP address.

Go to your router’s management interface to find the device’s IP address.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Router.webp').default} width="60%"/>

Alternatively, use [angryip](https://angryip.org) to scan all IP addresses on your network and locate the one named BTT-CB1.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/AngryIP.webp').default} width="60%"/>

Open the Mobaxterm software you have already installed, click “Session,” click ‘SSH’ in the pop-up window, enter the device's IP address in the “Remote host” field, and click “OK.”

:::note

Computers and devices must be on the same local area network

:::

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/MobaXterm_Login.webp').default} width="60%"/>

Enter your username and password to access the SSH terminal interface

```shell
login as: biqu
password: biqu
```

## Installing the System

### Downloading the System Image

:::info[CB1 系统]

CB1 System image [CB1/release](https://github.com/bigtreetech/CB1/releases)

:::

### Download and Install the Flashing Software

Insert the Micro SD card into your computer using a card reader.

Select the image file you downloaded to your computer.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Etcher_1.webp').default} width="600"/>

Select the Micro SD card you want to flash. Click `Flash`

:::warning

Flashing the image will format the microSD card.

:::

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Etcher_2.webp').default} width="600"/>

Wait for the Flash process to complete

<ImageView src={require('@site/docs/board-docs/iot-series/iot-cb1/img/Etcher_3.webp').default} width="600"/>
