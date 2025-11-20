---
sidebar_position: 2
---

# Manta M8P v1 硬件功能

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 外观尺寸

:::info[STEP 模型]

Manta M8P v1.0 模型 [BIGTREETECH MANTA M8P V1.0.step](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/3D/BIGTREETECH%20MANTA%20M8P%20V1.0.step)

Manta M8P v1.1 模型 [BIGTREETECH MANTA M8P V1.1.step.zip](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/3D/BIGTREETECH%20MANTA%20M8P%20V1.1.step.zip)

:::

<Tabs groupId="m8p-dim">
    <TabItem value="m8p-dim-1" label="正面尺寸" default>
        <img src={require('./img/M8P_dimensions_1.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-dim-2" label="反面尺寸">
        <img src={require('./img/M8P_dimensions_2.png').default} width="100%"/>
    </TabItem>
</Tabs>

## Pinout

:::info[原理图 / Schematic]

Manta M8P v1.0 原理图 [BIGTREETECH MANTA M8P V1.0-SCH.pdf](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/Hardware/BIGTREETECH%20MANTA%20M8P%20V1.0-SCH.pdf)

Manta M8P v1.1 原理图 [BIGTREETECH MANTA M8P V1.1-SCH.pdf](https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/Hardware/BIGTREETECH%20MANTA%20M8P%20V1.1-SCH.pdf)

:::

<Tabs groupId="m8p-pinout">
    <TabItem value="m8p-pinout-1_1" label="Manta M8P v1.1" default>
        <img src={require('./img/M8P_pinout-v1_1.png').default} width="100%"/>
    </TabItem>
    <TabItem value="m8p-pinout-1_0" label="Manta M8P v1.0">
        <img src={require('./img/M8P_pinout-v1_0.png').default} width="100%"/>
    </TabItem>
</Tabs>

:::info[Manta M8P V1.1 增加了功能]

CAN接口（2引脚*2 XH2.54）

USB端口功能选择（UART到USB，USB OTG）

Pi FAN（由GPIO26控制）

FAN4成为2线CNC风扇。

<img src={require('./img/M8P_Add_Func1.png').default} width="80%"/>

:::

## 硬件功能配置

### USB 供电

M8P主板通电后，MCU左侧的D32红灯亮起，表示电源正常。电路板中间的VUSB是电源选择端子。只有在使用USB向主板供电或需要通过USB供电时，才需要使用跳线将其短路。

<img src={require('./img/M8P_USB_PS.png').default} width="80%"/>

### 步进电机驱动

#### TMC 2208 / TMC 2209 UART 模式

<img src={require('./img/M8P_uart.png').default} width="80%"/>

#### TMC 2130 / TMC 5160 SPI 模式

<img src={require('./img/M8P_spi.png').default} width="80%"/>

#### TMC Sensorless

<img src={require('./img/M8P_Dri_sensorless.png').default} width="80%"/>

#### 仅使用 STEP/DIR 驱动

A4988 / DRV8825 使用跳线帽短接 MS0-MS2 以调整细分

:::info[已知问题]
如果使用 `A4988` 或 `DRV8825` 需要短接 `RST` 和 `SLP` 才能正常工作
:::

<img src={require('./img/M8P_Dri_Step.png').default} width="80%"/>

### 驱动电压选择

<Tabs groupId="m8p-driver-power">
    <TabItem value="m8p-power-24" label="使用 24V 电源" default>
        <img src={require('./img/M8P_driver_24.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-power-48" label="使用 48V 电源">
        <img src={require('./img/M8P_driver_48.png').default} width="80%"/>
    </TabItem>
</Tabs>

### 核心板安装

<Tabs groupId="m8p-cm">
    <TabItem value="m8p-cm-rpi" label="使用树莓派 CM4/CM5" default>
        <img src={require('./img/M8P_cm_rpi.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-cm-cb" label="使用 CB1/CB2">
        <img src={require('./img/M8P_cm_cb.png').default} width="80%"/>
    </TabItem>
</Tabs>

### 风扇电压选择

使用跳线帽配置输出电压

:::warning

在选择电压之前，请确认风扇的工作电压

:::

<img src={require('./img/M8P_fan.png').default} width="60%"/>

### 4Pin PWM 风扇接线

<img src={require('./img/M8P_4_pin_pwm.png').default} width="60%"/>

### 100K NTC 或 PT1000 设置

当使用100K NTC热敏电阻时，无需插入跳线帽 `TH0` `TH1` `TH2` `TH3` 的上拉电阻为 4.7K 0.1%。

:::info

使用PT1000时，需要插入 PT 的跳线帽。此时 `TH0` `TH1` `TH2` `TH3` 的上拉电阻为2.2K。

这样读取的温度精度将远不如MAX31865读取的精度

<img src={require('./img/M8P_pt1000.png').default} width="30%"/>

:::

### BLTouch

<img src={require('./img/M8P_BLTouch.png').default} width="80%"/>

### 接近开关接线

<Tabs groupId="m8p-proximity">
    <TabItem value="m8p-proximity-npn" label="NPN 接近开关" default>
        <img src={require('./img/M8P_Proximity_npn.png').default} width="80%"/>
    </TabItem>
    <TabItem value="m8p-proximity-pnp" label="PNP 接近开关">
        <img src={require('./img/M8P_Proximity_pnp.png').default} width="80%"/>
    </TabItem>
</Tabs>

### ADXL345 加速计

:::info

使用加速度计参考 Klipper [Measuring_Resonances](https://www.klipper3d.org/Measuring_Resonances.html)

Manta M8P ADXL 345 配置文件参考 [Manta M8P ADXL 配置文件](./manta-m8p-v1-firmware.md#adxl345-配置文件参考)

:::

<img src={require('./img/M8P_ADXL345.png').default} width="80%"/>

### Neopixel 

<img src={require('./img/M8P_RGB.png').default} width="80%"/>

### 断料检测

<img src={require('./img/M8P_Filament.png').default} width="80%"/>

### 40 Pin GPIO

<img src={require('./img/M8P_40_Pin.png').default} width="60%"/>

### DSI/CSI 接线

:::info

DSI/CSI 需要核心板硬件支持

:::

<img src={require('./img/M8P_DSI.png').default} width="80%"/>
