---
sidebar_position: 3
description: CB1 固件配置
---

# CB1 软件配置

## 配置网络

### 使用网线

网线即插即用，不需要额外的设置

### WiFi 设置

系统镜像烧录完成后，Micro SD 卡会有一个被电脑识别的 FAT32 分区，此分区下有个名为 `system.cfg` 的配置文件

<ImageView src={require("./img/system.webp").default} width="60%"/>

用记事本打开，将 WIFI-SSID 替换为实际的 WIFI 名称，PASSWORD 替换为实际的密码

例如: `WIFI_SSID="CB1 Tester"`

<ImageView src={require("./img/wifi.webp").default} width="60%"/>

## Overlays Settings

操作系统写入SD卡后，有一个名为 `BOOT` 的FAT32分区。`VSCode` 打开 `BoardEnv.txt` 文件。

<ImageView src={require("./img/BoardEnv.webp").default} width="60%"/>

根据需要进行设置，如下图所示。

<ImageView src={require("./img/overlays.webp").default} width="60%"/>

默认值为“console=display”，这意味着CB1的“UART0”默认用作调试端口。我们可以使用“MobaXterm”通过UART0连接到CB1并进行调试。如果klipper想要使用`UART0`来控制主板，我们需要将其设置为`console=serial`，现在klippe可以将`UART0'用作`/dev/ttyS0`。

CB1会自动识别HDMI分辨率，但如果您的HDMI屏幕无法正常通过EDID报告分辨率，我们可以通过取消注释extraargs=video来强制指定CB1输出的分辨率，并设置实际分辨率。
比如:

BTT-HDMI7 resolution = 1024x600: `extraargs=video=HDMI-A-1:1024x600-24@60`

BTT-HDMI5 resolution = 800x480: `extraargs=video=HDMI-A-1:800x480-24@60`

取消注释 `overlays=tft35_spi` 以启用tft35 spi屏幕。

取消注释 `overlays=mcp2515` 以启用mcp2515 spi到canbus模块。

取消注释 `overlays=tft35_spi mcp2515` 如果要同时使用tft35 spi屏幕和mcp2515 spi到can总线模块。

取消注释以下覆盖和参数以将 `spidev1.1` 释放到用户空间，并且 `spidev1.1` 不能与 TFT35_SPI 和 MCP2515 一起使用。

```systemd title="BoardEnv.txt"
overlays=spi-spidev
param_spidev_spi_bus=1
param_spidev_spi_cs=1
param_spidev_max_freq=1000000
```

:::note

TFT35 SPI和MCP2515多路复用一组SPI1

:::

```systemd title="BoardEnv.txt"
SPI1_CLK=PH6
SPI1_MISO=PH8
SPI1_MOSI=PH7
TFT35_SPI_CS=PC7
MCP2515_CS=PC11
MCP2515_IRQ=PC9
```

## SSH 连接

:::info

ssh 软件 [mobaxterm](https://mobaxterm.mobatek.net/download-home-edition.html)

:::

将Micro SD卡（已安装的操作系统）插入主板，等待系统通电后加载。1-2分钟。主板上的ACT LED在成功启动后会持续闪烁。

设备连上 WIFI 或者插上网线后，会被自动分配一个 IP

进入路由器管理界面找到设备的 IP

<ImageView src={require("./img/Router.webp").default} width="60%"/>

或者使用 [angryip](https://angryip.org)，扫描当前网络中的所有IP地址，找到名为 BTT-CB1 的IP。

<ImageView src={require("./img/AngryIP.webp").default} width="60%"/>

打开已经安装的 Mobaxterm 软件，点击“Session”，在弹出的窗口中点击“SSH”，在Remote host 一栏中输入设备的 IP 地址，点击“OK”（

:::note

电脑和设备必须要在同一个局域网下

:::

<ImageView src={require("./img/MobaXterm_Login.webp").default} width="60%"/>

输入登录名和登录密码进入 SSH 终端界面

```shell
login as: biqu
password: biqu
```

## 写入系统

### 下载系统镜像

:::info[CB1 系统]

CB1 系统镜像 [CB1/release](https://github.com/bigtreetech/CB1/releases)

:::

### 下载并安装烧录软件

将 Micro SD 卡通过读卡器插入到电脑。

选择下载到电脑中的镜像

<ImageView src={require("./img/Etcher_1.webp").default} width="600"/>

选择待烧录的 Micro SD 卡。点击 `Flash`

:::warning

烧录镜像会将 Micro SD 卡格式化。

:::

<ImageView src={require("./img/Etcher_2.webp").default} width="600"/>

等待烧录完成

<ImageView src={require("./img/Etcher_3.webp").default} width="600"/>
