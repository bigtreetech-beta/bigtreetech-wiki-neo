---
sidebar_position: 3
description: EZ 5160 T Plus 软件配置
---

# TMC 5160 T Plus 软件

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## Klipper 配置文件参考

```klipper_cfg title="printer.cfg"
[tmc5160 stepper_x]
cs_pin: PD2
spi_software_sclk_pin: PC6
spi_software_mosi_pin: PC8
spi_software_miso_pin: PC7
diag1_pin: PF3
run_current: 0.8
sense_resistor: 0.022
interpolate: False
stealthchop_threshold: 0
driver_SGT: 0
```

## Marlin 配置

:::info[Marlin 最低版本]
只有 Marlin 2.0 及更高版本的固件支持 TMC5160 的 SPI 模式
:::

