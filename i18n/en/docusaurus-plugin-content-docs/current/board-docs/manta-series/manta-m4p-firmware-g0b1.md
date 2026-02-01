---
sidebar_position: 10
---

# Manta M4P Series Firmware (STM32G0B1)

Manta M4P using the `STM32G0B1` MCU

<!-- import lib start -->

<!-- import lib end -->

## Build Firmware

Use SSH to connect to the Klipper Host. Then use the following command to enter the Klipper directory and use `make menuconfig` to configure the firmware.

``` shell
cd ~/klipper
make menuconfig 
```

Build the USB serial firmware for `Manta M4P` using `STM32G0B1` as the `MCU` according to the following options.

<img src={require('@site/docs/board-docs/manta-series/img/manta-m4p-make-usb.png').default} alt="manta m4p with g0b1 usb"/>

After configuration, use `q` to exit and `y` to save the build options.

Then use the `make` command to start compiling the Klipper firmware.

``` shell
make
```

## Flash Firmware (Via SD card)

1. Copy `klipper.bin` from `~/klipper/out/` and rename it to `firmware.bin`
2. Copy `firmware.bin` to the root directory of the MCU SD card
3. Insert the MCU SD card
4. Power on the mainboard
