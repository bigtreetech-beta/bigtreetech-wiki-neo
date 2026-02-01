---
sidebar_position: 2
---

# Panda Touch Hardware

Panda Touch Hardware

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

:::info Panda Touch CAD Files

Panda Touch CAD files are available in the GitHub repository [bigtreetech/PandaTouch/3D](https://github.com/bigtreetech/PandaTouch/tree/master/3D)

:::

## Assembly Instructions

### Overview

<img
    src={require('@site/docs/panda-series/panda-touch/img/pt_back.png').default}
    alt="" width="550"
/>

:::tip 

Slide the power switch to `Battery Power` to operate Panda Touch on its lithium battery for portability. Slide it to `DC 5V` to power directly from the magnetic charging dock, thereby extending the internal battery's lifespan. This mode is recommended if you frequently turn the printer on and off. Slide the switch to `OFF` to power down Panda Touch.

:::

### Charging Dock

<img
    src={require('@site/docs/panda-series/panda-touch/img/charging_dock.png').default}
    alt="" width="550"
/>

:::tip

The power input features hot-swap protection, allowing users to hot-swap the power supply.

:::

### 包装清单

| ![](@site/docs/panda-series/panda-touch/img/pl_1.png)     | ![](@site/docs/panda-series/panda-touch/img/pl_2.png) |
|:-----------------------:|:-------------------:|
| Panda Touch x 1         | mounting x 1            |
| ![](@site/docs/panda-series/panda-touch/img/pl_3.png)     | ![](@site/docs/panda-series/panda-touch/img/pl_4.png) |
| Magnetic Charging Dock x 1               | USB-C cable x 1       |
| ![](@site/docs/panda-series/panda-touch/img/pl_5.png)     | ![](@site/docs/panda-series/panda-touch/img/pl_6.png) |
| M3x6 screws x 4<br/>Hex wrench x 1 | BTT duck x 1            |

### Installing Panda Touch

* Assemble the charging dock and mounting bracket using a hex/Allen wrench and two M3x6 FHCS screws, as shown in the diagram.

<img
    src={require('@site/docs/panda-series/panda-touch/img/pt_1_1.png').default}
    alt="" width="300"
/>

* Peel the film from the bottom of the mounting bracket.

<img
    src={require('@site/docs/panda-series/panda-touch/img/pt_1_2.png').default}
    alt="" width="300"
/>

Ensure the printer surface is clean and free of oil, grease, or other contaminants. Secure the assembled charging dock at the center of the original screen. Apply pressure to ensure complete adhesion, and allow 12 hours for optimal bonding strength.

<img
    src={require('@site/docs/panda-series/panda-touch/img/pt_1_3.png').default}
    alt="" width="300"
/>

* Connect Panda Touch to the charging dock.

<img
    src={require('@site/docs/panda-series/panda-touch/img/pt_1_4.png').default}
    alt="" width="300"
/>

### Wiring and Power Connection

- Remove the foam cover from the printer's USB port to access it.

    <img src={require('@site/docs/panda-series/panda-touch/img/pt_2_1.png').default} alt="" width="300" />

- Thread the charging cable through the hole on the right side of the printer, then insert the USB-C end into the power input of the charging dock.
    
    <img src={require('@site/docs/panda-series/panda-touch/img/pt_2_2.png').default} alt="" width="300" />

- Connect the power supply by inserting the USB-A end of the charging cable into the printer's USB port. Then route the cable through the clip as shown in the illustration.

> Tip:
> Ensure the cable is fully secured in the clip to prevent the tool head from snagging it during retraction.

    <img src={require('@site/docs/panda-series/panda-touch/img/pt_2_3.png').default} alt="" width="300" />

- The rear power switch offers three positions.
  * In the `Off` position, the battery charges but Panda Touch remains powered off.

  * When switched to the Battery position, USB will charge the battery while simultaneously powering the Panda Touch. If the Panda Touch is removed from the dock, the battery will take over and power it for up to 30 minutes. Upon returning to the dock, USB will resume charging and powering the Panda Touch. This mode is recommended for users who do not frequently turn the printer on and off. Note: There is no battery level indicator. Panda Touch is designed for short-term use away from the dock and is not suitable for extended mobile operation.

* When switched to the DC 5V position, Panda Touch is powered directly by the USB input while continuing to charge the battery. Removing it from the dock will turn off the power, and Panda Touch will not drain the battery. This mode is recommended for users who frequently power the printer on and off, as it maintains the battery charge cycle. Should these users wish to operate Panda Touch in portable mode, they can switch the power source to battery power after removing it from the dock.

    <img src={require('@site/docs/panda-series/panda-touch/img/pt_2_4.png').default} alt="" width="300" />

- Panda Touch has been successfully installed and powered on. Please follow the on-screen instructions to complete the setup.
  
    <img src={require('@site/docs/panda-series/panda-touch/img/pt_2_5.png').default} alt="" width="300" />
