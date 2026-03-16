---
sidebar_position: 1
description: K HUB 扩展坞
---

# K HUB

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

<div class="div-table">

<ImageView src={require('./img/k-hub-title.webp').default} width="40%" class="right-image"/>

## 产品简介

BIGTREETECH K HUB V1 是必趣创新（深圳）科技有限公司推出的一款 USB2.0 HUB 拓展板，让客户在使用 Klipper 的 USB 方案时有更多的USB拓展接口，方便DIY。

## 产品特点

- 支持24V或者5V供电；
- 各个接口均有ESD保护；
- 24V电源口增设防反接保护；
- 采用大功率DCDC芯片，支持更大电流输出（USB接口输出）；
- 电源接口采用快接插头形式，方便客户DIY；
- 提供初版外壳模型文件，配套的成品配件，方便自行打印组装成品。

## 产品参数

| KHub | 规格 |
| ------ | ------ |
| 板子尺寸 | 109.6mm x 21.6mm |
| USB输出接口 | 4x USBA USB2.0，每路输出 5V 1.5A |
| Type-C输入接口 | Type-C信号输入接口，电源输入口 5V 2A |
| 24V输入接口 | 1x 24V 3A 输入接口 |
| 风扇输出接口 | 1x 24V风扇输出接口 |
| 配套配件 | 1x 风扇 1x 散热片 组装螺丝 |

</div>

## 接口介绍

### 接口示意图

<ImageView src={require('./img/k-hub-interface.webp').default} width="100%"/>

### 指示灯说明

- 绿色: TYPE-C供电
- 蓝色: 24V供电

<ImageView src={require('./img/k-hub-led.webp').default} width="30%"/>

## 配件清单

| 配件名称 | 规格 | 数量 |
| -------- | ------ | ---- |
| 螺丝 | 圆头内六角自攻螺丝 M2.6×14 | 7 |
| 螺丝 | 圆头内六角自攻螺丝 M2.6×10 | 2 |
| 螺丝 | BHCS M3×10 | 2 |
| 船型螺母 | M3 船型螺母 | 2 |
| 风扇 | 24V | 1 |

## 组装步骤

### Step 1 安装DIN固定架

使用2颗M2.6×10自攻螺丝，将底壳与DIN固定架连接到一起（DIN版本需要，型材版本不需要）。

<ImageView src={require('./img/k-hub-install-step1.webp').default} width="60%"/>

<ImageView src={require('./img/k-hub-install-step2.webp').default} width="60%"/>

### Step 2 固定主板与上壳

使用4颗M2.6×14自攻螺丝透过底壳与主板，将上壳固定。

<ImageView src={require('./img/k-hub-install-step3.webp').default} width="60%"/>

### Step 3 安装盖子

使用一根耗材（1.75mm），将盖子固定在上盖上。

<img src={require('./img/k-hub-install-step4.webp').default} width="60%"/>

<img src={require('./img/k-hub-install-step5.webp').default} width="60%"/>

### Step 4 安装风扇

使用3颗M2.6×14螺丝将风扇固定在打印件上。

<ImageView src={require('./img/k-hub-install-step6.webp').default} width="60%"/>

## 爆炸图

<Tabs groupId="khub-version">
    <TabItem value="khub-din" label="DIN版本爆炸图" default>
        <ImageView src={require('./img/k-hub-install-step7.webp').default} width="60%"/>
    </TabItem>
    <TabItem value="khub-extrusion" label="型材版本爆炸图">
        <ImageView src={require('./img/k-hub-install-step8.webp').default} width="60%"/>
    </TabItem>
</Tabs>

## 安装效果图

<Tabs groupId="khub-version">
    <TabItem value="khub-din" label="装到DIN导轨效果图" default>
        <ImageView src={require('./img/k-hub-install-step9.webp').default} width="60%"/>
    </TabItem>
    <TabItem value="khub-extrusion" label="装到型材效果图">

        使用2颗M3×10螺丝和2个M3船型螺母将K HUB固定到型材上。

        <ImageView src={require('./img/k-hub-install-step10.webp').default} width="60%"/>
    </TabItem>
</Tabs>

## 注意事项

- 输出接口标注的电流只在24V接入时有效，否则只有USB输入提供的电流；
- 各USB接口输出电压为5V，最大电流为1.5A；
- 请确保24V输入电源极性正确，虽然板子有防反接保护，但正确连接可确保设备正常工作；
- 安装风扇时请注意风扇方向，确保散热效果；
- 使用电烙铁时请注意安全，避免烫伤。
