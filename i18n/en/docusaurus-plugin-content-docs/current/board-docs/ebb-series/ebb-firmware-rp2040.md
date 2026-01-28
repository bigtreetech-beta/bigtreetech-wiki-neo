---
sidebar_position: 10
---

# EBB Series Firmware (RP2040)

EBB use `RP2040` MCU

## Build Firmware

Use SSH to connect to the Klipper host. Then use the following command to enter the Klipper directory, and run `make menuconfig` to configure the firmware.

``` shell
cd ~/klipper
make menuconfig 
```

Then build the EBB firmware using `RP2040` as the `MCU` according to the following options.

<img
    src={require('@site/docs/board-docs/ebb-series/img/ebb-g0b1-make-can.png').default}
    alt="EBB with RP2040 build config"
/>

After the configuration is complete, press `q` to exit and press `y` to save the build options.

Then use the `make` command to start compiling the Klipper firmware.

``` shell
make
```

## Flash Firmware

:::note[Power via USB]
If you are powering the board via the USB Type-C port when flashing the firmware, the `VUSB` jumper needs to be installed.
:::

After the Klipper firmware has been compiled, use a USB Type-C cable to connect the EBB to the Klipper host.

Then press and hold the `boot` button on the EBB, press the `reset` button once, and then release the `boot` button to enter `Boot` mode.

After that, you can use the `lsusb` command to verify whether the EBB is in `DFU` mode.

Once you have confirmed that the EBB is in DFU mode, you can use the following command to flash the firmware.

``` shell
make flash FLASH_DEVICE=2e8a:0003
```
