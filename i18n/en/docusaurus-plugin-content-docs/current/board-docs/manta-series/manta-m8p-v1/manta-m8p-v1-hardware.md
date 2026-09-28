---
sidebar_position: 2
---

# Manta M8P v1 Hardware

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Hardware Dimensions

:::info[STEP Models]

Manta M8P v1.0 Model [BIGTREETECH MANTA M8P V1.0.step](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/3D/BIGTREETECH%20MANTA%20M8P%20V1.0.step)

Manta M8P v1.1 Model [BIGTREETECH MANTA M8P V1.1.step.zip](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/3D/BIGTREETECH%20MANTA%20M8P%20V1.1.step.zip)

:::

<Tabs groupId="m8p-dim">
    <TabItem value="m8p-dim-1" label="Front Dimensions" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_dimensions_1.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-dim-2" label="Rear Dimensions">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_dimensions_2.png').default} width="100%"/>
    </TabItem>
</Tabs>

## Pinout

:::info[Schematic]

Manta M8P v1.0 Schematic [BIGTREETECH MANTA M8P V1.0-SCH.pdf](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/Hardware/BIGTREETECH%20MANTA%20M8P%20V1.0-SCH.pdf)

Manta M8P v1.1 Schematic [BIGTREETECH MANTA M8P V1.1-SCH.pdf](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/Hardware/BIGTREETECH%20MANTA%20M8P%20V1.1-SCH.pdf)

:::

<Tabs groupId="m8p-pinout">
    <TabItem value="m8p-pinout-1_1" label="Manta M8P v1.1" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_pinout-v1_1.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-pinout-1_0" label="Manta M8P v1.0">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_pinout-v1_0.png').default} width="100%"/>
    </TabItem>
</Tabs>

:::info[Features Added in Manta M8P V1.1]

CAN interface (two 2-pin XH2.54 connectors)

USB port function selection (UART-to-USB or USB OTG)

Pi FAN (controlled by GPIO26)

FAN4 is changed to a two-wire controllable fan.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_Add_Func1.png').default} width="80%"/>

:::

## Hardware Configuration

### USB Power

After powering on the M8P motherboard, the red D32 LED to the left of the MCU lights up to indicate normal power. VUSB, located in the middle of the board, is the power selection header. Short it with a jumper only when USB is used to power the motherboard or to supply power through USB.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_USB_PS.png').default} width="80%"/>

### Stepper Motor Drivers

#### TMC 2208 / TMC 2209 UART Mode

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_uart.png').default} width="80%"/>

#### TMC 2130 / TMC 5160 SPI Mode

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_spi.png').default} width="80%"/>

#### TMC Sensorless

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_Dri_sensorless.png').default} width="80%"/>

#### STEP/DIR-Only Drivers

For A4988 / DRV8825 drivers, use jumper caps to short MS0-MS2 as needed to set the microstepping mode.

:::info[Known Issues]

When using `A4988` or `DRV8825`, short `RST` and `SLP` for the driver to work properly.

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_Dri_Step.png').default} width="80%"/>

### Driver Voltage Selection

<Tabs groupId="m8p-driver-power">
    <TabItem value="m8p-power-24" label="Using a 24V Power Supply" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_driver_24.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-power-48" label="Using a 48V Power Supply">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_driver_48.png').default} width="80%"/>
    </TabItem>
</Tabs>

### Compute Module Installation

<Tabs groupId="m8p-cm">
    <TabItem value="m8p-cm-rpi" label="Using Raspberry Pi CM4/CM5" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_cm_rpi.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-cm-cb" label="Using CB1/CB2">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_cm_cb.png').default} width="80%"/>
    </TabItem>
</Tabs>

### SD Card Slots

Both the M8P V1.0 and V1.1 have two microSD card slots with different purposes, in the same locations. The image below shows the back of the V1.1; the slot locations also apply to V1.0. Do not mix up the system card and the MCU firmware card.

<ImageView
    src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/manta-m8p-v1-sd-cards.webp').default}
    width="100%"
/>

| Slot | Purpose |
| --- | --- |
| SOC-Card | Stores the system image for compute modules that use a microSD card. It is not used to update the motherboard MCU firmware. |
| MCU-Card | Updates the motherboard MCU firmware. It is not the compute module's system card slot. |

:::warning[MCU-Card Requirements]

Updating firmware through the MCU-Card requires the factory-installed bootloader to remain on the motherboard. If the bootloader is erased or overwritten, this slot cannot perform firmware updates. First restore the factory bootloader for this board model and hardware revision by another flashing method.

:::

### Fan Voltage Selection

Use jumper caps to configure the output voltage.

:::warning

Check the fan's operating voltage before selecting the supply voltage.

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_fan.png').default} width="60%"/>

### PWM Fan Wiring (4-Pin)

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_4_pin_pwm.png').default} width="60%"/>

### Temperature Sensor Settings (100K NTC or PT1000)

When using a 100K NTC thermistor, no jumper cap is required. The pull-up resistors for `TH0`, `TH1`, `TH2`, and `TH3` are $4.7\,\mathrm{k}\Omega$ with a tolerance of 0.1%.

:::info

When using a PT1000, install the PT jumper cap. The pull-up resistance for `TH0`, `TH1`, `TH2`, and `TH3` is then $2.2\,\mathrm{k}\Omega$.

Temperature readings obtained this way are significantly less accurate than those obtained with a MAX31865.

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_pt1000.png').default} width="30%"/>

:::

### BLTouch

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_BLTouch.png').default} width="80%"/>

### Proximity Switch Wiring

<Tabs groupId="m8p-proximity">
    <TabItem value="m8p-proximity-npn" label="NPN Proximity Switch" default>
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_Proximity_npn.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-proximity-pnp" label="PNP Proximity Switch">
        <ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_Proximity_pnp.png').default} width="80%"/>
    </TabItem>
</Tabs>

### ADXL345 Accelerometer

:::info

For accelerometer usage, refer to Klipper's [Measuring_Resonances](https://www.klipper3d.org/Measuring_Resonances.html)

For the Manta M8P ADXL345 configuration, refer to [Manta M8P ADXL Configuration](./manta-m8p-v1-firmware.md)

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_ADXL345.png').default} width="80%"/>

### Neopixel

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_RGB.png').default} width="80%"/>

### Filament Runout Detection

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_Filament.png').default} width="80%"/>

### GPIO (40 Pin)

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_40_Pin.png').default} width="60%"/>

### DSI/CSI Wiring

:::info

DSI/CSI requires hardware support from the compute module.

:::

<ImageView src={require('@site/docs/board-docs/manta-series/manta-m8p-v1/img/M8P_DSI.png').default} width="80%"/>
