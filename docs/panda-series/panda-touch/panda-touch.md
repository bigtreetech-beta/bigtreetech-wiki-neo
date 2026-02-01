---
sidebar_position: 1
---

# Panda Touch

Panda Touch 说明文档

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

:::warning 已知固件兼容性问题

拓竹可能会在未来发布影响Panda Touch可用功能的固件版本。Bigtreetech将监控所有测试版固件版本，如果我们发现影响Panda Touch功能的固件版本，我们将通过电子邮件、速卖通聊天和我们的社交渠道发出警报。然后，购买者可以决定是否要冒着失去功能的风险执行更新。请注意，Panda Touch保修不包括由于执行Bambu Lab固件更新而导致的功能损失。

Panda Touch 的部分功能（如发起打印、控制运动系统、调节温度、风扇、AMS设置及校准）预计将受到 Bambu Lab最近宣布的新固件中的授权和身份验证机制影响而无法使用（目前该固件在 X1 系列内测中），但获取打印进度、喷嘴温度、热床温度等打印机状态信息的功能不受影响，同时后续你仍可以在新固件的打印机中的LAN模式下手动启用开发者模式后以使用 Panda Touch 的全部功能。

https://bigtree-tech.com/blogs/news/announcement-on-bambu-lab-security-firmware-update 
https://blog.bambulab.com/firmware-update-introducing-new-authorization-control-system-2/ 
https://blog.bambulab.com/updates-and-third-party-integration-with-bambu-connect/

Panda Touch目前与所有 Bambu Lab 打印机固件版本兼容，直到:

P1P/S: 01.07.00.00

X1C: 01.08.02.00

X1E: 01.01.02.00

A1: 01.04.00.00

A1 Mini: 01.04.00.00

:::

:::warning 重要信息

当 P1P 或 P1S 使用“仅限局域网”模式时，无需将 Panda Touch 连接到云账户，所有打印机功能都可以从 Panda Touch 上使用。

当打印机设置为连接云端时，您需要在 Panda Touch 上启用云模式功能，以保留控制加热器和打印功能的能力。

请检查产品页面描述中的固件列表，以确保您的打印机固件与Panda Touch兼容。将打印机固件更新到可能限制Panda Touch功能的不兼容版本，不在保修范围内。

目前，MicroSD 卡和 USB 驱动器文件只能从根目录读取，并且只有在 Bambu Studio 中将模型切片到构建板 #1 时，且文件为 3mf 格式时才会被识别。文件夹浏览和缩略图预览将在未来的固件版本中推出。

Panda Touch 在其内置锂电池上运行时，电池续航时间大约为 20 到 30 分钟，具体取决于屏幕亮度。为了维护电池并延长产品寿命，建议在电池耗尽后及时给 Panda Touch 充电或关闭电源。

当锂电池电量不足时，屏幕可能会闪烁。这种闪烁是正常的，并向用户发出电池几乎耗尽的警告。然后，用户应立即给电池充电或关闭Panda Touch。

如果您计划经常打开和关闭打印机，我们建议您在 DC5V 模式下运行 Panda Touch。这样可以绕过电池，防止电池经历多次充放电循环。如果您想使用电池供电，只需将 
Panda Touch 背面的开关切换到电池电源模式。

最大支持USB驱动器的容量是8GB.

:::

## 基本参数

| Panda Touch | 参数 |
| ---- | ---- |
| 微处理器 | Xtensa 32位LX7双核ESP32S3R8<br/>时钟速度高达240MHz。 |
| 存储器 | PSRAM-8MB, Flash-16MB |
| 屏幕尺寸 | 5” |
| 分辨率 | 800 x 480 |
| 可视角度 | IPS完整视图 |
| 显示颜色 | 16.7M |
| 通信方式 | 2.4G Wi-Fi (IEEE 802.11 b/g/n) |
| 工作温度 | 0-60°C |
| 工作电流（充满电） | 屏幕激活：0.6A，屏幕非激活：0.2A |
| 工作电流（充电） | 屏幕激活：1.25A，(0.95A 2024年5月后) 屏幕非激活：0.85A |
| 逻辑电压 | 3.3V |
| 内置电池 | 允许Panda Touch便携式使用长达30分钟。 |
| 充电时间 | 1.2小时 |
| 扩展接口 | I2C（用于未来固件等中支持的温度/湿度传感器）<br/>USB驱动器（用于从USB驱动器读取3mf文件-仅限FAT32） |


