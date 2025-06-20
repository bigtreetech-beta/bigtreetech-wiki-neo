---
sidebar_position: 3
---

# Panda Touch 软件设置

Panda Touch 软件配置

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 首次连接指南

首次启动后或执行`恢复出厂设置`命令后，您将看到下面的屏幕。

### 语言选择指南

<img src={require('./img/language_guide.png').default} alt="" width="600" />

* 为Panda Touch选择一种语言，然后点击`下一步`

### WiFi连接指南

<img src={require('./img/guide_wifi.png').default} alt="" width="600" />

* 在初始设置过程中，Panda Touch将扫描WiFi网络，然后显示多达20个具有最佳信号强度的网络。如果您在列表中找不到所需的网络，请点击`刷新`，Panda Touch将重新扫描WiFi网络
>注意：
>当前的固件不支持连接到隐藏的WiFi网络。此外，当Panda Touch连接到WiFi的过程中，Panda Touch无法同时执行WiFi扫描任务。
* 点击列表中的WiFi名称，会弹出[键盘界面]（#键盘界面）。输入正确的密码后，单击`确定`开始连接WiFi。（密码长度：8~64个字符）
* 连接状态将显示在WiFi网络名称旁边。`Spinner`图形表示WiFi仍在尝试连接`✔` 表示连接成功。
* 连接成功后，将启用`下一步`按钮。单击`下一步`进入打印机连接菜单。

>注意：
>如果您使用的是具有多个共享相同SSID的WiFi网络时，请在列表中选择信号强度最强的SSID。

### 打印机连接菜单

<img src={require('./img/guide_printer.png').default} alt="" width="600" />

* 将Panda Touch连接到打印机有两种可能的方法。
    1. 自动扫描（推荐）。
    2. 手动输入。

### 查找您的连接详细信息

在此过程中，您可能需要输入连接详细信息。这些可以通过以下步骤找到。
#### P1P & P1S

* 导航至LCD菜单上的`设置->WLAN`，然后单击`确定`。

    <img src={require('./img/p1_1.png').default} alt="" width="600" />

* 在相应的Panda Touch输入框中输入IP和访问码（仅访问码用于自动扫描）。

    <img src={require('./img/p1_2.png').default} alt="" width="600" />

* 在屏幕菜单中找到`设置->设备`，然后单击`确定`。

    <img src={require('./img/p1_3.png').default} alt="" width="600" />

* 在相应的Panda Touch输入框中输入序列号代码

    <img src={require('./img/p1_4.png').default} alt="" width="600" />

#### 自动扫描

* 要进行自动扫描，只需点击`扫描`按钮。位于同一WiFi网络上的Bambu实验室打印机将显示在扫描结果中，并预先填充`名称`、`打印机IP`、`SN`和`型号`信息。预先填充这些字段有助于更容易地添加打印机，并且可以减少由于手动数据输入错误而导致的错误。您需要输入的唯一数据是`访问代码`，它可以在打印机WiFi/LAN菜单中找到。有关如何查找访问代码的说明将显示在熊猫触摸屏上。先前已连接到Panda Touch的打印机仍将显示在扫描结果中，但Panda Touch不允许再次添加它们，并且`已添加`将显示在打印机图标附近。输入访问代码后，您可以确认连接或手动添加下面的一些数据。

#### 手动输入

* 您可以单击左侧的打印机图标，进入选择打印机型号的菜单。您必须根据所连接打印机的实际型号进行设置。Panda Touch还会在后台进行一些检查以确认型号。可用型号如下：
    * P1P
    * P1S
    * X1C
    * A1 mini
    * A1

  使用图标选择模型后，`模型`字段中的内容将填充相应的模型名称。

* 选择打印机型号后，有4个必填字段。这些字段包含连接到打印机并识别打印机所需的信息。点击`i`图标并左右滑动以获取如何在打印机上查找此信息的说明。

    * `名称`：用户用来识别打印机的自定义名称。（长度：1~15个字符）
    * `打印机IP`：用于Panda Touch连接到打印机。（长度：7~15个字符）
    * `访问代码`：用于Panda Touch连接到打印机。（长度：8个字符）
    * `SN`：用于Panda Touch连接到打印机。（长度：15个字符）

* 有4个可选字段，可以帮助您在以后使用时识别打印机的某些参数。

    * `型号`：型号名称标识打印机的确切型号，并定义与之相关的图片。P1P、P1S、X1C、A1 mini、A1或自定义。（长度：0~15个字符）
    * `耗材颜色`：打印机使用的耗材颜色。（长度：0~6个字符）
    * `耗材材料`：打印机使用的耗材材料。（长度：0~6个字符）
    * `喷嘴直径`：打印机使用的喷嘴的直径。（长度：0~6个字符）

- `确认` 按钮

    填写`必需`信息后，您可以单击`确认`按钮开始连接打印机。Panda Touch的标题栏将显示连接状态。

## 云模式功能

如果您的任何P1P/P1S打印机未设置为`仅局域网`模式，则您需要将Panda Touch与P1P/P1S打印机的通信方式切换为云模式，以使用以下功能：

* 加热
* 开始打印
* 暂停打印
* 停止打印

请按照以下步骤将Panda Touch与P1P/P1S打印机的通信方式切换为云模式。

#### 登录拓竹账号
* 点击跳转到设置页面，然后点击`登录拓竹帐户`按钮。 

    <img src={require('./img/add_account.png').default} alt="" width="600" />

* 点击弹出窗口右上角的箭头选择您的地区。

* 中国用户使用手机号码，而全球地区的用户使用电子邮件地址。

* 如果您找不到登录凭据，请参阅以下部分：[如何找到我的拓竹账号信息](#bambu_account)

    <img src={require('./img/login.png').default} alt="" width="600" />
 
    :::info 已知问题

    目前，需要关闭2步身份验证才能在Panda Touch上启用云模式。如果你想保持启用状态，那么你可以关闭它，在Panda Touch上启用云模式，然后再重新打开。请注意，你可能需要每三个月重复一次此过程，因为在此期间之后，Panda Touch上的登录详细信息将过期。
    
    :::

    <img src={require('./img/input_account.png').default} alt="" width="600" />

#### 将帐户下的打印机同步到本地设备

* 成功登录后，您可以选择将所有现有打印机与PandaTouch的通信方式转换为云模式。

* 我们建议，只有您的所有打印机都使用云模式运行时，才执行此操作，如果打印机打开了`仅局域网`模式，则可以跳过此操作。如果要改变PandaTouch与打印机之间的通信方式请查看 [如何切换PandaTouch和打印机之间的通信方式](#communication_mode)

    <img src={require('./img/login_ok.png').default} alt="" width="600" />

* 如果您想将现有打印机与PandaTouch之间的通信方式转换为云模式，请点击`是`。 

* 在此过程中，打印机必须与PandaTouch位于同一网络上。如果网络连接不佳，您可能需要重新编辑打印机的IP地址。

    <img src={require('./img/sync_ok.png').default} alt="" width="600" />

* 一旦打印机在云模式下工作，您将在多打印机视图中注意到与其卡片关联的绿色云。云表示打印机与PandaTouch之间的通信方式。

* 您还将注意到一对绿色箭头，指示与该打印机的连接状态。
    <img src={require('./img/cloud_mode.png').default} alt="" width="600" />

#### 如何删除已登录的账号

* 点击账户信息右上角的`X`按钮，删除保存在PandaTouch上的账户信息。

* 删除帐户信息后，PandaTouch和打印机之间的通信模式将更改为本地模式。请注意，这不会将打印机本身设置为`仅LAN`模式，而是会告诉Panda Touch仅使用LAN模式与打印机通话，这可能会导致某些功能丢失。

    <img src={require('./img/del_account.png').default} alt="" width="600" />

#### 如何切换PandaTouch和打印机之间的通信方式

* 导航到打印机/组卡页面。
* 找到要启用或禁用云模式的打印机。
* 向下滚动到该打印机的`编辑`按钮。
* 选择`启用云`将打印机与PandaTouch的通信方式切换为云模式。

:::tip

必须在设置菜单中启用云帐户，否则将无法将该打印机与PandaTouch之间的通信方式设置为云模式。

<img src={require('./img/switch_work_mode.png').default} alt="" width="600" />

:::

## 键盘输入

1. 使用此键可以隐藏或显示输入的信息。
2. 在大写字母和小写字母之间切换。
3. 切换到`符号输入`。
4. 切换到`数字输入`。

- 字母输入

    <img src={require('./img/keyboard_letter.png').default} alt="" width="600" />

- 符号输入

    <img src={require('./img/keyboard_symbol.png').default} alt="" width="600" />

- 数字输入

    <img src={require('./img/keyboard_number.png').default} alt="" width="600" />

## 打印任务和缩略图显示

<img src={require('./img/thumbnail_preview.png').default} alt="" width="600" />

:::info

仅显示从Bambu Studio发起的打印任务，该.3mf文件需要小于 20M，X1系列机器暂不支持。

缩略图不匹配: 仅当image文件夹下的图片时间戳与其他打印文件相同时会导致缩略图不匹配。

增强缩略图显示: 在设置页面有个选项用于增强缩略图显示，开启后，从U盘打印或者在SD卡面板操作时都会有比较长的延时。

:::

## 耗材控制

Panda Touch允许用户配置外部线轴支架和AMS上使用的耗材的类型和颜色。用户还可以使用此菜单加载和卸载过滤器。

执行任何操作时，请确保选择了正确的AMS装置和灯丝槽。当耗材周围有红色边框时，您就会知道耗材已被选中。如果未选择任何内容，则`加载`和`卸载`按钮将变灰。

<img src={require('./img/filament_screen.png').default} alt="" width="600" />

## 耗材烘干
Panda Touch允许用户在X1系列和P1S上烘干耗材 

* 点击烘干按钮

<img src={require('./img/drying.png').default} alt="" width="500" />

* 按照右侧的步骤操作

<img src={require('./img/filament_dry.png').default} alt="" width="500" />

## 零件跳过

:::note

打印任务需要从Bambu Studio 或者 Handy app上发起，不支持重新打印的任务。  

以下情况不可用
- 单盘1个或者64个以上零件 
- Bambu studio 版本低于V1.6

:::

<img src={require('./img/skip_objects.gif').default} alt="" width="500" />

## HMS (健康管理系统)

<img src={require('./img/hms.png').default} alt="" width="600" />

* 点击Panda Touch的标题栏，HMS通知中心菜单将展开。
* 当检测到新的HMS通知时，Panda Touch将自动扩展HMS通知中心。
* 标题栏的左上角将显示已发送HMS通知的打印机的数量。
* 点击相应的HMS通知，弹出wiki链接二维码，用于解决此问题。
* 单击`X`可忽略此通知。
* 单击`全部忽略`可忽略所有通知**注意：** Panda Touch将忽略除X1C以外的所有打印机的通知。由于X1C以规则的间隔重复发送通知信息，因此被忽略的通知可能在此后不久再次出现。

## 分组逻辑
Panda Touch允许您创建多达10个组，每个组可以包含单个或多个打印机。

### 如何添加到组

* 在已连接的打印机列表中点击+，弹出多功能菜单。
    
    <img src={require('./img/press_plus.png').default} alt="" width="600" />

* 选择添加组选项。

    <img src={require('./img/press_add_group.png').default} alt="" width="600" />

* 选择要添加到组中的打印机，并确保选择其中一台作为主机（组中的其他打印机将遵循发送给主机的命令）。

    <img src={require('./img/group_choose_printer.png').default} alt="" width="600" />

* 点击下一步，输入组名，然后单击`确定`。
    <img src={require('./img/group_name.png').default} alt="" width="600" />

* 现在，您可以在打印机列表中看到该组，点击该组将允许您控制整个组，但显示的控件将是组长的控件。

### 在打印机组控制和单个打印机控制之间切换

* 要控制单个打印机，只需单击与其对应的卡片，您就会注意到顶部栏中的名称更改为该打印机的名称。现在，即使它是组的一部分，您也可以单独向它发送命令。
* 如果您向单个打印机发送一个需要一些时间的命令（如归位），然后向它所属的组发送一个命令，如果第一个命令仍然繁忙，则第二个命令将被忽略。
* 要控制整个组，只需单击与该组对应的卡片，您就会注意到顶部栏中的名称更改为组的名称和主机的名称，用正斜杠分隔。现在，您可以向组长发送命令，组中的其他打印机也将随之发送命令。

<img src={require('./img/add_group_ok.png').default} alt="" width="600" />

### 从USB打印的注意事项

尝试从USB打印时，请注意以下要点。

* 确保USB闪存驱动器的文件系统格式化为 `FAT32`。
* 使用`导出所有盘`选项从Bambu Studio或Orca Slicer导出`.3mf`文件。

    <img src={require('./img/export_3mf.png').default} alt="" width="300" />

* 将切好的 `.3mf` 文件写入USB储存设备的根目录

    * Panda Touch仅支持在Bambu Studio的`Build Plate#1`上切片的文件。
    * Panda Touch仅支持 `.3mf` 文件，不支持 `.gcode` 文件。
    * Panda Touch仅支持读取根目录中的文件，不支持读取文件夹中的文件。

* 将USB储存设备插入Panda Touch，然后转到`USB储存设备`菜单。

    <img src={require('./img/usb_flash_drive.png').default} alt="" width="600" />

### 使用一台打印机开始打印

* 点击以选择USB磁盘或SD卡上的文件进行打印。
* 设置打印参数。根据打印机的不同，您可能会看到：
    * `热床调平`
    * `流量校准` (`P1P` and `P1S` 没有这个功能, 因此这些打印机不会显示此选项)
    * `延时摄影`
    * `使用 AMS` (Panda Touch将自动识别此打印机是否已插入AMS，然后确定是否需要显示此选项)
    * `自动断电` (自动识别在线的Panda PWR,开启自动断电功能)
    * `清除用电量` (自动识别在线的Panda PWR,重置Panda PWR的用电量)

    <img src={require('./img/start_print_one.png').default} alt="" width="600" />

* 请确保切片的`.3mf`文件与所选打印机兼容。
* 如果使用AMS，请确保AMS托盘中的耗材与切片的`.3mf`文件中的耗材一致，因为在打印开始时无法动态映射耗材。

* 如果您从USB开始打印，则Panda Touch将开始将USB闪存驱动器中的文件上传到打印机MicroSD卡的根目录。为避免上传问题，请确保：
    1. 打印机中插入了MicroSD卡。
    2. MicroSD卡的剩余容量足以写入要上传的文件。

    <img src={require('./img/uploading.png').default} alt="" width="600" />

* 上传完成后，将开始打印。对于非常大的`.3mf`文件，传输到每台打印机可能需要几分钟的时间。

* 开始打印后，Panda Touch将自动跳转到主界面并显示打印机数据。

    <img src={require('./img/start_print_one_ing.png').default} alt="" width="600" />

### 组打印

* 仅支持存储在USB磁盘上的文件进行组打印。
* 点击以选择USB磁盘上要打印的文件。
* 设置打印参数。根据组中的打印机，可能会看到
    * `热床调平`
    * `流量校准` (`P1P`和`P1S`没有此功能，因此这些型号的打印机将不会显示此选项。)
    * `延时摄影`
    * `使用 AMS` (Panda Touch将自动识别此打印机是否已插入AMS，然后确定是否需要显示此选项。)
    * `自动断电` (自动识别在线的Panda PWR,开启自动断电功能)
    * `清除用电量`(自动识别在线的Panda PWR,重置Panda PWR的用电量)

* 特定组的复选框打印选项将基于组中功能最强大的机器可用的功能。例如，您正在使用包含X1C\P1P\P1S的组，您将有激光雷达扫描选项可用，但此选项将仅发送给支持它的组中的打印机。

    <img src={require('./img/start_print.png').default} alt="" width="600" />

* Panda Touch将生成一个可用打印机列表供您选择。
* 已忙的打印机和组将被排除在此列表之外。这意味着，如果组中的单个打印机已经繁忙，则您将无法打印到该组中的任何打印机。这允许组始终保持彼此同步。

* 请确保切片的`.3mf`文件与所选打印机兼容。
* 如果使用AMS，请确保AMS托盘中的耗材与切片的`.3mf`文件中的耗材一致，因为在打印开始时无法动态映射耗材。

* 如果使用AMS，请确保AMS托盘中的耗材与切片的`.3mf`文件中的耗材一致，因为无法动态传输。Panda Touch将开始将USB闪存驱动器中的文件上传到打印机MicroSD卡的根目录。为了避免上传问题，请确保在打印开始时绘制耗材:
    1. 打印机中插入了MicroSD卡。
    2. MicroSD卡的剩余容量足以写入要上传的文件。

    <img src={require('./img/udisk_upload.png').default} alt="" width="600" />


* 上传完成后，将开始打印。对于非常大的`.3mf`文件，传输到每台打印机可能需要几分钟的时间。

    <img src={require('./img/group_printing.png').default} alt="" width="600" />

* 开始打印后，您将被带到打印摘要页面，在该页面上，组中每个打印机的状态都在单独的卡片上进行了摘要。

### 组打印描述

当选择一个组并且组中的多台打印机正忙于打印时，Panda Touch将显示`多台打印`菜单，如下所示。

<img src={require('./img/multi_printing.png').default} alt="" width="600" />

此菜单中存在以下组控件：

1. 打开/关闭当前打印列表中打印机的腔室LED。
2. 停止当前打印列表中的所有打印作业。
3. 暂停/恢复当前打印列表中的所有打印作业。

### 组打印设置延时

在组打印时根据这个时间来进行延时，如果当前打印机加热完成或者时间到了，就发送打印任务到下一台。

<img src={require('./img/group_delay.png').default} alt="" width="600" />
