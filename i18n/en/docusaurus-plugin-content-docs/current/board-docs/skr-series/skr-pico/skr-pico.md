---
sidebar_position: 1
description: SKR Pico
---

# SKR Pico

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import DocCardList from '@theme/DocCardList';

{/* import lib end */}

<div class="div-table">

<ImageView 
    src={require('@site/docs/board-docs/skr-series/skr-pico/img/skr-pico-main.png').default} 
    width="45%" class="right-image"
/>

## Introduction

The SKR Pico is a board designed specifically for the Voron 0 series. It can be stacked directly on top of the Raspberry Pi series, reducing the required installation space.

## Specifications

| Specification                              | SKR Pico                 |
| ------------------------------------------ | ------------------------ |
| MCU                                        | ARM Cortex-M0+ RP2040    |
| Dimensions                                 | 85 x 56 mm               |
| Board Layers                               | 4 layers                 |
| Power Input                                | DC 12/24 V               |
| Logic Voltage                              | 3.3V                     |
| Motor Drivers                              | $4*$ TMC2209             |
| Motor Driver Interfaces                    | X / Y / Z1 / Z2 / E      |
| Temperature Sensor Interfaces              | TH0, THB                 |
| Communication Interfaces with Raspberry Pi | USB Type-C / Serial Port |

</div>

<DocCardList />
