---
sidebar_position: 1
description: PyroGrip Series Build Plates
---

# PyroGrip Build Plates

<div class="div-table">

<ImageView src={require('@site/docs/accessories-docs/build-plate/pyrogrip/img/product.webp').default} width="30%" class="right-image"/>

## Product Overview

**The PyroGrip** Build Plate is a premium PEI-coated spring steel plate for serious 3D printing enthusiasts who demand consistency and performance. Designed to operate within your filament's recommended temperature range, it delivers dependable first-layer adhesion and effortless model release once the plate cools. Built on a flexible stainless spring steel core and finished with a durable, powder-coated golden PEI surface, PyroGrip combines strength, longevity, and ease of use—giving you a more reliable and refined printing experience from start to finish.

</div>

## Specifications & Compatibility

Supported Printer Models

| Print Area        | Compatible Models |
| ----------------- | ----------------- |
| **180mm × 180mm** | [`Bambu Lab A1 mini`](https://biqu.equipment/collections/all-products/products/biqu-panda-buildplate-cryogrip-pro)                                                                                                                     |
| **256mm × 256mm** | [`Bambu Lab A1` `Bambu Lab P1P` `Bambu Lab P1S` `Bambu Lab X1C` `Bambu Lab X1E` `Bambu Lab X2D`](https://biqu.equipment/collections/all-products/products/biqu-panda-buildplate-cryogrip-pro)                                                                              |
| **330mm × 320mm** | [`Bambu Lab H2C`](https://biqu.equipment/products/biqu-panda-buildplate-cryogrip-pro?_pos=3&_sid=e99b2e229&_ss=r&variant=42381362462818)                                                                                                                         |
| **350mm × 320mm** | [`Bambu Lab H2D Pro` `Bambu Lab H2D` `Bambu Lab H2S`](https://biqu.equipment/collections/all-products/products/biqu-panda-buildplate-cryogrip-pro) |

## PyroGrip | Stick It to the Heat.

**The PyroGrip** build plates are produced by powder-coating a PEI layer onto a stainless spring steel substrate and curing it to form a durable, mechanically bonded surface. The textured PEI surface features a controlled roughness profile that enhances first-layer adhesion through improved mechanical interlocking. This texture is also transferred to the bottom surface of printed parts. Textured PEI plates are compatible with a wide range of filaments and, in most cases, provide strong adhesion without the need for additional adhesives. The powder-coated PEI layer offers high wear resistance and long-term durability under repeated thermal cycling.

**Textured PEI vs. mooth PEI**: Smooth PEI plates are produced by laminating a PEI film onto a spring steel sheet using high-temperature-resistant 3M adhesive. They provide a flat, smooth bottom surface and are ideal for applications that require high surface flatness. For Bambu Lab `A1 mini`, `A1`, `P1P`, `P1S`, `X1C`, and `X1E` models, PyroGrip offers dual-sided options featuring one smooth PEI surface and one textured PEI surface.

- **Hot Grip, Cold Release**: Provides strong adhesion at printing temperatures and enables effortless model removal once cooled.

    <ImageView src={require('./img/rl.webp').default} width="50%"/>

- **Pre-Printed QR Code**: Factory-printed QR codes are included on compatible versions to prevent build plate recognition errors during printing.

    <ImageView src={require('@site/docs/accessories-docs/build-plate/pyrogrip/img/erweima.webp').default} width="50%"/>

- **50mm Printed Grid**: A 50mm × 50mm grid is printed on the surface to assist with alignment and measurement.

    <ImageView src={require('./img/wangge.webp').default} width="50%"/>

- **Textured Surface Finish**: Compared to standard PEI plates, PyroGrip produces a finer bottom-layer texture, improving overall print aesthetics and design consistency.

    <ImageView src={require('./img/wenli.webp').default} width="100%"/>

## QR Code Recognition (Bambu Lab Models)

Currently, only X1C, P2S, and H2 series printers support QR code detection during the printing process. If detection issues occur, you may disable Build Plate Detection feature in the printer settings to proceed with the print.

You may submit a request through the community forum. Feedback is reviewed regularly to prioritize and accelerate compatibility development for additional models.

- **X1C**: Current PyroGrip plates include a compatible QR code to ensure proper recognition.

- **P2S**: Current PyroGrip plates do not yet support build plate detection. Compatibility is under development. Users may print community-developed adapters from open-source resources

- **H2 series**: PyroGrip plates include factory-positioned QR codes to ensure proper recognition.

## Troubleshooting & Special Notes

### Print Quality Does Not Match Expectations

- **Clean the Build Surface**: Clean the build plate regularly using soapy water to remove debris, glue residue, and skin oils. Even small amounts of oil from your hands can significantly reduce adhesion.

- **Plate Designated Wiping Area**: Before each print job, the printer performs an automatic nozzle-cleaning routine consisting of two stages: **Coarse Wipe**: Removes accumulated filament residue from the heated nozzle. **Fine Wipe**: Cleans the nozzle tip to ensure a smooth, contamination-free contact surface. During the fine wipe stage, the nozzle makes light downward contact with a designated area of the build plate, typically moving approximately 1-2mm. Localized surface wear in this wiping area is normal due to repeated mechanical contact. This wear does not affect adhesion performance or compromise the structural integrity of the build plate.

- **Slightly Increase Bed Temperature**:

    - Bed temperature has a significant impact on adhesion. Higher temperatures increase the bonding strength between the filament and the textured PEI surface. If adhesion is insufficient, try increasing the bed temperature slightly.

    - **Note:** Excessively high bed temperatures may cause nozzle clogging or noticeable elephant's foot effects with certain filaments.

- **Use Brims and Supports When Needed**: Tall, slender models are more likely to be knocked over during high-speed printing. Adding brims or appropriate support structures can improve stability and reduce the risk of detachment.

- **Check Bed Temperature and Filament Type**: Most filaments come with preset temperature profiles in slicing software. If you are using custom profiles, verify that the bed temperature is set correctly. Adjust temperatures according to the specific filament and its material properties.

- **Optimize First-Layer Settings**: To improve adhesion, first-layer settings can be adjusted in the slicing software. Although most slicer profiles are preconfigured with validated baseline parameters, manual tuning may be necessary if adhesion issues occur. **Recommended starting point:**First-layer line width: **0.5mm**, height: **0.25mm**. These settings help create a stronger first layer and improve overall print success rates.
