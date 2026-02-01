---
sidebar_position: 3
---

# Panda Touch Firmware Config

Panda Touch Firmware Config

<!-- import lib start -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- import lib end -->

## First-Time Connection Guide

After initial startup or executing the `factory reset` command, you will see the following screen.

### Language Selection Guide

<img src={require('@site/docs/panda-series/panda-touch/img/language_guide.png').default} alt="" width="600" />

* Select a language for Panda Touch, then tap `Next`

### WiFi Connection Guide

<img src={require('@site/docs/panda-series/panda-touch/img/guide_wifi.png').default} alt="" width="600" />

During the initial setup process, Panda Touch will scan for WiFi networks and display up to 20 networks with the strongest signal strength. If you cannot find the desired network in the list, tap `Refresh`, and Panda Touch will rescan for WiFi networks.
>Note:
>The current firmware does not support connecting to hidden WiFi networks. Additionally, while Panda Touch is connecting to WiFi, it cannot simultaneously perform WiFi scanning tasks.
* Clicking a WiFi name in the list will bring up the [Keyboard Interface] (#Keyboard Interface). After entering the correct password, click `Confirm` to begin connecting to WiFi. (Password length: 8–64 characters)
* Connection status will display next to the WiFi network name. The `Spinner` graphic indicates WiFi is still attempting to connect. `✔` indicates a successful connection.
* After successful connection, the `Next` button will become active. Click `Next` to proceed to the printer connection menu.

>Note:
>If you are using a WiFi network with multiple access points sharing the same SSID, select the SSID with the strongest signal strength from the list.

Translated with DeepL.com (free version)

### 打印机连接菜单

<img src={require('@site/docs/panda-series/panda-touch/img/guide_printer.png').default} alt="" width="600" />

There are two possible methods to connect Panda Touch to a printer.
    1. Automatic scanning (recommended).
    2. Manual input.

### Locating Your Connection Details

During this process, you may need to enter connection details. These can be found by following the steps below.

#### P1P & P1S

* Navigate to `Settings -> WLAN` on the LCD menu, then click `OK`.

    <img src={require('@site/docs/panda-series/panda-touch/img/p1_1.png').default} alt="" width="600" />

* Enter the IP address and access code in the corresponding Panda Touch input fields (the access code is used for automatic scanning only).

    <img src={require('@site/docs/panda-series/panda-touch/img/p1_2.png').default} alt="" width="600" />

* In the screen menu, locate `Settings -> Device`, then click `OK`.

    <img src={require('@site/docs/panda-series/panda-touch/img/p1_3.png').default} alt="" width="600" />

* Enter the serial number code in the corresponding Panda Touch input field.

    <img src={require('@site/docs/panda-series/panda-touch/img/p1_4.png').default} alt="" width="600" />

#### Auto Scan

* To perform an auto scan, simply click the `Scan` button. Bambu Lab printers on the same WiFi network will appear in the scan results with pre-filled `Name`, `Printer IP`, `SN`, and `Model` information. Pre-filling these fields makes adding printers easier and reduces errors caused by manual data entry mistakes. The only data you need to enter is the `Access Code`, which can be found in the printer's WiFi/LAN menu. Instructions on how to locate the access code will appear on the Panda Touch screen. Printers previously connected to Panda Touch will still appear in the scan results, but Panda Touch will not allow them to be added again, and `Already Added` will display near the printer icon. After entering the access code, you can confirm the connection or manually add some of the data below.

#### Manual Input

* You can click the printer icon on the left to access the menu for selecting the printer model. You have to set the printer according to the actual model of the connected printer.Panda Touch will also do some checking in the background to confirm the model. The available models are listed below:
    * P1P
    * P1S
    * X1C
    * A1 mini
    * A1
    
  After selecting a model using the icon, the contents of the `Model` field will be populated with the corresponding model name.

* After selecting a printer model, there are four required fields. These fields contain the information needed to connect to and identify the printer. Click on the `i` icon and swipe left or right for instructions on how to find this information on the printer.

    * `Name`: User-defined name used to identify the printer. (Length: 1~15 characters)
    * `Printer IP`: Used by the Panda Touch to connect to the printer. (Length: 7~15 characters) * `Access Code`: for Panda Touch to connect to the printer.
    * `Access Code`: used for Panda Touch to connect to the printer. (Length: 8 characters)
    * `SN`: for Panda Touch to connect to the printer. (Length: 15 characters)

* There are 4 optional fields that can help you identify certain parameters of the printer for later use.

    * `Model': The model name identifies the exact model of the printer and defines the picture associated with it. p1p, p1s, x1c, a1 mini, a1 or custom. (Length: 0~15 characters)
    * `Supply Color`: The color of the supplies used by the printer. (length: 0~6 characters)
    * `Supply Material`: the supply material used by the printer. (Length: 0~6 characters) * `Consumable Color`: The consumable color used by the printer.
    * `Nozzle Diameter`: the diameter of the nozzle used by the printer. (Length: 0~6 characters) * `Confirm` button

- `Confirmation` button

    After filling in the `Required` information, you can click the `Confirm` button to start connecting to the printer.The title bar of the Panda Touch will show the connection status.

## Cloud Mode Features

If any of your P1P/P1S printers are not set to `LAN only` mode, you will need to switch the Panda Touch's communication method with the P1P/P1S printer to cloud mode in order to use the following functions:

* Heat up
* Start Printing
* Pause Printing
* Stop Printing

Please follow the steps below to switch the communication method between Panda Touch and P1P/P1S printer to cloud mode.

#### Log in to your Takitake account
* Click to jump to the setting page, and then click the `Login to Takitake Account` button. 

    <img src={require('@site/docs/panda-series/panda-touch/img/add_account.png').default} alt="" width="600" />

* Select your region by clicking the arrow in the upper right corner of the pop-up window.

* Users in China use cell phone numbers, while users in global regions use email addresses.

::::info How to find bambulab account

<img src={require('@site/docs/panda-series/panda-touch/img/login.png').default} alt="" width="600" />

:::warning know issue

Currently, 2-step authentication needs to be turned off to enable Cloud Mode on Panda Touch. If you want to keep it enabled then you can turn it off, enable Cloud Mode on Panda Touch and then turn it back on again. Please note that you may need to repeat this process every three months as the login details on Panda Touch will expire after this period.

:::

<img src={require('@site/docs/panda-series/panda-touch/img/input_account.png').default} alt="" width="600" />

::::

#### Synchronizing printers under an account to a local device

* After successfully logging in, you have the option to convert all existing printers to communicate with PandaTouch to Cloud Mode.

* Perform this action only if all printers are running in Cloud Mode, if the printer has `LAN Only` mode turned on, this action can be skipped. To change the communication method between PandaTouch and printers see [How to switch the communication method between PandaTouch and printers](#How to switch the communication method between pandatouch and printers)

    <img src={require('@site/docs/panda-series/panda-touch/img/login_ok.png').default} alt="" width="600" />

* Click `Yes' if you want to convert the communication between your existing printer and PandaTouch to cloud mode. 

* The printer must be on the same network as the PandaTouch during this process. If the network connection is poor, you may need to re-edit the printer's IP address.

    <img src={require('@site/docs/panda-series/panda-touch/img/sync_ok.png').default} alt="" width="600" />

* Once the printer is working in cloud mode, you will notice a green cloud associated with its card in the multi-printer view. The cloud indicates how the printer is communicating with PandaTouch.

* You will also notice a pair of green arrows indicating the connection status to that printer.
    <img src={require('@site/docs/panda-series/panda-touch/img/cloud_mode.png').default} alt="" width="600" />

#### How to delete a logged in account

* Delete the account information saved on the PandaTouch by clicking the `X` button in the upper right corner of the account information.

* After deleting the account information, the communication mode between the PandaTouch and the printer will be changed to local mode. Please note that this will not set the printer itself to `LAN only` mode, but will tell the Panda Touch to only use LAN mode to talk to the printer, which may result in some loss of functionality.

    <img src={require('@site/docs/panda-series/panda-touch/img/del_account.png').default} alt="" width="600" />

#### How to switch the communication between PandaTouch and the printer

* Navigate to the Printers/Group Cards page.
* Locate the printer for which you want to enable or disable Cloud Mode.
* Scroll down to the `Edit` button for that printer.
* Select `Enable Cloud` to switch the way the printer communicates with PandaTouch to Cloud Mode.

:::tip

The cloud account must be enabled in the setup menu or the communication method between this printer and PandaTouch will not be set to cloud mode.

<img src={require('@site/docs/panda-series/panda-touch/img/switch_work_mode.png').default} alt="" width="600" />

:::

## Keyboard Input

1. Use this key to hide or show the entered information.
2. toggle between uppercase and lowercase letters.
3. Switch to `Symbol Input`.
4. toggles to `Number Input`.

- Letters Input 

    <img src={require('@site/docs/panda-series/panda-touch/img/keyboard_letter.png').default} alt="" width="600" />

- Symbol Input

    <img src={require('@site/docs/panda-series/panda-touch/img/keyboard_symbol.png').default} alt="" width="600" />

- Number Inputs

    <img src={require('@site/docs/panda-series/panda-touch/img/keyboard_number.png').default} alt="" width="600" />

## Print jobs and thumbnail displays

<img src={require('@site/docs/panda-series/panda-touch/img/thumbnail_preview.png').default} alt="" width="600" />

:::info

Only print jobs initiated from Bambu Studio will be displayed, the .3mf file needs to be less than 20M, which is not supported on X1 series machines at this time.

Thumbnail Mismatch: Thumbnail mismatch will only occur if the image in the image folder has the same timestamp as another print file.

Enhanced Thumbnail Display: There is an option in the settings page to enhance the thumbnail display, when turned on, there will be a longer delay when printing from a USB flash drive or operating from the SD card panel.

:::

## Consumables Control

The Panda Touch allows the user to configure the type and color of consumables used on the external spool holder and AMS. The user can also load and unload filters using this menu.

When performing any operation, make sure the correct AMS unit and filament slot are selected. You will know that a consumable is selected when it has a red border around it. If nothing is selected, the `Load` and `Unload` buttons will be grayed out.

<img src={require('@site/docs/panda-series/panda-touch/img/filament_screen.png').default} alt="" width="600" />

## Supplies Drying 
The Panda Touch allows the user to dry supplies on the X1 Series and P1S. 

* Click on the Dry button

<img src={require('@site/docs/panda-series/panda-touch/img/drying.png').default} alt="" width="500" />

* Follow the steps on the right

<img src={require('@site/docs/panda-series/panda-touch/img/filament_dry.png').default} alt="" width="500" />

## Part Skip

:::note

Print jobs need to be initiated from Bambu Studio or the Handy app, reprinted jobs are not supported.  

Not available in the following cases
- 1 or more 64 parts on a single disk 
- Bambu studio version is lower than V1.6.

:::

<img src={require('@site/docs/panda-series/panda-touch/img/skip_objects.gif').default} alt="" width="500" />

## HMS (Health Management System)

<img src={require('@site/docs/panda-series/panda-touch/img/hms.png').default} alt="" width="600" />

* Tap the title bar of Panda Touch and the HMS Notification Center menu will expand.
* The Panda Touch will automatically expand the HMS Notification Center when a new HMS notification is detected.
* The top left corner of the title bar will display the number of printers that have sent HMS notifications.
* Clicking on the appropriate HMS notification brings up the wiki link QR code for this issue.
* Click `X` to ignore this notification.
* Click `Ignore All` to ignore all notifications **Note: ** Panda Touch will ignore notifications for all printers except X1C. Since the X1C sends repeated notification messages at regular intervals, ignored notifications may reappear shortly thereafter.

## Grouping Logic 

Panda Touch allows you to create up to 10 groups, each of which can contain single or multiple printers.

### How to add to a group

* Click + in the list of connected printers to bring up the multifunction menu.
    
    <img src={require('@site/docs/panda-series/panda-touch/img/press_plus.png').default} alt="" width="600" />

* Select the Add Group option.

    <img src={require('@site/docs/panda-series/panda-touch/img/press_add_group.png').default} alt="" width="600" />

* Select the printers to be added to the group and make sure that one of them is selected as the host (the other printers in the group will follow the commands sent to the host).

    <img src={require('@site/docs/panda-series/panda-touch/img/group_choose_printer.png').default} alt="" width="600" />

* Click Next, enter a group name, and click `OK'.

    <img src={require('@site/docs/panda-series/panda-touch/img/group_name.png').default} alt="" width="600" />

* Now you can see the group in the list of printers, clicking on the group will allow you to control the entire group, but the controls displayed will be those of the group leader.

### Switching between printer group control and individual printer control

* To control an individual printer, simply click on the card that corresponds to it, and you will notice that the name in the top bar changes to the name of that printer. You can now send commands to it individually, even if it is part of a group.
* If you send a command to an individual printer that takes some time (such as homing) and then send a command to the group it belongs to, the second command will be ignored if the first one is still busy.
* To control an entire group, simply click on the card that corresponds to that group and you will notice that the name in the top bar changes to the name of the group and the name of the host, separated by a forward slash. You can now send commands to the group leader and the other printers in the group will follow.

<img src={require('@site/docs/panda-series/panda-touch/img/add_group_ok.png').default} alt="" width="600" />

### Precautions for printing from USB

Please note the following points when attempting to print from USB.

* Ensure that the file system of the USB flash drive is formatted as `FAT32`.
* Use the `Export All Disks` option to export `.3mf` files from Bambu Studio or Orca Slicer.

    <img src={require('@site/docs/panda-series/panda-touch/img/export_3mf.png').default} alt="" width="300" />

* Write the sliced `.3mf` file to the root directory of the USB storage device.

    * Panda Touch only supports files sliced on `Build Plate#1` of Bambu Studio.
    * Panda Touch only supports `.3mf` files, not `.gcode` files.
    * Panda Touch only supports reading files in the root directory, it does not support reading files in folders.

* Insert a USB storage device into Panda Touch and go to the `USB Storage Device` menu.

    <img src={require('@site/docs/panda-series/panda-touch/img/usb_flash_drive.png').default} alt="" width="600" />

### Start printing using one printer

* Click to select a file on a USB disk or SD card for printing.
* Set the print parameters. Depending on the printer, you may see:
    * `Heatbed leveling`.
    * `Flow Calibration` (`P1P` and `P1S` do not have this feature, so these printers will not show this option)
    * ``Time-lapse''
    * `Use AMS` (Panda Touch will automatically recognize if this printer has AMS plugged in and then determine if this option needs to be displayed)
    * `Auto Power Off` (Automatically recognizes the online Panda PWR and turns on the auto power off feature)
    * `Clear Power Usage` (Automatically recognizes the Panda PWR online and resets the power usage of the Panda PWR).

    <img src={require('@site/docs/panda-series/panda-touch/img/start_print_one.png').default} alt="" width="600" />

* Make sure that the `.3mf` file of the slice is compatible with the selected printer.
* If using AMS, make sure that the consumables in the AMS tray match the consumables in the sliced `.3mf` file, as consumables cannot be dynamically mapped at the start of printing.

* If you start printing from USB, the Panda Touch will begin uploading files from the USB flash drive to the root directory of the printer's MicroSD card. To avoid upload issues, make sure:
    1. a MicroSD card is inserted in the printer.
    2. the remaining capacity of the MicroSD card is sufficient to write the files to be uploaded.

    <img src={require('@site/docs/panda-series/panda-touch/img/uploading.png').default} alt="" width="600" />

* When uploading is complete, printing will begin. For very large `.3mf` files, the transfer to each printer may take several minutes.

* Once printing has started, Panda Touch will automatically jump to the main screen and display the printer data.

    <img src={require('@site/docs/panda-series/panda-touch/img/start_print_one_ing.png').default} alt="" width="600" />

### Group printing

* Group printing is supported only for files stored on USB disks.
* Click to select the files on the USB disk to be printed.
* Set the print parameters. Depending on the printers in the group, you may see
    * `Heatbed leveling`.
    * `Flow Calibration` (The `P1P` and `P1S` do not have this feature, so this option will not be displayed for these models.)
    * `Time lapse photography`.
    * `Use AMS` (The Panda Touch will automatically recognize if this printer has an AMS plugged in and then determine if this option needs to be displayed.)
    * `Auto Power Off` (Automatically recognizes a Panda PWR that is online, and turns on the Auto Power Off feature.)
    * `Clear Power Usage` (automatically recognizes the Panda PWR that is online, resets the power usage of the Panda PWR)

* Checkbox print options for a particular group will be based on the features available on the most powerful machine in the group. For example, if you are using a group that contains X1C\P1P\P1S, you will have the Lidar Scan option available, but this option will only be sent to printers in the group that support it.

    <img src={require('@site/docs/panda-series/panda-touch/img/start_print.png').default} alt="" width="600" />

* Panda Touch will generate a list of available printers for you to choose from.
* Printers and groups that are already busy will be excluded from this list. This means that if a single printer in a group is already busy, you will not be able to print to any of the printers in that group. This allows groups to always stay synchronized with each other.

* Make sure that the sliced `.3mf` file is compatible with the selected printer.
* If using AMS, make sure that the consumables in the AMS tray match the consumables in the sliced `.3mf` file, as it is not possible to dynamically map consumables at the start of printing.

* If using AMS, make sure that the consumables in the AMS tray match the consumables in the sliced `.3mf` file, as it is not possible to dynamically transfer them.The Panda Touch will begin uploading files from the USB flash drive to the root directory of the printer's MicroSD card. To avoid upload issues, make sure that you plot supplies at the start of printing:.
    1. a MicroSD card is inserted in the printer.
    2. the remaining capacity of the MicroSD card is sufficient to write the files to be uploaded.

    <img src={require('@site/docs/panda-series/panda-touch/img/udisk_upload.png').default} alt="" width="600" />


* When uploading is complete, printing will begin. For very large `.3mf' files, transfer to each printer may take several minutes.

    <img src={require('@site/docs/panda-series/panda-touch/img/group_printing.png').default} alt="" width="600" />

* After you start printing, you will be taken to the Print Summary page where the status of each printer in the group is summarized on a separate card.

### Group Printing Description

When a group is selected and multiple printers in the group are busy printing, the Panda Touch displays the `Multiple Printing` menu as shown below.

<img src={require('@site/docs/panda-series/panda-touch/img/multi_printing.png').default} alt="" width="600" />

The following groups of controls exist in this menu:

1. turns on/off the chamber LEDs for the printers in the current print list.
2. stops all print jobs in the current print list.
3. pauses/resumes all print jobs in the current print list.

### Group Print Setup Delay

The delay is based on this time during group printing, so that if the current printer heats up or the time is up, the print job is sent to the next one.

<img src={require('@site/docs/panda-series/panda-touch/img/group_delay.png').default} alt="" width="600" />
