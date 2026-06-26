---
sidebar_position: 2
description: Panda Treat Hardware
---

# Panda Treat Hardware

## What's in the box?

A Panda Treat kit contains the hardware needed to assemble and wire the edible ink adapter. Printed mounting parts are not included in the box because they are specific to the printer that you plan to install the Panda Treat onto. The user must print the correct mounting parts for the selected printer model before installation.

<ImageView src={require('@site/docs/panda-series/module/panda-treat/img/whats-in-the-box.webp').default} width="50%"/>

The box includes:

- Panda Treat PCB (A)
- Official edible ink cartridge (B)
- Printer interface cable set for A1, A1 mini, P1, and X1C: 2 cables in total (C)
- M3 x 6 mm low-profile, hex socket, self-tapping screws: 14 pieces (D)
- Silicone cartridge seal x 1 (E)
- SD card x 1 (F)
- Allen key x 1 (G)
- Magnets for P1S / X1C installations x 4 (H)
- Quick start card x 1 (I)

:::info[Note]

Use the installation instructions, parts, and tools mentioned in the installation guide for your specific printer. Typical parts that ship with a Panda Treat kit are shown above. Parts may vary as updates are made.

:::

## Interfaces

During installation and maintenance, reference may be made to certain Panda Treat interfaces. These interfaces are shown and described here so that the reader has an understanding of what is being referenced later when this naming convention is used.

<ImageView src={require('@site/docs/panda-series/module/panda-treat/img/hw-interfaces.webp').default} width="50%"/>

- `USB-C`: Used for service tasks such as manual updates where supported by the firmware. This interface is not required for installation.
- `Printer interface connector`: Connects the Panda Treat to the printer using the supplied model-specific cable. This interface is required for installation.
- `Cartridge contacts and pins`: Provide the electrical connection to the edible ink cartridge.
- `SD card slot`: Stores the files used by the Panda Treat during printing.

:::info[Note]

Do not touch the cartridge electrical contacts. Oils from fingers and damage to the contact area can cause poor prints or cartridge faults.

:::

## Important installation notes

:::info[Important]

Always power off the printer before connecting or disconnecting the Panda Treat cable or cartridge.

:::

- Never tug directly on small cables. Hold the connector body and gently work it loose using fingernails or a suitable plastic tool such as the [JST connector removal tool](https://makerworld.com/en/models/1169414-jst-connector-removal-tool).
- Once the smaller end of the cable has been installed into the Panda Treat, avoid removing it to prevent cable damage. Instead, remove the cable on the printer end using the method mentioned above.
- Do not force the cartridge into the mount. It should clip into position using the intended lever and support points.

## Installation onto an A1

### Required components

For this installation you will require the parts below. Please reference the [What's in the box?](#whats-in-the-box) and [Interfaces](#interfaces) sections if you need help identifying one of them.

- Panda Treat PCB x 1
- Printed mounts for the A1 x 1 full set: [panda-treat-a1-a1-mini-mount](https://makerworld.com/en/models/2963559-biqu-x-cmy-labs-panda-treat-a1-a1-mini-mount)
- Printed purge container for A1 x 1: [panda-treat-a1-purge-bucket](https://makerworld.com/en/models/2963618-biqu-x-cmy-labs-panda-treat-a1-purge-bucket)
- SD card
- A1 interface cable
- M3 x 6 mm self-tapping screws x 8
- Allen key
- Optional but highly recommended: [JST detachment tool](https://makerworld.com/en/models/1169414-jst-connector-removal-tool)
- Optional: [replacement rear toolhead cover with wire opening](https://makerworld.com/en/models/2967583-biqu-x-cmy-labs-panda-treat-a1-a1-mini-rear-cover)

### Printing parts

Begin by printing the linked A1 mounting parts. Use the provided 3MF file and do not change the part orientation or support settings unless updated official instructions say to do so.

PLA is suitable for the printed mounting parts. Once printing is complete, confirm that the following parts are present:

- Panda Treat A1 / A1 Mini Mount - Front x 1
- Panda Treat A1 / A1 Mini Mount - Rear x 1
- Panda Treat A1 Purge Bucket x 1
- JST detachment tool x 1
- Optional: Panda Treat A1 / A1 Mini Toolhead Rear Cover x 1

### Assembly

To assemble the Panda Treat, complete the following steps.

1. Place the PCB into the rear mount with the display facing upward. Press the PCB towards the base of the rear mount so that there is no gap between the bottom of the rear mount and the PCB. This will align the mounting holes with the screw holes in the rear mount. Fasten the PCB using the supplied screws but do not over-tighten.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/pcb-to-rear-mount.webp').default} width="30%"/>

2. Insert the front part of the mount over the rear part, ensuring that the alignment tabs on the side are fully inserted and that the display is not pinched between the front and rear parts as this could cause damage to the display.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/front-and-rear-alignment.webp').default} width="30%"/>

3. Insert four of the M3 x 6 mm self-tapping screws into the rear holes of the rear mount and tighten them. Do not over-tighten them as you will strip the plastic of the mount.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-mount-rear-screws.webp').default} width="30%"/>

4. Insert the SD card supplied with the Panda Treat.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/sd-inserted-a1.webp').default} width="30%"/>

5. Insert the small end of the A1 cable into the Panda Treat power connector. Take note of the orientation of installation.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-connector.webp').default} width="30%"/>

The assembly process is now complete. This process only needs to be performed on a one-time basis for any given printer that you plan to use the Panda Treat with. The following installation process details the procedure that you would need to perform repeatedly if you plan on installing and removing the Panda Treat from your printer.

### Installation

The following steps document what you need to do to take a fully assembled Panda Treat and install it onto or remove it from an A1 printer. Always perform them with the power to the printer switched off.

1. Clip the edible ink purge bucket onto the existing purge bucket area of the A1. Note that there are two posts on the bottom of the part of the purge bucket that align with holes in the bottom of the A1 purge plastic base. Ensure that the edible ink purge bucket is pushed all the way forward until these click into place. When removing the edible ink purge bucket, pull this part of it down first to release the posts.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-purge.webp').default} width="50%"/>

2. Remove the front cover of the A1 toolhead. You can leave the yellow and grey extruder wheel beneath the cover in place or remove it. There is no requirement from the Panda Treat installation either way.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/remove-front-cover-a1.webp').default} width="30%"/>

3. Clip the Panda Treat onto the front of the toolhead by first aligning and latching the top into place and then pressing in at the base. You will feel it click on the lower section when it has clipped in properly. Ensure that the mating surface between the Panda Treat and the toolhead is flat to guarantee proper attachment.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-clipped-in.webp').default} width="30%"/>

4. Remove the rear toolhead cover by prying at the gap in the bottom, centre. Using a tool can often make this easier.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/pry-rear-cover-a1.webp').default} width="30%"/>

5. Use the JST removal tool to unplug the connector marked in red. Never pull directly on the wires themselves as this can easily result in damage.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-jst-connector-removal.webp').default} width="30%"/>

6. Fold the disconnected connector into the open area to the left of it.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-jst-fold-connector.webp').default} width="30%"/>

7. Plug in the Panda Treat connector using the orientation shown.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-jst-insert-pt.webp').default} width="30%"/>

8. At this point, you can install the rear toolhead cover designed by K2 Kevin.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-rear-cover.webp').default} width="30%"/>

9. Ensure that the blue sealing tape has been removed from the edible ink cartridge and then install the cartridge by inserting the bottom of it into the cartridge mount and rotating the top into the lever arm clip until it is secured. You may need to lift the arm using your fingers to get it in place if the lever arm is particularly stiff.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-cart-insertion-process.webp').default} width="70%"/>

The A1 installation is complete once the hardware is mounted, the cable is connected, the SD card is installed, and the cartridge is inserted.

:::info[Important]

In order to ensure longevity of the ink cartridge it is critical to read and follow the guidance in the [Ink cartridge handling](#ink-cartridge-handling) section before starting the software setup.

:::

## Installation onto an A1 mini

### Required components

For this installation you will require the parts below. Please reference the [What's in the box?](#whats-in-the-box) and [Interfaces](#interfaces) sections if you need help identifying one of them.

- Panda Treat PCB x 1
- Printed mounts for the A1 / A1 mini x 1 full set: [panda-treat-a1-a1-mini-mount](https://makerworld.com/en/models/2963559-biqu-x-cmy-labs-panda-treat-a1-a1-mini-mount)
- Printed purge container for A1 mini x 1: [panda-treat-a1-mini-purge-bucket](https://makerworld.com/en/models/2964696-biqu-x-cmy-labs-panda-treat-a1-mini-purge-bucket)
- SD card
- A1 interface cable
- M3 x 6 mm self-tapping screws x 8
- Allen key
- Optional but highly recommended: [JST detachment tool](https://makerworld.com/en/models/1169414-jst-connector-removal-tool)
- Optional: [replacement rear toolhead cover with wire opening](https://makerworld.com/en/models/2967583-biqu-x-cmy-labs-panda-treat-a1-a1-mini-rear-cover)

### Printing parts

Begin by printing the linked A1 / A1 mini mounting parts. Use the provided 3MF file and do not change the part orientation or support settings unless updated official instructions say to do so.

PLA is suitable for the printed mounting parts. Once printing is complete, confirm that the following parts are present:

- Panda Treat A1 / A1 Mini Mount - Front x 1
- Panda Treat A1 / A1 Mini Mount - Rear x 1
- Panda Treat A1 mini Purge Bucket x 1
- JST detachment tool x 1
- Optional: Panda Treat A1 / A1 Mini Toolhead Rear Cover x 1

### Assembly

To assemble the Panda Treat for an A1 mini, follow the same assembly steps used for the A1. Insert the small end of the A1 / A1 mini cable into the Panda Treat power connector and take note of the orientation of installation.

### Installation

The following steps document what you need to do to take a fully assembled Panda Treat and install it onto or remove it from an A1 mini printer. Always perform them with the power to the printer switched off.

1. Clip the edible ink purge bucket onto the existing purge bucket area of the A1 mini. Note that there are two posts on the bottom of the part of the purge bucket that align with holes in the bottom of the A1 mini purge plastic base. Ensure that the edible ink purge bucket is pushed all the way forward until these click into place. When removing the edible ink purge bucket, pull this part of it down first to release the posts.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-mini-purge.webp').default} width="50%"/>

2. Remove the front cover of the A1 mini toolhead. You can leave the yellow and grey extruder wheel beneath the cover in place or remove it. There is no requirement from the Panda Treat installation either way.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/remove-front-cover-a1.webp').default} width="30%"/>

3. Clip the Panda Treat onto the front of the toolhead by first aligning and latching the top into place and then pressing in at the base. You will feel it click on the lower section when it has clipped in properly. Ensure that the mating surface between the Panda Treat and the toolhead is flat to guarantee proper attachment.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-clipped-in.webp').default} width="30%"/>

4. Remove the rear toolhead cover by prying at the gap in the bottom, centre. Using a tool can often make this easier.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/pry-rear-cover-a1.webp').default} width="30%"/>

5. Use the JST removal tool to unplug the connector marked in red. Never pull directly on the wires themselves as this can easily result in damage.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-jst-connector-removal.webp').default} width="30%"/>

6. Fold the disconnected connector into the open area to the left of it.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-jst-fold-connector.webp').default} width="30%"/>

7. Plug in the Panda Treat connector using the orientation shown.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-jst-insert-pt.webp').default} width="30%"/>

8. At this point, you can install the rear toolhead cover designed by K2 Kevin.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-rear-cover.webp').default} width="30%"/>

9. Ensure that the blue sealing tape has been removed from the edible ink cartridge and then install the cartridge by inserting the bottom of it into the cartridge mount and rotating the top into the lever arm clip until it is secured. You may need to lift the arm using your fingers to get it in place if the lever arm is particularly stiff.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/a1-cart-insertion-process.webp').default} width="70%"/>

The A1 mini installation is complete once the hardware is mounted, the cable is connected, the SD card is installed, and the cartridge is inserted.

:::info[Important]

In order to ensure longevity of the ink cartridge it is critical to read and follow the guidance in the [Ink cartridge handling](#ink-cartridge-handling) section before starting the software setup.

:::

## Installation onto P1S

P1S support is planned for release through the matching firmware, mounting parts, and installation instructions. Do not attempt to install the Panda Treat onto a P1S until the official P1S installation mounts, instructions, and firmware are available.

## Installation onto X1C

X1C support is planned for release through the matching firmware, mounting parts, and installation instructions. Do not attempt to install the Panda Treat onto an X1C until the official X1C installation mounts, instructions, and firmware are available.

## Ink cartridge handling

Print quality depends heavily on how the edible ink cartridge is handled. Damage to the printhead or poor storage can cause missing lines, colour shifts, and visible print artefacts. This section describes how to store and handle your Panda Treat ink cartridges to get the best performance and life out of them.

The image below shows the main anatomy of your Panda Treat ink cartridge and will be referenced extensively in the sub-headings that follow. It is also beneficial to read the brief description of how the cartridge works below, as this helps to explain the need for many of the storage and maintenance tasks.

<ImageView src={require('@site/docs/panda-series/module/panda-treat/img/print-cartridge-anatomy.webp').default} width="50%"/>

The print cartridge has three internal food colouring reservoirs. One contains cyan (blue), one contains magenta (red), and one contains yellow colouring. Each of these feeds tiny nozzles that are on the printhead. When the cartridge is printing, these tiny nozzles spray ink downwards onto your object without having to touch the object itself. That ink is designed to dry rapidly so that it does not smudge easily after printing. As a result, the ink can also dry rapidly within the nozzles, which can cause clogs and print defects. The storage, handling, and maintenance tasks explain how to prevent clogging and how to remove clogs if they form.

### Storage

Since the edible ink dries rapidly, it is important to ensure that there is a seal around the printhead that prevents air from drying it out when it is not in use.

Your Panda Treat ink cartridge ships with a foam seal stuck onto the cartridge holder. This foam seal is ideal for securing the cartridge while the blue sealing tape is still stuck over the printhead, but once the blue tape is removed, the foam seal can result in inks mixing if the cartridge is re-inserted into the cartridge holder. Therefore, after removing the blue sealing tape before the first cartridge use, you should remove the foam seal by slowly peeling it up and then replace it with the silicone seal.

Before sticking it down, align the silicone seal with the back of the cartridge holder and make sure that the right edge of the silicone seal aligns with the rib that runs down the length of the cartridge holder. After you have installed the silicone seal, the cartridge holder should be used to store the cartridge when it is not in use. When storing the cartridge, keep it standing upright and avoid placing it upside down or lying on its side.

<ImageView src={require('@site/docs/panda-series/module/panda-treat/img/cartridge-seal-replacement.webp').default} width="50%"/>

### Maintenance and care

Your ink cartridge requires proper maintenance and care to produce high quality prints. Follow the steps below to ensure that it performs well for the full service life.

- Always store the cartridge in the cartridge holder with the silicone seal installed when it is not in use.
- If the cartridge has not been used for more than 15 minutes, gently wipe the printhead with a clean paper towel starting from the back and moving towards the front. You will see three distinct colour lines appear when it is ready to be used. Repeat the wipe a few times after the colour lines are visible.

    <ImageView src={require('@site/docs/panda-series/module/panda-treat/img/wiping-cartridge.webp').default} width="50%"/>

- If the cartridge has not been used for several days, hold a damp paper towel against the printhead for a few seconds before wiping. Do not soak the whole cartridge.
- Never stand the cartridge directly on the printhead or touch the printhead with your fingers. The printhead is the shiny strip at the base of the cartridge.
- Never clean the printhead with alcohol. Alcohol may be used only on the rear contact pads if they tarnish.
- Never store the cartridge on its side. Store it upright so ink does not move between wells or leak across the printhead.
- Make sure that the cartridge vents are not blocked with dirt or ink. The cartridge vents are the small holes around the edge of the vent label.
- Avoid touching the contact pads as finger grease can cause them to corrode.
