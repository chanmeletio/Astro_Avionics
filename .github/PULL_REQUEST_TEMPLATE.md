## Description of Changes
<!-- Provide a concise summary of the changes made in this pull request and the rationale behind them. -->

## Subsystem Impacted
- [ ] Hardware (KiCad EDA Schematic / Layout / DRC)
- [ ] Firmware (STM32 HAL / Drivers / App logic)
- [ ] Ground Station (Telemetry Decoder / UI)
- [ ] Simulation / HIL / SITL
- [ ] Documentation / Safety Protocol

## Engineering Verification Checklist

### For Hardware Changes (KiCad v10):
- [ ] KiCad ERC ran with **0 errors** on all hierarchical sheets.
- [ ] KiCad DRC ran with **0 violations** and **0 unconnected nets**.
- [ ] Netlist and pinout assignments match firmware pinout definitions in `docs/pinout.md`.
- [ ] Trace current capacities verified for high-current pyro firing circuits.
- [ ] Power budget checked against battery specifications in `docs/power_budget.xlsx`.
- [ ] Manufacturing files (Gerbers, Drill, PDF Schematics) generated and visually inspected.

### For Firmware Changes:
- [ ] Firmware builds cleanly with ARM GCC (`arm-none-eabi-gcc`) without errors or new warnings.
- [ ] Static analysis (`cppcheck` / `clang-format`) passes cleanly.
- [ ] Host unit tests pass (`ctest`).
- [ ] Flash and RAM footprint impact reviewed (`arm-none-eabi-size`).
- [ ] Bench tested on STM32 hardware or verified in simulation (`sim/`).

### Safety & Documentation:
- [ ] Safety protocols and arming interlocks preserved.
- [ ] Relevant documentation in `docs/` updated.

## Linked Issues
Fixes #<!-- issue number -->
