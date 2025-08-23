---
sidebar_position: 2
---

# EBB 36 CAN 硬件功能

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

:::info[固件支持]
EBB 36 V1.0/V1.1/V1.2 目前只支持 Klipper 固件
:::

## 外观尺寸

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('./img/G0B1/EBB_G0B1_Diagram.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('./img/072/EBB_072_Diagram.png').default} width="450"/>
    </TabItem>
</Tabs>

## Pinout

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('./img/G0B1/EBB_G0B1_Pin.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('./img/072/EBB_072_Pin.png').default} width="450"/>
    </TabItem>
</Tabs>

## 硬件功能配置

### USB 接口供电

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        当 `EBB 36 v1.1 / v1.2` 通电的时候 LED1 才会亮起。`EBB 36` 右侧的 `VUSB` 是选择使用 USB 接口对 MCU 进行供电。
        <img src={require('./img/G0B1/EBB_G0B1_USB_Power.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        当 `EBB 36 v1.0` 通电的时候 `D1 LED` 才会亮起。`EBB 36` 上的 `VUSB` 是选择使用 USB 接口对 MCU 进行供电。
        <img src={require('./img/072/EBB_072_USB_Power.png').default} width="450"/>
    </TabItem>
</Tabs>

## 硬件安装

### NTC 100K 或 PT1000 

不带 31865 的版本： 使用 100K NTC 热敏电阻时无需插入跳线帽，`TH0`上拉电阻值为 `4.7K`。使用 `PT1000` 时，需要使用跳线帽将两个引脚短接，如下图所示。此时，`TH0`上拉电阻值为`2.2K`。

:::info[温度准确性]
这样使用 `PT1000` 的温度准确性会比使用 `MAX31865` 低
:::

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('./img/G0B1/EBB_G0B1_PT100.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('./img/072/EBB_072_PT100.png').default} width="450"/>
    </TabItem>
</Tabs>

### MAX 31865

<div class="div-table">
    <Tabs groupId="ebb-version">
        <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
            <img src={require('./img/G0B1/EBB_G0B1_TwoW.png').default} width="300" class="image-margin"/>
            <img src={require('./img/G0B1/EBB_G0B1_FourW.png').default} width="300" class="image-margin"/>
        </TabItem>
        <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
            <img src={require('./img/072/EBB_072_TwoW.png').default} width="300" class="image-margin"/>
            <img src={require('./img/072/EBB_072_FourW.png').default} width="300" class="image-margin"/>
        </TabItem>
    </Tabs>
</div>

:::info
MAX 31865 选择 PT100/PT1000 2线或4线配置

| 1   | 2   | 3   | 4   | Sensor Model  |
| --- | --- | --- | --- | ------------- |
| ON  | ON  | ON  | OFF | 2 wire PT100  |
| ON  | ON  | OFF | ON  | 2 wire PT1000 |
| OFF | OFF | ON  | OFF | 4 wire PT100  |
| OFF | OFF | OFF | ON  | 4 wire PT1000 |
:::

### BL-Touch 接线

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('./img/G0B1/EBB_G0B1_BLTouch.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('./img/072/EBB_072_BLTouch.png').default} width="450"/>
    </TabItem>
</Tabs>

### 耗材传感器

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('./img/G0B1/EBB_G0B1_Broke.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('./img/072/EBB_072_Broke.png').default} width="450"/>
    </TabItem>
</Tabs>

### Neopixel

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('./img/G0B1/EBB_G0B1_RGB.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('./img/072/EBB_072_RGB.png').default} width="450"/>
    </TabItem>
</Tabs>
