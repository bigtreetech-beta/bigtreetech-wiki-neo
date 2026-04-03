---
sidebar_position: 3
description: CB2 软件配置
---

# CB2 软件配置

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 烧录系统

### 下载系统镜像

:::info[CB2 系统]

CB2 系统镜像 [CB2/releases](https://github.com/bigtreetech/CB2/releases)

:::

### 写入系统

<Tabs groupId="cb2-emmc-sd">
    <TabItem value="cb2-sd" label="使用SD卡" default>
        1. 下载 [balenaEtcher](https://www.balena.io/etcher/)

        2. 将 Micro SD 卡通过读卡器插入到电脑。

        3. 选择下载到电脑中的镜像。

            <ImageView src={require('./img/CB2_System1.webp').default} width="60%"/>

        4. 选择待烧录的 Micro SD 卡，点击“烧录”
        
            :::warning

            烧录镜像会将 Micro SD 卡格式化

            :::

            <ImageView src={require('./img/CB2_System2.webp').default} width="60%"/>

        5. 等待烧录完成

            <ImageView src={require('./img/CB2_System3.webp').default} width="60%"/>
    </TabItem>
    <TabItem value="cb2-emmc" label="使用eMMC">
        :::info

        使用 `电脑 (Windows) 烧录` 或者 `MicroSD卡烧录` 步骤，均可正常的将系统烧录到eMMC中，任选一种适合您的方式即可。

        :::
        <Tabs groupId="emmc-write">
            <TabItem value="emmc-windows" label="电脑 (Windows) 烧录" default>
                :::note

                设备中不要插入 Micro SD 卡。

                :::

                1. 首先将设备的拨码开关`nRPIBOOT`，`USB_OTG`拨到 `ON` 使设备进入BOOT模式(如下图以 Pad5 V2 为例)。

                    <ImageView src={require('./img/boot.webp').default} width="60%"/>

                2. 将设备的 USB OTG 连接到电脑上

                    :::note

                    为了避免出现电脑 USB 供电不足导致的问题，最好使用带有外部供电的 USB-Hub，或者先使用外部的电源给设备供电

                    :::

                3. 若eMMC中已经烧录过V3.0.1及其之后版本的系统，电脑会将eMMC识别为UMS设备（类似U盘一样的设备），否则会识别为LOADER设备。UMS相对于LOADER有以下好处：

                    1. 可以直接修改 /boot/ 分区中的配置信息。

                    2. 可以直接像Micro SD卡那样，直接烧录系统到eMMC。

                    3. 可以通过软件擦除eMMC中的所有内容。

                4. 若设备被识别为UMS设备，则参考下面的`UMS`步骤，若识别为LOADER设备吗，则参考下面的`LOADER`步骤
                <Tabs groupId="device-mode">
                    <TabItem value="ums-mode" label="UMS" default>
                        参考`写入系统`->`使用SD卡`中的步骤使用balenaEtcher软件烧录系统
                    </TabItem>
                    <TabItem value="loader-mode" label="LOADER">
                        1. 下载 [RKDevTool](https://github.com/bigtreetech/CB2) 到电脑上并解压。

                        2. 安装驱动

                            1. 在 “设备管理器” 中，如果发现“未知设备”意味着电脑缺少驱动

                                <ImageView src={require('./img/CB2_System5.webp').default} width="60%"/>

                            2. 打开下载的 RKDevTool 中的 DriverAssitant 工具，先点击 “驱动卸载”，再点击 “驱动安装”，这样可以保证安装的驱动为最新版本的。

                                <ImageView src={require('./img/CB2_System6.webp').default} width="60%"/>

                            3. 等待安装完成后，重新拔插一下 Type-C 线，“设备管理器” 会识别出 “Rockusb Device”，意味着驱动已经安装成功

                                <ImageView src={require('./img/CB2_System7.webp').default} width="60%"/>

                        3. 打开 RKDevTool

                            <ImageView src={require('./img/CB2_System8.webp').default} width="60%"/>

                            :::info

                            软件中的参数默认如图所示，正常情况下仅需要设置 .img 系统实际的路径”即可。如果您软件中的参数与图中不一致，请手动修改为一致。

                            :::

                            <ImageView src={require('./img/CB2_System9.webp').default} width="60%"/>

                            1. 找到下载的工具所在的路径

                            2. 打开 RKDevTool 工具

                            3. 软件会识别出一个“LOADER”或者“MASKROOM”的设备

                            4. 选择要烧录的系统（系统镜像需要提前解压为.img 文件，此工具不支持直接烧录压缩后的.xz 文件）

                            5. 勾选“Write by Address”

                            6. 点击“Run”，开始烧录系统

                            7. `Download image OK` 意味着系统已经烧录成功
                    </TabItem>
                </Tabs>
            </TabItem>
            <TabItem value="emmc-micro-sd" label="MicroSD卡烧录">
                1. 先将系统烧录到MicroSD卡中，然后将MicroSD卡插到主板的卡槽，然后等待系统启动。

                2. 通过网线，WiFi或者USB转UART连接到系统的终端，登录系统

                    ```shell title="biqu 普通用户"
                    Login: biqu
                    Password: biqu
                    ```

                3. 运行 `sudo nand-sata-install `命令，在弹出的界面中，选择 `2 Boot From eMMC - system on eMMC`, 然后选择 `OK`

                    <ImageView src={require('./img/CB2_System36.webp').default} width="60%"/>

                4. 选择 `Yes`，开始擦除并烧录系统到eMMC

                    <ImageView src={require('./img/CB2_System37.webp').default} width="60%"/>

                5. 选择文件系统为 `1 ext4`，然后选择 `OK`

                    <ImageView src={require('./img/CB2_System38.webp').default} width="60%"/>

                6. 等待烧录完成

                    <ImageView src={require('./img/CB2_System39.webp').default} width="60%"/>

                7. 烧录完成后会弹窗提示是否关机，选择`Power off`关机

                    <ImageView src={require('./img/CB2_System40.webp').default} width="60%"/>

                8. 关机后断电，然后拔出MicroSD卡，重新再通电即可从eMMC启动
            </TabItem>
        </Tabs>
    </TabItem>
    <TabItem value="cb2-nvme" label="使用NVMe">

        :::info

        需要 V3.0.2 及其之后版本的系统才支持 NVMe 启动。

        RK3566 不能直接从 NVMe 启动，所以我们需要先写入 u-boot(bootloader) 到 eMMC, u-boot(bootloader) 从 eMMC 运行后，检测到 NVMe 后，可以跳转到 NVMe 启动系统。

        :::

        1. 先从SD卡启动系统。

        2. 清除整个eMMC以防止系统从eMMC启动，因为eMMC的启动优先级高于NVMe。

            ```shell
            sudo mkfs /dev/mmcblk1
            ```

            然后输入`y`确认。

            <ImageView src={require('./img/CB2_System42.webp').default} width="60%"/>

        3. 写入 u-boot(bootloader) 到 eMMC

            ```shell
            sudo armbian-install
            ```

            在弹窗中选择 `Install/Update the bootloader on eMMC (/dev/mmcblk1)`

        4. 写入完成后关闭系统

            ```shell
            sudo poweroff
            ```

        5. 参照 `写入系统`->`使用eMMC`->`电脑 (Windows) 烧录` 中的步骤，将设备连接到电脑，eMMC中的 u-boot(bootloader) 会把 NVMe 当作 UMS (USB大容量存储)挂在到电脑上。

        6. 参考`写入系统`->`使用SD卡`中的步骤使用balenaEtcher软件烧录系统
    </TabItem>
</Tabs>

### 擦除eMMC

:::info

如果您的硬件是eMMC版本，并且之前写入过系统到eMMC中，现在不想从eMMC中启动而是希望从MicroSD卡启动。我们需要将之前写入到eMMC的系统数据擦除，以免设备错误的从eMMC启动。

:::

<Tabs groupId="emmc-write">
    <TabItem value="emmc-windows" label="使用电脑擦除 (Windows)" default>
        1. 参照 `写入系统`->`使用eMMC`->`电脑 (Windows) 烧录` 中的步骤，将主板连接到电脑。

        2. 若设备被识别为UMS设备，则参考下面的`UMS`步骤，若识别为LOADER设备吗，则参考下面的`LOADER`步骤
        <Tabs groupId="device-mode">
            <TabItem value="ums-mode" label="UMS (Windows)" default>
                安装 [SD Card Formatter](https://www.sdcard.org/downloads/formatter/) 软件，格式化eMMC的UMS设备。

                :::info

                请不要直接使用windows系统提供的格式化功能，因为它无法完全擦除eMMC中的数据

                :::
            </TabItem>
            <TabItem value="loader-mode" label="LOADER">
                1. 参照 `电脑 (Windows) 烧录`->`LOADER` 中的步骤，下载软件、安装驱动、识别设备为LOADER设备。

                2. 使用 `RKDevTool` 软件擦除数据

                    <ImageView src={require('./img/CB2_System41.webp').default} width="60%"/>

                    1. 找到下载的工具所在的路径

                    2. 打开 RKDevTool 工具

                    3. 软件会识别出一个`LOADER`的设备，如果是`MASKROOM`则说明eMMC中没有数据，不需要擦除

                    4. 点击`Advanced Function`

                    5. 点击`EraseAll`开始擦除eMMC中的数据

                    6. `Erasing sectors success`擦除完成
            </TabItem>
        </Tabs>
    </TabItem>
    <TabItem value="emmc-micro-sd" label="从MicroSD卡启动系统后擦除">
        1. 参照`写入系统`->`使用eMMC`->`MicroSD卡烧录`中的步骤，登录到系统终端

        2. 执行以下命令擦除数据

            ```shell
            sudo mkfs /dev/mmcblk1
            ```

            然后输入`y`确认。

            <ImageView src={require('./img/CB2_System42.webp').default} width="60%"/>
    </TabItem>
</Tabs>

## 系统配置

### 使用网线

网线即插即用，不需要额外的设置

### 设置 WiFi

系统镜像烧录完成后，MicroSD 卡会有一个被电脑识别的 FAT32 分区，此分区下有个名为"system.cfg" 的配置文件，打开后将 Your SSID 替换为实际的 WIFI 名称，Your Password 替换为实际的密码

<ImageView src={require('./img/CB2_System17.webp').default} width="60%"/>

### 配置 overlays

打开 BOOT 分区下的 armbianEnv.txt 文件,设置 overlays 的值。配置文件中同一时间仅支持打开一行 overlays，如果打开了多行 overlays 的配置，只会生效最后一行的配置。如果有打开多个 overlays 配置的需求，可以将多个配置的内容放在同一行overlays 后面，并且多个配置中间用一个空格隔开。例如我们需要同时使用 DSI 屏幕. mcp2515 SPI 转 CAN 模块，和 I2C1：

```systemd title="armbianEnv.txt"
overlays=dsi mcp2515 i2c1
```

<ImageView src={require('./img/CB2_System18.webp').default} width="60%"/>

### 配置显示屏

1. 打开 BOOT 分区下的 armbianEnv.txt 文件

    <ImageView src={require('./img/CB2_System19.webp').default} width="60%"/>

2. overlays 默认设置为 hdmi，代表系统默认使用 hdmi 屏幕。可以将其修改为实际使用的屏幕，可设置的选项如下：

    :::info[overlays 配置]

    hdmi: [HDMI 接口的屏幕](https://biqu.equipment/collections/lcd/products/bigtreetech-hdmi5-v1-0-hdmi7-v1-0)

    dsi: [DSI接口的屏幕](https://biqu.equipment/collections/lcd/products/bigtreetech-pi-tft43-v2-0-screen-board)

    tft_35: [SPI 接口 3.5 寸屏幕](https://biqu.equipment/collections/lcd/products/bigtreetech-tft35-spi-v2-1-touchscreen-io2can-module)

    :::

    其中“tft_35”还有一个参数“tft35_spi_rotate”在系统级旋转显示界面，默认的“0”代表不旋转，可使用的参数还有“90”，“180”，“270”。

    :::info

    屏幕只能选择使用其中的一个，无法同时使用多个屏幕
    
    :::

3. 设置 KlipperScreen，打开 BOOT 分区下的 system.cfg 文件，设置屏幕的类`ks_src`，和旋转角度`ks_angle`

    <ImageView src={require('./img/CB2_System20.webp').default} width="60%"/>

### SPI 转 CAN 的使用

打开 BOOT 分区下的 armbianEnv.txt 文件，将“mcp2515”添加到 overlays 的配置中

<ImageView src={require('./img/CB2_System21.webp').default} width="60%"/>

### CSI 相机使用及 crowsnest 配置

无论是 rpi v1.3 的 ov5647 还是 rpi v2 的 imx219 均不需要在 armbianEnv.txt 文件中配置 overlays，即插即用。

```systemd title="crowsnest.conf"
device: /dev/video0 # CSI 相机的节点固定为 `video0`

custom_flags: --format=UYVY # 当前系统 CSI 相机不支持默认的 `YUYV`，需要设置为支持的 `UYVY` 格式
```

<ImageView src={require('./img/CB2_System22.webp').default} width="60%"/>

### 蓝牙的使用

1. 扫描蓝牙设备，输入如下命令，出现如下列表的蓝牙设备，如下图

    ```shell
    bluetoothctl --timeout 15 scan on
    ```

    <ImageView src={require('./img/CB2_System23.webp').default} width="60%"/>

2. 找到自己的蓝牙设备，比如我的蓝牙设备名字是 HONOR xSport PRO，在设备列表中找到对应的蓝牙 MAC ID 如下图

    <ImageView src={require('./img/CB2_System24.webp').default} width="60%"/>

3. 连接蓝牙设备，输入如下命令，连接成功如下图

    ```shell
    bluetoothctl connect E0:9D:FA:50:CD:4F
    ```

    <ImageView src={require('./img/CB2_System25.webp').default} width="60%"/>

    1. 若出现如下图输出，请重新打开蓝牙设备，然后重新按 1 和 2 的步骤连接蓝牙设备

        <ImageView src={require('./img/CB2_System26.webp').default} width="60%"/>

    2. 若如下图输出，请输入如下命令，然后重新进行 1 和 2 步骤

        ```shell
        bluetoothctl remove E0:9D:FA:50:CD:4F # bluetooth device mac address

        rfkill block bluetooth

        sleep 3s

        rfkill unblock bluetooth

        pulseaudio -k

        pulseaudio –start
        ```

        <ImageView src={require('./img/CB2_System27.webp').default} width="60%"/>

4. 蓝牙使用中途退出语音播放功能，如果不能再次使用蓝牙，需要手动删除对应的播放进程，用 ps 命令查看播放的进程号，然后用 kill -9 进程号 删除对应的播放进程。如下图所示

    <ImageView src={require('./img/CB2_System28.webp').default} width="60%"/>

### 音频输出设置

```shell
aplay -l
```

查看对应的声卡，如下图所示：(由图所示耳机口的声卡对应的是 card 0).

<ImageView src={require('./img/CB2_System29.webp').default} width="60%"/>

```shll
amixer -c 0 contents # 0 表示的上述的 aplay -l 所找到的 card 0
```

查看播放通道和录音通道设置，如下图所示：

<ImageView src={require('./img/CB2_System30.webp').default} width="60%"/>

```shell
amixer -c 0 cset numid=1 3
```

设置播放通道，如下图所示：

<ImageView src={require('./img/CB2_System31.webp').default} width="60%"/>

```shell
amixer -c 0 cset numid=2 1
```

设置录音通道，如下图所示

<ImageView src={require('./img/CB2_System32.webp').default} width="60%"/>

输入如下命令播放音频，音频文件目录 xxx 加音频文件名 xxxxx.wav

```shell
aplay -D plughw:0,0 /xxx/xxxxx.wav
```

输入如下命令录音（其中 10 表示录音 10 秒），录音存放的目录是 xxx，文件名 xxxx.wav:

```shell
sudo arecord -Dhw:0,0 -d 10 -f cd -r 44100 -c 2 -t wav /xxx/xxxx.wav
```

输入如下命令播放录音:

```shell
aplay -D plughw:0,0 /xxx/xxxx.wav
```

## SSH 连接设备

1. 安装 [Mobaxterm](https://mobaxterm.mobatek.net/download-home-edition.html)

2. 通电后等待系统启动，大概 1~2 分钟

3. 设备连上 WIFI 或者插上网线后，会被自动分配一个 IP

4. 进入路由器管理界面找到设备的 IP（这里应为 `BIGTREETECH-CB2`/`BTT-CB2`）

    <ImageView src={require('./img/CB2_System33.webp').default} width="60%"/>

5. 打开已经安装的 Mobaxterm 软件，点击“Session”，在弹出的窗口中点击“SSH”，在 Remote host 一栏中输入设备的 IP 地址，点击“OK”（注意：电脑和设备必须要在同一个局域网下）

    <ImageView src={require('./img/CB2_System34.webp').default} width="60%"/>

6. 输入登录名和登录密码进入 SSH 终端界面

    ```shell title="root 管理员"
    Login: root
    Password: root
    ```

    ```shell title="biqu 普通用户"
    Login: biqu
    Password: biqu
    ```

    <ImageView src={require('./img/CB2_System35.webp').default} width="60%"/>

## 注意事项

上电后大概 10s 左右，系统进入 kernel 阶段。此时 power 灯常亮，act 灯会不断的闪烁，代表系统在正常运行

### 接口使用

- PCIe M.2 接口不支持热插拔，需要预先插上固态硬盘才能识别到设备。
- 使用 eMMC 启动时，不要插 MicroSD 卡。使用 MicroSD 卡启动时，需要将 eMMC 中的数据擦除。
