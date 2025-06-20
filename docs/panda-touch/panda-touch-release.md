---
sidebar_position: 4
---

# Panda Touch 固件发布记录

Panda Touch 发布记录

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

### [V1.0.7.1](https://github.com/bigtreetech/PandaTouch/blob/master/Firmware/1.0.7.1/panda_touch-v1.0.7.1.bin)

#### Bug修复

- **Panda Sense问题**：Panda Sense温度值有时不更新
- **零件跳过不可用**：有些打印任务零件跳过功能不可用
- **重打印功能异常**：同步拓竹最新云打印请求格式（暂不支持自定义耗材）
- **AMS打印异常**：可配置AMS映射（当前仅支持AMS-1，不支持自定义耗材）
- **FTPS其他目录的缩略图不显示**
- **SD卡文件年份信息丢失**

#### 功能优化
- **提升缩略图尺寸**：通过Bambu Studio/Handy app打印时，主页缩略图分辨率由128 * 128增大至280 * 306.
- **后台机型实时更新**：实时从云服务器同步打印机机型.
- **调整MQTT缓存**：将MQTT缓冲区大小调整为40KB.

### [V1.0.7](https://github.com/bigtreetech/PandaTouch/blob/master/Firmware/1.0.7/panda_touch-v1.0.7.bin)

#### 修复BUG

- **修复打印机名称不同步问题**：实时获取服务器上打印机名称，如果发生变化就更新它。
- **修复轴方向错误问题**: 修复控制A1和A1-mini的Y轴和Z轴运动时方向错误问题。

#### 新特性

- **支持零件跳过**: 允许用户在打印机选择需要跳过的零件. 
- **支持烘干耗材**: 允许用户在P1S上烘干耗材.  

### [V1.0.6.3](https://github.com/bigtreetech/PandaTouch/blob/master/Firmware/1.0.6.3/panda_touch-v1.0.6.3.bin)

#### 修复BUG
- **当打印时崩溃**: 从U盘打印时崩溃重启.
- **在OTA页面崩溃**: 在OTA页面点击wifi名称时崩溃重启.

#### 功能修改
- **在打印时停止加载缩略图**. 
