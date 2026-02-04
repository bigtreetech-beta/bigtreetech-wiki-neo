---
sidebar_position: 3
description: Microprobe 固件配置
---

# Microprobe 固件配置

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## Klipper 配置文件参考

### 基本配置

```klipper_cfg title="printer.cfg"
# microprobe config
[output_pin probe_enable]
pin: ebb:PB9
value: 0

# Probe deploy
[gcode_macro Probe_Deploy]
gcode:
    SET_PIN PIN=probe_enable VALUE=1

# Probe stow
[gcode_macro Probe_Stow]
gcode:
    SET_PIN PIN=probe_enable VALUE=0

[probe]
pin: ^!ebb:PB8
deactivate_on_each_sample: False
x_offset: 0.0 
y_offset: 25.0
z_offset: 1.660
speed: 15
activate_gcode:
    Probe_Deploy
    G4 P500
deactivate_gcode:
    Probe_Stow
```

### 配置为Z限位

替换原本的 `endstop_pin` 为 `probe:z_virtual_endstop`

```klipper_cfg title="printer.cfg"
[stepper_z]
endstop_pin: probe:z_virtual_endstop
```
