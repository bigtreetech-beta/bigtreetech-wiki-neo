---
sidebar_position: 2
description: Panda Bamboo Feeder Hardware
---

# Panda Bamboo Feeder Hardware

## Dimensions {#p_size}

:::info[models]

[reference models for external dimensions](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Reference%20Cad)

:::

<ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/03size.webp').default} width="50%"/>

## Hardware Interface

<ImageView src={require('./img/hardware.webp').default} width="50%"/>

- `Retract Button`: Used to retract/unload filament.

- `Load Button`: Used to feed filament into the printer extruder.

- `Type-C` Port: Can be used for factory resets via USB.

## Important Notes

1. Linkage Limit: A maximum of three Panda Bamboo Feeders can be linked and used together.

2. Power Requirements: When using multiple units, the topmost Feeder requires an external DC power supply (a 24V/2.8A power adapter must be purchased separately). Due to the limited power output of the Bambu Lab AMS interface, attempting to power multiple units through the printer simultaneously may cause system instability or malfunctions.

3. AMS Compatibility: The Panda Bamboo Feeder can be installed alongside the AMS or AMS 2 Pro; however, they cannot be used simultaneously. When printing via the AMS, please use the switch on the power adapter to turn off the Panda Bamboo Feeder.

4. Functionality Clarification: The Panda Bamboo Feeder is designed specifically for filament relay (auto-refill) and material buffering. It does not support multi-color printing.

## Installation Guide

### P1/X1 Series Models

1. Pre-print Required Components

    Ensure all required components are printed before starting the installation. The print files are available for download [here](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Mounting%20solution/Universal%20Mounting%20Bracket%20for%20PX%20series).

    <ImageView src={require('./img/install00.webp').default} width="50%"/>

2. Install the Mounting Tab

    Use the screws in the package to secure the 3D printed Mounting Tab to the back of the Panda Bamboo Feeder.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install01.webp').default} width="30%"/>

3. Install the Quick-Release Mounting Grid

    As shown in the diagram, thread the cable through the printed Quick-Release Mounting Grid and place it into the cable channel (ensure the DC head and MX3.0 are inserted correctly)

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install02.webp').default} width="30%"/>

    Snap the printed Cable Management Insert into the quick-release mounting grid.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install03.webp').default} width="30%"/>

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install04.webp').default} width="30%"/>

4. Attach Base

    Once the cables are arranged, slide the entire quick-release mounting frame into the printed Fixed Base.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install05.webp').default} width="30%"/>

5. Mount the Feeder

    Snap the Panda Bamboo Feeder onto the quick-release mounting grid via the mounting tab and connect the cables.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install06.webp').default} width="30%"/>

    Apply the included double-sided tape to the back of the fixed base, remove the release liner, and stick the base to a suitable location, such as the side of the printer.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install06.2.webp').default} width="20%"/>

### Panda Perch Installation

For BIQU Panda Perch users: Following Step 2 in P1/X1 Series Models, snap the Feeder into the hexagonal hole on the side of the Perch using the mounting tab. Secure the hook firmly from the inside with the printed clip shown below. [Click here to download the required print files](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Mounting%20solution/Panda%20Perch%20H2D%20mounting%20bracket).

<ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install07.webp').default} width="30%"/>

<ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/install08.webp').default} width="30%"/>

### A1 Series Models

1. Pre-print Required Components

    Pre-print the Tangle Detection Delete Module and Mounting Bracket before installation. Download files [here](https://github.com/bigtreetech/Panda_Bamboo_Feeder/tree/master/3D%20Model/Mounting%20solution/A1).

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install00.01.webp').default} width="30%"/>

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install00.02.webp').default} width="30%"/>

2. Begin Installation

    Open the buckle at the indicated position, being careful not to apply too much force to avoid damage.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install01.webp').default} width="30%"/>

    Remove the spring and rotate the securing ring, circled in the image, by 90 degrees to detach it.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install02.webp').default} width="30%"/>

    Insert the Tangle Detection Delete Module into the print head.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install03.webp').default} width="30%"/>

    Reinstall the securing ring that was previously removed.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install04.webp').default} width="30%"/>

    Pay attention to the direction: the protrusion on the securing ring should face the cutter side.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install05.webp').default} width="30%"/>

    Use the screws in the package to secure the printed Mounting Bracket to the back of the Panda Bamboo Feeder (pay attention to the orientation).

    <ImageView src={require('./img/a1install06.webp').default} width="30%"/>

    As shown in the diagram, snap it into the top end of the filament spool holder.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install07.webp').default} width="30%"/>

    :::info

    If you are only using the Panda Bamboo Feeder as a buffer, or if you plan to use filament directly from this filament spool holder, you will need to replace the PTFE tube at the Panda Bamboo Feeder filament inlet with a slightly longer one to prevent filament tangling.

    :::

    The PTFE tube should not be too long or too short. It should form a natural, smooth curve.

    <ImageView src={require('@site/docs/panda-series/module/panda-bamboo-feeder/img/a1install08.webp').default} width="30%"/>

### Custom DIY Mounting

[Refer to here](#p_size) to download the reference models for external dimensions and design your own custom mounting brackets for other printer models.
