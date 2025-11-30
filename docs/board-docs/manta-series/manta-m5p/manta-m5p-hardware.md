---
sidebar_position: 2
description: Manta M5P 硬件功能配置
---

# Manta M5P 硬件功能

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 外观尺寸

:::info[STEP 模型]

Manta M5P 模型 [BIGTREETECH MANTA M5P-step.rar](https://github.com/bigtreetech/Manta-M5P/blob/master/3D/BIGTREETECH%20MANTA%20M5P-step.rar)

:::

<Tabs groupId="m5p-dim">
    <TabItem value="m5p-dim-1" label="正面尺寸" default>
        <img src={require('./img/M5P_Dimension1.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m5p-dim-2" label="反面尺寸">
        <img src={require('./img/M5P_Dimension2.png').default} width="80%"/>
    </TabItem>
</Tabs>

## Pinout

:::info[原理图 / Schematic]

Manta M5P 原理图 [BIGTREETECH MANTA M5P V1.0-SCH.pdf](https://github.com/bigtreetech/Manta-M5P/blob/master/Hardware/BIGTREETECH%20MANTA%20M5P%20V1.0-SCH.pdf)

:::

<img src={require('./img/manta-m5p-pinout.png').default} width="100%"/>

## 步进电机驱动

### 驱动模式

<Tabs groupId="m5p-stepper-driver">
    <TabItem value="tmc-uart" label="Uart 模式" default>
        使用 Uart 模式连接驱动
        <img
            src={require('./img/manta-m5p-driver-uart.png').default}
            alt="" width="80%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI 模式">
        使用 SPI 模式连接驱动
        <img
            src={require('./img/manta-m5p-driver-spi.png').default}
            alt="" width="80%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / DIR 模式">
        A4988 / DRV8825 使用跳线帽短接 MS0-MS2 以调整细分
        <img
            src={require('./img/manta-m5p-driver-step.png').default}
            alt="" width="80%"
        />
    </TabItem>
</Tabs>

### TMC Sensorless

<img src={require('./img/manta-m5p-sensorless.png').default} width="80%"/>

### 驱动电压选择

<Tabs groupId="m5p-driver-power">
    <TabItem value="m5p-power-24" label="使用 24V 电源" default>
        <img src={require('./img/manta-m5p-driver-24.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m5p-power-48" label="使用 48V 电源">
        <img src={require('./img/manta-m5p-driver-48.png').default} width="80%"/>
    </TabItem>
</Tabs>

## 核心板

### 核心板安装

<Tabs groupId="m5p-cm">
    <TabItem value="m5p-cm-rpi" label="使用树莓派 CM4/CM5" default>
        <img src={require('./img/m5p_cm_rpi.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m5p-cm-cb" label="使用 CB1/CB2">
        <img src={require('./img/m5p_cm_cb.png').default} width="80%"/>
    </TabItem>
</Tabs>

### USB 供电

MANTA M5P通电后，MCU左侧的红灯D22将亮起，表示已通电。当仅使用USB为板供电或通过USB供电时，请将跳线帽插入VUSB。

<img src={require('./img/M5P_USB_PS.png').default} width="45%"/>

### DSI / CSI连接

:::info[需要硬件支持]

DSI / CSI 需要核心板硬件支持

:::

<img src={require('./img/M5P_DSI.png').default} width="100%"/>

## 风扇

### 风扇电压选择

使用跳线帽配置输出电压

:::warning

在选择电压之前，请确认风扇的工作电压

:::

<img src={require('./img/manta-m5p-fan-voltage.png').default} width="40%"/>

## 传感器

### BLTouch

<img src={require('./img/M5P_BLTouch_Wiring.png').default} width="80%"/>

### 100K NTC 或 PT1000 设置

当使用100K NTC热敏电阻时，无需插入跳线帽 `TH0` `TH1` 的上拉电阻为 4.7K 0.1%。

:::info[使用 PT1000]

使用PT1000时，需要插入 PT 的跳线帽。此时 `TH0` `TH1` 的上拉电阻为2.2K。

这样读取的温度精度将远不如MAX31865读取的精度

<img src={require('./img/M5P_100K.png').default} width="20%"/>

:::

### 耗材传感器

<img src={require('./img/M5P_Filament.png').default} width="80%"/>

### 接近开关接线

使用 PNP 接近开关

<img src={require('./img/M5P_Proximity-PNP.png').default} width="80%"/>

:::info[NPN 接近开关]

NPN 接近开关不需要接 `Pull UP` 跳线帽

:::

## 其他硬件

### Neopixel 

<img src={require('./img/M5P_RGB_Wiring.png').default} width="80%"/>
