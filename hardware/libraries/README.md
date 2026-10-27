# Hardware Custom Component Libraries

Contains project-specific, version-controlled schematic symbols, footprints, and 3D mechanical models.

## Structure:
- `symbols/`: Custom `.kicad_sym` symbol libraries (e.g., STM32F405 breakout, SX1262 LoRa module, MS5611).
- `footprints/`: Custom footprint libraries (`astro_avionics.pretty/`) with verified solder pads.
- `3d_models/`: STEP (`.step` / `.stp`) and VRML (`.wrl`) models mapped to footprints for 3D CAD clearance checks in rocket airframe bays.
