---
sidebar_position: 2
---

# Octopus Max EZ Hardware

Max EZ 硬件详细

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 外观尺寸

<img
    src={require('./img/max-ez-size-v1.png').default}
    alt="max ez size" width="550"
/>

## Pinout

<img
    src={require('./img/max-ez-pinout-v1.png').default}
    alt="max ez pinout" width="550"
/>

## 硬件功能配置

### USB 接口供电

Octopus Max EZ 上电后，MCU 左侧的红灯 `D32` 将亮起，表示电源已打开。仅使用 `USB` 为电路板供电或通过 `USB` 供电时，请将跳线帽插入 `VUSB。`

<img
    src={require('./img/Octopus_MAX_EZ_Hardware1.png').default}
    alt="max ez vusb" width="550"
/>

### EZ 驱动模式配置

通过固件直接设置，无需手动跳线帽选择。

### TMC 驱动 DIAG PIN (Sensorless Homing)

<img
    src={require('./img/Octopus_MAX_EZ_Hardware2.png').default}
    alt="max ez tmc" width="550"
/>

### 驱动供电

<Tabs groupId="maxez-v">
    <TabItem value="VBB" label="Max EZ VBB" default>
        当使用 `VBB` 进行供电的时候。来源为主板 `Power` 输入。最高电压为 `24V`。
        <img
            src={require('./img/Octopus_MAX_EZ_Hardware4.png').default}
            alt="max ez vbb" width="550"
        />
    </TabItem>
    <TabItem value="high-oltage" label="Max EZ High Voltage">
        当使用 `High Voltage` 进行供电的时候。来源为主板 `Motor Power` 输入。最高电压为 `56V`。需要注意驱动最大电压范围。
        <img
            src={require('./img/Octopus_MAX_EZ_Hardware3.png').default}
            alt="max ez high voltage" width="550"
        />
    </TabItem>
</Tabs>

### 风扇电压选择

:::warning 
选择电压前需要注意风扇最高电压。过高的电压可能导致风扇损坏。
:::

通过跳帽来设置输出电压为 `5V` `12V` 或是 `24V`。 (其中 `MFAN` 与 `FAN6` 共用电源 `VFAN6`).

<img
    src={require('./img/Octopus_MAX_EZ_Hardware5.png').default}
    alt="max ez fan" width="550"
/>

### 100K NTC 或 PT1000 跳线配置

使用 100K NTC 时，无需连接跳线，`TH0` `TH1` `TH2` 和 `TH3`的上拉电阻为 **4.7K 0.1%**。使用 `PT1000` 时，需要通过跳线连接下图所示引脚，并联 **4.12K 0.1%** 电阻，`TH0` `TH1` `TH2`和 `TH3`的上拉电阻为 **2.2K**。

:::info
这种连接 PT1000 的方法读取温度的精度远低于 `MAX31865`
:::

<img
    src={require('./img/Octopus_MAX_EZ_Hardware6.png').default}
    alt="max ez ntc" width="550"
/>

### BLTouch 接线

<img
    src={require('./img/Octopus_MAX_EZ_Hardware7.png').default}
    alt="max ez bltouch" width="550"
/>

### 自动断电模块 (v1.2) 接线

<img
    src={require('./img/Octopus_MAX_EZ_Hardware8.png').default}
    alt="max ez auto power" width="550"
/>

### MINI12864 / TFT 屏幕

<img
    src={require('./img/Octopus_MAX_EZ_Hardware9.png').default}
    alt="max ez screen" width="550"
/>

### Neopixel

<img
    src={require('./img/Octopus_MAX_EZ_Hardware10.png').default}
    alt="max ez Neopixel" width="550"
/>

### 耗材传感器

<img
    src={require('./img/Octopus_MAX_EZ_Hardware11.png').default}
    alt="max ez Filament sensor" width="550"
/>

### 接近开关

<Tabs groupId="maxez-pro-switch">
    <TabItem value="VBB" label="常开 NPN 接近开关" default>
        <img
            src={require('./img/Octopus_MAX_EZ_Hardware12.png').default}
            alt="max ez npn" width="550"
        />
    </TabItem>
    <TabItem value="high-oltage" label="常闭 PNP 接近开关">
        <img
            src={require('./img/Octopus_MAX_EZ_Hardware13.png').default}
            alt="max ez pnp" width="550"
        />
    </TabItem>
</Tabs>

### 4 PIN PWM 风扇 或者水冷

下面是使用 12V电压的接线方法

<img
    src={require('./img/Octopus_MAX_EZ_Hardware14.png').default}
    alt="max ez pnp" width="550"
/>
