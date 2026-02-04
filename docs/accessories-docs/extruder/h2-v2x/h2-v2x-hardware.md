---
sidebar_position: 2
---

# H2 V2X 硬件

H2 V2X 硬件文档

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import ThemedImage from '@theme/ThemedImage';

<!-- import lib end -->

## 模型下载

:::info 3D 参考文件

H2 V2X 3D 建模参考文件 [bigtreetech/H2-V2X/3D Model/Reference Cad Model](https://github.com/bigtreetech/H2-V2X/tree/master/3D%20Model/Reference%20Cad%20Model)

:::

:::info 挤出机适配件下载 

Stealthburner 适配件 [bigtreetech/H2-V2X/3D Model/Stealthburner](https://github.com/bigtreetech/H2-V2X/tree/master/3D%20Model/Stealthburner)

EVA3 适配件 [bigtreetech/H2-V2X/3D Model/EVA3](https://github.com/bigtreetech/H2-V2X/tree/master/3D%20Model/EVA3)

:::

## 外观尺寸

XYZ尺寸: $53.9 mm * 37.88 mm * 51.52 mm$

<img
    src={require('./img/H2V2X_Dimension1.png').default}
    alt="h2 v2x" width="60%"
/>

<img
    src={require('./img/H2V2X_Dimension2.png').default}
    alt="h2 v2x" width="60%"
/>

## 挤出机调节

:::warning
当调节螺钉停止转动时，请勿用力，以免损坏挤出机结构
:::

<div class="div-table">
    <img
    src={require('./img/H2V2X_Filament1.png').default}
    alt="h2 v2x" width="35%" class="right-image"
    />
    挤出齿轮的松紧可调节，以适应不同的耗材，逆时针方向转动螺杆为夹紧，顺时针方向转动螺杆为松弛(当螺杆停止转动时，请勿用力，以免造成挤出机损坏）
</div>

## 挤出机元件耐温

| H2 V2X | 元件最高温度  |
| ------ | ------------- |
| 电机   | $130^\circ C$ |
| 轴承   | $100^\circ C$ |

## 电机规格

<div class="div-table">

<img
    src={require('./img/H2V2X_motor1.png').default}
    alt="h2 v2x" width="60%" class="right-image"
/>

| H2 V2X       | 电机规格                              |
| ------------ | ------------------------------------- |
| 额定电压     | DC 3.45V                              |
| 额定电流     | DC 1.5A per phase                     |
| 相数         | 2                                     |
| 绕组直流电阻 | $2.3 \Omega \pm 10 \%$ ($25^\circ C$) |
| 绕组电感     | $2.0 mH \pm 20 \%$                    |
| 保持扭矩     | $\ge 110mN*m$                         |
| 定位扭矩     | $7mN*mREF$                            |
| 绝缘电阻     | $\ge 100 M \Omega$ (DC 500V)          |
| 绝缘级别     | Class B                               |
| 转动惯量     | $8g*cm^3$                             |

</div>

## H2 V2X 结构图

<ThemedImage
    alt="Docusaurus themed image"
    sources={{
        light: require('./img/h2-v2x-component-light.png').default,
        dark: require('./img/h2-v2x-component-dark.png').default,
    }}
/>

| H2 V2X        | 结构图                 |             |                          |
| ------------- | ---------------------- | ----------- | ------------------------ |
| 1. 挤出机电机 | 2. 主齿轮              | 3. 齿轮箱   | 4. 682XZZ 轴承           |
| 5. 673ZZ 轴承 | 6. M3X4 杯头内六角螺丝 | 7. 从动齿轮 | 8. 输出齿轮              |
| 9. 挤出齿轮   | 10. 拨杆               | 18. 前盖    | 19. M3x35 平头内六角螺丝 |

