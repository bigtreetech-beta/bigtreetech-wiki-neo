---
sidebar_position: 2
description: Octopus Pro Hardware
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
    <TabItem value="tmc-uart" label="Uart Mode" default>
        Use Uart to connect
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-uart.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI Mode">
        Connecting the Driver Using SPI Mode
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-spi.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / dir Mode">
        Use a driver that does not support UART or SPI.
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-step-dir.png').default}
            alt="" width="100%"
        />
        The following is a jumper reference; different drivers may have different jumper configurations.
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
        When using `VBB` for power, the source is the motherboard's `Power` input. The maximum voltage is `24V`.
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-vbb.png').default}
            alt="octo pro vbb" width="60%"
        />
    </TabItem>
    <TabItem value="high-oltage" label="Octopus Pro High Voltage">
        When using `High Voltage` for power supply, the source is the motherboard's `Motor Power` input. The maximum voltage is `56V`. Be sure to observe the driver's maximum voltage range.
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
    <TabItem value="24v-fan" label="24V Fan / Proximity Switch" default>
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-24.png').default}
            alt="octo pro fan 24" width="100%"
        />
    </TabItem>
    <TabItem value="12v-fan" label="12V Fan / Proximity Switch">
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-12.png').default}
            alt="octo pro fan 12" width="100%"
        />
    </TabItem>
    <TabItem value="5v-fan" label=" 5V Fan / Proximity Switch">
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

MAX 31865 PT100/PT1000 2-wire or 4-wire configuration

| 1   | 2   | 3   | 4   | Sensor Model  |
| --- | --- | --- | --- | ------------- |
| ON  | ON  | ON  | OFF | 2 wire PT100  |
| ON  | ON  | OFF | ON  | 2 wire PT1000 |
| OFF | OFF | ON  | OFF | 4 wire PT100  |
| OFF | OFF | OFF | ON  | 4 wire PT1000 |

</div>
