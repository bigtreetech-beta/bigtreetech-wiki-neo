---
sidebar_position: 2
---

# EBB 36 CAN Hardware 

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

:::info[Firmware support]

EBB 36 V1.0/V1.1/V1.2 currently only supports Klipper firmware

:::

## Dimensions

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_Diagram.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_Diagram.png').default} width="450"/>
    </TabItem>
</Tabs>

## Pinout

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_Pin.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_Pin.png').default} width="450"/>
    </TabItem>
</Tabs>

## Hardware Function Configuration

### USB Power

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        LED1 lights up only when `EBB 36 v1.1 / v1.2` is powered on. The `VUSB` on the right side of `EBB 36` is used to select USB interface power for the MCU.
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_USB_Power.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        The `D1 LED` lights up only when `EBB 36 v1.0` is powered on. The `VUSB` on `EBB 36` is used to select USB interface power for the MCU.
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_USB_Power.png').default} width="450"/>
    </TabItem>
</Tabs>

## Hardware Installation

### NTC 100K or PT1000

For versions without 31865: When using a 100K NTC thermistor, no jumper is needed, and the `TH0` pull-up resistor value is `4.7K`. When using a `PT1000`, a jumper must short the two pins as shown below. At this point, the `TH0` pull-up resistor value is `2.2K`.

:::info[Temperature Accuracy]
Using PT1000 in this way results in lower temperature accuracy compared to using `MAX31865`.
:::

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_PT100.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_PT100.png').default} width="450"/>
    </TabItem>
</Tabs>

### MAX 31865

<div class="div-table">
    <Tabs groupId="ebb-version">
        <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
            <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_TwoW.png').default} width="300" class="image-margin"/>
            <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_FourW.png').default} width="300" class="image-margin"/>
        </TabItem>
        <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
            <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_TwoW.png').default} width="300" class="image-margin"/>
            <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_FourW.png').default} width="300" class="image-margin"/>
        </TabItem>
    </Tabs>
</div>

:::info
MAX 31865 selects PT100/PT1000 2-wire or 4-wire configuration

| 1   | 2   | 3   | 4   | Sensor Model  |
| --- | --- | --- | --- | ------------- |
| ON  | ON  | ON  | OFF | 2 wire PT100  |
| ON  | ON  | OFF | ON  | 2 wire PT1000 |
| OFF | OFF | ON  | OFF | 4 wire PT100  |
| OFF | OFF | OFF | ON  | 4 wire PT1000 |
:::

### BL-Touch wire

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_BLTouch.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_BLTouch.png').default} width="450"/>
    </TabItem>
</Tabs>

### Filament Sensor

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_Broke.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_Broke.png').default} width="450"/>
    </TabItem>
</Tabs>

### Neopixel

<Tabs groupId="ebb-version">
    <TabItem value="ebb-36-1_2" label="EBB 36 V1.1 / V1.2" default>
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/G0B1/EBB_G0B1_RGB.png').default} width="450"/>
    </TabItem>
    <TabItem value="ebb-36-1_0" label="EBB 36 V1.0">
        <img src={require('@site/docs/board-docs/ebb-series/ebb-36/img/072/EBB_072_RGB.png').default} width="450"/>
    </TabItem>
</Tabs>
