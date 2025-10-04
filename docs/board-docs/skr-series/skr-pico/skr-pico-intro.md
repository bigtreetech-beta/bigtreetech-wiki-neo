---
sidebar_position: 1
---

# SKR Pico 简介

SKR PICO 说明文档

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<img 
    src={require('./img/skr-pico-main.png').default} 
    width="45%" class="right-image"
/>

## 简介

SKR Pico 是一块专门为 Voron 0 系列设计的板子。可以直接和 Raspberry Pi 系列直接堆叠安装。减少所需要的安装空间。

## Specification

| Specification                  | SKR Pico              |
| ------------------------------ | --------------------- |
| MCU                            | ARM Cortex-M0+ RP2040 |
| 外观尺寸                       | 85 * 56mm             |
| 板层                           | 4层                   |
| 电源输入                       | DC 12/24V             |
| 逻辑电压                       | 3.3V                  |
| 电机驱动器                     | $4*$ TMC2209          |
| 电机驱动接口                   | X / Y / Z1 / Z2 / E   |
| 温度传感器接口                 | TH0、 THB             |
| 与Raspberry Pi(树莓派)通信接口 | USB TYPE-C / 串口     |

</div>
