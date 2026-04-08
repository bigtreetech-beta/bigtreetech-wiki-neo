---
sidebar_position: 3
description: Panda Bamboo Feeder 固件配置
---

# Panda Bamboo Feeder 软件设置

## 首次使用

:::info[注意]

从机或者主机模式下，只需要给主机绑定打印机，在绑定之前需要先给主机配网并且绑定打印机

:::

### 配网

- 没有配置网络时，显示屏会显示热点名称"XXXXXXXXXXXXPanda_Bamboo_Feeder"

    <ImageView src={require('./img/ap-name.webp').default} width="256"/>

- 使用手机或者电脑连接该热点，密码默认是 `987654321`

    <ImageView src={require('./img/ap-select.webp').default} width="256"/>

- 连接热点后如果没有自动跳转到WEB UI，需要在浏览器手动输入: `http://192.168.254.1/`

- 选择语言

    <ImageView src={require('./img/select-lang.webp').default} width="256"/>

- 扫描WiFi后，选择需要连接的WiFi名称，输入wifi密码后点击连接

    <ImageView src={require('./img/ap-connect.webp').default} width="256"/>

### 绑定打印机

- 点击扫描打印机,输入访问码后点击连接

    <ImageView src={require('./img/bind-printer.webp').default} width="256"/>

- 绑定成功后，显示屏会显示打印机名称

    <ImageView src={require('./img/printer-name.webp').default} width="256"/>

## 工作模式

长按退料键进入选择模式界面，使用退料键切换选项，使用进料键确认

<ImageView src={require('./img/select-mode.webp').default} width="256"/>

### 独立模式

在此模式下，使用1台喂竹器与外挂料盘搭配使用。

### 联动模式

#### 从机

在此模式下，与1台主机模式的喂竹器使用，由主机绑定打印机

#### 主机

在此模式下，与1台或者2台从机模式的喂竹器绑定使用，主机绑定打印机

## 主从机绑定

### 如何绑定主机

- 使用至少2台喂竹器，将一台设置为主机，另一台为从机

- 从机长按进料键进入绑定状态

    <ImageView src={require('./img/follower-binding.webp').default} width="256"/>

- 主机端收到绑定请求后，按下确认

    <ImageView src={require('./img/leader-bind-remind.webp').default} width="256"/>

### 解除绑定

#### 主机

- 长按进料键后进入解绑界面，选择需要解除绑定的从机

    <ImageView src={require('./img/unbind-follower-step1.webp').default} width="256"/>

- 确认解除绑定

    <ImageView src={require('./img/unbind-follower-step2.webp').default} width="256"/>

#### 从机

- 长按进料键后进入解绑界面，确认解除绑定

    <ImageView src={require('./img/unbind-leader.webp').default} width="256"/>

## 恢复出厂设置

- 长按退料键8秒左右恢复出厂设置

    <ImageView src={require('./img/factory.webp').default} width="256"/>

## 状态显示

### 传感器状态

显示屏的右侧有几个圆圈用于指示各个传感器的触发状态

- 5通耗材传感器

    <ImageView src={require('./img/sensor-5way.webp').default} width="70"/>

- 出口2

    <ImageView src={require('./img/sensor-out2.webp').default} width="70"/>

    - 当缓存满时，此传感器被触发

- 出口1

    <ImageView src={require('./img/sensor-out1.webp').default} width="70"/>

- 入口2

    <ImageView src={require('./img/sensor-in2.webp').default} width="70"/>

    - 处于waiting状态下，走到此传感器触发后停

- 入口1

    <ImageView src={require('./img/sensor-in1.webp').default} width="70"/>

    - 此传感器由触发变为不触发时，进入断料状态

    - 此传感器由不触发变为触发时，进入等待或者进料状态

### 运行状态或告警信息

显示当前的运行状态(如进料,退料,等待,断料等)，和告警信息

<ImageView src={require('./img/running-status.webp').default} width="256"/>

### 工作状态或模式

显示当前工作设备的状态或者工作模式

<ImageView src={require('./img/work-follower.webp').default} width="256"/>

## 参数配置

- 打印机类型

    可以选择拓竹,klipper打印机

- 蜂鸣器开关

    关闭后，告警时蜂鸣器不响

- 压力级别

    进料压力值决定了智能缓冲系统对耗材施加的正压。使用"自动校准"按钮自动校准适当的进料压力，如果自动校准值不足以实现可靠的耗材再填充，则手动调整到更高的压力值

    如打印较软耗材如TPU等，建议重新校准压力级别或手动调整降低压力级别

    最低支持60ATPU耗材打印，可改善软料打印耗材卡顿断料问题，实际可使用的TPU硬度视最终耗材路径决定，耗材路径越复杂，软料打印成功率越低

- Hostname

    在浏览器输入 `http://pandabamboofeeder.local` 可以打开WEB UI

- 热点名称

    在WEB UI可以修改热点名称

## 校准

在耗材进料的通道内会有一定的阻力，如果阻力大于当前设置的校准级别，耗材可能会被卡住无法继续进料，在更换不同的耗材,铁氟龙管后，需要进行一次校准。

:::info[注意]

太大的压力可能会导致脆性材料在长丝路径中断裂，也可能导致柔软材料在长丝通道中弯曲，请谨慎手动设置进料压力值

:::

### 校准模式

- 快速校准: 由主机进行校准，完成校准后，压力级别都设置为同一个值

- 全部校准: 主机和从机分开校准，完成校准后，压力级别相互独立

### 开始校准

- 打开设置页面

- 点击自动校准

    <ImageView src={require('./img/auto-calibration.webp').default} width="256"/>

- 再点击开始校准

    <ImageView src={require('./img/start-calibration.webp').default} width="256"/>

## Klipper 配置

通过自定义宏可以在Klipper打印机上实现自动加载和卸载耗材

- 下载配置文件 [feeder.cfg](https://github.com/bigtreetech/Panda_Bamboo_Feeder/blob/master/klipper/feeder.cfg)

- 上传并添加到printer.cfg.

    ```systemd title="printer.cfg"
    [include feeder.cfg]
    ```

## 故障排除

#### Q: 耗材卡在PTFE管里面，没有到达挤出机

- 管内阻力过大

    - 尽量使用机器自带或PFB配送的ptfe管，尽可能的使用更短的管，整个耗材路径曲率应当尽可能平顺没有硬弯或锐角折弯，耗材路径阻力过大可能会导致所需正压超出PBF所能提供最大值

    - 可以利用五通上预留的安装固定五通，但需要确保五通口处的PTFE（连接至打印的这个）切口平整且已完全插入到快接头，尽量不要让PTFE管在靠近快接头处弯折

- 尝试手动设置更大一些的压力级别

#### Q: 5通传感器有耗材并且已触发，耗材卡在5通里

- 5通传感器可能损坏了导致误报，检查下面几个状态是否能正常显示

    - 移除5通后，屏幕只显示4个传感器的圆圈

    - 插上5通后，5通里面没有耗材，屏幕显示5通传感器未触发状态

    - 插上5通后，5通里面有耗材，屏幕显示5通传感器已触发状态

    - 插上5通后，外部通道有耗材，并且已经插到位，屏幕显示外部通道已触发

- 五通出口端（打印机自带的PTFE管入口端）可能存在磨损

    <ImageView src={require('./img/ptfe-broken.webp').default} width="256"/>


## 固件

### 功能请求

如果您希望在即将发布的 Panda Bamboo Feeder 固件中增加产品需求，请在官方 [Panda Bamboo Feeder github repo](https://github.com/bigtreetech/Panda_Bamboo_Feeder/issues)上提交请求让我们知道。

### OTA更新

- [下载](./panda-bamboo-feeder-release.md)最新的固件

- 使用手机或者电脑打开浏览器访问设备的WEB UI

    - 连接喂竹器自身的AP，名称默认为 xxxxxxxxxxxxPanda_Bamboo_Feeder，在浏览器输入地址 `http://192.168.254.1`

    - 如果喂竹器已经连上路由器（以IP地址 192.168.3.161 为例，在浏览器输入屏幕上显示的IP地址 `http://192.168.3.161`

- 切换到设置页面

    - 点击选择 `.bin` 文件

        <ImageView src={require('./img/select-bin.webp').default} width="256"/>

    - 更新成功

        <ImageView src={require('./img/update_ok.webp').default} width="256"/>

### flash_download_tool (Type-C 线刷)

:::info[注意]

Panda Bamboo Feeder 理应可以自由的OTA，此步骤仅在无法OTA时使用

:::

- 如果电脑上没有 CH340 的驱动，请先下载安装驱动 [CH341SER.EXE](https://www.wch.cn/downloads/CH341SER_EXE.html)

- 下载 [Flash 下载工具](https://www.espressif.com/zh-hans/support/download/other-tools)

    <ImageView src={require('./img/download_esp_tool.webp').default} width="70%"/>

- 下载 [Panda Bamboo Feeder 可烧录固件](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/recovery_tool/flash)

- 通过 `Type-C` 将 Panda Bamboo Feeder 插到电脑上，电脑的设备管理器中理应识别出一个新的 COM 端口

    <ImageView src={require('./img/typec.webp').default} width="35%"/>

- 打开 `flash_download_tool_3.x.x.exe`, 在弹窗中按照下图配置

    ChipType: `ESP32-S3`

    WorkMode: `Develop`

    LoadMode: `UART`

    <ImageView src={require('./img/download.webp').default} width="200"/>

- 烧录软件的配置如下图

    <ImageView src={require('./img/esp_tool_config.webp').default} width="400"/>

    1. 设置.bin文件的烧录地址, 并且前面的复选框都勾选上

        - `panda_bamboo_feeder_flash.bin` 写入到 `0x0000`

    2. 设置COM端口为实际的端口（可在电脑的`设备管理器`->`端口`中查看）, 并且设置一个合适的波特率, 我们推荐使用 `460800`

    3. 点击 `START` 开始烧录，等待烧录完成, 断电重启即可。
