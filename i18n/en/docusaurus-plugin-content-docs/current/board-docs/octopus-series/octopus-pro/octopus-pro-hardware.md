---
sidebar_position: 2
description: Octopus Pro 硬件详细
---

# Octopus Pro 硬件功能

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import ThemedImage from '@theme/ThemedImage';

<!-- import lib end -->

## 尺寸

:::info

尺寸参考 GitHub Repo [bigtreetech/BIGTREETECH-OCTOPUS-Pro/Hardware/BIGTREETECH Octopus Pro - SIZE](https://github.com/bigtreetech/BIGTREETECH-OCTOPUS-Pro/blob/master/Hardware/BIGTREETECH%20Octopus%20Pro%20-%20SIZE.pdf)

:::

## Pinout 

<a href={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-pinout-light.png').default} target="_blank">
    <ThemedImage
        alt="octopus-pro-pinout"
        sources={{
            light: require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-pinout-light.png').default,
            dark: require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-pinout-dark.png').default,
        }} width="100%"
    />
</a>

## 硬件功能配置

### USB 接口供电

插入跳线即可使用 `USB-C` 为 `octopus` 供电。这可以使使用DFU模式直接编译和下载固件到主板更容易。

如果您不连接此跳线，那么如果您想通过 `USB-C` 进行通信，则必须通过主输入电源为板供电。

<img src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-usb-power.png').default} width="80%"/>

### 自动断电接线

当使用 BIGTREETECH 继电器 V1.2 模块时，可以按照下图所示进行接线。

<img src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-relay.png').default} width="80%"/>

:::warning

由于 `Relay 1.2` 模块在切断主板电源后仍将供电，因此在打印机仍连接到电源时触摸它是极其危险的。在处理此接线时，请务必断开所有主电源。

:::

### BL TOUCH

使用BL Touch时，如下图所示将其连接到主板。

<img src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-bltouch.png').default} width="80%"/>

### Neopixel

<img src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-neopix.png').default} width="80%"/>

### Raspberry Pi

Octopus Pro 支持连接到树莓派进行打印。有几种连接方式可用于连接 Raspberry Pi。

- Raspberry Pi 直接连接到 USB-C 端口
- 使用 UART 或 SPI 使用直接串行连接将 Raspberry Pi 连接

### 电机驱动配置

<Tabs groupId="octopus-stepper-driver">
    <TabItem value="tmc-uart" label="Uart 模式" default>
        使用 Uart 模式连接驱动
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-uart.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI 模式">
        使用 SPI 模式连接驱动
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-spi.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / dir 模式">
        使用不支持 Uart 或者 SPI 的驱动。
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-step-dir.png').default}
            alt="" width="100%"
        />
        以下是跳线参考，不同的驱动会有不同的跳线配置
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-step-dir-config.png').default}
            alt="" width="100%"
        />
    </TabItem>
</Tabs>

### 电机驱动电压选择

:::warning 

请勿在通电状态下插拔跳线帽

:::

<Tabs groupId="octopus-driver-v">
    <TabItem value="VBB" label="Octopus Pro VBB" default>
        当使用 `VBB` 进行供电的时候。来源为主板 `Power` 输入。最高电压为 `24V`。
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-vbb.png').default}
            alt="octo pro vbb" width="60%"
        />
    </TabItem>
    <TabItem value="high-oltage" label="Octopus Pro High Voltage">
        当使用 `High Voltage` 进行供电的时候。来源为主板 `Motor Power` 输入。最高电压为 `56V`。需要注意驱动最大电压范围。
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-hv.png').default}
            alt="octo pro high voltage" width="60%"
        />
    </TabItem>
</Tabs>

### 风扇电压选择

Octopus_Pro具有6个PWM风扇输出和两个“常开”风扇输出。还有一个用于接近传感器或探针的专用针头。

所有风扇输出和接近传感器输入都可以通过配置与每个插头相关的跳线来分别选择由其引脚插头提供的电压。

按以下方式配置跳线以选择24V（注意，所有跳线都显示在相同的配置中，即使它们可以单独配置）。

<Tabs groupId="octopus-fan-v">
    <TabItem value="24v-fan" label="24V 风扇 / 接近开关" default>
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-24.png').default}
            alt="octo pro fan 24" width="100%"
        />
    </TabItem>
    <TabItem value="12v-fan" label="12V 风扇 / 接近开关">
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-12.png').default}
            alt="octo pro fan 12" width="100%"
        />
    </TabItem>
    <TabItem value="5v-fan" label=" 5V 风扇 / 接近开关">
        <img
            src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-fan-5.png').default}
            alt="octo pro fan 5" width="100%"
        />
    </TabItem>
</Tabs>

### TMC STALLGUARD 跳线设置

可在下图所示的位置找到用于将诊断输出引脚连接到支持安装保护功能（TMC2209/TMC2226等）的驱动器端部停止输入的“diag”跳线。

确切的diag编号可以通过查看引脚文件或板下的丝印来找到。

<img src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-driver-spi.png').default} width="80%"/>

### MAX 31865

<div class="div-table">

<img src={require('@site/docs/board-docs/octopus-series/octopus-pro/img/octopus-pro-max-31865.png').default} width="50%" class="right-image"/>

MAX 31865 选择 PT100/PT1000 2线或4线配置

| 1   | 2   | 3   | 4   | Sensor Model  |
| --- | --- | --- | --- | ------------- |
| ON  | ON  | ON  | OFF | 2 wire PT100  |
| ON  | ON  | OFF | ON  | 2 wire PT1000 |
| OFF | OFF | ON  | OFF | 4 wire PT100  |
| OFF | OFF | OFF | ON  | 4 wire PT1000 |

</div>
