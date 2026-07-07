---
sidebar_position: 2
description: Octopus Pro 硬件详细
---

# Octopus Pro Hardware Features

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import ThemedImage from '@theme/ThemedImage';

{/* import lib end */}

## Dimensions

:::info

Size reference: GitHub Repo [bigtreetech/BIGTREETECH-OCTOPUS-Pro/Hardware/BIGTREETECH Octopus Pro - SIZE](https://github.com/bigtreetech/BIGTREETECH-OCTOPUS-Pro/blob/master/Hardware/BIGTREETECH%20Octopus%20Pro%20-%20SIZE.pdf)

:::

## Pinout

<a href={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-pinout-light.png').default} target="_blank">
    <ThemedImage
        alt="octopus-pro-pinout"
        sources={{
            light: require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-pinout-light.png').default,
            dark: require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-pinout-dark.png').default,
        }} width="100%"
    />
</a>

## Hardware Feature Configuration

### USB Power Supply

Simply insert a jumper to power the octopus via USB-C. This makes it easier to compile and download firmware directly to the mainboard using DFU mode.

If you do not connect this jumper, you must power the board through the main input power supply if you want to communicate via USB-C.

<ImageView src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-usb-power.png').default} width="80%"/>

### Automatic Power Off Wiring

When using the BIGTREETECH Relay V1.2 module, you can wire it as shown in the figure below.

<ImageView src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-relay.png').default} width="80%"/>

:::warning

The `Relay 1.2` module continues to supply power even after the mainboard power is cut, making it extremely dangerous to touch while the printer is still connected to power. Always disconnect all main power before handling this wiring.

:::

### BL TOUCH

When using the BL Touch, connect it to the motherboard as shown in the figure below.

<ImageView src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-bltouch.png').default} width="80%"/>

### Neopixel

<ImageView src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-neopix.png').default} width="80%"/>

### Raspberry Pi

Octopus Pro supports connecting to a Raspberry Pi for printing. There are several connection methods available for connecting to a Raspberry Pi.

- Connect Raspberry Pi directly to USB-C port
- Connect Raspberry Pi using direct serial connection via UART or SPI

### Motor Driver Configuration

<Tabs groupId="octopus-stepper-driver">
    <TabItem value="tmc-uart" label="Uart 模式" default>
        使用 Uart 模式连接驱动
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-uart.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI 模式">
        使用 SPI 模式连接驱动
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-spi.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / dir 模式">
        使用不支持 Uart 或者 SPI 的驱动。
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-step-dir.png').default}
            alt="" width="100%"
        />
        以下是跳线参考，不同的驱动会有不同的跳线配置
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-step-dir-config.png').default}
            alt="" width="100%"
        />
    </TabItem>
</Tabs>

### Motor Drive Voltage Selection

:::warning

Do not plug or unplug the jumper caps while powered.

:::

<Tabs groupId="octopus-driver-v">
    <TabItem value="VBB" label="Octopus Pro VBB" default>
        当使用 `VBB` 进行供电的时候。来源为主板 `Power` 输入。最高电压为 `24V`。
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-vbb.png').default}
            alt="octo pro vbb" width="60%"
        />
    </TabItem>
    <TabItem value="high-oltage" label="Octopus Pro High Voltage">
        当使用 `High Voltage` 进行供电的时候。来源为主板 `Motor Power` 输入。最高电压为 `56V`。需要注意驱动最大电压范围。
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-hv.png').default}
            alt="octo pro high voltage" width="60%"
        />
    </TabItem>
</Tabs>

### Fan Voltage Selection

Octopus_Pro features 6 PWM fan outputs and two "always-on" fan outputs. It also includes a dedicated pin for proximity sensors or probes.

All fan outputs and proximity sensor inputs can be individually selected to derive their voltage from the respective pin headers by configuring the jumpers associated with each header.

Configure the jumpers as shown below to select 24V (note that all jumpers are displayed in the same configuration, even though they can be configured individually).

<Tabs groupId="octopus-fan-v">
    <TabItem value="24v-fan" label="24V 风扇 / 接近开关" default>
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-24.png').default}
            alt="octo pro fan 24" width="100%"
        />
    </TabItem>
    <TabItem value="12v-fan" label="12V 风扇 / 接近开关">
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-12.png').default}
            alt="octo pro fan 12" width="100%"
        />
    </TabItem>
    <TabItem value="5v-fan" label=" 5V 风扇 / 接近开关">
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-5.png').default}
            alt="octo pro fan 5" width="100%"
        />
    </TabItem>
</Tabs>

### TMC STALLGUARD Jumpers Configuration

The "diag" jumper for connecting the diagnostic output pin to the driver's endstop input supporting the stall guard feature (e.g., TMC2209/TMC2226) can be found at the location shown in the following figure.

The exact diag number can be found by checking the pinout file or silkscreen under the board.

<ImageView src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-spi.png').default} width="80%"/>

### MAX 31865

<div class="div-table">

<ImageView src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-max-31865.png').default} width="50%" class="right-image"/>

MAX 31865 选择 PT100/PT1000 2线或4线配置

| 1   | 2   | 3   | 4   | Sensor Model  |
| --- | --- | --- | --- | ------------- |
| ON  | ON  | ON  | OFF | 2 wire PT100  |
| ON  | ON  | OFF | ON  | 2 wire PT1000 |
| OFF | OFF | ON  | OFF | 4 wire PT100  |
| OFF | OFF | OFF | ON  | 4 wire PT1000 |

</div>
