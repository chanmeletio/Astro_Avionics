# Contributing to Astro Avionics

Thank you for contributing to the Astro at Baylor High Power Rocketry Avionics subsystem for IREC 2027! To maintain mission reliability and safety, all contributors must adhere to the following engineering standards.

---

## 1. Git Branching Strategy

We follow a structured branching model:
* `main`: Flight-certified code and manufactured hardware releases. Direct commits are strictly prohibited.
* `develop`: Integration branch for tested features and hardware revisions.
* Feature & Fix branches:
  * `feat/<subsystem>-<description>`: e.g., `feat/driver-bmi088`, `feat/telemetry-framing`
  * `fix/<subsystem>-<description>`: e.g., `fix/pyro-timer-overflow`
  * `hw/<board>-<description>`: e.g., `hw/rev-a-usb-esd-protection`
  * `docs/<topic>`: e.g., `docs/state-machine-update`

---

## 2. Hardware Engineering Guidelines (KiCad v10)

Before opening any hardware pull request:
1. **KiCad Version**: Designs must be edited and saved using **KiCad v10** (or compatible nightly build).
2. **Schematic Rules**:
   - Every net crossing hierarchical sheets must use proper hierarchical labels.
   - All components must have complete, valid manufacturer part numbers (MPNs) and footprint associations.
   - Run `ERC` (Electrical Rules Check) and ensure **zero errors** and **zero warnings** without justified documentation.
3. **Layout & PCB Rules**:
   - Run `DRC` (Design Rules Check) against [`hardware/drc/default.kicad_dru`](hardware/drc/default.kicad_dru).
   - Ensure **zero unrouted nets** and **zero clearance violations**.
   - Verify ground plane stitching and high-current traces (pyro channels, buck converter inductors) meet thermal and current capacity rules.

---

## 3. Firmware Coding Standards (STM32 / Embedded C)

1. **Language Standard**: C11 / C++17.
2. **Formatting**: Format code using `clang-format` before committing.
3. **Static Analysis**: Verify changes locally with `cppcheck` or your IDE's static analyzer.
4. **Safety Critical Rules**:
   - **No dynamic memory allocation (`malloc`, `free`)** after system initialization / RTOS scheduler start.
   - Always verify sensor return codes and timeouts on I2C/SPI transactions.
   - Never block in interrupt service routines (ISRs); defer work to FreeRTOS tasks or task notifications.

---

## 4. Pull Request & Review Process

1. Open a pull request against `develop`.
2. Fill out all sections of the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md).
3. Ensure all automated GitHub Actions CI checks pass:
   - `Hardware DRC & Verification (KiCad v10)`
   - `Firmware Build & Verification`
   - `Firmware Code Quality & Static Analysis`
4. Obtain at least **one approved review** from the Avionics Lead or designated subsystem lead before merging.
