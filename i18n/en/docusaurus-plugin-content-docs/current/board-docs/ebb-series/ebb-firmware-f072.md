---
sidebar_position: 11
---

# EBB Series Firmware (STM32F072)

EBB using the `STM32F072` MCU

## Build Firmware

Use SSH to connect to the Klipper Host. Then use the following command to enter the Klipper directory, and use `make menuconfig` to configure the firmware.

``` shell
cd ~/klipper
make menuconfig 
```

Then build the `EBB` firmware using `STM32F072` as the `MCU` according to the following options.

<img
    src={require('@site/docs/board-docs/ebb-series/img/ebb-f072-make-can.png').default}
    alt="EBB with f072 build config"
/>

After the configuration is complete, use `q` to exit. Use `y` to save the compilation options.

Then use the `make` command to start compiling the Klipper firmware.

``` shell
make
```

## Flash Firmware

:::note USB Power Supply
If you use the USB Type-C interface for power supply when flashing the firmware, the `VUSB` jumper needs to be connected.
:::

After the Klipper firmware compilation is complete, use a USB Type-C cable to connect to the Klipper Host.

Then press and hold the `boot` button on the `EBB`. Then press the `reset` button once and release the `boot` button to enter `DFU` mode.

Then you can use the `lsusb` command to confirm whether the `EBB` is in `DFU` mode.

After confirming that the EBB is in DFU mode, you can use the following command to flash the firmware.

``` shell
make flash FLASH_DEVICE=0483:df11
```
