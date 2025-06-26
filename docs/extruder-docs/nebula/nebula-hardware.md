---
sidebar_position: 2
---

# Nebula hardware

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## 模型下载

:::info 3D 参考文件

Nebula 3D 建模参考文件 [bigtreetech/Nebula/3D Model/Reference Cad Model](https://github.com/bigtreetech/Nebula/tree/master/3D%20Model/Reference%20Cad%20Model)

:::

:::info 挤出机适配件下载 

Stealthburner 适配件 [bigtreetech/Nebula/3D Model/Stealthburner](https://github.com/bigtreetech/Nebula/tree/master/3D%20Model/Stealthburner)

EVA3 适配件 [bigtreetech/Nebula/3D Model/EVA3](https://github.com/bigtreetech/Nebula/tree/master/3D%20Model/EVA3)

:::

## 外观尺寸

XYZ 尺寸: $52.73 mm * 36.5 mm * 54.82 mm$

<img
    src={require('./img/nebula_dimensions.png').default}
    alt="nebula" width="60%"
/>

## 挤出机调节

:::warning
当调节螺钉停止转动时，请勿用力，以免损坏挤出机结构
:::

<div class="div-table">
    <img
    src={require('./img/nebula_adjusting.png').default}
    alt="nebula" width="35%" class="right-image"
    />
    逆时针旋转调节螺钉（朝标记 `–` 的方向）可以减小间距、增加夹紧力，适合`较硬`的耗材使用；顺时针旋转（朝标记 `+` 的方向）可以增大间距、降低夹紧力，更适合`柔性`耗材。
</div>

## Nebula Pin 

<div class="div-table">
    <img
        src={require('./img/nebula_pin.png').default}
        alt="nebula" width="60%" class="right-image"
    />

| Nebula | PIN              |
| ------ | ---------------- |
| 5V     | 电源输入 (5V)    |
| GND    | 电源输入 (GND)   |
| FS     | 挤出机耗材传感器 |
| GB     | Nebula 顶部按钮  |
| RGB    | neopixel 接口    |

</div>


## Nebula 电机规格

<div class="div-table">
    <img
        src={require('./img/nebula_motor.png').default}
        alt="nebula" width="60%" class="right-image"
    />


| Nebula           | 电机              |
| ---------------- | ----------------- |
| 相数             | 2                 |
| 步距角           | 1.8°              |
| 额定电压         | DC 2.4V           |
| 额定电流         | DC 1.0A           |
| 保持转矩         | ≥110mN·m          |
| 相电阻           | 2.4±10% ohm (20℃) |
| 相电感           | 1.7±20% mH (1kHz) |
| 转向（轴伸向看） | A-AB-B-CW         |
| 转动惯量         | 15 g·cm²          |
| 电机重量         | 0.1 kg            |
| 绝缘等级         | Class F           |

</div>

## Nebula 结构
<div class="div-table">

<img
    src={require('./img/nebula_view.png').default}
    alt="nebula" width="60%" class="right-image"
/>

	
| Nebula          | 结构                    |
| --------------- | ----------------------- |
| 1. 电机         | 15. 惰轮                |
| 2. 齿圈盘       | 16. 3-5-6 PEEK轴承      |
| 3. 行星小齿轮   | 17. 扳手                |
| 4. MR85ZZ 轴承  | 18. 挤出齿轮            |
| 5. 行星架       | 19. 耗材传感器模块      |
| 6. 14齿齿轮     | 20. 滚花销钉 直径3*11   |
| 7. MF128ZZ_轴承 | 21. 3-5-10 PEEK轴承     |
| 8. 后壳         | 22. 右透镜              |
| 9. 配电板       | 23. 前壳                |
| 10. 卡扣        | 24. 左透镜              |
| 11. 卡爪        | 25. M3*25沉头内六角螺丝 |
| 12. M2x4螺丝    | 26. 透盖                |
| 13. 调节螺钉    | 27. 磁吸盖框            |
| 14. 弹簧        |                         |

</div>
