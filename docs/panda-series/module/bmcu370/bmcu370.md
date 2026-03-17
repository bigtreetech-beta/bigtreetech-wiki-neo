# BMCU-370

<div class="div-table">

<ImageView src={require('./img/panda-bmcu370-5.webp').default} width="40%" class="right-image"/>


产品购买链接：[点击购买](https://item.taobao.com/item.htm?id=1026843975380&mi_id=0000-YhadGR9vqdAPhcaJyR0ZqxIe84HSe_mbNvLbvjH44E&spm=a21xtw.29978516.0.0&xxc=shop)

打印件下载链接：[结构件](https://makerworld.com/zh/models/2472248-bmcu-c-370-hall-effect-structural-components#profileId-2714532)

回转料架下载链接：[回转轴料架](https://makerworld.com/zh/models/2472284-rotary-spool-holder-for-bmcu-370#profileId-2714571)

## 修订历史

| 版本号 | 日期 | 更新内容 |
| --- | --- | --- |
| v1.0.0 | 2026年03月10号 | 初始版本 |

## 固件版本

| BMCU-370固件版本 | 兼容 A1 固件版本 | 兼容 A1 mini 固件版本 | 兼容P1S固件版本 | 兼容X1固件版本 | BMCU-370固件下载链接 |
| --- | --- | --- | --- | --- | --- |
| BMCU-V0.1-0027改(本产品已烧录该版本固件) | 01.04.00.00 01.05.00.00 01.06.00.00 01.07.00.00   01.07.02.00  | 01.04.00.00 01.05.00.00 01.06.00.00 01.07.00.00 01.07.02.00 |  |  |  [BMCU-V0.1-0027-upgrade](https://github.com/bigtreetech/BMCU/tree/master/BMCU-V0.1-0027-upgrade) |
| BMCU-CV0.1-0020-Auto Direction 745 Retract Distance | -- | -- | 01.07.00.00 | 01.08.50.32 | [BMCU-CV0.1-0020-Auto Direction 745 Retract Distance](https://github.com/bigtreetech/BMCU/blob/master/BMCU-CV0.1-0020-Auto%20Direction%20745%20Retract%20Distance.bin) |

## 产品简介

BMCU 是根据开源资料设计的模拟 AMS 运行的多材料控制系统，适用于 Bambu Lab A系列/X系列/P系列（P2S暂未适配）。BMCU 设计为四通道单元，目前设计方案以CH32微控制器为主控制单元。暂不支持 RFID 材料识别。

BMCU 的稳定性不如 AMS Lite，作为第三方DIY配件，后续可能因为官方更新适配的打印机固件而无法使用。BMCU仍然在不断更新迭代中，在后续的使用过程中可能会发布新的固件或者结构件，您可能需要自行升级。

同时，BMCU 仅供 DIY 学习使用，非常感谢原作者 4061N。BIQU是BMCU项目原作者唯一官方合作伙伴。

## 产品特点

- 退料不需要像AMCU一样退到断料检测，而是退出五通即可，切换耗材速度较快。
- 并排式结构，不包含料架，这意味着你可以将耗材放在密封箱中，由它来给你的打印机供料。
- 具有一个缓冲器，在打印机触发缠料之前就可以主动送料，防止耗材阻力过大导致的问题。
- 器件标准化，我们在设计机械时，将许多部件确定为统一参数，这使得一次性DIY成功率得以提高，防止成本增加。
- BMCU探索出了光电探测设计，允许光电开关探测透明耗材，杜绝了微动探测方式造成的耗材阻力和其不稳定性。光电的设计将另行使用其他开源协议，允许借用。

</div>

## 产品参数

| 产品名称 | BIQU BMCU-370 霍尔版 |
| --- | --- |
| 产品版本 | BMCU-370 霍尔版【组装成品套件】开箱即用，10分钟完成安装,BMCU-370 霍尔版【DIY套件】需自行打印结构件并组装。
| 兼容机型 | A1,A1 mini,P1P,P1S,X1C,X1E |
| 主控 | ch32v203c8t6 |
| 电源输入 | AC 24V |
| 通道 | 四通道 |
| 通信接口 | 4-PIN |
| 外壳材质 | ABS |

## BMCU-370 Bambu Lab A1 安装指南

- 第一步：取出包装中的固定支架，使用附带的 M3*8 自攻螺丝按下图方式固定在 BMCU-370 壳体上。

    <ImageView src={require('./img/panda-bmcu370-6.webp').default} width="70%"/>

- 第二步：将已安装完成固定支架的产品按如下图方式固定到Bambu Lab A1龙门架上方。

    <ImageView src={require('./img/panda-bmcu370-3.webp').default} width="70%"/>

- 第三步：将 BMCU-370 通过附带的4-PIN线与Bambu Lab A1机器预留的4-PIN接口(在机器背部，任意一个即可)相连接。

    <ImageView src={require('./img/panda-bmcu370-2.webp').default} width="70%"/>

    <ImageView src={require('./img/panda-bmcu370-7.webp').default} width="70%"/>

- 第四步：打开Bambu Lab电源开关。在操作屏幕首页点击“设置”（若有外挂耗材还未退料，需要先退料），然后选择“AMS选项”，最后点击“AMS类型”设置为“AMS/AMS 2 Pro/AMS HT”模式，最后将Bambu Lab A1 重新开机即可。

:::note

注意：BMCU-370不具备自动进料功能，需要先进行手动进料。

:::

## BMCU-370 Bambu Lab A1 mini 安装指南

- 第一步：下载并打印 BMCU A1 mini 旋转支架，推荐[bmcu-A1mini 旋转支架](https://makerworld.com/zh/models/1186174-bmcu-a1mini-rotary-mount?from=search#profileId-1198642)
- 第二步：按教程中所示安装好BMCU-370，与Bambu Lab A1 mini通过 4-pin线连接。

    <ImageView src={require('./img/panda-bmcu370-4.webp').default} width="70%"/>

- 第三步：需要切换AMS类型，步骤同上。

## BMCU-370 Bambu Lab P/X 安装指南

- 第一步：参考下方“BMCU-370 固件烧录指南”烧录适配P/X的固件版本。
- 第二步：需要准备适配 P/X 的五通结构件，可自行在makerworld平台寻找心怡的方案或者购买。（推荐购买成品，3D打印件内部摩檫力较大，影响打印，可能会造成耗材进出出问题。）
- 第三步：准备 BMCU-370 安装到 P/X 的安装支架和零件，同样在makerworld平台有很多优秀的方案。
- 第四步：准备耗材收纳支架，推荐下载链接：[料架收纳](https://makerworld.com/zh/models/2472284-rotary-spool-holder-for-bmcu-370#profileId-2714571)
- 将BMCU-370通过4-pin线与P1S连接，并重新开机，即可准备完成。

:::note

需要在Bambu Studio软件的设备页面，将P/X连接后，并操作外挂料盘退料。

:::

## BMCU-370 两个以上多色打印指南

可以参考开源作者Paweł Jarczak 在 Github 开源分支：[BMCU-C-PJARCZAK](https://github.com/jarczakpawel/BMCU-C-PJARCZAK)

## BMCU-370 固件烧录指南

- 第一步：准备好烧录器，推荐购买[**BIGTREETECH Writer串行端口调试模块**](https://item.taobao.com/item.htm?id=627331721359&mi_id=0000vQL5NFKOkDLZMe08bh723s-7olAAl4oH9995m6kZHfY&spm=a21xtw.29978518.0.0&xxc=shop&skuId=4625623931905)，并且按如下图线序将烧录器与 BMCU-370 主板相连接；

    |   烧录器接口 |    主板接口 |
    | --- | --- |
    |   3V3 |   V+  |
    |   GND |   GND |
    |   RXD |   Tx  |
    |   TXD |   Rx  |

    <ImageView src={require('./img/panda-bmcu370-1.webp').default} width="70%"/>

- 安装 [WCHISPTool_Setup.exe](https://www.wch.cn/downloads/WCHISPTool_Setup_exe.html)
- 打开 WCHISPTool_Setup ，如果出现如下图弹窗，只需要点击“确定”或右上角的“X”关闭此弹窗即可。

    <ImageView src={require('./img/panda-bmcu370-9.webp').default} width="70%"/>

- 烧录准备：

    1. 点击“通用RISC-V系列 CH32Vxxx”

    2. 选择“芯片系列”为“CH32V20x”

    3. 选择“芯片型号”为“CH32V203C8T”

    4. 选择“下载接口”为“串口”

    5. 点击“搜索”，搜索烧录串口

    6. 将COM端口设置为烧录串口的端口号

    7. “下载配置”，默认即为如下图中的配置无需修改，如果不小心修改过了，请按照图片中的配置设置回来。

    <ImageView src={require('./img/panda-bmcu370-10.webp').default} width="70%"/>

- 选择测试固件的路径

    <ImageView src={require('./img/panda-bmcu370-11.webp').default} width="70%"/>

- 按住BOOT不松，点击一下RESET之后，松开BOOT按键。即可进入烧录模式。

    <ImageView src={require('./img/panda-bmcu370-8.webp').default} width="70%"/>

- 点击“解除代码保护”。

    <ImageView src={require('./img/panda-bmcu370-12.webp').default} width="70%"/>

- 再次按住BOOT不松，点击一下RESET之后，松开BOOT按键。再次进入烧录模式。点击“下载”开始烧录固件，等待烧录完成即可。

    <ImageView src={require('./img/panda-bmcu370-13.webp').default} width="70%"/>
