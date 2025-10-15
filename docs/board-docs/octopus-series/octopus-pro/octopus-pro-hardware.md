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

## 外观尺寸


## Pinout 

<a href={require('./img/octopus-pro-pinout-light.png').default} target="_blank">
    <ThemedImage
        alt="octopus-pro-pinout"
        sources={{
            light: require('./img/octopus-pro-pinout-light.png').default,
            dark: require('./img/octopus-pro-pinout-dark.png').default,
        }} width="100%"
    />
</a>

## 硬件功能配置

### USB 接口供电

插入跳线即可使用 `USB-C` 为 `octopus` 供电。这可以使使用DFU模式直接编译和下载固件到主板更容易。

如果您不连接此跳线，那么如果您想通过 `USB-C` 进行通信，则必须通过主输入电源为板供电。

<img src={require('./img/octopus-pro-usb-power.png').default} width="80%"/>

### 自动断电接线

当使用 BIGTREETECH 继电器 V1.2 模块时，可以按照下图所示进行接线。

<img src={require('./img/octopus-pro-relay.png').default} width="80%"/>

:::warning

由于 `Relay 1.2` 模块在切断主板电源后仍将供电，因此在打印机仍连接到电源时触摸它是极其危险的。在处理此接线时，请务必断开所有主电源。

:::

### BL TOUCH

使用BL Touch时，如下图所示将其连接到主板。

<img src={require('./img/octopus-pro-bltouch.png').default} width="80%"/>

### Neopixel

<img src={require('./img/octopus-pro-neopix.png').default} width="80%"/>

### Raspberry Pi

Octopus Pro 支持连接到树莓派进行打印。有几种连接方式可用于连接 Raspberry Pi。

- Raspberry Pi 直接连接到 USB-C 端口
- 使用 UART 或 SPI 使用直接串行连接将 Raspberry Pi 连接

### 电机驱动配置

<Tabs groupId="octopus-stepper-driver">
    <TabItem value="tmc-uart" label="Uart 模式" default>
        使用 Uart 模式连接驱动
        <img
            src={require('./img/octopus-pro-driver-uart.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="tmc-spi" label="SPI 模式">
        使用 SPI 模式连接驱动
        <img
            src={require('./img/octopus-pro-driver-spi.png').default}
            alt="" width="100%"
        />
    </TabItem>
    <TabItem value="step-dir" label="Step / dir 模式">
        使用不支持 Uart 或者 SPI 的驱动。
        <img
            src={require('./img/octopus-pro-driver-step-dir.png').default}
            alt="" width="100%"
        />
        以下是跳线参考
        <img
            src={require('./img/octopus-pro-driver-step-dir-config.png').default}
            alt="" width="100%"
        />
    </TabItem>
</Tabs>

