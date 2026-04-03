---
sidebar_position: 3
description: CB1 软件配置
---

# CB1 软件配置

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 烧录系统

### 下载系统镜像

:::info[CB1 系统]

CB1 系统镜像 [CB1/release](https://github.com/bigtreetech/CB1/releases)

:::

### 写入系统

<Tabs groupId="cb1-emmc-sd">
    <TabItem value="cb1-sd" label="使用SD卡" default>
        1. 下载 [balenaEtcher](https://www.balena.io/etcher/)

        2. 将 Micro SD 卡通过读卡器插入到电脑。

        3. 选择下载到电脑中的镜像。

            <ImageView src={require('./img/Etcher_1.webp').default} width="600"/>

        4. 选择待烧录的 Micro SD 卡，点击“烧录”
        
            :::warning

            烧录镜像会将 Micro SD 卡格式化

            :::

            <ImageView src={require('./img/Etcher_2.webp').default} width="600"/>

        5. 等待烧录完成

            <ImageView src={require('./img/Etcher_3.webp').default} width="600"/>
    </TabItem>
    <TabItem value="cb1-emmc" label="使用eMMC">
        :::info

        使用 `balenaEtcher烧录` 或者 `MicroSD卡烧录` 步骤，均可正常的将系统烧录到eMMC中，任选一种适合您的方式即可。

        :::
        <Tabs groupId="emmc-usage">
            <TabItem value="emmc-balena-etcher" label="balenaEtcher烧录" default>
                1. 下载[sunxi-fel 工具](https://github.com/bigtreetech/sunxi-tools)(还不支持Mac OS)以及[CB1 eMMC uboot](https://github.com/bigtreetech/sunxi-tools/raw/master/u-boot-sunxi-cb1-emmc.bin)到电脑的相同路径中。

                2. 将拨码开关的`nRPIBOOT`，`USB_OTG`拨到 `ON` 进入BOOT模式(如下图以 Pad5 V2 为例)

                    <ImageView src={require('./img/boot.webp').default} width="60%"/>

                3. 将设备的 USB OTG 连接到电脑上

                    :::note

                    为了避免出现电脑 USB 供电不足导致的问题，最好使用带有外部供电的 USB-Hub，或者先使用外部的电源给设备供电

                    :::

                4. Linux系统内置了驱动，Windows系统需要额外安装驱动，可以参考[AllWinner官方说明](https://linux-sunxi.org/FEL/USBBoot)

                    1. 下载[Zadig](https://zadig.akeo.ie/)

                    2. 使能 `Options->List All Devices`

                        <ImageView src={require('./img/zadig1.webp').default} width="60%"/>

                    3. 选择CB1的USB设备，大多时候显示为 `unknown 未知的设备`，设备的USB ID为`1F3A:EFE8`。确保选择了正确的USB设备后，点击`Install Driver`安装驱动

                        <ImageView src={require('./img/zadig2.webp').default} width="60%"/>

                5. 在下载的sunxi-fel工具的路径下，打开`Powershell(windows)` 或者 `console terminal(linux)`

                6. 运行以下命令检查USB通信是否正常。

                    <Tabs groupId="system">
                        <TabItem value="windows" label="Windows系统" default>
                            ```shell
                            .\sunxi-fel.exe -v ver
                            ```
                        </TabItem>
                        <TabItem value="linux-armhf" label="linux-armhf系统">
                            ``` shell
                            sudo ./sunxi-fel-armhf -v ver
                            ```
                        </TabItem>
                        <TabItem value="linux-aarch64" label="linux-aarch64系统">
                            ``` shell
                            sudo ./sunxi-fel-aarch64 -v ver
                            ```
                        </TabItem>
                    </Tabs>

                    如果显示 `ERROR: Allwinner USB FEL device not found!` 代表未识别到正确的USB，请重新检查连接和驱动是否正常安装。

                    如果显示 `AWUSBFEX soc=00001823(H616)` 代表正常识别到CB1设备了。

                    如下图所示，第一个命令的结果是未插入CB1设备，第二个命令的结果是正常识别到了CB1。

                    <ImageView src={require('./img/cb1.webp').default} width="60%"/>

                7. 运行以下命令，将u-boot写入到CB1中。

                    <Tabs groupId="system">
                        <TabItem value="windows" label="Windows系统" default>
                            ```shell
                            .\sunxi-fel.exe uboot .\u-boot-sunxi-cb1-emmc.bin
                            ```
                        </TabItem>
                        <TabItem value="linux-armhf" label="linux-armhf 系统">
                            ``` shell
                            sudo ./sunxi-fel-armhf uboot ./u-boot-sunxi-cb1-emmc.bin
                            ```
                        </TabItem>
                        <TabItem value="linux-aarch64" label="linux-aarch64 系统">
                            ``` shell
                            sudo ./sunxi-fel-aarch64 uboot ./u-boot-sunxi-cb1-emmc.bin
                            ```
                        </TabItem>
                    </Tabs>

                    当u-boot写入完成后，会将eMMC挂载为一个U盘到电脑上。

                8. 使用balenaEtcher软件烧录系统镜像，步骤与烧录到Micro SD卡完全相同。

                    CB1 eMMC版本烧录完成后，还需要额外修改配置。打开配置文件 `/BOOT/armbianEnv.txt`(或者旧版本系统为`/BOOT/BoardEnv.xt`)，将 fdtfile 由默认的 sd 版本配置修改为 emmc 版本：

                    ```shell
                    fdtfile=sun50i-h616-bigtreetech-cb1-emmc.dtb
                    ```

                    <ImageView src={require('./img/emmc.webp').default} width="60%"/>

                9. 配置完成后，保存并断电后将拨码开关的 `nRPIBOOT`, `USB_OTG` 拨回到 `OFF`，重新上电后进入正常工作模式。
            </TabItem>
            <TabItem value="emmc-micro-sd" label="MicroSD卡烧录">
                1. 先将系统烧录到MicroSD卡中，然后将MicroSD卡插到主板的卡槽，然后等待系统启动。

                2. 通过网线，WiFi或者USB转UART连接到系统的终端，登录系统

                    ```shell title="biqu 普通用户"
                    Login: biqu
                    Password: biqu
                    ```

                3. CB1 eMMC版本的配置与不带 eMMC版本的不同，所以我们需要先修改配置后，再将系统从SD卡写入到eMMC中。

                    打开配置文件 `/BOOT/armbianEnv.txt`(或者旧版本系统为`/BOOT/BoardEnv.txt`)，将 fdtfile 由默认的 sd 版本配置修改为 emmc 版本：

                    ```shell
                    fdtfile=sun50i-h616-bigtreetech-cb1-emmc.dtb
                    ```

                    <ImageView src={require('./img/emmc.webp').default} width="60%"/>

                4. 配置完成后，保存并执行命令将系统写入到eMMC中。

                    :::warning

                    SD卡中的系统配置修改为eMMC后，再次重启是无法启动的，除非将配置修改回 sd 的配置。所以修改完成配置后，请立刻将修改后的系统写入到 eMMC 中。

                    :::

                5. 运行 `sudo nand-sata-install `命令，在弹出的界面中，选择 `2 Boot From eMMC - system on eMMC`, 然后选择 `OK`

                    <ImageView src={require('./img/ok.webp').default} width="60%"/>

                6. 选择 `Yes`，开始擦除并烧录系统到eMMC

                    <ImageView src={require('./img/yes.webp').default} width="60%"/>

                7. 选择文件系统为 `1 ext4`，然后选择 `OK`

                    <ImageView src={require('./img/ext4.webp').default} width="60%"/>

                8. 等待烧录完成

                    <ImageView src={require('./img/wait.webp').default} width="60%"/>

                9. 烧录完成后会弹窗提示是否关机，选择`Power off`关机

                    <ImageView src={require('./img/off.webp').default} width="60%"/>

                10. 关机后断电，然后拔出MicroSD卡，重新再通电即可从eMMC启动
            </TabItem>
        </Tabs>
    </TabItem>
</Tabs>

## 系统配置

### 使用网线

网线即插即用，不需要额外的设置

### 设置 WiFi

系统镜像烧录完成后，MicroSD 卡会有一个被电脑识别的 FAT32 分区，此分区下有个名为"system.cfg" 的配置文件

<ImageView src={require('./img/system.webp').default} width="60%"/>

打开后将 Your SSID 替换为实际的 WIFI 名称，Your Password 替换为实际的密码

例如: `WIFI_SSID="CB1 Tester"`

<ImageView src={require('./img/wifi.webp').default} width="60%"/>

### 配置 overlays

操作系统写入SD卡后，有一个名为 `BOOT` 的FAT32分区。`VSCode` 打开 `/BOOT/armbianEnv.txt`(或者旧版本系统为`/BOOT/BoardEnv.xt`) 文件。

<ImageView src={require('./img/BoardEnv.webp').default} width="60%"/>

根据需要进行设置，如下图所示。

<ImageView src={require('./img/overlays.webp').default} width="60%"/>

默认值为“console=display”，这意味着CB1的“UART0”默认用作调试端口。我们可以使用“MobaXterm”通过UART0连接到CB1并进行调试。如果klipper想要使用`UART0`来控制主板，我们需要将其设置为`console=serial`，现在klippe可以将`UART0'用作`/dev/ttyS0`。

CB1会自动识别HDMI分辨率，但如果您的HDMI屏幕无法正常通过EDID报告分辨率，我们可以通过取消注释extraargs=video来强制指定CB1输出的分辨率，并设置实际分辨率。
比如:

BTT-HDMI7 resolution = 1024x600: `extraargs=video=HDMI-A-1:1024x600-24@60`

BTT-HDMI5 resolution = 800x480: `extraargs=video=HDMI-A-1:800x480-24@60`

取消注释 `overlays=tft35_spi` 以启用tft35 spi屏幕。

取消注释 `overlays=mcp2515` 以启用mcp2515 spi到canbus模块。

取消注释 `overlays=tft35_spi mcp2515` 如果要同时使用tft35 spi屏幕和mcp2515 spi到can总线模块。

取消注释以下覆盖和参数以将 `spidev1.1` 释放到用户空间，并且 `spidev1.1` 不能与 TFT35_SPI 和 MCP2515 一起使用。

```systemd title="armbianEnv.txt"
overlays=spi-spidev
param_spidev_spi_bus=1
param_spidev_spi_cs=1
param_spidev_max_freq=1000000
```

:::note

TFT35 SPI和MCP2515多路复用一组SPI1

:::

```systemd title="armbianEnv.txt"
SPI1_CLK=PH6
SPI1_MISO=PH8
SPI1_MOSI=PH7
TFT35_SPI_CS=PC7
MCP2515_CS=PC11
MCP2515_IRQ=PC9
```

## SSH 连接

1. 安装 [Mobaxterm](https://mobaxterm.mobatek.net/download-home-edition.html)

2. 通电后等待系统启动，大概 1~2 分钟

3. 设备连上 WIFI 或者插上网线后，会被自动分配一个 IP

4. 进入路由器管理界面找到设备的 IP（这里应为 `BIGTREETECH-CB1`/`BTT-CB1`）

    <ImageView src={require('./img/Router.webp').default} width="60%"/>

    或者使用 [angryip](https://angryip.org)，扫描当前网络中的所有IP地址，找到名为 `BIGTREETECH-CB1`/`BTT-CB1` 的 IP。

    <ImageView src={require('./img/AngryIP.webp').default} width="60%"/>

5. 打开已经安装的 Mobaxterm 软件，点击“Session”，在弹出的窗口中点击“SSH”，在Remote host 一栏中输入设备的 IP 地址，点击“OK”

    :::note

    电脑和设备必须要在同一个局域网下

    :::

    <ImageView src={require('./img/MobaXterm_Login.webp').default} width="60%"/>

6. 输入登录名和登录密码进入 SSH 终端界面

    ```shell title="root 管理员"
    Login: root
    Password: root
    ```

    ```shell title="biqu 普通用户"
    Login: biqu
    Password: biqu
    ```
