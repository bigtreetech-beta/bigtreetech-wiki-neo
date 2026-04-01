---
sidebar_position: 2
description: Pad5 V2.0 Hardware Configuration
---

# Pad5 V2 Hardware

## Peripheral Interfaces

### Interface Diagram

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/interface.webp').default} width="60%"/>

### Feature Overview

The table below summarizes the features supported by each compatible core board: `√`= Supported, `×`= Not supported.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/functional.webp').default} width="60%"/>

## Feature Details

### 40 Pin GPIO

The diagram shows the GPIO pinout mapping for different core boards on the 40-pin header.

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/40pin-gpio.webp').default} width="100%"/>

### CAN Interface

The Pad5 supports CAN communication when used with CM5 or CM4.This is achieved by converting the SoC’s SPI signals to CAN signals.

SPI to CAN Mapping: CS-GPIO8，MISO-GPIO9，MOSI-GPIO10，SCK-GPIO11，INT-GPIO24

### Fan Interface

The Pad5 supports a 4-wire fan for active cooling when used with CM5. Connector type: ZX-SH1.0 4P

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/fan.webp').default} width="60%"/>

### RTC Circuit

The Pad5 provides an RTC circuit when used with CM5, CM4, or CB2, using the SoC’s I2C interface to control a PCF8563 clock chip.

:::info

Before using the RTC, install a CR1220 3V coin cell battery with the logo side facing up; recommended brands include Panasonic, Lithium Cell, and similar.

:::

### MIPI Interfaces

The Pad5 supports MIPI-DSI (display) and MIPI-CSI (camera) when used with CM5, CM4, or CB2. On the CM5, both MIPI interfaces can be used interchangeably, with DPHY0 and DPHY1 functioning as either DSI or CSI. On the CM4 and CB2, the CSI interface connects only to a camera, while the DSI interface connects only to a DSI display.

:::info

Use the correct cable for each device—do not use a camera cable for the display or vice versa—and ensure the gold fingers are properly aligned with the connector and the latch is secured.

:::

DSI Cable:

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/mipi-dsi.webp').default} width="45%"/>

CSI Cable：

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/mipi-csi.webp').default} width="45%"/>

Pin Sequence:

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/mipi.webp').default} width="45%"/>

### Buttons

<ImageView src={require('@site/docs/board-docs/iot-series/iot-pad5-v2/img/button.webp').default} width="60%"/>

BK+: Increase backlight brightness (0–100%). Each click increases by 1%; long press adjusts faster.

Rotate: Rotate display 180°.

BK-: Decrease backlight brightness (0–100%). Each click decreases by 1%; long press adjusts faster.

ON/OFF: Power switch (supported only with Raspberry Pi CM5).
