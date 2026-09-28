---
sidebar_position: 10
---

# Manta M4P 系列固件 (STM32G0B1)

使用 `STM32G0B1` MCU 的 Manta M4P

{/* import lib start */}

{/* import lib end */}

## 构建固件

使用 ssh 连接到 Klipper Host. 然后使用以下命令进入 Klipper 目录。并且使用 `make menuconfig` 配置固件。

``` shell
cd ~/klipper
make menuconfig
```

按照以下选项构建使用 `STM32G0B1` 为 `MCU` 的 `Manta M4P` USB 串口固件

<ImageView src={require('./img/manta-m4p-make-usb.png').default} alt="manta m4p with g0b1 usb"/>

当配置完成使用 `q` 来退出。使用 `y` 来保存编译选项。

然后使用 `make` 命令来开始编译 Klipper 固件

``` shell
make
```

## 写入固件 (Via SD card)

:::warning[MCU-Card 使用条件]

通过 MCU-Card 更新固件，要求主板保留出厂自带的 Bootloader。若 Bootloader 被擦除或覆盖，该卡槽便无法执行固件更新；须先通过其他烧录方式恢复适用于此型号及硬件版本的出厂 Bootloader。

:::

1. 从 `~/klipper/out/` 中复制 `klipper.bin` 并且改名为 `firmware.bin`
2. 复制 `firmware.bin` 到 SD 卡的根目录中
3. 将 SD 卡插入主板的 MCU-Card 卡槽，不要插入 SOC-Card 卡槽
4. 给主板通电
