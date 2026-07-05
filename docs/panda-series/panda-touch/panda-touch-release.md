---
sidebar_position: 4
---

# Panda Touch 固件发布记录

Panda Touch 发布记录

{/* import lib start */}

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

{/* import lib end */}

### [V1.0.8.0](https://github.com/bigtreetech/PandaTouch/releases/tag/release%2Fv1.0.8.0)

#### Bug修复

- **休眠 / 唤醒重启问题**：修复休眠 / 唤醒崩溃导致的反复重启问题。
- **唤醒 / 开始打印重启问题**：修复唤醒或开始打印后频繁短周期重启、循环重启的问题。
- **OTA IMG升级问题**：增加 OTA IMG 升级校验并提升升级稳定性，降低升级过程中刷写失败的概率。
- **AMS2 / AMS-HT检测问题**：修复 AMS2 / AMS-HT 的搜索和检测逻辑。
- **外挂料架进料问题**：修复外挂料架加载逻辑，确保进料 / 退料操作正常。
- **外挂料架刷新和AMS槽位映射问题**：修复外挂料架刷新和 AMS 槽位映射问题，确保槽位状态正确显示。
- **Wi-Fi兼容性问题**：优化 WPA2 / WPA3 Wi-Fi 兼容性。
- **云账号登录重启问题**：修复登录 Bambu Lab 云账号时可能导致设备重启的问题。

#### 功能优化

- **打印唤醒行为**：优化打印唤醒逻辑，打印任务运行时设备保持唤醒状态。
- **固件警告流程**：重新设计固件警告流程，使恢复路径更加清晰。
- **固件升级警告提示**：优化固件升级过程中的警告提示。
- **AMS界面**：重新设计 AMS 界面，槽位布局和状态显示更加清晰。
- **耗材管理界面**：重构耗材管理界面及相关耗材管理逻辑。
- **打印机 / 分组列表模式**：新增打印机和分组列表视图模式。
- **进料 / 退料操作流程**：优化进料 / 退料操作流程中的步骤提示。
- **警告弹窗**：优化警告弹窗。
- **打印中屏保模式**：新增打印过程中的屏保模式，避免打印时误操作。
- **文件管理器界面**：重构文件管理器界面，并优化文件管理逻辑和缩略图显示逻辑。
- **通知提示**：更新通知提示并新增通知消息内容。

### [v1.0.7.3](https://github.com/bigtreetech/PandaTouch/releases/tag/release%2Fv1.0.7.3)

- 添加固件不兼容提示

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
