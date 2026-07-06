---
sidebar_position: 10
---

# Manta M8P Series Firmware (STM32H723)

Manta M8P with the `STM32H723` MCU 

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

## Building the Firmware

Connect to the Klipper Host via SSH. Then use the following command to navigate to the Klipper directory. Use `make menuconfig` to configure the firmware.

``` shell
cd ~/klipper
make menuconfig 
```

<Tabs groupId="m8p-v2-make-connect">
    <TabItem value="bridge" label="CAN Bridge Firmware" default>
        Build the `Manta M8P` CAN bridge firmware using the `STM32H723` as the `MCU` according to the following options
        <ImageView
            src={require('@site/docs/board-docs/manta-series/img/manta-h723-make-bridge.png').default}
            alt="manta m8p with h723 bridge"
        />
    </TabItem>
    <TabItem value="usb" label="USB Serial Firmware">
        Build the `Manta M8P` USB serial firmware using the `STM32H723` as the `MCU`, following the options below
        <ImageView
            src={require('@site/docs/board-docs/manta-series/img/manta-h723-make-usb.png').default}
            alt="manta m8p with h723 usb"
        />
    </TabItem>
</Tabs>

When you're done configuring, use `q` to exit. Use `y` to save the compilation options.

Then use the `make` command to start compiling the Klipper firmware

``` shell
make
```

## Flash Firmware

Once the Klipper firmware has finished compiling, press and hold the `boot` button on the `Manta M8P`. Then press the `reset` button once and release the `boot` button to enter `DFU` mode.

You can then use the `lsusb` command to verify whether the `Manta M8P` is in `DFU` mode.

Once you have confirmed that the Manta M8P is in DFU mode, you can use the following command to flash the firmware.

``` shell
make flash FLASH_DEVICE=0483:df11
```
