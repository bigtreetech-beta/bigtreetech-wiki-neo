---
sidebar_position: 10
---

# SKR 系列固件 (RP2040)

使用 `RP2040` MCU 的 SKR

## 构建固件

使用 ssh 连接到 Klipper Host. 然后使用以下命令进入 Klipper 目录。并且使用 `make menuconfig` 配置固件。

``` shell
cd ~/klipper
make menuconfig 
```

然后按照以下选项构建使用 `RP2040` 为 `MCU` 的 `SKR` 固件

<img
    src={require('./img/skr-rp2040-make-usb.png').default}
    alt="skr rp2040 usb"
/>

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

然后插入 `SKR` 的 `boot` 跳线。然后按一下 `reset` 按钮进入 `Boot` 模式。

然后可以使用 `lsusb` 命令来确认 `MCU` 是否在 `Boot` 模式中。

当确认 `MCU` 在 `Boot` 模式中后。可以使用以下命令来写入固件。

``` shell
make flash FLASH_DEVICE=2e8a:0003
```
