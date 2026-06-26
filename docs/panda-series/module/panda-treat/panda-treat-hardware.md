---
sidebar_position: 2
description: Panda Treat Hardware
---

# Panda Treat 硬件

## 包装内容

Panda Treat 套件包含组装和连接食用墨水适配器所需的硬件。盒内不包含打印安装件，因为这些安装件取决于你计划安装 Panda Treat 的打印机型号。用户必须在安装前为所选打印机型号打印正确的安装件。

<ImageView src={require('./img/whats-in-the-box.webp').default} width="50%"/>

盒内包含：

- Panda Treat PCB (A)
- 官方食用墨水墨盒 (B)
- 适用于 A1，A1 mini，P1 和 X1C 的打印机接口线缆套件：共 2 条线缆 (C)
- M3 x 6 mm 低头内六角自攻螺丝：14 颗 (D)
- 硅胶墨盒密封垫 x 1 (E)
- SD card x 1 (F)
- Allen key x 1 (G)
- P1S / X1C 安装用磁铁 x 4 (H)
- Quick start card x 1 (I)

:::info[Note]

请使用适用于你具体打印机的安装指南中提到的安装说明，零件和工具。上图展示的是 Panda Treat 套件通常随附的零件。随着产品更新，零件可能会有所变化。

:::

## 接口

在安装和维护过程中，说明中可能会提到某些 Panda Treat 接口。此处展示并说明这些接口，便于读者在后续使用这些名称时理解它们指的是什么。

<ImageView src={require('./img/hw-interfaces.webp').default} width="50%"/>

- `USB-C`: 用于手动更新等固件支持的维护任务。安装时不需要使用此接口。
- `Printer interface connector`: 使用随附的特定机型线缆将 Panda Treat 连接到打印机。安装时需要使用此接口。
- `Cartridge contacts and pins`: 为食用墨水墨盒提供电气连接。
- `SD card slot`: 存储 Panda Treat 打印过程中使用的文件。

:::info[Note]

请勿触摸墨盒电气触点。手指油脂以及触点区域损伤可能导致打印效果不佳或墨盒故障。

:::

## 重要安装注意事项

:::info[Important]

连接或断开 Panda Treat 线缆或墨盒之前，请务必关闭打印机电源。

:::

- 请勿直接拉拽小线缆。请握住连接器本体，并用指甲或合适的塑料工具（例如 [JST connector removal tool](https://makerworld.com/en/models/1169414-jst-connector-removal-tool)）轻轻将其松开。
- 将线缆较小的一端安装到 Panda Treat 后，请尽量避免拆下它，以防损坏线缆。需要拆卸时，请使用上述方法从打印机端拆下线缆。
- 不要强行将墨盒压入安装座。它应通过设计好的拨杆和支撑点卡入到位。

## 安装到 A1

### 所需组件

本安装需要以下零件。如果需要帮助识别其中某个零件，请参考 [包装内容](#包装内容) 和 [接口](#接口) 部分。

- Panda Treat PCB x 1
- A1 打印安装件 x 1 full set: [panda-treat-a1-a1-mini-mount](https://makerworld.com/en/models/2963559-biqu-x-cmy-labs-panda-treat-a1-a1-mini-mount)
- A1 打印废墨容器 x 1: [panda-treat-a1-purge-bucket](https://makerworld.com/en/models/2963618-biqu-x-cmy-labs-panda-treat-a1-purge-bucket)
- SD card
- A1 interface cable
- M3 x 6 mm self-tapping screws x 8
- Allen key
- 可选但强烈推荐：[JST detachment tool](https://makerworld.com/en/models/1169414-jst-connector-removal-tool)
- 可选：[replacement rear toolhead cover with wire opening](https://makerworld.com/en/models/2967583-biqu-x-cmy-labs-panda-treat-a1-a1-mini-rear-cover)

### 打印零件

首先打印链接中的 A1 安装件。请使用提供的 3MF 文件，除非更新后的官方说明要求这样做，否则不要更改零件方向或支撑设置。

PLA 适用于打印安装件。打印完成后，请确认包含以下零件：

- Panda Treat A1 / A1 Mini Mount - Front x 1
- Panda Treat A1 / A1 Mini Mount - Rear x 1
- Panda Treat A1 Purge Bucket x 1
- JST detachment tool x 1
- 可选：Panda Treat A1 / A1 Mini Toolhead Rear Cover x 1

### 组装

请按照以下步骤组装 Panda Treat。

1. 将 PCB 放入后部安装件中，并使显示屏朝上。将 PCB 朝后部安装件底部按压，使后部安装件底部与 PCB 之间没有间隙。这样可以让安装孔与后部安装件中的螺丝孔对齐。使用随附螺丝固定 PCB，但不要过度拧紧。

    <ImageView src={require('./img/pcb-to-rear-mount.webp').default} width="30%"/>

2. 将安装件前部套到后部上方，确保侧面的定位凸台完全插入，并确保显示屏没有被夹在前后两部分之间，否则可能损坏显示屏。

    <ImageView src={require('./img/front-and-rear-alignment.webp').default} width="30%"/>

3. 将四颗 M3 x 6 mm 自攻螺丝插入后部安装件背面的孔中并拧紧。不要过度拧紧，否则会滑牙并损坏塑料安装件。

    <ImageView src={require('./img/a1-mount-rear-screws.webp').default} width="30%"/>

4. 插入 Panda Treat 随附的 SD card。

    <ImageView src={require('./img/sd-inserted-a1.webp').default} width="30%"/>

5. 将 A1 线缆的小端插入 Panda Treat power connector。请注意安装方向。

    <ImageView src={require('./img/a1-connector.webp').default} width="30%"/>

组装过程到此完成。对于你计划搭配 Panda Treat 使用的每台打印机，此过程只需要执行一次。以下安装流程说明了如果你计划反复在打印机上安装和拆卸 Panda Treat，需要重复执行的步骤。

### 安装

以下步骤说明如何将已完全组装的 Panda Treat 安装到 A1 打印机上，或从 A1 打印机上拆下。执行这些步骤时，请始终关闭打印机电源。

1. 将食用墨水废墨桶卡到 A1 现有废料桶区域。请注意，废墨桶底部有两个柱子，需要与 A1 废料塑料底座底部的孔对齐。确保食用墨水废墨桶一直向前推，直到这些柱子卡入到位。拆下食用墨水废墨桶时，请先向下拉这部分以释放柱子。

    <ImageView src={require('./img/a1-purge.webp').default} width="50%"/>

2. 拆下 A1 工具头前盖。前盖下方的黄色和灰色挤出轮可以保留，也可以拆下。Panda Treat 安装对此没有要求。

    <ImageView src={require('./img/remove-front-cover-a1.webp').default} width="30%"/>

3. 先对齐并扣住顶部，再按压底部，将 Panda Treat 卡到工具头前方。正确卡入时，你会感觉到底部区域咔哒一声。确保 Panda Treat 与工具头之间的配合面平整，以保证可靠固定。

    <ImageView src={require('./img/a1-clipped-in.webp').default} width="30%"/>

4. 从底部中央的缝隙处撬开后部工具头盖。使用工具通常会更容易。

    <ImageView src={require('./img/pry-rear-cover-a1.webp').default} width="30%"/>

5. 使用 JST removal tool 拔下红色标记的连接器。切勿直接拉扯线材本身，否则很容易造成损坏。

    <ImageView src={require('./img/a1-jst-connector-removal.webp').default} width="30%"/>

6. 将断开的连接器折入其左侧的开放区域中。

    <ImageView src={require('./img/a1-jst-fold-connector.webp').default} width="30%"/>

7. 按图示方向插入 Panda Treat connector。

    <ImageView src={require('./img/a1-jst-insert-pt.webp').default} width="30%"/>

8. 此时可以安装由 K2 Kevin 设计的后部工具头盖。

    <ImageView src={require('./img/a1-rear-cover.webp').default} width="30%"/>

9. 确认已经从食用墨水墨盒上取下蓝色密封胶带，然后安装墨盒：先将墨盒底部插入墨盒安装座，再将顶部旋入拨杆卡扣，直到固定到位。如果拨杆比较紧，可能需要用手指抬起拨杆才能将墨盒放入。

    <ImageView src={require('./img/a1-cart-insertion-process.webp').default} width="70%"/>

硬件已安装，线缆已连接，SD card 已插入且墨盒已安装后，A1 安装即完成。

:::info[Important]

为了确保墨盒的使用寿命，在开始软件设置之前，务必阅读并遵循 [墨盒处理](#墨盒处理) 部分中的指导。

:::

## 安装到 A1 mini

### 所需组件

本安装需要以下零件。如果需要帮助识别其中某个零件，请参考 [包装内容](#包装内容) 和 [接口](#接口) 部分。

- Panda Treat PCB x 1
- A1 / A1 mini 打印安装件 x 1 full set: [panda-treat-a1-a1-mini-mount](https://makerworld.com/en/models/2963559-biqu-x-cmy-labs-panda-treat-a1-a1-mini-mount)
- A1 mini 打印废墨容器 x 1: [panda-treat-a1-mini-purge-bucket](https://makerworld.com/en/models/2964696-biqu-x-cmy-labs-panda-treat-a1-mini-purge-bucket)
- SD card
- A1 interface cable
- M3 x 6 mm self-tapping screws x 8
- Allen key
- 可选但强烈推荐：[JST detachment tool](https://makerworld.com/en/models/1169414-jst-connector-removal-tool)
- 可选：[replacement rear toolhead cover with wire opening](https://makerworld.com/en/models/2967583-biqu-x-cmy-labs-panda-treat-a1-a1-mini-rear-cover)

### 打印零件

首先打印链接中的 A1 / A1 mini 安装件。请使用提供的 3MF 文件，除非更新后的官方说明要求这样做，否则不要更改零件方向或支撑设置。

PLA 适用于打印安装件。打印完成后，请确认包含以下零件：

- Panda Treat A1 / A1 Mini Mount - Front x 1
- Panda Treat A1 / A1 Mini Mount - Rear x 1
- Panda Treat A1 mini Purge Bucket x 1
- JST detachment tool x 1
- 可选：Panda Treat A1 / A1 Mini Toolhead Rear Cover x 1

### 组装

为 A1 mini 组装 Panda Treat 时，请按照 A1 使用的相同组装步骤进行。将 A1 / A1 mini 线缆的小端插入 Panda Treat power connector，并注意安装方向。

### 安装

以下步骤说明如何将已完全组装的 Panda Treat 安装到 A1 mini 打印机上，或从 A1 mini 打印机上拆下。执行这些步骤时，请始终关闭打印机电源。

1. 将食用墨水废墨桶卡到 A1 mini 现有废料桶区域。请注意，废墨桶底部有两个柱子，需要与 A1 mini 废料塑料底座底部的孔对齐。确保食用墨水废墨桶一直向前推，直到这些柱子卡入到位。拆下食用墨水废墨桶时，请先向下拉这部分以释放柱子。

    <ImageView src={require('./img/a1-mini-purge.webp').default} width="50%"/>

2. 拆下 A1 mini 工具头前盖。前盖下方的黄色和灰色挤出轮可以保留，也可以拆下。Panda Treat 安装对此没有要求。

    <ImageView src={require('./img/remove-front-cover-a1.webp').default} width="30%"/>

3. 先对齐并扣住顶部，再按压底部，将 Panda Treat 卡到工具头前方。正确卡入时，你会感觉到底部区域咔哒一声。确保 Panda Treat 与工具头之间的配合面平整，以保证可靠固定。

    <ImageView src={require('./img/a1-clipped-in.webp').default} width="30%"/>

4. 从底部中央的缝隙处撬开后部工具头盖。使用工具通常会更容易。

    <ImageView src={require('./img/pry-rear-cover-a1.webp').default} width="30%"/>

5. 使用 JST removal tool 拔下红色标记的连接器。切勿直接拉扯线材本身，否则很容易造成损坏。

    <ImageView src={require('./img/a1-jst-connector-removal.webp').default} width="30%"/>

6. 将断开的连接器折入其左侧的开放区域中。

    <ImageView src={require('./img/a1-jst-fold-connector.webp').default} width="30%"/>

7. 按图示方向插入 Panda Treat connector。

    <ImageView src={require('./img/a1-jst-insert-pt.webp').default} width="30%"/>

8. 此时可以安装由 K2 Kevin 设计的后部工具头盖。

    <ImageView src={require('./img/a1-rear-cover.webp').default} width="30%"/>

9. 确认已经从食用墨水墨盒上取下蓝色密封胶带，然后安装墨盒：先将墨盒底部插入墨盒安装座，再将顶部旋入拨杆卡扣，直到固定到位。如果拨杆比较紧，可能需要用手指抬起拨杆才能将墨盒放入。

    <ImageView src={require('./img/a1-cart-insertion-process.webp').default} width="70%"/>

硬件已安装，线缆已连接，SD card 已插入且墨盒已安装后，A1 mini 安装即完成。

:::info[Important]

为了确保墨盒的使用寿命，在开始软件设置之前，务必阅读并遵循 [墨盒处理](#墨盒处理) 部分中的指导。

:::

## 安装到 P1S

P1S 支持计划通过匹配的固件，安装件和安装说明发布。在官方 P1S 安装件，说明和固件可用之前，请勿尝试将 Panda Treat 安装到 P1S 上。

## 安装到 X1C

X1C 支持计划通过匹配的固件，安装件和安装说明发布。在官方 X1C 安装件，说明和固件可用之前，请勿尝试将 Panda Treat 安装到 X1C 上。

## 墨盒处理

打印质量在很大程度上取决于食用墨水墨盒的处理方式。打印头损坏或存储不当可能导致缺线，颜色偏移和明显打印瑕疵。本节说明如何存储和处理 Panda Treat 墨盒，以获得最佳性能和使用寿命。

下图显示了 Panda Treat 墨盒的主要结构，并会在后续小节中反复引用。建议同时阅读下方关于墨盒工作原理的简要说明，因为它有助于理解许多存储和维护任务的必要性。

<ImageView src={require('./img/print-cartridge-anatomy.webp').default} width="50%"/>

打印墨盒内部有三个食用色素储液仓。其中一个包含青色（蓝色），一个包含品红色（红色），一个包含黄色色素。每个储液仓都会向打印头上的微小喷嘴供墨。墨盒打印时，这些微小喷嘴会向下将墨水喷到物体上，而无需接触物体本身。该墨水设计为快速干燥，因此打印后不易涂抹晕开。因此，墨水也可能在喷嘴内快速干燥，从而导致堵塞和打印缺陷。下面的存储，处理和维护任务说明了如何防止堵塞，以及如果出现堵塞应如何清除。

### 存储

由于食用墨水干燥很快，因此不使用时，需要确保打印头周围有密封，以防空气将其吹干。

Panda Treat 墨盒出厂时，墨盒托架上贴有泡棉密封垫。当蓝色密封胶带仍贴在打印头上时，此泡棉密封垫非常适合固定墨盒；但取下蓝色胶带后，如果将墨盒重新插入墨盒托架，泡棉密封垫可能导致墨水混色。因此，在首次使用墨盒前取下蓝色密封胶带后，应缓慢揭起并移除泡棉密封垫，然后用硅胶密封垫替换。

粘贴前，将硅胶密封垫与墨盒托架背面对齐，并确保硅胶密封垫右边缘与沿墨盒托架长度方向延伸的加强筋对齐。安装硅胶密封垫后，不使用墨盒时应将墨盒存放在墨盒托架中。存放墨盒时，请保持其直立，避免倒置或侧放。

<ImageView src={require('./img/cartridge-seal-replacement.webp').default} width="50%"/>

### 维护与保养

为了获得高质量打印效果，墨盒需要正确维护和护理。请按照以下步骤操作，确保它在整个使用寿命内表现良好。

- 不使用时，请始终将墨盒存放在已安装硅胶密封垫的墨盒托架中。
- 如果墨盒超过 15 分钟未使用，请用干净的纸巾从后向前轻轻擦拭打印头。当它可以使用时，你会看到三条清晰的颜色线。颜色线出现后，请再重复擦拭几次。

    <ImageView src={require('./img/wiping-cartridge.webp').default} width="50%"/>

- 如果墨盒已经数天未使用，请先将湿纸巾贴在打印头上几秒钟，然后再擦拭。不要浸泡整个墨盒。
- 切勿让墨盒直接以打印头朝下站立，也不要用手指触摸打印头。打印头是墨盒底部的亮色条带。
- 切勿使用酒精清洁打印头。只有当后部接触焊盘变色时，才可以在该位置使用酒精。
- 切勿侧放存储墨盒。请直立存放，以免墨水在各墨仓之间移动或从打印头处泄漏。
- 确保墨盒通气孔没有被灰尘或墨水堵塞。墨盒通气孔是通气标签边缘周围的小孔。
- 避免触摸接触焊盘，因为手指油脂可能导致其腐蚀。
