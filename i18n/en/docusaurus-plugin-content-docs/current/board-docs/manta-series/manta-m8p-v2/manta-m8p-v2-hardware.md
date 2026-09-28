---
sidebar_position: 2
description: Manta M8P V2 Hardware Configuration
---

# Manta M8P v2 Hardware

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Hardware Dimensions

:::info[STEP Models]

Manta M8P v2 Model [BIGTREETECH MANTA M8P V2.0.zip](https://github.com/bigtreetech/Manta-M8P/blob/master/V2.0/3D/BIGTREETECH%20MANTA%20M8P%20V2.0.zip)

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p-v2-dimensions.png').default} width="100%"/>

## Pinout

:::info[Schematic]

Manta M8P v2 Schematic [BIGTREETECH MANTA M8P V2.0-SCH.pdf](https://github.com/bigtreetech/Manta-M8P/blob/master/V2.0/Hardware/BIGTREETECH%20MANTA%20M8P%20V2.0-SCH.pdf)

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p-v2-pinout.png').default} width="100%"/>

## Stepper Motor Drivers

### Motor Driver Configuration (SPI / UART)

<Tabs groupId="m8p-v2-stepper-driver">
    <TabItem value="tmc-uart" label="UART Mode" default>
        Connect the driver in UART mode.
        <ImageView
            src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_tmc_uart.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI Mode">
        Connect the driver in SPI mode.
        <ImageView
            src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_tmc_spi.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="STEP/DIR Mode">
        For A4988 / DRV8825 drivers, use jumper caps to short MS0-MS2 as needed to set the microstepping mode.

        :::info[Known Issues]
        When using `A4988` or `DRV8825`, short `RST` and `SLP` for the driver to work properly.
        :::
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_step-dir.png').default} width="100%"/>
    </TabItem>
</Tabs>

### Driver Voltage Selection

<Tabs groupId="m8p-v2-driver-power">
    <TabItem value="m8p-power-24" label="Using a 24V Power Supply" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/M8P_driver_24.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-power-48" label="Using a 48V Power Supply">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/M8P_driver_48.png').default} width="100%"/>
    </TabItem>
</Tabs>

### TMC Sensorless

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_tmc_sensorless.png').default} width="100%"/>

## Compute Module

### Compute Module Installation

<Tabs groupId="m8p-v2-cm">
    <TabItem value="m8p-cm-rpi" label="Using Raspberry Pi CM4/CM5" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/M8P-v2_cm_rpi.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-cm-cb" label="Using CB1/CB2">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/M8P-v2_cm_cb.png').default} width="100%"/>
    </TabItem>
</Tabs>

### SD Card Slots

The M8P V2.0 motherboard has two microSD card slots with different purposes. The product photo below shows the back of the V2.0 and marks the SOC-Card and MCU-Card locations. Do not mix up the system card and the MCU firmware card.

<ImageView
    src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/manta-m8p-v2-sd-cards.webp').default}
    width="100%"
/>

| Slot | Purpose |
| --- | --- |
| SOC-Card | Stores the system image for compute modules that use a microSD card. It is not used to update the motherboard MCU firmware. |
| MCU-Card | Updates the motherboard MCU firmware. It is not the compute module's system card slot. |

:::warning[MCU-Card Requirements]

Updating firmware through the MCU-Card requires the factory-installed bootloader to remain on the motherboard. If the bootloader is erased or overwritten, this slot cannot perform firmware updates. First restore the factory bootloader for this board model and hardware revision by another flashing method.

:::

### USB Power

After powering on the M8P motherboard, the LED in the lower-left corner lights up to indicate normal power. VUSB, located in the middle of the board, is the power selection header. Short it with a jumper cap only when powering the motherboard via USB or supplying power to external devices via USB.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_usb.png').default} width="50%"/>

### DSI / CSI Connections

:::info[Hardware Support Required]

DSI / CSI requires hardware support from the compute module.

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_dsi.png').default} width="100%"/>

## Fans

### Fan Voltage Selection

Use jumper caps to configure the output voltage.

:::warning

Check the fan's operating voltage before selecting the supply voltage.

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_cnc.png').default} width="100%"/>

### 4-Pin PWM Fan Wiring

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_4pin_fan.png').default} width="60%"/>

## Sensors

### 100K NTC or PT1000 Settings

When using a 100K NTC thermistor, no jumper cap is required. The pull-up resistors for `TH0`, `TH1`, `TH2`, and `TH3` are 4.7 kΩ with a tolerance of 0.1%.

:::info

When using a PT1000, install the PT jumper cap. The pull-up resistance for `TH0`, `TH1`, `TH2`, and `TH3` is then 2.2 kΩ.

Temperature readings obtained this way are significantly less accurate than those obtained with a MAX31865.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_100k.png').default} width="20%"/>

:::

### BLTouch

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_bltouch.png').default} width="100%"/>

### Proximity Switch Wiring

<Tabs groupId="m8p-v2-proximity">
    <TabItem value="m8p-v2-proximity-npn" label="NPN Proximity Switch" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_proximity1.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-v2-proximity-pnp" label="PNP Proximity Switch">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_proximity.png').default} width="80%"/>
    </TabItem>
</Tabs>

### I2C Wiring (Temperature and Humidity Sensor)

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_i2c.png').default} width="80%"/>

## Other Hardware

### Neopixel

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_rgb.png').default} width="80%"/>

### Servo Wiring

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v2/img/m8p_v2_0_servo.png').default} width="80%"/>
