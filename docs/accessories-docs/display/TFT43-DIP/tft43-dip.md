---
sidebar_position: 1
description: TFT 43 DIP 文档
---

# TFT 43 DIP

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<img src={require('./img/TFT43_DIP_Title.png').default} width="45%" class="right-image"/>

## 产品简介

TFT43-DIP是带电容式触摸屏的树莓派显示器。

</div>

## 软件配置

:::note

"2022-04-04"之后的Raspberry Pi操作系统具有内置的DPI驱动程序，因此我们只需要在 `/boot/config.txt` 文件中进行简单配置即可使用此屏幕。

"2022-09-22"的操作系统显示180度旋转功能异常，请不要使用。

::: 

### 显示功能

将以下配置添加到 `/boot/config.txt` 文件的 `[all]` 部分。(通常，它可以添加到/boot/config.txt文件的底部)

```systemd title="/boot/config.txt"
dtoverlay=vc4-kms-dpi-generic
dtparam=rgb666-padhi,clock-frequency=32000000
dtparam=hactive=800,hfp=16,hsync=1,hbp=46
dtparam=vactive=480,vfp=7,vsync=3,vbp=23
dtparam=backlight-gpio=19
dtparam=rotate=0
```

:::info[配置显示器旋转]

`rotate=显示旋转` 可设置的值包括 `0`, `90`, `180`, `270`。默认值为 `0`

:::

### 触摸功能

使用以下命令下载配置文件

```shell
sudo wget https://raw.githubusercontent.com/bigtreetech/TFT43-DIP/master/gt911_btt_tft43_dip.dtbo -O /boot/overlays/gt911_btt_tft43_dip.dtbo
```

并将以下配置添加到 `/boot/config.txt` 文件的 `[all]` 部分。

``` systemd title="/boot/config.txt"
dtoverlay=gt911_btt_tft43_dip
dtparam=rotate_0
```

:::info [旋转触摸]

`rotate_*` 是触摸旋转，可设置为 `rotate_0`, `rotate_90`, `rotate_180`, `rotate_270` 与显示器旋转相对应

:::

## 示例配置文件

### 正常显示

复制 gt911_btt_tft43_dip.dtbo（./gt911_bttl_tft43.dtbo）文件

将以下配置添加到 `/boot/config.txt` 文件的 `[all]` 部分

```systemd title="/boot/config.txt"
dtoverlay=vc4-kms-dpi-generic
dtparam=rgb666-padhi,clock-frequency=32000000
dtparam=hactive=800,hfp=16,hsync=1,hbp=46
dtparam=vactive=480,vfp=7,vsync=3,vbp=23
dtparam=backlight-gpio=19
dtparam=rotate=0

dtoverlay=gt911_btt_tft43_dip
dtparam=rotate_0
```

### 旋转90度显示

复制 gt911_btt_tft43_dip.dtbo（./gt911_bttl_tft43.dtbo）文件

将以下配置添加到 `/boot/config.txt` 文件的 `[all]` 部分

```systemd title="/boot/config.txt"
dtoverlay=vc4-kms-dpi-generic
dtparam=rgb666-padhi,clock-frequency=32000000
dtparam=hactive=800,hfp=16,hsync=1,hbp=46
dtparam=vactive=480,vfp=7,vsync=3,vbp=23
dtparam=backlight-gpio=19
dtparam=rotate=90

dtoverlay=gt911_btt_tft43_dip
dtparam=rotate_90
```
