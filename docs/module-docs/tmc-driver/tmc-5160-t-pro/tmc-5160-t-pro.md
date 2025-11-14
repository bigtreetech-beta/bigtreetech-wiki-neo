---
sidebar_position: 1
description: TMC 5160 T Pro
---

# TMC 5160 T Pro

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<img
    src={require('./img/tmc-5160-t-pro-title.png').default}
    alt="" width="35%" class="right-image"
/>

## Specifications

| Specifications | TMC 5160 T Pro     |
| -------------- | ------------------ |
| 驱动芯片       | TMC 5160           |
| 驱动电压       | 8V - 48V DC        |
| 驱动电流       | 3.1A RMS 4.4A peak |
| 采样电阻       | 0.075 ohms         |
| MOSFET 型号    | JMSL0615AUD        |

</div>

## 接口示意图

:::info[原理图 / Schematic]

TMC 5160 T Pro 原理图 [BIGTREETECH TMC5160T_Pro-SCH.pdf](https://github.com/bigtreetech/BIGTREETECH-Stepper-Motor-Driver/blob/master/TMC5160(T)%20Pro%20V1.1/Hardware/BIGTREETECH%20TMC5160T_Pro-SCH.pdf)
:::

<img
    src={require('./img/tmc-5160-t-pro-pinout.png').default}
    alt="" width="45%"
/>


## 尺寸

:::info[STEP 模型]

TMC 5160 T Pro 模型 [TMC5160_Pro V1.1.step](https://github.com/bigtreetech/BIGTREETECH-Stepper-Motor-Driver/blob/master/TMC5160(T)%20Pro%20V1.1/3D/TMC5160_Pro%20V1.1.step)

:::

<img
    src={require('./img/tmc-5160-t-pro-size.png').default}
    alt="" width="45%"
/>

## Klipper SPI 配置

```klipper_cfg title="printer.cfg"
[tmc5160 stepper_x]
cs_pin: PD2
spi_software_sclk_pin: PC6
spi_software_mosi_pin: PC8
spi_software_miso_pin: PC7
diag1_pin: PF3
run_current: 0.80
sense_resistor: 0.075
interpolate: False
stealthchop_threshold: 0
driver_SGT: 0
```
