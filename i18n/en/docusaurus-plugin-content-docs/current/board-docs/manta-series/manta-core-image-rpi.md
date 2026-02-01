---
sidebar_position: 10
description: Manta Series Core Board System Writing
---

# Manta Series Core Board Raspberry CM4/CM5

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

### Before Start 

:::info[Raspberry Pi Imager]

[Raspberry Pi Imager](https://www.raspberrypi.com/software/)

:::

:::info[Raspberry Pi System]

[software/operating-systems](https://www.raspberrypi.com/software/operating-systems/)

:::

:::info[rpiboot]

The eMMC version requires this tool to read and write to eMMC.

[rpiboot](https://github.com/raspberrypi/usbboot/tree/master/win32)
:::

### Flash System

<Tabs groupId="cm-system-flash">
    <TabItem value="sd-card" label="Use SD Card" default>
        Insert the Micro SD card into the computer using a card reader, then select the system.

        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-1.png').default} width="65%"/>

        Select `Use custom`, then choose the image downloaded to the computer.

        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-2.png').default} width="65%"/>

        Select the Micro SD card to be written, then write the system image.

        :::warning

        Writing the image will format all data on the SD card. Please make sure your data is backed up before formatting.

        :::

        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-3.png').default} width="65%"/>

        Wait for the system writing to complete
        
        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-4.png').default} width="65%"/>
    </TabItem>
    <TabItem value="emmc" label="Use eMMC">
        First, set switches 3 `RPIBOOT` and 4 `USBOTG` to `ON` to enter BOOT mode

        Then connect the Type-C cable to the computer. It is recommended to use an external 24V power supply.

        Use `rpiboot` to put the Raspberry Pi into BOOT mode. At this time, the eMMC will be recognized as a mass storage device.
        
        Then use Raspberry Pi Imager to select the system

        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-1.png').default} width="65%"/>

        Select `Use custom`, then choose the image downloaded to the computer.

        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-2.png').default} width="65%"/>

        Select the eMMC device to be written, then write the system image.

        :::warning

        Writing the image will format all data on the eMMC. Please make sure your data is backed up before formatting.

        :::

        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-3.png').default} width="65%"/>

        Wait for the system writing to complete

        <img src={require('@site/docs/board-docs/manta-series/img/cm-flash-4.png').default} width="65%"/>
    </TabItem>
</Tabs>
