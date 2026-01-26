---
sidebar_position: 1
description: Manta M8P V2 一体打印板
---

# Manta M8P V2

Manta M8P 板说明文档

<!-- import lib start -->

import DocCardList from '@theme/DocCardList';

<!-- import lib end -->

<div class="div-table">

<img 
    src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p-v2-main.png').default} 
    width="45%" class="right-image"
/>

## 简介

M8P 亦是在解决 Klipper 接线过于复杂的问题。一体化的 Klipper 电路控制。并且保留 Octopus 系列的部分功能，使得拓展性得到提升。

M8P V2 在保留 V1 的简化接线的同时更新了MCU到STM32H723。

## 硬件规格

| Specification    | Manta M8P v2                       |
| ---------------- | ---------------------------------- |
| MCU              | Arm Cortex-M7 STM32H723ZET6 550MHz |
| 主板供电         | DC 12V - DC 24V                    |
| 驱动供电         | 最高 DC 48V (需要驱动支持)         |
| 热床接口供电     | DC 12V - DC 24V                    |  |
| 热床最大电流     | 10A (峰值 12A)                     |
| 热端加热最大电流 | 5.5A (峰值 6A)                     |

</div>

<DocCardList />
