---
sidebar_position: 10
---

# Manta M8P 系列固件 (STM32G0B1)

使用 `STM32G0B1` MCU 的 Manta M8P 

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

:::info

M8P v1.0 不能使用 CAN Bridge

:::

<Tabs groupId="m8p-v1-make-connect">
    <TabItem value="bridge" label="CAN 桥接固件" default>
        按照以下选项构建使用 `STM32G0B1` 为 `MCU` 的 `Manta M8P` CAN 桥接固件
        <img
            src={require('./img/manta-m8p-v1-make-bridge.png').default}
            alt="manta m8p with g0b1 bridge"
        />
    </TabItem>
    <TabItem value="usb" label="USB 串口固件">
        按照以下选项构建使用 `STM32G0B1` 为 `MCU` 的 `Manta M8P` USB 串口固件
        <img
            src={require('./img/manta-m8p-v1-make-usb.png').default}
            alt="manta m8p with g0b1 usb"
        />
    </TabItem>
</Tabs>

当配置完成使用 `q` 来退出。使用 `y` 来保存编译选项。

然后使用 `make` 命令来开始编译 Klipper 固件

``` shell
make
```

## 写入固件

当使用 Klipper 固件编译完成后。然后按住 `Manta M8P` 的 `boot` 按钮。然后按一下 `reset` 然后松开 `boot` 按钮进入 `DFU` 模式。

然后可以使用 `lsusb` 命令来确认 `Manta M8P` 是否在 `DFU` 模式中。

当确认 Manta M8P 在 DFU 模式中后。可以使用以下命令来写入固件。

``` shell
make flash FLASH_DEVICE=0483:df11
```
