---
sidebar_position: 2
description: CB1 硬件
---

# CB1 硬件

## 外观尺寸

<ImageView src={require('./img/cb1-size.webp').default} width="80%"/>

## 原理图

[BIGTREETECH_CB1_V22_220812_SCH](https://raw.githack.com/bigtreetech/docs/master/docs/download/BIGTREETECH_CB1_V22_220812_SCH.pdf)

## 外设接口

### 40 pin GPIO

当CB1与Manta M4P M5P M8P PI4B_Adapter 等主板一起使用时，主板上的40引脚GPIO

| 引脚 | 信号 | 描述               | 引脚 | 信号 | 描述              |
| ---- | ---- | ------------------ | ---- | ---- | ----------------- |
| 1    | 3.3V |                    | 2    | 5V   |                   |
| 3    | NC   |                    | 4    | 5V   |                   |
| 5    | NC   |                    | 6    | GND  |                   |
| 7    | PC7  | GPIO71             | 8    | PH0  | GPIO224, UART0_TX |
| 9    | GND  |                    | 10   | PH1  | GPIO225, UART0_RX |
| 11   | PC14 | GPIO78             | 12   | PC13 | GPIO77            |
| 13   | PC12 | GPIO76             | 14   | GND  |                   |
| 15   | PC10 | GPIO74             | 16   | PC11 | GPIO75            |
| 17   | 3.3V |                    | 18   | PC9  | GPIO73            |
| 19   | PH7  | GPIO231, SPI1_MOSI | 20   | GND  |                   |
| 21   | PH8  | GPIO232, SPI1_MISO | 22   | NC   |                   |
| 23   | PH6  | GPIO230, SPI1_CLK  | 24   | NC   |                   |
| 25   | GND  |                    | 26   | PG8  | GPIO200           |
| 27   | NC   |                    | 28   | PG7  | GPIO199           |
| 29   | NC   |                    | 30   | GND  |                   |
| 31   | PG6  | GPIO198            | 32   | PG9  | GPIO201           |
| 33   | NC   |                    | 34   | GND  |                   |
| 35   | PC6  | GPIO70             | 36   | NC   |                   |
| 37   | PC15 | GPIO79             | 38   | PH10 | GPIO234, IR_RX    |
| 39   | GND  |                    | 40   | PC8  | GPIO72            |

### 2 * 100 pins

| A 引脚 | 信号     | 描述         | A 引脚 | 信号     | 描述              |
| ------ | -------- | ------------ | ------ | -------- | ----------------- |
| 1      | GND      |              | 2      | GND      |                   |
| 3      | NC       |              | 4      | EPHY-TXP | 以太网TX正极      |
| 5      | NC       |              | 6      | EPHY-TXN | 以太网TX负极      |
| 7      | GND      |              | 8      | GND      |                   |
| 9      | NC       |              | 10     | EPHY-RXP | 以太网RX正极      |
| 11     | NC       |              | 12     | EPHY-RXN | 以太网RX负极      |
| 13     | GND      |              | 14     | GND      |                   |
| 15     | LINK_LED | 以太网灯     | 16     | NC       |                   |
| 17     | SPD_LED  | 以太网灯     | 18     | NC       |                   |
| 19     | NC       |              | 20     | NC       |                   |
| 21     | PH5      | 信号灯(ACT)  | 22     | GND      |                   |
| 23     | GND      |              | 24     | PC15     |                   |
| 25     | PC8      |              | 26     | PC6      |                   |
| 27     | PH10     |              | 28     | NC       |                   |
| 29     | NC       |              | 30     | PG6      |                   |
| 31     | PG9      |              | 32     | GND      |                   |
| 33     | GND      |              | 34     | NC       |                   |
| 35     | PG7      |              | 36     | NC       |                   |
| 37     | PG8      |              | 38     | PH6      |                   |
| 39     | NC       |              | 40     | PH8      |                   |
| 41     | NC       |              | 42     | GND      |                   |
| 43     | GND      |              | 44     | PH7      |                   |
| 45     | PC9      |              | 46     | PC10     |                   |
| 47     | PC11     |              | 48     | PC12     |                   |
| 49     | PC13     |              | 50     | PC14     |                   |
| 51     | SoC_RX   | 调试 UART    | 52     | GND      |                   |
| 53     | GND      |              | 54     | PC7      |                   |
| 55     | SoC_TX   | 调试 UART    | 56     | NC       |                   |
| 57     | SDC0-CLK | MicroSD Card | 58     | NC       |                   |
| 59     | GND      |              | 60     | GND      |                   |
| 61     | SDC0-D3  | MicroSD Card | 62     | SDC0-CMD | MicroSD Card      |
| 63     | SDC0-D0  | MicroSD Card | 64     | PG11     |                   |
| 65     | GND      |              | 66     | GND      |                   |
| 67     | SDC0-D1  | MicroSD Card | 68     | PG12     |                   |
| 69     | SDC0-D2  | MicroSD Card | 70     | PG13     |                   |
| 71     | GND      |              | 72     | PG14     |                   |
| 73     | PG16     |              | 74     | GND      |                   |
| 75     | NC       |              | 76     | PI16     | MicroSD Card 检测 |
| 77     | 5V       |              | 78     | NC       |                   |
| 79     | 5V       | In 2A        | 80     | NC       |                   |
| 81     | 5V       | In 2A        | 82     | NC       |                   |
| 83     | 5V       | In 2A        | 84     | 3.3V     | Out 200mA         |
| 85     | 5V       | In 2A        | 86     | 3.3V     | Out 200mA         |
| 87     | 5V       | In 2A        | 88     | 1.8V     | Out 100mA         |
| 89     | NC       |              | 90     | 1.8V     | Out 100mA         |
| 91     | NC       |              | 92     | PWRON    |                   |
| 93     | FEL      |              | 94     | NC       |                   |
| 95     | NC       |              | 96     | NC       |                   |
| 97     | NC       |              | 98     | GND      |                   |
| 99     | Recovery |              | 100    | Reset    |                   |

| B 引脚 | 信号    | 描述        | B 引脚 | 信号      | 描述          |
| ------ | ------- | ----------- | ------ | --------- | ------------- |
| 101    | NC      |             | 102    | NC        |               |
| 103    | USB1-DM | Host USB1   | 104    | LineOut L |               |
| 105    | USB1-DP | Host USB1   | 106    | LineOut R |               |
| 107    | GND     |             | 108    | GND       |               |
| 109    | NC      |             | 110    | NC        |               |
| 111    | TV_OUT  | CVBS OUT    | 112    | NC        |               |
| 113    | GND     |             | 114    | GND       |               |
| 115    | NC      |             | 116    | NC        |               |
| 117    | NC      |             | 118    | NC        |               |
| 119    | GND     |             | 120    | GND       |               |
| 121    | NC      |             | 122    | NC        |               |
| 123    | NC      |             | 124    | NC        |               |
| 125    | GND     |             | 126    | GND       |               |
| 127    | NC      |             | 128    | USB3-DM   | Host USB3     |
| 129    | NC      |             | 130    | USB3-DP   | Host USB3     |
| 131    | GND     |             | 132    | GND       |               |
| 133    | NC      |             | 134    | USB2-DM   | Host USB2     |
| 135    | NC      |             | 136    | USB2-DP   | Host USB3     |
| 137    | GND     |             | 138    | GND       |               |
| 139    | NC      |             | 140    | USB0-DM   | OTG USB       |
| 141    | NC      |             | 142    | USB0-DP   | OTG USB       |
| 143    | NC      |             | 144    | GND       |               |
| 145    | NC      |             | 146    | NC        |               |
| 147    | NC      |             | 148    | NC        |               |
| 149    | NC      |             | 150    | GND       |               |
| 151    | HCEC    | HDMI CEC    | 152    | NC        |               |
| 153    | HHPD    | HDMI 热插拔 | 154    | NC        |               |
| 155    | GND     |             | 156    | GND       |               |
| 157    | NC      |             | 158    | NC        |               |
| 159    | NC      |             | 160    | NC        |               |
| 161    | GND     |             | 162    | GND       |               |
| 163    | NC      |             | 164    | NC        |               |
| 165    | NC      |             | 166    | NC        |               |
| 167    | GND     |             | 168    | GND       |               |
| 169    | NC      |             | 170    | HTX2P     | HDMI TX2 正极 |
| 171    | NC      |             | 172    | HTX2N     | HDMI TX2 负极 |
| 173    | GND     |             | 174    | GND       |               |
| 175    | NC      |             | 176    | HTX1P     | HDMI TX1 正极 |
| 177    | NC      |             | 178    | HTX1N     | HDMI TX1 负极 |
| 179    | GND     |             | 180    | GND       |               |
| 181    | NC      |             | 182    | HTX0P     | HDMI TX0 正极 |
| 183    | NC      |             | 184    | HTX0N     | HDMI TX0 负极 |
| 185    | GND     |             | 186    | GND       |               |
| 187    | NC      |             | 188    | HTXCP     | HDMI CLK 正极 |
| 189    | NC      |             | 190    | HTXCN     | HDMI CLK 负极 |
| 191    | GND     |             | 192    | GND       |               |
| 193    | NC      |             | 194    | NC        |               |
| 195    | NC      |             | 196    | NC        |               |
| 197    | GND     |             | 198    | GND       |               |
| 199    | HSDA    | HDMI I2C    | 200    | HSCL      | HDMI I2C      |
