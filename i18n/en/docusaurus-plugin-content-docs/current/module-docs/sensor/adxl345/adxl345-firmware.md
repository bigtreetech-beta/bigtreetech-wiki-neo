---
sidebar_position: 3
---

# ADXL345 固件配置

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 编译 Klipper 固件

使用 ssh 连接到 Klipper Host. 然后使用以下命令进入 Klipper 目录。并且使用 `make menuconfig` 配置固件。

``` shell
cd ~/klipper
make menuconfig 
```

<img src={require('@site/docs/module-docs/sensor/adxl345/img/adxl-firmware-config.png').default} width="80%"/>

当配置完成使用 `q` 来退出。使用 `y` 来保存编译选项。

然后使用 `make` 命令来开始编译 Klipper 固件

``` shell
make
```

## 写入固件

当使用 Klipper 固件编译完成后。然后按住 `ADXL345` 的 `boot` 按钮。然后插入 `USB` 进入 `Boot` 模式。

然后可以使用 `lsusb` 命令来确认 `ADXL345` 是否在 `Boot` 模式中。

当确认 ADXL345 在 Boot 模式中后。可以使用以下命令来写入固件。

``` shell
make flash FLASH_DEVICE=2e8a:0003
```

## 配置 Klipper

``` klipper_cfg title="printer.cfg"
# This file contains common pin mappings for the bigtreetech adxl345 v2.0
# To use this config, the firmware should be compiled for the
# RP2040 with "USB"
# The micro-controller will be used to control the components on the nozzle.

# See docs/Config_Reference.md for a description of parameters.

[mcu btt_adxl345]
serial: /dev/serial/by-id/usb-Klipper_rp2040_btt_acc-if00

[adxl345]
cs_pin: btt_adxl345:gpio9
#spi_bus: spi1a
spi_software_sclk_pin: btt_adxl345:gpio10
spi_software_mosi_pin: btt_adxl345:gpio11
spi_software_miso_pin: btt_adxl345:gpio8
axes_map: -x,-y,-z

[resonance_tester]
probe_points: 100, 100, 20
accel_chip: adxl345
```
