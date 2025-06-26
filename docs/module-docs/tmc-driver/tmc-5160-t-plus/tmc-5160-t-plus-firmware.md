---
sidebar_position: 3
description: EZ 5160 T Plus 软件配置
---

# EZ 5160 T Plus Firmware

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
