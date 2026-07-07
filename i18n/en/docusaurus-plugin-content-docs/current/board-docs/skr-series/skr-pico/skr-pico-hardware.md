---
sidebar_position: 2
---

# SKR Pico Hardware Features

SKR Pico Hardware Details

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Appearance Dimensions

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/skr-pico-size.png').default}
    alt="size" width="800"
/>

## Pinout

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/skr-pico-pin.png').default}
    alt="pinout" width="800"
/>

## Hardware Feature Configuration

### TMC 2209 Sensorless

:::warning

After enabling Sensorless for the corresponding axis, external ENDSTOP cannot be used.

:::

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Sensorless.png').default}
    alt="sensorless" width="550"
/>

### Neopixel

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_RGB.png').default}
    alt="neopixel" width="550"
/>

### BLTouch

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_BLtouch.png').default}
    alt="bltouch" width="550"
/>

### Proximity Switch

:::info[NPN and PNP Type Sensor Selection]

The connection of the proximity switch can be set to either PNP or NPN type via a jumper cap.

:::

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Proximity.png').default}
    alt="proximity" width="550"
/>

### USB Connection

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Rasp.png').default}
    alt="rpi_usb" width="550"
/>

### UART Connection

<ImageView
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/SKR_Pico_Rasp3.png').default}
    alt="rpi_uart" width="550"
/>
