---
sidebar_position: 1
description: TFT 24 文档
---

# TFT 24

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<img src={require('@site/docs/accessories-docs/display/TFT24/img/TFT24_Title.png').default} width="45%" class="right-image"/>

## 产品规格

| Specification | TFT 24             |
| ------------- | ------------------ |
| 外观尺寸      | 105*46mm           |
| 安装尺寸      | 详见TFT24-V1.1-DSI |
| MCU           | STM32F105CT6       |
| 电源输入      | DC5V               |

</div>

## 尺寸

<img src={require('@site/docs/accessories-docs/display/TFT24/img/TFT24_Diagram.png').default} width="50%"/>

## 接口示意图

<img src={require('@site/docs/accessories-docs/display/TFT24/img/TFT24_Interface.png').default} width="50%"/>

:::info[固件与功能选择]

使用12864屏幕模式时，将端口EXP1和EXP2连接到主板。此模式下没有触摸功能。

当使用串行端口屏幕模式时，通过RS232与主板上的TFT或aux-2连接。在这种模式下，有触摸功能。

这两种模式对应两个不同的固件，需要根据 Flash 固件的模式来进行接线。

:::

## 软件配置

出厂已经包含固件，它可以直接使用。也可以按照以下方法进行升级

1. 从 GitHub repo [bigtreetech/BIGTREETECH-TouchScreenFirmware](https://github.com/bigtreetech/BIGTREETECH-TouchScreenFirmware) 下载固件
2. 然后把固件复制进 SD 卡根目录
3. 把 SD 卡插入板的SD卡插槽
4. 重新给主板通电或按下重置键
5. 等待10秒后更新完成
