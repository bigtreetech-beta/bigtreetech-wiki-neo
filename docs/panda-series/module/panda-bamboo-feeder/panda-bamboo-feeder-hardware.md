---
sidebar_position: 2
description: Panda Bamboo Feeder 硬件
---

# Panda Bamboo Feeder 硬件

## 产品外观尺寸 {/* #p_size */}

:::info[模型]

[外尺寸参考模型](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Reference%20Cad)

:::

<ImageView src={require('./img/03size.webp').default} width="50%"/>

## 硬件接口

<ImageView src={require('./img/hardware.webp').default} width="50%"/>

- `退料键`: 用于退出耗材。

- `进料键`: 用于将耗材送入打印机挤出机。

- `Type-C` 接口: 可通过USB进行恢复出厂设置。

## 注意事项

1. 最多三个熊猫喂竹器联动使用。

2. 如需同时使用多个熊猫喂竹器，位于最上方的喂竹器需要额外连接 DC 电源（需额外购买 24V/2.8A 电源适配器）。由于拓竹 AMS 接口供电能力有限，若同时为多个熊猫喂竹器供电，可能导致打印机运行异常。

3. 喂竹器可与 AMS 及 AMS 2 Pro 同时安装，但是不可同时使用， 通过AMS打印时请使用电源适配器上的开关，给喂竹器断电。

4. 喂竹器仅为连续打印续料以及耗材缓冲设计，无多色打印功能。

## 安装指南

### P1/X1 系列机型

1. 准备打印件

    提前打印好需要的安装打印件,[点击此处下载。](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Mounting%20solution/Universal%20Mounting%20Bracket%20for%20PX%20series)

    <ImageView src={require('./img/install00.webp').default} width="50%"/>

2. 安装固定挂扣

    使用包装内的螺丝，将打印好的“固定挂扣”固定在熊猫喂竹器的背部。

    <ImageView src={require('./img/install01.webp').default} width="30%"/>

3. 安装快拆安装架

    如图所示，将线缆穿过打印好的的“快拆安装架”并放入理线槽内（请确保 DC 接头和 MX3.0 接头方向正确）。

    <ImageView src={require('./img/install02.webp').default} width="30%"/>

    将打印的“理线锁扣”卡入快拆安装架中。

    <ImageView src={require('./img/install03.webp').default} width="30%"/>

    <ImageView src={require('./img/install04.webp').default} width="30%"/>

4. 安装底座

    排好线后，将快拆安装架整体滑入打印好的“固定底座”中。

    <ImageView src={require('./img/install05.webp').default} width="30%"/>

5. 固定喂竹器

    通过固定挂扣将喂竹器卡入快拆安装架上，并接好线缆。

    <ImageView src={require('./img/install06.webp').default} width="30%"/>

    使用随附的纳米双面胶粘贴于固定底座背面并移除离型纸，后将固定底座粘贴于机器合适的位置，如打印机侧面。

    <ImageView src={require('./img/install06.2.webp').default} width="20%"/>

### Panda Perch 安装

如果你有 BIQU Panda Perch，可在步骤二后通过固定挂扣将喂竹器卡入其侧面的六角孔中并用下图卡扣将挂扣牢牢固定在Panda Perch 内部。（亦需提前打印好固定挂扣，请[点击此处下载](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Mounting%20solution/Panda%20Perch%20H2D%20mounting%20bracket)）

<ImageView src={require('./img/install07.webp').default} width="30%"/>

<ImageView src={require('./img/install08.webp').default} width="30%"/>

### A1 系列机型

1. 准备打印件

    提前打印好需要的安装打印件：缠料检测删除， 安装支架。[点击此处下载模型文件](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Mounting%20solution/A1)。

    <ImageView src={require('./img/a1install00.01.webp').default} width="30%"/>

    <ImageView src={require('./img/a1install00.02.webp').default} width="30%"/>

2. 开始安装

    使用螺丝刀轻轻按压图示位置打开卡扣，切勿用力过猛以免损坏。

    <ImageView src={require('./img/a1install01.webp').default} width="30%"/>

    取下弹簧，并将图中圈出的固定环旋转 90 度以卸下。

    <ImageView src={require('./img/a1install02.webp').default} width="30%"/>

    将缠料检测删除模块插入打印头。

    <ImageView src={require('./img/a1install03.webp').default} width="30%"/>

    重新装回刚才卸下的固定环。

    <ImageView src={require('./img/a1install04.webp').default} width="30%"/>

    注意安装方向：固定环上的突起部分必须朝向切刀侧。

    <ImageView src={require('./img/a1install05.webp').default} width="30%"/>

    使用包装内的螺丝，将打印好的安装支架固定在喂竹器背部（请留意支架的安装方向，如图所示）。

    <ImageView src={require('./img/a1install06.webp').default} width="30%"/>

    如图所示，将其卡入耗材架的顶端。

    <ImageView src={require('./img/a1install07.webp').default} width="30%"/>

    :::info

    进料管优化：如果您仅将喂竹器作为缓冲器使用，或直接从该料架供料，请将进料口的 PTFE 管更换为稍长一些的规格，以防止耗材缠绕。

    :::

    弧度提醒：注意，PTFE 管不宜过长或过短，应保持自然,顺滑的曲线弧度。

    <ImageView src={require('./img/a1install08.webp').default} width="30%"/>

### DIY定制支架

可[参考此处](#p_size)下载外尺寸参考模型自行设计其他打印机的安装支架。
