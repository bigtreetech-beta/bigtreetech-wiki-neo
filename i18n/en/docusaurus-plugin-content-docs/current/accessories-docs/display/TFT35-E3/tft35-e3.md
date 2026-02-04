---
sidebar_position: 1
description: TFT 35 E3 文档
---

# TFT 35 E3

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<img src={require('@site/docs/accessories-docs/display/TFT35-E3/img/TFT35_E3_Title.png').default} width="45%" class="right-image"/>

## 产品简介

TFT35-E3 是一款中等尺寸、双模、超清晰的3D打印机显示器，可以直接替换Ender3打印机原有的液晶屏幕。

## 规格

| Specification | TFT 35 E3                                                           |
| ------------- | ------------------------------------------------------------------- |
| 外观尺寸      | 93*87mm                                                             |
| 安装尺寸      | 完美替换Ender3打印机的原始LCD屏幕，详细信息请查看TFT35-E3 V3.0 尺寸 |
| 微处理器      | STM32F207VCT6                                                       |
| 电源输入      | DC 5V                                                               |
| SD卡逻辑电压  | 3.3V和5V（如：支持MEGA2560主控芯片主板，兼容性更高）                |

</div>

:::note

红灯D6为电源指示灯：红灯亮，表示正常供电；

绿色指示灯D3为SD卡检测指示灯：插入SD卡时D3常亮，拔出SD卡时D3熄灭。

:::

## 尺寸

<img src={require('@site/docs/accessories-docs/display/TFT35-E3/img/TFT35_E3_Diagram.png').default} width="50%"/>

## 接口示意图

:::info

1.使用12864屏幕模式时，将端口EXP1和EXP2连接到主板。此模式下没有触摸功能。

2.使用串口屏模式时，通过RS232与主板上的TFT或AUX-1连接。此模式具有触摸功能

3.一键切换两种工作模式。按下编码器约3秒，直到出现模式选择页面，然后在选择模式后按下编码器。

:::

<img src={require('@site/docs/accessories-docs/display/TFT35-E3/img/TFT35_E3_Interface.png').default} width="50%"/>

## 软件配置

出厂已经包含固件，它可以直接使用。也可以按照以下方法进行升级

1. 从 GitHub repo [bigtreetech/BIGTREETECH-TouchScreenFirmware](https://github.com/bigtreetech/BIGTREETECH-TouchScreenFirmware) 下载固件
2. 然后把固件复制进 SD 卡根目录
3. 把 SD 卡插入板的SD卡插槽
4. 重新给主板通电或按下重置键
5. 等待10秒后更新完成
