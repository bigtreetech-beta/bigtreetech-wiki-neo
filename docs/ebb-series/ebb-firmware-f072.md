---
sidebar_position: 11
---

# EBB 系列固件 (STM32F072)

使用 `STM32F072` MCU 的 EBB

## 构建固件

使用 ssh 连接到 Klipper Host. 然后使用以下命令进入 Klipper 目录。并且使用 `make menuconfig` 配置固件。

``` shell
cd ~/klipper
make menuconfig 
```

然后按照以下选项构建使用 `STM32F072` 为 `MCU` 的 `EBB` 固件

