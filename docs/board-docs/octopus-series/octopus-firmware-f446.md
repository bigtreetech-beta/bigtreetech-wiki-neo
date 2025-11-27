---
sidebar_position: 10
---

# Octopus 系列固件 (STM32F446)

使用 `STM32F446` MCU 的 Octopus 

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 构建固件

使用 ssh 连接到 Klipper Host. 然后使用以下命令进入 Klipper 目录。并且使用 `make menuconfig` 配置固件。

``` shell
cd ~/klipper
make menuconfig 
```

<Tabs groupId="octopus-make-connect">
    <TabItem value="bridge" label="CAN 桥接固件" default>
        按照以下选项构建使用 `STM32F446` 为 `MCU` 的 `Octopus` CAN 桥接固件
        <img
            src={require('./img/octopus-f446-make-bridge.png').default}
            alt="octopus with h723 bridge"
        />
    </TabItem>
    <TabItem value="usb" label="USB 串口固件">
        按照以下选项构建使用 `STM32F446` 为 `MCU` 的 `Octopus` USB 串口固件
        <img
            src={require('./img/octopus-f446-make-usb.png').default}
            alt="octopus with h723 usb"
        />
    </TabItem>
</Tabs>

当配置完成使用 `q` 来退出。使用 `y` 来保存编译选项。

然后使用 `make` 命令来开始编译 Klipper 固件

``` shell
make
```

## 写入固件

:::note USB 供电
如果你在写入固件的时候使用 USB Type-C 接口进行供电。`VUSB` 跳线需要接上。
:::

当使用 Klipper 固件编译完成后。使用 USB Type-C 连接线连接到 Klipper Host 上。

然后按住 `Octopus` 的 `boot` 按钮。然后按一下 `reset` 然后松开 `boot` 按钮进入 `DFU` 模式。

然后可以使用 `lsusb` 命令来确认 `Octopus` 是否在 `DFU` 模式中。

当确认 Octopus 在 DFU 模式中后。可以使用以下命令来写入固件。

``` shell
make flash FLASH_DEVICE=0483:df11
```
