---
sidebar_position: 2
---

# Eddy Duo Hardware

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## **产品尺寸及接口**

<img src={require('./img/Eddy_Dimensions.png').default} alt="" width="600" />

用于计算 XY 偏移的线圈中心点如下：

<img src={require('./img/Eddy_Dimensions1.png').default} alt="" width="600" />

## **BOOT 按键位置**

<img src={require('./img/eddy_boot_1.png').default} alt="" width="600" />

BOOT 按钮在首次对 Eddy 烧录 Klipper 固件时使用；之后 Klipper 可以自动进入BOOT 模式并重新烧录固件。

**注意：**仅仅 Eddy V1.0 拥有 BOOT 功能，Eddy Coil V1.0 上的按键无功能。

## **安装指南** 

### 安装高度

确保 Eddy 的安装位置高于喷嘴 2 至 3 毫米，以确保最佳性能。如果在校准过程中遇到错误，这些可能与 Eddy 的安装高度有关。有关解决方案，请参阅本手册
的故障排除部分。

重要提示：需要注意的是，用户可能会将电流校准高度 20 毫米与 Eddy 的安装高度 2 至 3 毫米混淆。20 毫米的高度仅在本手册后续部分进行线圈电流校准时使用。

### 以 Voron2.4 为例

安装位置，完全替代原有 PL-08N 安装位
使用两颗 M3*25 螺丝（包装内附）将模块固定再 X Carriage 打印件上，如视图

<img src={require('./img/Eddy_Installation1.png').default} alt="" width="600" />

<img src={require('./img/Eddy_Installation2.png').default} alt="" width="600" />

### 在其他机器上的安装

用户可在我们的 GitHub 仓库以及其他常见模型分享平台中找到适用于多种常见机型的支架。在安装 Eddy 的过程中，请确保 PCB 侧（背面）与热端保持尽可能大的距离。此类布局有助于最小化从热端到 Eddy 的热传导。

### Eddy + Manta M5P

<img src={require('./img/Eddy_Connection.png').default} alt="" width="600" />

### Eddy + Manta M8P V2.0

<img src={require('./img/Eddy_Connection1.png').default} alt="" width="600" />

### Eddy Coil + EBB36 V1.2

<img src={require('./img/Eddy_Connection2.png').default} alt="" width="600" />

### Eddy Coil + EBB42 V1.2

<img src={require('./img/Eddy_Connection3.png').default} alt="" width="600" />

### Eddy Duo + MANTA M5P（USB）

<img src={require('./img/eddy_connection4.png').default} alt="" width="600" />

### Eddy Duo + MANTA M8P V2.0（USB）

<img src={require('./img/eddy_connection6.png').default} alt="" width="600" />

### Eddy Duo + MANTA M8P V2.0（CAN）

<img src={require('./img/eddy_connection7.png').default} alt="" width="600" />

### Eddy Duo + EBB36

<img src={require('./img/eddy_connection8.png').default} alt="" width="600" />

### Eddy Duo + EBB42

<img src={require('./img/eddy_connection9.png').default} alt="" width="600" />

### Eddy Duo + EBB SB

<img src={require('./img/eddy_connection10.png').default} alt="" width="600" />

### Octopus V1.1/Pro V1.0/Pro V1.0.1 + Eddy Duo（USB）

<img src={require('./img/eddy_connection11.png').default} alt="" width="600" />

### Octopus V1.1/Pro V1.0/Pro V1.0.1 + Eddy Duo（CAN）

<img src={require('./img/eddy_connection12.png').default} alt="" width="600" />

### Octopus Pro V1.1 + Eddy Duo（USB）

<img src={require('./img/eddy_connection13.png').default} alt="" width="600" />

### Octopus Pro V1.1 + Eddy Duo（CAN）

<img src={require('./img/eddy_connection14.png').default} alt="" width="600" />
