---
sidebar_position: 1
description: TFT 35 文档
---

# TFT 35

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<img src={require('@site/docs/module-docs/display/TFT35/img/TFT35_V3.0_Title.png').default} width="45%" class="right-image"/>

## 产品规格

| Specification | TFT 35                                 |
| ------------- | -------------------------------------- |
| 尺寸          | 110x58mm                               |
| 输入电压      | 5V DC                                  |
| 安装尺寸      | 103.76*49.43 mm                        |
| SD卡逻辑电压  | 3.3V或5V，支持MEGA2560主板，兼容性更高 |

</div>

## 尺寸

<img src={require('@site/docs/module-docs/display/TFT35/img/TFT35_V3.0_Diagram.png').default} width="50%"/>

## 接口示意图

<img src={require('@site/docs/module-docs/display/TFT35/img/TFT35_V3.0_Interface.png').default} width="50%"/>

:::info 

1. 使用12864屏幕模式时，将端口EXP1和EXP2连接到主板。此模式下没有触摸功能。（使用SKR MINI E3或SKR E3 DIP，只需将EXP3连接到主板即可）

2. 使用串口屏模式时，通过RS232与主板上的TFT或aux-2连接。此模式具有触摸功能。

3. 一键切换两种工作模式。按下旋转编码器约3秒钟，直到出现模式选择页面，然后在选择模式后按下编码器。

:::

## 软件配置

出厂已经包含固件，它可以直接使用。也可以按照以下方法进行升级

1. 从 GitHub repo [bigtreetech/BIGTREETECH-TouchScreenFirmware](https://github.com/bigtreetech/BIGTREETECH-TouchScreenFirmware) 下载固件
2. 然后把固件复制进 SD 卡根目录
3. 把 SD 卡插入板的SD卡插槽
4. 重新给主板通电或按下重置键
5. 等待10秒后更新完成
