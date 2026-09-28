---
sidebar_position: 2
description: Manta M4P 硬件功能配置
---

# Manta M4P 硬件功能

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## 外观尺寸

:::info[STEP 模型]

Manta M4P 模型 [BIGTREETECH_Manta_M4P_V2.1_220608_3D.step](https://github.com/bigtreetech/Manta-M4P/blob/master/3D/BIGTREETECH_Manta_M4P_V2.1_220608_3D.step)

:::

<ImageView src={require('./img/M4P_Size.webp').default} width="100%"/>

## Pinout

:::info[原理图 / Schematic]

Manta M4P v2 原理图 [bigtreetech_manta_m4p_v2.1_220608_SCH.pdf](https://github.com/bigtreetech/Manta-M4P/blob/master/Hardware/bigtreetech_manta_m4p_v2.1_220608_SCH.pdf)

:::

<ImageView src={require('./img/M4P_Pinout.webp').default} width="100%"/>

## 步进电机驱动

### 驱动模式

<Tabs groupId="m4p-stepper-driver">
    <TabItem value="tmc-uart" label="Uart 模式" default>
        使用 Uart 模式连接驱动
        <ImageView
            src={require('./img/M4P_TMC_UART_Mode.webp').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI 模式">
        使用 SPI 模式连接驱动
        <ImageView
            src={require('./img/M4P_TMC_SPI_Mode.webp').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / dir 模式">
        A4988 / DRV8825 使用跳线帽短接 MS0-MS2 以调整细分
        <ImageView src={require('./img/M4P_Stepper_Driver.webp').default} width="100%"/>
    </TabItem>
</Tabs>

### TMC Sensorless

<ImageView src={require('./img/M4P_TMC_DIAG_Mode.webp').default} width="100%"/>

### 驱动电压选择

<Tabs groupId="m4p-driver-power">
    <TabItem value="m4p-power-24" label="使用 24V 电源" default>
        <ImageView src={require('./img/M4P_driver_24.webp').default} width="100%"/>
    </TabItem>
    <TabItem value="m4p-power-48" label="使用 48V 电源">
        <ImageView src={require('./img/M4P_driver_48.webp').default} width="100%"/>
    </TabItem>
</Tabs>

## 核心板

### 核心板安装

<Tabs groupId="m4p-cm">
    <TabItem value="m4p-cm-rpi" label="使用树莓派 CM4/CM5" default>
        <ImageView src={require('./img/m4p_cm_rpi.webp').default} width="100%"/>
    </TabItem>
    <TabItem value="m4p-cm-cb" label="使用 CB1/CB2">
        <ImageView src={require('./img/m4p_cm_cb.webp').default} width="100%"/>
    </TabItem>
</Tabs>

### SD 卡接口

M4P 主板设有两个用途不同的 SD 卡槽。下图标注主板背面的卡槽位置，SOC-Card 与 MCU-Card 相邻；不同硬件版本请以实物丝印为准。

<ImageView
    src={require('./img/manta-m4p-sd-cards.webp').default}
    width="100%"
/>

| 卡槽 | 用途 |
| --- | --- |
| SOC-Card | 供使用 microSD 卡的核心板存放系统镜像，不用于更新主板 MCU 固件。 |
| MCU-Card | 用于更新主板 MCU 固件，不是核心板的系统卡槽。 |

:::warning[MCU-Card 使用条件]

通过 MCU-Card 更新固件，要求主板保留出厂自带的 Bootloader。若 Bootloader 被擦除或覆盖，该卡槽便无法执行固件更新；须先通过其他烧录方式恢复适用于此型号及硬件版本的出厂 Bootloader。

:::

### USB 供电

M4P 开机后，主板右下侧的红色 LED1 会亮起，表示电源正常。板中间的 J8 是电源选择端子，只有当type-C USB用于向主板供电或USB用于外部供电时，才需要短接。type-C的信号连接到 SoC，仅在写入 CM4 eMMC 版本的操作系统映像时使用。

<ImageView src={require('./img/M4P_TYPE_C.webp').default} width="45%"/>

### GPIO（40 Pin）

<ImageView src={require('./img/m4p-40pin-gpio.webp').default} width="50%"/>

### DSI / CSI连接

:::info[需要硬件支持]

DSI / CSI 需要核心板硬件支持

:::

<ImageView src={require('./img/M4P_DSI_CSI_Wiring.webp').default} width="100%"/>

### SPI 显示器

<ImageView src={require('./img/M4P_SPI_Display_Wiring.webp').default} width="100%"/>

## 传感器

### BLTouch

<ImageView src={require('./img/M4P_BLTouch_Wiring.webp').default} width="60%"/>

### ADXL 345

<ImageView src={require('./img/M4P_ADXL345.webp').default} width="60%"/>

## 其他硬件

### Neopixel 

<ImageView src={require('./img/M4P_RGB_Wiring.webp').default} width="80%"/>
