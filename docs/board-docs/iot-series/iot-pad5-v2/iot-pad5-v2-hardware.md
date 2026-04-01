---
sidebar_position: 2
description: Pad5 V2 硬件功能配置
---

# Pad5 V2 硬件

## 外设接口

### 接口示意图

<ImageView src={require('./img/interface.webp').default} width="60%"/>

### 功能概要

搭配各个核心板对应拥有的功能如下图所示，`√`代表支持，`×`代表不支持。

<ImageView src={require('./img/functional.webp').default} width="60%"/>

## 功能介绍

### 40 Pin GPIO

搭配各个核心板对应的 40Pin GPIO 如下图:

<ImageView src={require('./img/40pin-gpio.webp').default} width="100%"/>

### CAN接口

本产品搭配CM5/CM4使用时，支持CAN通讯，实现方式是由SOC的SPI信号转换为CAN信号。

SPI信号为：CS-GPIO8，MISO-GPIO9，MOSI-GPIO10，SCK-GPIO11，INT-GPIO24

### 风扇接口

本产品搭配CM5使用时，支持4线风扇进行主动散热，插座型号是ZX-SH1.0 4P接口线序如下图：

<ImageView src={require('./img/fan.webp').default} width="60%"/>

### RTC电路

本产品搭配CM5/CM4/CB2使用时，支持RTC电路，实现方式是由SOC的I2C驱动PCF8563时钟芯片。

:::info

使用此功能之前必须确保板子已安装CR1220 3V的纽扣电池，安装时需要带LOGO的一面朝上。推荐品牌：Lithium Cell，Panasonic等等。

:::

### MIPI接口

本产品搭配CM5/CM4/CB2使用时，支持MIPI-DSI（DSI）和MIPI-CSI（CAM）接口。其中搭配CM5使用时，两路MIPI接口可以混合使用，即：DPHY0和DPHY1可作为DSI接口使用，也可作为CSI接口使用；搭配CM4和CB2使用时，CAM接口仅可接摄像头，DSI接口仅可接DSI屏幕使用。

:::info

连接摄像头或者屏幕时，需要检查使用的线是对应的，不可将摄像头的线用于接屏幕，也不可将屏幕的线用于接摄像头；接线时，注意查看金手指对应金手指触点插入，插入完毕后扣紧锁扣。

:::

DSI线材：

<ImageView src={require('./img/mipi-dsi.webp').default} width="45%"/>

CSI线材：

<ImageView src={require('./img/mipi-csi.webp').default} width="45%"/>

线序：

<ImageView src={require('./img/mipi.webp').default} width="45%"/>

### 按键

<ImageView src={require('./img/button.webp').default} width="60%"/>

BK+: 增加背光亮度，范围为0~100%，每次点击增加1%，长按按钮可快速调整亮度

Rotate: 显示方向旋转180°

BK-: 降低背光亮度，范围为0~100%，每次点击降低1%，长按按钮可快速调整亮度

ON/OFF: 电源开关按键（仅支持搭配Raspberry Pi CM5时使用）
