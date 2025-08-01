---
sidebar_position: 2
---

# Panda Touch 硬件

Panda Touch 硬件

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

:::info Panda Touch CAD 文件

Panda Touch 的 CAD 文件可以在 GitHub repo [bigtreetech/PandaTouch/3D](https://github.com/bigtreetech/PandaTouch/tree/master/3D)

:::

## 装配说明

### 概述

<img
    src={require('./img/pt_back.png').default}
    alt="" width="550"
/>

:::tip 

将电源开关滑动至`锂电池电源`，Panda Touch即可使用锂电池运行，实现便携性。将其滑动至`DC 5V`，从磁性充电座直接供电，从而延长内部电池的使用寿命。如果您经常打开和关闭打印机，建议使用此模式。将开关滑动至`OFF`（关闭）可关闭 Panda Touch。

:::

### 充电座

<img
    src={require('./img/charging_dock.png').default}
    alt="" width="550"
/>

:::tip 

电源输入配备了热插拔保护，允许用户热插拔电源

:::

### 包装清单

| ![](./img/pl_1.png)     | ![](./img/pl_2.png) |
|:-----------------------:|:-------------------:|
| Panda Touch x 1         | 安装支架 x 1            |
| ![](./img/pl_3.png)     | ![](./img/pl_4.png) |
| 磁性充电座 x 1               | USB-C充电电缆 x 1       |
| ![](./img/pl_5.png)     | ![](./img/pl_6.png) |
| M3x6螺钉 x 4<br/>六角扳手 x 1 | BTT鸭 x 1            |

### 安装Panda Touch

* 如图所示，使用六角/内六角扳手和两个M3x6 FHCS组装充电座和安装支架。

<img
    src={require('./img/pt_1_1.png').default}
    alt="" width="300"
/>

* 从安装支架的底部剥离薄膜。

<img
    src={require('./img/pt_1_2.png').default}
    alt="" width="300"
/>

* 确保打印机表面清洁、无油、油脂等，将组装好的充电座固定在原始屏幕的中央。施加压力使其完全粘附，并等待12小时以获得最佳粘附力。

<img
    src={require('./img/pt_1_3.png').default}
    alt="" width="300"
/>

* 将Panda Touch连接到充电座。

<img
    src={require('./img/pt_1_4.png').default}
    alt="" width="300"
/>

### 接线和电源连接

- 卸下打印机USB端口上的泡沫，即可访问该端口。

    <img src={require('./img/pt_2_1.png').default} alt="" width="300" />

- 将充电电缆穿过打印机右侧的孔，然后将USB-C端插入充电底座的电源输入。
    
    <img src={require('./img/pt_2_2.png').default} alt="" width="300" />

- 将充电电缆的USB-A端插入打印机上的USB端口以连接电源。然后如图所示将电缆布置在夹子中。

> 提示:
> 请 100% 确定您已将电缆拧入夹子，以防止工具头在归位过程中卡住电缆。

    <img src={require('./img/pt_2_3.png').default} alt="" width="300" />

- 后部电源开关上有三个选项。
  * 在`关闭`位置，电池将充电，但Panda Touch不会通电。

  * 当切换到电池位置时，USB将为电池充电，同时为Panda Touch供电。如果从底座上卸下Panda Touch，则电池将接管并为其供电长达30分钟。回到底座后，USB将再次恢复为Panda Touch充电和供电。建议不经常打开和关闭打印机的用户使用此模式。请注意，没有电池电量指示灯。Panda Touch专为远离码头的短时间使用而设计，不适合长时间移动使用。

  * 当切换到DC 5V位置时，Panda Touch直接由USB输入供电，同时仍在为电池充电。将其从底座上卸下将关闭电源，而Panda Touch不会耗尽电池电量。建议经常打开和关闭打印机的用户使用此模式，因为它可以保持电池充电周期。如果这些用户希望在便携式模式下使用Panda Touch，那么他们可以在将其从底座上取下后将开关切换到电池电源。

    <img src={require('./img/pt_2_4.png').default} alt="" width="300" />

- Panda Touch已成功安装并通电。请按照屏幕上的说明进行下一步设置。
  
    <img src={require('./img/pt_2_5.png').default} alt="" width="300" />
