---
sidebar_position: 3
description: Pad5 V2 固件配置
---

# Pad5 V2 软件配置

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## 烧录系统

:::info

使用 Pad5 的 USB OTG 烧录系统到eMMC版本硬件时，设备的拨码开关请参考下图，将拨码开关的`nRPIBOOT`，`USB_OTG`拨到`ON`进入BOOT模式。系统烧录完成后, 将开关拨回`OFF`即可正常启动。

<ImageView src={require('./img/boot.webp').default} width="60%"/>

:::

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi CM4/CM5" default>
        下载系统镜像。根据需求下载合适的系统镜像，例如[树莓派官方镜像](https://www.raspberrypi.com/software/operating-systems)或者[Mainsail系统镜像](https://github.com/mainsail-crew/MainsailOS/releases)

        :::info

        eMMC版本的树莓派不会运行Micro SD卡中的系统, 必须要烧录系统到eMMC中运行。

        :::
        <Tabs groupId="rpi-emmc-sd">
            <TabItem value="rpi-sd" label="SD卡版本" default>
                1. 下载并安装树莓派官方的烧录软件：https://www.raspberrypi.com/software/

                2. 打开软件，将Micro SD卡通过读卡器插入到电脑。

                3. 选择设备为`NO FILTERING`

                    <ImageView src={require('./img/pi1.webp').default} width="60%"/>

                4. 选择系统

                    <ImageView src={require('./img/pi2.webp').default} width="60%"/>

                5. 选择`Use custom`用户自定义，然后选择下载到电脑中的镜像

                    <ImageView src={require('./img/pi3.webp').default} width="60%"/>

                6. 选择待烧录的Micro SD卡，然后点击“Next”下一步

                    :::warning

                    烧录镜像会将选中的存储设备格式化，千万注意不要选错存储设备。

                    :::

                    <ImageView src={require('./img/pi4.webp').default} width="60%"/>

                7. 在弹出的弹窗中选则`EDIT SETTINGS`编辑设置

                    <ImageView src={require('./img/pi5.webp').default} width="60%"/>

                8. 在 `General` 中设置：

                    :::info

                    Set hostname: raspberrypi.local  // 设置主机名，默认为raspberrypi.local

                    Set username and password // 设置用户名和密码，默认用户名：pi 密码：raspberry

                    Configure wireless LAN // 设置WiFi名称和密码

                    :::

                    <ImageView src={require('./img/pi6.webp').default} width="60%"/>

                9. 在`Services`中设置：

                    :::info

                    Enable SSH

                    Use password authentication

                    :::

                    然后点击`SAVE`保存设置

                    <ImageView src={require('./img/pi7.webp').default} width="60%"/>

                10. 点击`YES`开始烧录系统

                    <ImageView src={require('./img/pi8.webp').default} width="60%"/>

                11. 等待烧录完成

                    <ImageView src={require('./img/pi9.webp').default} width="60%"/>
            </TabItem>
            <TabItem value="rpi-emmc" label="eMMC版本">
                1. 安装rpiboot 软件，提供有[Windows](http://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)和[Mac/Linux](https://github.com/raspberrypi/usbboot#building)版本

                2. 将拨码开关的nRPIBOOT，USB_OTG拨到ON进入BOOT模式

                    <ImageView src={require('./img/boot.webp').default} width="60%"/>

                3. 将设备的 USB OTG 连接到电脑上。运行如下命令：
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
                    eMMC会被电脑识别为一个大容量存储设备（如果此时rpiboot报错，可以尝试重新拔插一下USB）

                    :::note

                    为了避免出现电脑 USB 供电不足导致的问题，最好使用带有外部供电的 USB-Hub，或者先使用外部的电源给设备供电

                    :::

                4. 使用Raspberry Pi Imager软件烧录系统镜像，步骤与烧录到Micro SD卡完全相同。

                5. 烧录完成后，断电后将拨码开关的nRPIBOOT,USB_OTG拨回到OFF，重新上电后进入正常工作模式。
            </TabItem>
        </Tabs>
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        - [参考CB2使用手册](../iot-cb2/iot-cb2-firmware)
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - [参考CB1使用手册](../iot-cb1/iot-cb1-firmware)
    </TabItem>
</Tabs>

## 系统设置

### DSI 显示

:::info

将I2C的2pin拨码开关的都拨到ON，此接口是DSI1接口屏幕的触摸信号线

<ImageView src={require('./img/i2c.webp').default} width="60%"/>

:::

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi" default>
        1. 在 `/boot/firmware/config.txt` 文件里面修改如下配置，然后重启设备生效

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

        2. 此时设备自带的屏幕和外接的DSI屏幕都理应可以正常显示，但是多屏显示的触摸需要重新绑定映射。

            1. 在显示屏上打开界面：首选项`Preferences`->`Screen Configuration`

                <ImageView src={require('./img/dsi.webp').default} width="60%"/>

            2. 拖动 “DSI-1”,“DSI-2”,“HDMI-A-1”, “HDMI-A-2”随意的排列组合，显示屏实际显示的内容就会按照此布局显示，并且可以将所有的显示屏完全叠加重合起来，这样所有的显示屏显示的就会是完全一样的内容。

            3. 设置每个显示屏对应的触摸设备，设置完后对应的触摸设备就会仅作用于匹配的显示屏。

            4. 应用配置，点击确认后配置就会生效。
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        1. 在`/boot/armbianEnv.txt`文件的`overlays`的值中添加`dsi`配置，多个配置中间用空格隔开。

            系统默认带了`hdmi`的配置，如果您想同时启用两个屏幕，可以同时保留`hdmi`和`dsi`的配置，如果您只希望其中一个屏幕显示，那么只保留想要的屏幕配置，删除其他的屏幕配置即可。

            重启设备后配置即可生效。如果您同时配置了hdmi和外接的dsi屏幕，两个屏幕理应可以正常显示，并且显示完全一模一样的内容。此设备的DSI触摸I2C信号线与标准的BITREETECH Pi2不同，当前的系统镜像中还不支持此信号线的触摸，所以DSI屏幕上的触摸目前是无用的

        2. 多屏显示的触摸需要重新绑定映射。

            1. 设置DISPLAY为实际的屏幕：

                ``` shell
                export DISPLAY=:0.0
                ```

            2. 查询显示器名称：

                ``` shell
                xrandr -q
                ```

                应答为：

                ``` shell
                Screen 0: minimum 320 x 200, current 1600 x 480, maximum 16384 x 16384
                HDMI-1 connected primary 800x480+0+0 (normal left inverted right x axis y axis) 108mm x 62mm
                800x480       68.35*+  68.35
                640x480       60.00    59.94
                DSI-1 connected 800x480+800+0 (normal left inverted right x axis y axis) 0mm x 0mm
                800x480       56.06*+
                ```

                可知，我们有HDMI-1和DSI-1两个显示屏可用

            3. 查询触摸设备：

                ``` shell
                xinput list
                ```

                应答为：

                ``` shell
                BIQU BTT-HDMI5                     id=9    [slave  pointer  (2)]
                ```

                可知，我们有BIQU BTT-HDMI5和id为9的触控设备可用

            4. 执行以下命令

                ``` shell
                xinput map-to-output 9 HDMI-1
                ```

                将id为9的BIQU BTT-HDMI5触控设备映射到HDMI输出中。CB2的显示屏仅支持双屏同显，也就是说HDMI屏幕是作为主显示器，DSI的屏幕是跟随HDMI显示的，所以我们需要将触摸设备都绑定到HDMI上才行。

            5. 此命令重启后会失效，可自行添加到脚本中，开机自动运行
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 不支持此功能
    </TabItem>
</Tabs>

### CAM 摄像头

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi" default>
        1. 在 `/boot/firmware/config.txt` 文件里面修改如下配置，然后重启设备生效。这里以0v5647型号的摄像头为例，如果使用其他的型号请配置为实际使用的型号。

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

        2. 测试摄像头

            读取摄像头信息：

            ``` shell
            rpicam-hello --list-camera
            ```

            设置摄像头的画面显示到屏幕上：

            ``` shell
            export DISPLAY=:0.0
            ```

            开始监控摄像头（不能以root权限运行）：

            ``` shell
            rpicam-hello --timeout 0 --camera 0
            ```

            更详细的用法请参考：
            https://www.raspberrypi.com/documentation/computers/camera_software.html
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        1. 在`/boot/armbianEnv.txt`文件的`overlays`的值中添加 `csi` 配置，多个配置中间用空格隔开,然后重启设备。CB2的系统镜像中目前仅适配了` ov5647` 和 `imx219`的驱动，所以目前仅支持这两款类型的CSI摄像头，系统会自动识别摄像头类型，无需额外设置。

        2. 启动后使用命令

            ``` shell
            dmesg | grep csi
            dmesg | grep ov5647
            dmesg | grep imx219
            ```

            查找CSI摄像头是否有被正常识别。
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 不支持此功能
    </TabItem>
</Tabs>

### RTC

:::info

板载的 RTC 为 `PCF8563`，需要安装 CR1220 纽扣电池，RTC才能在断电时正常工作。

:::

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi" default>
        1. 在 `/boot/firmware/config.txt` 文件里面修改如下配置，然后重启设备生效

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

        2. 启动后使用命令

            ``` shell
            dmesg | grep rtc
            ```

            查找RTC挂载的设备号，如果pcf8563挂载为 rtc0时，读写rtc的命令就需要使用rtc0，如果挂载为rtc1，就需要使用rtc1。

        3. 测试RTC，以pcf8563挂载为rtc1为例

            将系统时间写入RTC：

            ``` shell
            sudo hwclock -w -f /dev/rtc1
            ```

            将RTC的时间设置为系统时间：

            ``` shell
            sudo hwclock -s -f /dev/rtc1
            ```

            打印RTC中的时间：

            ``` shell
            sudo hwclock -r -f /dev/rtc1
            ```
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        1. 在 `/boot/armbianEnv.txt `文件的`overlays`的值中添加` rtc_pcf8563 `配置，多个配置中间用空格隔开，然后重启设备。

        2. 启动后使用命令

            ``` shell
            dmesg | grep rtc
            ```

            查找RTC挂载的设备号，如果`pcf8563`挂载为 `rtc0`时，读写rtc的命令就需要使用rtc0，如果挂载为`rtc1`，就需要使用`rtc1`。

        3. 测试RTC，以`pcf8563`挂载为`rtc0`为例
            将系统时间写入RTC：

            ``` shell
            sudo hwclock -w -f /dev/rtc0
            ```

            将RTC的时间设置为系统时间：

            ``` shell
            sudo hwclock -s -f /dev/rtc0
            ```

            打印RTC中的时间：

            ``` shell
            sudo hwclock -r -f /dev/rtc0
            ```
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 不支持此功能
    </TabItem>
</Tabs>

### CANBus

<Tabs groupId="core-board">
    <TabItem value="rpi" label="Raspberry Pi" default>
        1. 在 /boot/firmware/config.txt 文件里面配置, CM5与CM4都使用如下配置

            ``` systemd title="/boot/firmware/config.txt"
            [all]
            dtparam=spi=on
            dtoverlay=mcp2515-can0,oscillator=12000000,interrupt=24,spimaxfrequency=10000000
            ```

            然后重启设备

        2. 启动后使用命令

            ``` shell
            dmesg | grep -i '\(can\|spi\)'
            ```

            查询 MCP2515 是否正常启动，正常的应答如下

            ``` shell
            [ 8.680446] CAN device driver interface
            [ 8.697558] mcp251x spi0.0 can0: MCP2515 successfully initialized.
            [ 9.482332] IPv6: ADDRCONF(NETDEV_CHANGE): can0: link becomes ready
            ```
    </TabItem>
    <TabItem value="cb2" label="BIGTREETECH CB2">
        - CB2 不支持此功能
    </TabItem>
    <TabItem value="cb1" label="BIGTREETECH CB1">
        - CB1 不支持此功能
    </TabItem>
</Tabs>

## 注意事项

1. 设备板载的SPI转CANbus芯片，使用的是40 Pin GPIO上面的pin，所以40 Pin GPIO 上对应的pin不推荐再外接其他设备。使用的SPI pin详情如下：

    | 功能 | Raspberry Pi | BIGTREETECH CB2            | BIGTREETECH CB1 | BIGTREETECH CB1 eMMC |
    | ---- | ------------ | -------------------------- | --------------- | -------------------- |
    | CS   | GPIO8        | GPIO4_A2(gpiochip4/gpio2)  | NC              | NC                   |
    | MISO | GPIO9        | GPIO3_C2(gpiochip3/gpio18) | PH8(GPIO232)    | PH8(GPIO232)         |
    | MOSI | GPIO10       | GPIO3_C1(gpiochip3/gpio17) | PH7(GPIO231)    | PH7(GPIO231)         |
    | SCK  | GPIO11       | GPIO3_C3(gpiochip3/gpio19) | PH6(GPIO230)    | PH6(GPIO230)         |
    | INT  | GPIO24       | GPIO4_A3(gpiochip4/gpio3)  | PC9(GPIO73)     | PI3(GPIO259)         |

2. Raspberry Pi CM5 的DSI和CSI均可使用相同的pin输出，所以设备板载的DSI，CAM (CSI)接口当搭配 CM5 使用时，均可随意配置为DSI，CSI功能，即可以配置为两个DSI显示屏，也可配置为两个CSI摄像头。
    <Tabs groupId="cm5-dphy">
        <TabItem value="cm5-dphy0" label="CAM(CSI) DPHY0端口" default>
            <Tabs groupId="dphy0">
                <TabItem value="dphy0-dsi" label="配置为DSI显示屏" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=vc4-kms-v3d
                    dtoverlay=vc4-kms-dsi-7inch,dsi0
                    dtoverlay=edt-ft5406,i2c_csi_dsi0
                    ```
                </TabItem>
                <TabItem value="dphy0-csi" label="配置为CSI摄像头">
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=ov5647,cam0
                    ```
                </TabItem>
            </Tabs>
        </TabItem>
        <TabItem value="cm5-dphy1" label="DSI DPHY1端口">
            <Tabs groupId="dphy1">
                <TabItem value="dphy1-dsi" label="配置为DSI显示屏" default>
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=vc4-kms-v3d
                    dtoverlay=vc4-kms-dsi-7inch
                    dtoverlay=edt-ft5406,i2c_csi_dsi
                    ```
                </TabItem>
                <TabItem value="dphy1-csi" label="配置为CSI摄像头">
                    ``` systemd title="/boot/firmware/config.txt"
                    [cm5]
                    dtoverlay=ov5647
                    ```
                </TabItem>
            </Tabs>
        </TabItem>
    </Tabs>

3. eMMC版本的Raspberry Pi CM4/CM5 仅支持系统运行在eMMC中，完全不支持从Micro SD卡启动。而 eMMC 版本的BIGTREETECH CB1/CB2 仍然支持并以 Micro SD 中的系统作为第一优先级启动。
