---
sidebar_position: 10
---

# Manta M5P Series Firmware (STM32G0B1)

Manta M5P using the `STM32G0B1` MCU

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## Build Firmware

Use SSH to connect to the Klipper Host. Then use the following command to enter the Klipper directory and use `make menuconfig` to configure the firmware.

``` shell
cd ~/klipper
make menuconfig 
```

<Tabs groupId="M5P-v1-make-connect">
    <TabItem value="bridge" label="CAN Bridge Firmware" default>
        Build the CAN bridge firmware for `Manta M5P` using `STM32G0B1` as the `MCU` according to the following options.
        <img
            src={require('@site/docs/board-docs/manta-series/img/manta-m5p-make-bridge.png').default}
            alt="manta M5P with g0b1 bridge"
        />
    </TabItem>
    <TabItem value="usb" label="USB Serial Firmware">
        Build the USB serial firmware for `Manta M5P` using `STM32G0B1` as the `MCU` according to the following options.
        <img
            src={require('@site/docs/board-docs/manta-series/img/manta-m5p-make-usb.png').default}
            alt="manta M5P with g0b1 usb"
        />
    </TabItem>
</Tabs>

After configuration, use `q` to exit and `y` to save the build options.

Then use the `make` command to start compiling the Klipper firmware.

``` shell
make
```

## 写入固件

After compiling the Klipper firmware, press and hold the `boot` button on the `Manta M5P`. Then press `reset` once and release the `boot` button to enter `DFU` mode.

You can then use the `lsusb` command to confirm whether the `Manta M5P` is in `DFU` mode.

Once confirmed that the Manta M5P is in DFU mode, you can use the following command to flash the firmware.

``` shell
make flash FLASH_DEVICE=0483:df11
```
