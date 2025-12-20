---
sidebar_position: 2
description: Manta M8P V2 硬件功能配置
---

# Manta M8P v2 硬件功能

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 外观尺寸

:::info[STEP 模型]

Manta M8P v2 模型 [BIGTREETECH MANTA M8P V2.0.zip](https://github.com/bigtreetech/Manta-M8P/blob/master/V2.0/3D/BIGTREETECH%20MANTA%20M8P%20V2.0.zip)

:::

<img src={require('./img/m8p-v2-dimensions.png').default} width="100%"/>

## Pinout

:::info[原理图 / Schematic]

Manta M8P v2 原理图 [BIGTREETECH MANTA M8P V2.0-SCH.pdf](https://github.com/bigtreetech/Manta-M8P/blob/master/V2.0/Hardware/BIGTREETECH%20MANTA%20M8P%20V2.0-SCH.pdf)

:::

<img src={require('./img/m8p-v2-pinout.png').default} width="100%"/>

## 步进电机驱动

### 电机驱动配置 (SPI / Uart)

<Tabs groupId="m8p-v2-stepper-driver">
    <TabItem value="tmc-uart" label="Uart 模式" default>
        使用 Uart 模式连接驱动
        <img
            src={require('./img/m8p_v2_0_tmc_uart.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI 模式">
        使用 SPI 模式连接驱动
        <img
            src={require('./img/m8p_v2_0_tmc_spi.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / dir 模式">
        A4988 / DRV8825 使用跳线帽短接 MS0-MS2 以调整细分

        :::info[已知问题]
        如果使用 `A4988` 或 `DRV8825` 需要短接 `RST` 和 `SLP` 才能正常工作
        :::
        <img src={require('./img/m8p_v2_0_step-dir.png').default} width="100%"/>
    </TabItem>
</Tabs>

### 驱动电压选择

<Tabs groupId="m8p-v2-driver-power">
    <TabItem value="m8p-power-24" label="使用 24V 电源" default>
        <img src={require('./img/M8P_driver_24.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-power-48" label="使用 48V 电源">
        <img src={require('./img/M8P_driver_48.png').default} width="100%"/>
    </TabItem>
</Tabs>

### TMC Sensorless

<img src={require('./img/m8p_v2_0_tmc_sensorless.png').default} width="100%"/>

## 核心板

### 核心板安装

<Tabs groupId="m8p-v2-cm">
    <TabItem value="m8p-cm-rpi" label="使用树莓派 CM4/CM5" default>
        <img src={require('./img/M8P-v2_cm_rpi.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-cm-cb" label="使用 CB1/CB2">
        <img src={require('./img/M8P-v2_cm_cb.png').default} width="100%"/>
    </TabItem>
</Tabs>

### USB 供电

M8P主板上电之后，板子左下角的灯会亮起，表示供电正常。板子中部的VUSB是电源选择端，仅当使用USB给主板供电或需通过USB向外供电时，才需要使用跳帽将它短接。

<img src={require('./img/m8p_v2_0_usb.png').default} width="50%"/>

### DSI / CSI连接

:::info[需要硬件支持]

DSI / CSI 需要核心板硬件支持

:::

<img src={require('./img/m8p_v2_0_dsi.png').default} width="100%"/>

## 风扇

### 风扇电压选择

使用跳线帽配置输出电压

:::warning

在选择电压之前，请确认风扇的工作电压

:::

<img src={require('./img/m8p_v2_0_cnc.png').default} width="100%"/>

### 4Pin PWM 风扇接线

<img src={require('./img/m8p_v2_0_4pin_fan.png').default} width="60%"/>

## 传感器

### 100K NTC 或 PT1000 设置

当使用100K NTC热敏电阻时，无需插入跳线帽 `TH0` `TH1` `TH2` `TH3` 的上拉电阻为 4.7K 0.1%。

:::info

使用PT1000时，需要插入 PT 的跳线帽。此时 `TH0` `TH1` `TH2` `TH3` 的上拉电阻为2.2K。

这样读取的温度精度将远不如MAX31865读取的精度

<img src={require('./img/m8p_v2_0_100k.png').default} width="20%"/>

:::

### BLTouch

<img src={require('./img/m8p_v2_0_bltouch.png').default} width="100%"/>

### 接近开关接线

<Tabs groupId="m8p-v2-proximity">
    <TabItem value="m8p-v2-proximity-npn" label="NPN 接近开关" default>
        <img src={require('./img/m8p_v2_0_proximity1.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-v2-proximity-pnp" label="PNP 接近开关">
        <img src={require('./img/m8p_v2_0_proximity.png').default} width="80%"/>
    </TabItem>
</Tabs>

### I2C接线 (温湿度传感器)

<img src={require('./img/m8p_v2_0_i2c.png').default} width="80%"/>

## 其他硬件

### Neopixel 

<img src={require('./img/m8p_v2_0_rgb.png').default} width="80%"/>

### 舵机接线

<img src={require('./img/m8p_v2_0_servo.png').default} width="80%"/>

