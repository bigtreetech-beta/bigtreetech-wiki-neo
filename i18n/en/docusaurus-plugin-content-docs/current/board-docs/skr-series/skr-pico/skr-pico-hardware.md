---
sidebar_position: 2
---

# SKR Pico 硬件功能

SKR Pico 硬件详细

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 外观尺寸

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/skr-pico-size.png').default}
    alt="size" width="800"
/>

## Pinout

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/skr-pico-pin.png').default}
    alt="pinout" width="800"
/>

## 硬件功能配置

### TMC 2209 Sensorless

:::warning 

对应轴使用了 Sensorless 后。不能使用外部ENDSTOP。

:::

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Sensorless.png').default}
    alt="sensorless" width="550"
/>

### Neopixel

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_RGB.png').default}
    alt="neopixel" width="550"
/>

### BLTouch 

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_BLtouch.png').default}
    alt="bltouch" width="550"
/>

### 接近开关

:::info[NPN 与 PNP 类型传感器选择] 

与接近开关的连接，可通过跳帽选择接近开关的类型为PNP或者NPN

:::

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Proximity.png').default}
    alt="proximity" width="550"
/>

### USB 连接

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Rasp.png').default}
    alt="rpi_usb" width="550"
/>

### UART 连接

<img
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Rasp3.png').default}
    alt="rpi_uart" width="550"
/>