---
sidebar_position: 1
description: HDMI 7 V1.0 文档
---

# HDMI 7 V1.0

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<img src={require('@site/docs/accessories-docs/display/HDMI7-v1-display/img/HDMI7_Title.png').default} width="45%" class="right-image"/>

## 产品规格

| Specification | HDMI 7         |
| ------------- | -------------- |
| 产品尺寸      | 100 x 165mm    |
| 安装尺寸      | 100 x 165mm    |
| 电源输入      | DC 5V          |
| 逻辑电压      | DC 3.3V        |
| 屏幕尺寸      | 7英寸IPS显示屏 |
| 屏幕分辨率    | 1024x600       |
| 屏幕视角      | 160°           |

</div>

## 尺寸

<img src={require('@site/docs/accessories-docs/display/HDMI7-v1-display/img/HDMI7_Dimension.png').default} width="80%"/>

## 接口示意图

<img src={require('@site/docs/accessories-docs/display/HDMI7-v1-display/img/HDMI7_Interface.png').default} width="80%"/>

## 硬件配置

### 连接到显示输出设备

1. 使用 USB Type-C 连接 HDMI7 到显示输出设备（与Raspberry Pi/PC/其他支持HDMI显示输出的设备兼容）。当连接到电脑时，电脑会在正常情况下自动加载驱动程序。在加载驱动程序之后，可以识别触摸设备。

2. 使用 HDMI 线连接 HDMI7 到显示输出设备。通常，连接HDMI电缆后，LCD可以在5秒内正常显示。

### 音频输出

将3.5毫米耳机/扬声器插入AUDIO接口，实现音频输出。

<img src={require('@site/docs/accessories-docs/display/HDMI7-v1-display/img/HDMI7_Audio.png').default} width="80%"/>

### 屏幕亮度调整

BIGTREETECH HDMI7 V1.0 支持亮度调节，可以通过 `Ks1` 按钮增加亮度，通过 `Ks3` 按钮降低亮度。

<img src={require('@site/docs/accessories-docs/display/HDMI7-v1-display/img/HDMI7_Brightness.png').default} width="80%"/>

### 显示方向调整

BIGTREETECH HDMI7 V1.0 支持通过 `Ks2` 按钮进行水平显示方向调整。

<img src={require('@site/docs/accessories-docs/display/HDMI7-v1-display/img/HDMI7_Direction.png').default} width="80%"/>

### 指示灯

当主板通电时：

电源指示灯D11（电源）红灯亮起，表示电源工作正常。

工作状态指示灯D12（状态）绿光闪烁，表示屏幕工作正常。

## 软件配置

### HDMI显示输出 (树莓派)

修改 `config.txt` 中的配置

```systemd title="config.txt"
# uncomment to force a specific HDMI mode (this will force VGA)
hdmi_group=2
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0
# uncomment to force a HDMI mode rather than DVI. This can make audio work in
# DMT (computer monitor) modes
hdmi_drive=1
```

### HDMI音频输出 (树莓派)

进入系统桌面后，右键单击右上角的音频源图标，然后选择HDMI。

<img src={require('@site/docs/accessories-docs/display/HDMI7-v1-display/img/HDMI7_Desktop.png').default} width="80%"/>
