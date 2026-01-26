---
sidebar_position: 3
---

# EBB 36 CAN 固件配置

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

:::info[固件支持]
EBB 36 V1.0/V1.1/V1.2 目前只支持 Klipper 固件
:::

## 写入 Klipper 固件

EBB 36 v1.1 / v1.2 写入 Klipper 固件参考 [EBB 系列固件 (STM32G0B1)](../ebb-firmware-g0b1.md)

EBB 36 v1.0 写入 Klipper 固件参考 [EBB 系列固件 (STM32F072)](../ebb-firmware-f072.md)

## Klipper 配置文件参考

``` klipper_cfg title="printer.cfg"
[mcu EBBCan]
canbus_uuid: 11aa22bb33cc

[adxl345]
cs_pin: EBBCan: PB12
spi_software_sclk_pin: EBBCan: PB10
spi_software_mosi_pin: EBBCan: PB11
spi_software_miso_pin: EBBCan: PB2
axes_map: x,y,z

[extruder]
step_pin: EBBCan: PD0
dir_pin: !EBBCan: PD1
enable_pin: !EBBCan: PD2
microsteps: 16
rotation_distance: 33.500
nozzle_diameter: 0.400
filament_diameter: 1.750
heater_pin: EBBCan: PB13
sensor_type: EPCOS 100K B57560G104F
sensor_pin: EBBCan: PA3
control: pid
pid_Kp: 21.527
pid_Ki: 1.063
pid_Kd: 108.982
min_temp: 0
max_temp: 250

# sensor_type: MAX31865
# sensor_pin: EBBCan: PA4
# spi_bus: spi1
# rtd_nominal_r: 100
# rtd_reference_r: 430
# rtd_num_of_wires: 2

[tmc2209 extruder]
uart_pin: EBBCan: PA15
run_current: 0.650
stealthchop_threshold: 999999

[fan]
pin: EBBCan: PA0

[heater_fan hotend_fan]
pin: EBBCan: PA1
heater: extruder
heater_temp: 50.0

#[neopixel hotend_rgb]
#pin: EBBCan:PD3

#[bltouch]
#sensor_pin: ^EBBCan:PB8
#control_pin: EBBCan:PB9

#[filament_switch_sensor switch_sensor]
#switch_pin: EBBCan:PB4

#[filament_motion_sensor motion_sensor]
#switch_pin: ^EBBCan:PB3

```
