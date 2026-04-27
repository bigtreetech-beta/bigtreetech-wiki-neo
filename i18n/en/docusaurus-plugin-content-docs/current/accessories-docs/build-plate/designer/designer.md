---
sidebar_position: 1
description: Designer Series Build Plates
---

# Designer Series Build Plate

<div class="div-table">

<ImageView src={require('@site/docs/accessories-docs/build-plate/designer/img/product.webp').default} width="40%" class="right-image"/>

## Product Overview

The **Designer Series** Build Plate is specifically engineered for PLA, PETG, and TPU filaments. It transfers distinctive surface textures directly onto the first layer of your 3D printed models, creating a refined decorative finish right out of the box - no additional setup or special parameter adjustments required. **The Designer Series** is available in multiple patterns: Carbon Fiber Surface,  Diamond Surface, Honeycomb Surface, Houndstooth Surface.

</div>

## Specifications & Compatibility

Supported Printer Models

| Print Area        | Compatible Models |
| ----------------- | ----------------- |
| **180mm × 180mm** | [`Bambu Lab A1 mini（Carbon Fiber & Diamond Surfaces available）`](https://biqu.equipment/collections/all-products/products/biqu-panda-buildplate-cryogrip-pro)                                                                                  |
| **256mm × 256mm** | [`Bambu Lab A1` `Bambu Lab P1P` `Bambu Lab P1S` `Bambu Lab P2S` `Bambu Lab X1C` `Bambu Lab X1E` `Bambu Lab X2D`](https://biqu.equipment/collections/all-products/products/biqu-panda-buildplate-cryogrip-pro)                                                            |
| **350mm × 320mm** | [`Bambu Lab H2D Pro` `Bambu Lab H2D` `Bambu Lab H2S`](https://biqu.equipment/collections/all-products/products/biqu-panda-buildplate-cryogrip-pro) |

## Designer Series

:::warning[Service Life and Care]

The transfer film is a consumable item. To extend the life of the transferred texture, periodically vary the print position of your models on the build plate. Use the scraper carefully to avoid damaging the film surface.

:::

The **Designer Series** uses precision laser processing to create fine optical micro-textures on a specialized transfer film. This film is then bonded to a custom spring steel substrate using a high-temperature-resistant adhesive system. The engineered surface creates controlled optical effects, including enhanced light reflection and diffraction. During printing, molten plastic flows into these micro-structured patterns and replicates the design onto the bottom layer of your model. When viewed under different lighting conditions, the first layer displays dynamic visual effects and surprising depth - turning the bottom of your prints into a feature, not an afterthought.

- **Hot Grip, Cold Release**: Provides strong adhesion at printing temperatures and enables effortless model removal once cooled.

    <ImageView src={require('./img/diwen.webp').default} width="30%"/>

- **Unique Textures**: Print with PLA, PETG, TPU, and more to create striking surface finishes on the bottom layer - such as carbon fiber or diamond patterns - that instantly give your print a more refined, premium look.

    <ImageView src={require('./img/zuanshi.webp').default} width="30%"/>

    <ImageView src={require('./img/carbon.webp').default} width="30%"/>

## QR Code Recognition (Bambu Lab Models)

Currently, only X1C, P2S, and H2 series printers support QR code recognition during printing. If you encounter recognition issues, you can disable build plate detection in your printer settings.

You may submit a request through the community forum. Feedback is reviewed regularly to prioritize and accelerate compatibility development for additional models.

- **X1C**: Current Designer Series plates include an X1C-compatible QR code in the correct position to ensure proper recognition.

- **P2S**: Designer Series plates do not currently support recognition with Build Plate Detection enabled. Compatibility updates are under development. Users may also print community-developed adapter models if needed.

## Troubleshooting & Special Notes

- **Cleaning the Build Surface**: Clean your build plate regularly using soapy water to remove dust, glue residue, and skin oils. Even small amounts of oil from your fingers can significantly reduce adhesion.

- **Recommended Print Settings**: When using the Designer Series build plate: Set the build plate type to **Smooth PEI / High-Temperature Plate** in your slicer, and follow the recommended bed temperature settings.

- **Lidar Calibration Limitations**: Due to the reflective properties of the transfer film, printers with lidar-based calibration systems may have difficulty detecting the plate surface. **If calibration fails:** Skip the lidar calibration process, or Perform calibration using a standard build plate, then switch to the Designer Series plate for printing.
