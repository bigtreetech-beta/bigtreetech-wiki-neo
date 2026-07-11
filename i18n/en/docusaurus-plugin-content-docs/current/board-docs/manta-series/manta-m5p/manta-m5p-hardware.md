---
sidebar_position: 2
description: Manta M5P Hardware
---

# Manta M5P Hardware

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Hardware Dimensions

:::info[STEP File]

Manta M5P STEP [BIGTREETECH MANTA M5P-step.rar](https://github.com/bigtreetech/Manta-M5P/blob/master/3D/BIGTREETECH%20MANTA%20M5P-step.rar)

:::

<Tabs groupId="m5p-dim">
    <TabItem value="m5p-dim-1" label="Front Dimensions" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_Dimension1.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m5p-dim-2" label="Back Dimensions">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_Dimension2.png').default} width="80%"/>
    </TabItem>
</Tabs>

## Pinout

:::info[Schematic]

Manta M5P Schematic [BIGTREETECH MANTA M5P V1.0-SCH.pdf](https://github.com/bigtreetech/Manta-M5P/blob/master/Hardware/BIGTREETECH%20MANTA%20M5P%20V1.0-SCH.pdf)

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-pinout.png').default} width="100%"/>

## Stepper Motor Driver

### Drive Modes

<Tabs groupId="m5p-stepper-driver">
    <TabItem value="tmc-uart" label="Uart Mode" default>
        Connecting the Driver Using UART Mode
        <ImageView
            src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-driver-uart.png').default}
            alt="" width="80%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI Mode">
        Connecting the Driver Using SPI Mode
        <ImageView
            src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-driver-spi.png').default}
            alt="" width="80%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / DIR Mode">
        A4988 / DRV8825 jumper cap to short MS0 to MS2 to adjust microstepping
        <ImageView
            src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-driver-step.png').default}
            alt="" width="80%"
        />
    </TabItem>
</Tabs>

### TMC Sensorless

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-sensorless.png').default} width="80%"/>

### Selecting the Drive Voltage

<Tabs groupId="m5p-driver-power">
    <TabItem value="m5p-power-24" label="Use 24V PSU" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-driver-24.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m5p-power-48" label="Use 48V PSU">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-driver-48.png').default} width="80%"/>
    </TabItem>
</Tabs>

## Core Board

### Core Board Install

<Tabs groupId="m5p-cm">
    <TabItem value="m5p-cm-rpi" label="Use RPI CM4/CM5" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/m5p_cm_rpi.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m5p-cm-cb" label="Use CB1/CB2">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/m5p_cm_cb.png').default} width="80%"/>
    </TabItem>
</Tabs>

### USB Power

When the MANTA M5P is powered on, the red LED D22 on the left side of the MCU will light up, indicating that power is on. When powering the board via USB only, or when using USB as the power source, please insert the jumper cap into VUSB.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_USB_PS.png').default} width="45%"/>

### DSI / CSI Connect

:::info[Requires hardware support]

DSI / CSI Requires hardware support

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_DSI.png').default} width="100%"/>

## Fans

### Fan Voltage Selection

Configure the Output Voltage Using Jumper Caps

:::warning

Before selecting a voltage, please confirm the fan's operating voltage.

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/manta-m5p-fan-voltage.png').default} width="40%"/>

## Sensors

### BLTouch

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_BLTouch_Wiring.png').default} width="80%"/>

### 100K NTC Or PT1000 Setup

When using a 100K NTC thermistor, there is no need to insert a jumper cap; the pull-up resistors for `TH0` and `TH1` are 4.7K 0.1%.

:::info[Use PT1000]

When using a PT1000, you must insert the PT jumper cap. In this case, the pull-up resistors for `TH0` and `TH1` are 2.2K.

The temperature reading accuracy in this configuration will be significantly lower than that achieved with the MAX31865.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_100K.png').default} width="20%"/>

:::

### Filament sensor

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_Filament.png').default} width="80%"/>

### Proximity Switch Wiring

Using a PNP Proximity Switch

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_Proximity-PNP.png').default} width="80%"/>

:::info[NPN Proximity Switch]

NPN proximity switches do not require a `Pull-Up` jumper cap.

:::

## Other Hardware

### Neopixel 

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m5p/img/M5P_RGB_Wiring.png').default} width="80%"/>
