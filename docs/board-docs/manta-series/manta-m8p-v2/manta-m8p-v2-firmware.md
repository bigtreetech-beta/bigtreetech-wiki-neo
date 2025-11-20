---
sidebar_position: 3
description: Manta M8P V2 固件配置
---

# Manta M8P v2 固件配置

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 核心板固件写入

### Raspberry CM4/CM5

#### 在开始之前

:::info[Raspberry Pi Imager]

[Raspberry Pi Imager](https://www.raspberrypi.com/software/)

:::

:::info[Raspberry Pi 系统]

[software/operating-systems](https://www.raspberrypi.com/software/operating-systems/)

:::

:::info[rpiboot]

eMMC 版本需要这个工具来读写 eMMC

[rpiboot](https://github.com/raspberrypi/usbboot/tree/master/win32)
:::

#### 写入系统

<Tabs groupId="cm-system-flash">
    <TabItem value="sd-card" label="使用 SD 卡" default>
        将 Micro SD 卡通过读卡器插入到电脑, 然后选择系统。

        <img src={require('./img/cm-flash-1.png').default} width="65%"/>

        选择 `Use custom` 然后选择下载到电脑中的镜像。

        <img src={require('./img/cm-flash-2.png').default} width="65%"/>

        选择需要写入的 Micro SD。然后写入系统镜像。

        :::warning

        写入镜像会格式化 SD 卡内的所有数据。请在格式化前确保数据已备份。

        :::

        <img src={require('./img/cm-flash-3.png').default} width="65%"/>

        等待系统写入完成
        
        <img src={require('./img/cm-flash-4.png').default} width="65%"/>
    </TabItem>
    <TabItem value="emmc" label="使用 eMMC">
        首先将开关的 3 `RPIBOOT` 和 4 `USBOTG` 调整到 `ON` 进入 BOOT 模式

        然后将 Type-C 线连接到电脑。推荐使用外置 24V 电源进行供电。

        使用 `rpiboot` 让 Raspberry Pi 进入 BOOT 模式。这时候 eMMC 会被识别成大容量储存设备。
        
        然后使用 Raspberry Pi Imager 选择系统

        <img src={require('./img/cm-flash-1.png').default} width="65%"/>

        选择 `Use custom` 然后选择下载到电脑中的镜像。

        <img src={require('./img/cm-flash-2.png').default} width="65%"/>

        选择需要写入的 eMMC 设备。然后写入系统镜像。

        :::warning

        写入镜像会格式化 eMMC 内的所有数据。请在格式化前确保数据已备份。

        :::

        <img src={require('./img/cm-flash-3.png').default} width="65%"/>

        等待系统写入完成
        
        <img src={require('./img/cm-flash-4.png').default} width="65%"/>
    </TabItem>
</Tabs>
