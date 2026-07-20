---
sidebar_position: 10
---

# Octopus Series Firmware (STM32F446)

Octopus with the `STM32F446` MCU 

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

<Tabs groupId="octopus-make-connect">
    <TabItem value="bridge" label="CAN Bridge Firmware" default>
        Build the `Octopus` CAN bridge firmware using the `STM32F446` as the `MCU` according to the following options
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/img/octopus-f446-make-bridge.png').default}
            alt="octopus with h723 bridge"
        />
    </TabItem>
    <TabItem value="usb" label="USB Serial Firmware">
        Build the `Octopus` USB serial firmware using the `STM32F446` as the `MCU` according to the following options
        <ImageView
            src={require('@site/docs/board-docs/octopus-series/img/octopus-f446-make-usb.png').default}
            alt="octopus with h723 usb"
        />
    </TabItem>
</Tabs>

When you're done configuring, use `q` to exit. Use `y` to save the compilation options.

Then use the `make` command to start compiling the Klipper firmware

``` shell
make
```

## Flash Firmware

:::note[USB Power]

If you are using the USB Type-C port for power while flashing the firmware, the `VUSB` jumper must be connected.

:::

Once the Klipper firmware has finished compiling, connect it to the Klipper Host using a USB Type-C cable.

Next, hold down the `boot` button on the `Octopus`. Then press the `reset` button once and release the `boot` button to enter `DFU` mode.

You can then use the `lsusb` command to verify whether `Octopus` is in `DFU` mode.

Once you have confirmed that Octopus is in DFU mode, you can use the following command to flash the firmware.

``` shell
make flash FLASH_DEVICE=0483:df11
```
