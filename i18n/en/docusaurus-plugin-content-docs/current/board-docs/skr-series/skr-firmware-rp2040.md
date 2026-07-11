---
sidebar_position: 10
---

# SKR Series Firmware (RP2040)

SKR using the `RP2040` MCU

## Building the Firmware

Connect to the Klipper Host via SSH. Then use the following command to navigate to the Klipper directory. Use `make menuconfig` to configure the firmware.

``` shell
cd ~/klipper
make menuconfig 
```

然后按照以下选项构建使用 `RP2040` 为 `MCU` 的 `SKR` 固件

<ImageView
    src={require('@site/docs/board-docs/skr-series/img/skr-rp2040-make-usb.png').default}
    alt="skr rp2040 usb"
/>

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

Next, insert the `boot` jumper on the `SKR`. Then press the `reset` button once to enter `Boot` mode.

You can then use the `lsusb` command to verify whether the `MCU` is in `Boot` mode.

Once you have confirmed that the `MCU` is in `Boot` mode, you can use the following command to write the firmware.

``` shell
make flash FLASH_DEVICE=2e8a:0003
```
