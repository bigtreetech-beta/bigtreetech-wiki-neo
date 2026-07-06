---
sidebar_position: 2
---

# Octopus Max EZ Hardware Features

Max EZ Hardware Details

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Dimensions

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/max-ez-size-v1.png').default}
    alt="max ez size" width="800"
/>

## Pinout

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/max-ez-pinout-v1.png').default}
    alt="max ez pinout" width="800"
/>

## Hardware Features and Specifications

### Powered via USB Port

When the Octopus Max EZ is powered on, the red LED `D32` on the left side of the MCU will light up, indicating that the power is on. When powering the board using only `USB` or via `USB`, insert the jumper cap into `VUSB`.

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware1.png').default}
    alt="max ez vusb" width="70%"
/>

### EZ Drive Mode Configuration

Configure directly via firmware; no need to manually select jumper caps.

### TMC Driver DIAG PIN (Sensorless Homing)

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware2.png').default}
    alt="max ez tmc" width="70%"
/>

### Driver Power Supply

<Tabs groupId="maxez-v">
    <TabItem value="VBB" label="Max EZ VBB" default>
        When using `VBB` for power, the source is the motherboard's `Power` input. The maximum voltage is `24V`.
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/max-ez/img/max-ez-driver-vbb.png').default}
            alt="max ez vbb" width="70%"
        />
    </TabItem>
    <TabItem value="high-oltage" label="Max EZ High Voltage">
        When using `High Voltage` for power supply, the source is the motherboard's `Motor Power` input. The maximum voltage is `56V`. Be sure to observe the driver’s maximum voltage range.
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/max-ez/img/max-ez-driver-hv.png').default}
            alt="max ez high voltage" width="70%"
        />
    </TabItem>
</Tabs>

### Fan Voltage Selection

:::warning

Before selecting a voltage, be sure to check the fan's maximum voltage. Excessively high voltage may damage the fan.111

:::

Use jumpers to set the output voltage to `5V`, `12V`, or `24V`. (Note that `MFAN` and `FAN6` share the `VFAN6` power supply.)

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware5.png').default}
    alt="max ez fan" width="70%"
/>

### 100K NTC or PT1000 Jumper Configuration

When using a 100K NTC, no jumper is required, and the pull-up resistors for `TH0`, `TH1`, `TH2`, and `TH3` are **4.7K 0.1%**. When using a `PT1000`, you must connect the pins shown in the figure below using jumpers and connect **4.12K 0.1%** resistors in parallel; the pull-up resistors for `TH0`, `TH1`, `TH2`, and `TH3` are **2.2K**.

:::info

This method of connecting a PT1000 results in much lower temperature reading accuracy than the `MAX31865`.

:::

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware6.png').default}
    alt="max ez ntc" width="70%"
/>

### BLTouch Wiring

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware7.png').default}
    alt="max ez bltouch" width="70%"
/>

### Automatic Power-Off Module (v1.2) Wiring

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware8.png').default}
    alt="max ez auto power" width="70%"
/>

### MINI12864 / TFT Screen

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware9.png').default}
    alt="max ez screen" width="70%"
/>

### Neopixel

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware10.png').default}
    alt="max ez Neopixel" width="70%"
/>

### Filament Sensors

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware11.png').default}
    alt="max ez Filament sensor" width="70%"
/>

### Proximity Switch

<Tabs groupId="maxez-pro-switch">
    <TabItem value="VBB" label="Normally Open NPN Proximity Switch" default>
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware12.png').default}
            alt="max ez npn" width="70%"
        />
    </TabItem>
    <TabItem value="high-oltage" label="Normally Closed PNP Proximity Switch">
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware13.png').default}
            alt="max ez pnp" width="70%"
        />
    </TabItem>
</Tabs>

### 4-Pin PWM Fan or Water Cooling

Below are the wiring instructions for a 12V system.

<ImageView
    src={require('@site/docs/board-docs/octopus-series/max-ez/img/Octopus_MAX_EZ_Hardware14.png').default}
    alt="max ez pnp" width="70%"
/>
