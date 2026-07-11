---
sidebar_position: 2
description: Manta M4P Hardware
---

# Manta M4P Hardware

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Hardware Dimensions

:::info[STEP File]

Manta M4P STEP [BIGTREETECH_Manta_M4P_V2.1_220608_3D.step](https://github.com/bigtreetech/Manta-M4P/blob/master/3D/BIGTREETECH_Manta_M4P_V2.1_220608_3D.step)

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_Size.webp').default} width="100%"/>

## Pinout

:::info[Schematic]

Manta M4P v2 Schematic [bigtreetech_manta_m4p_v2.1_220608_SCH.pdf](https://github.com/bigtreetech/Manta-M4P/blob/master/Hardware/bigtreetech_manta_m4p_v2.1_220608_SCH.pdf)

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_Pinout.webp').default} width="100%"/>

## Stepper Motor Driver

### Drive Modes

<Tabs groupId="m4p-stepper-driver">
    <TabItem value="tmc-uart" label="Uart Mode" default>
        Connecting the Driver Using UART Mode
        <ImageView
            src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_TMC_UART_Mode.webp').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI Mode">
        Connecting the Driver Using SPI Mode
        <ImageView
            src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_TMC_SPI_Mode.webp').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / dir Mode">
        A4988 / DRV8825 jumper cap to short MS0 to MS2 to adjust microstepping
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_Stepper_Driver.webp').default} width="100%"/>
    </TabItem>
</Tabs>

### TMC Sensorless

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_TMC_DIAG_Mode.webp').default} width="100%"/>

### Selecting the Drive Voltage

<Tabs groupId="m4p-driver-power">
    <TabItem value="m4p-power-24" label="Use 24V PSU" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_driver_24.webp').default} width="100%"/>
    </TabItem>
    <TabItem value="m4p-power-48" label="Use 48V PSU">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_driver_48.webp').default} width="100%"/>
    </TabItem>
</Tabs>

## Core Board

### Core Board Install

<Tabs groupId="m4p-cm">
    <TabItem value="m4p-cm-rpi" label="Use RPI CM4/CM5" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/m4p_cm_rpi.webp').default} width="100%"/>
    </TabItem>
    <TabItem value="m4p-cm-cb" label="Use CB1/CB2">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/m4p_cm_cb.webp').default} width="100%"/>
    </TabItem>
</Tabs>

### USB Power

After powering on the M4P, the red LED1 in the lower-right corner of the motherboard will light up, indicating that the power supply is functioning normally. J8, located in the center of the board, is the power selection terminal; it needs to be shorted only when the Type-C USB port is used to power the motherboard or when an external power supply is used. The Type-C signal connects to the SoC and is used only when writing the operating system image to the CM4 eMMC.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_TYPE_C.webp').default} width="45%"/>

### 40 Pin GPIO

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/m4p-40pin-gpio.webp').default} width="50%"/>

### DSI / CSI Connect

:::info[Require Hardware Support]

DSI / CSI Require Hardware Support

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_DSI_CSI_Wiring.webp').default} width="100%"/>

### SPI Display

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_SPI_Display_Wiring.webp').default} width="100%"/>

## Sensor

### BLTouch

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_BLTouch_Wiring.webp').default} width="60%"/>

### ADXL 345

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_ADXL345.webp').default} width="60%"/>

## Other Hardware

### Neopixel 

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m4p/img/M4P_RGB_Wiring.webp').default} width="80%"/>
