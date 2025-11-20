---
sidebar_position: 2
---

# ADXL345 硬件

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import ThemedImage from '@theme/ThemedImage';

<!-- import lib end -->

## 外观尺寸

<ThemedImage
    alt="Docusaurus themed image"
    sources={{
        light: require('./img/adxl-dim-light.png').default,
        dark: require('./img/adxl-dim-dark.png').default,
    }} width="65%"
/>

## Pinout

<img src={require('./img/adxl-pinout.png').default} width="60%"/>

## 连接 Klipper Host

### 使用 PI2 / Raspberry Pi

<img src={require('./img/adxl-connect-rpi.png').default} width="60%"/>

### 使用 USB 连接 Manta M8P / Manta M5P / Manta M4P

<img src={require('./img/adxl-connect-manta-usb.png').default} width="60%"/>
