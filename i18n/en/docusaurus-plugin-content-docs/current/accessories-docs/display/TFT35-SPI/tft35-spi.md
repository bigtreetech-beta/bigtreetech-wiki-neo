---
sidebar_position: 1
description: TFT 35 SPI 文档
---

# TFT 35 SPI

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 规格

| Specification   | TFT 35 SPI                                  |
| --------------- | ------------------------------------------- |
| 产品尺寸        | 98 x 56毫米                                 |
| 安装尺寸        | 98 x 56毫米。有关更多详细信息，请阅读：尺寸 |
| 输入电压        | DC 5V                                       |
| 逻辑电压        | DC 3.3V                                     |
| 屏幕尺寸        | 3.5英寸                                     |
| 分辨率          | 480x320                                     |
| SPI显示器驱动IC | ILI9488                                     |
| 触摸驱动IC      | NS2009                                      |

## 尺寸

<img src={require('@site/docs/accessories-docs/display/TFT35-SPI/img/TFT35_SPI_Dimension.png').default} width="50%"/>

## 接口示意图

<img src={require('@site/docs/accessories-docs/display/TFT35-SPI/img/TFT35_SPI_Interface.png').default} width="50%"/>

## Pinout

<img src={require('@site/docs/accessories-docs/display/TFT35-SPI/img/TFT35_SPI_Pinout.png').default} width="50%"/>

## 软件安装

目前 TFT 35 SPI 只支持 CB1

:::info[系统版本]

V2.2.0及更早版本的操作系统不支持 TFT35 SPI。需要使用 V2.2.1 及更高版本的操作系统。

:::

CB1 系统 img [bigtreetech/CB1/releases](https://github.com/bigtreetech/CB1/releases)

<img src={require('@site/docs/accessories-docs/display/TFT35-SPI/img/TFT35_SPI_Soft1.png').default} width="80%"/>

操作系统写入SD卡后，有一个名为 `BOOT` 的 `FAT32` 分区，用 VSCode 打开 `BoardEnv.txt` 文件。

取消注释覆盖 `=tft35_spi` 以启用 tft35 spi 屏幕

<img src={require('@site/docs/accessories-docs/display/TFT35-SPI/img/TFT35_SPI_Soft2.png').default} width="80%"/>

:::warning[已知问题]

如果使用 v2.2.1 版本的操作系统映像。设置为 `overlay=tft35_spi25` 而不是 `overlay=tft35_spi` 使用25Mhz的spi速度而不是默认的50Mhz，以避免显示异常。

如果使用 V2.2.1 之后的操作系统映像，默认情况下操作系统将使用更低更稳定的速度。

:::

<img src={require('@site/docs/accessories-docs/display/TFT35-SPI/img/TFT35_SPI_Soft3.png').default} width="80%"/>
