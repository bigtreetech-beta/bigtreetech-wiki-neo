---
sidebar_position: 1
description: K HUB
---

# K HUB

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

<div class="div-table">

<ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-title.webp').default} width="40%" class="right-image"/>

## Product Overview

The BIGTREETECH K HUB V1.0 is a high-performance USB 2.0 expansion board engineered by Shenzhen BIQU Innovation Technology Co., Ltd. This specialized hardware is optimized for Klipper-based USB architectures, offering robust quad-port expansion to consolidate peripheral management and enhance system scalability in DIY 3D printing environments.

## Key Features

- Supports 24V or 5V power supply;
- All ports feature ESD protection;
- 24V power port includes reverse polarity protection;
- Utilizes high-power DC-DC chips for increased 5V current output;
- Power interface employs quick-connect plugs for DIY convenience;
- Includes initial enclosure model files and matching finished components for self-assembly printing.

## Product Specifications

| KHub | Specification |
| ------ | ------ |
| Board Dimensions | 109.6mm x 21.6mm |
| USB Output Ports | 4x USB Type-A female ports (USB 2.0), each outputting 5V 1.5A |
| Type-C Input Port | Type-C signal input port, power input 5V 2A |
| 24V Input Port | 1x 24V 3A input port |
| Fan Output Port | 1x 24V fan output port |
| Included Accessories | 1x fan, 1x heat sink, assembly screws |

</div>

## Interface Overview

### Interface Diagram

<ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-interface.webp').default} width="100%"/>

### Indicator Light Explanation

- Green: Type-C Power Supply
- Blue: 24V Power Supply

<ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-led.webp').default} width="30%"/>

## Parts List

| Part Name | Specification | Quantity |
| -------- | ------ | ---- |
| Screw | Round-head hex socket self-tapping screw M2.6×14 | 7 |
| Screw | Round-head hex socket self-tapping screw M2.6×10 | 2 |
| Screw | BHCS M3×10 | 2 |
| Boat Nut | M3 Boat Nut | 2 |
| Fan | 24V | 1 |

## Assembly Steps

### Step 1 Install DIN Mounting Bracket

Use 2 M2.6×10 self-tapping screws to connect the base housing to the DIN mounting bracket (required for DIN version, not required for profile version).

<ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step1.webp').default} width="60%"/>

<ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step2.webp').default} width="60%"/>

### Step 2 Board and Top Cover

Attach the top cover to the motherboard and bottom cover using four M2.6×14 self-tapping screws.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step3.webp').default} width="60%"/>

### Step 3 Install the Cover

Using one filament (1.75mm), secure the cover to the top plate.

<img src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step4.webp').default} width="60%"/>

<img src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step5.webp').default} width="60%"/>

### Step 4 Install Fan

Install the fan to the printed part using three M2.6×14 screws.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step6.webp').default} width="60%"/>

## Exploded view diagram

<Tabs groupId="khub-version">
    <TabItem value="khub-din" label="DIN Version exploded view diagram" default>
        <ImageView src={require('./img/k-hub-install-step7-en.webp').default} width="60%"/>
    </TabItem>
    <TabItem value="khub-extrusion" label="Extrusion version exploded view diagram">
        <ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step8.webp').default} width="60%"/>
    </TabItem>
</Tabs>

## Install Reference

<Tabs groupId="khub-version">
    <TabItem value="khub-din" label="DIN Install Reference" default>
        <ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step9.webp').default} width="60%"/>
    </TabItem>
    <TabItem value="khub-extrusion" label="Extrusion Install Reference">

        Use two M3×10 screws and two M3 boat-shaped nuts to mount the K HUB onto the Extrusion.

        <ImageView src={require('@site/docs/board-docs/iot-series/iot-khub-v1/img/k-hub-install-step10.webp').default} width="60%"/>
    </TabItem>
</Tabs>

## Important Notes

- The current ratings marked on the output ports are valid only when 24V is applied; otherwise, only the current supplied by the USB input is available.
- Each USB port outputs 5V with a maximum current of 1.5A.
- Ensure the polarity of the 24V input power supply is correct. Although the board features reverse polarity protection, proper connection ensures normal device operation.
- When installing the fan, pay attention to its direction to ensure effective heat dissipation;
- Exercise caution when using a soldering iron to avoid burns.
