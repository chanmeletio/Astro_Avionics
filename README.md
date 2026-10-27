# Astro at Baylor — Avionics Subsystem

[![Hardware DRC (KiCad v10)](https://github.com/chanmeletio/Astro_Avionics/actions/workflows/hardware-drc.yml/badge.svg)](https://github.com/chanmeletio/Astro_Avionics/actions/workflows/hardware-drc.yml)
[![Firmware Build](https://github.com/chanmeletio/Astro_Avionics/actions/workflows/firmware-build.yml/badge.svg)](https://github.com/chanmeletio/Astro_Avionics/actions/workflows/firmware-build.yml)
[![Firmware CI](https://github.com/chanmeletio/Astro_Avionics/actions/workflows/firmware-ci.yml/badge.svg)](https://github.com/chanmeletio/Astro_Avionics/actions/workflows/firmware-ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Flight computer, sensor acquisition, dual-deployment recovery actuation, and telemetry subsystem developed by **Astro at Baylor** for the **2027 Intercollegiate Rocket Engineering Competition (IREC)** at Spaceport America.

---

## Subsystem Architecture

```
Astro_Avionics/
├── .github/
│   ├── workflows/          # Automated CI/CD (KiCad v10 DRC/ERC, ARM GCC cross-compilation)
│   ├── ISSUE_TEMPLATE/     # Hardware ECO, firmware bug, and flight anomaly reports
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                   # Flight documentation, state machines, pinouts, and link budgets
├── firmware/
│   ├── app/                # Flight state machine, telemetry dispatcher, and mission logic
│   ├── bsp/                # Board Support Package for Astro Flight Computer
│   ├── cube/               # STM32CubeMX HAL initialization and CMSIS DSP libraries
│   ├── drivers/            # Sensor drivers (Baro, High-G & Low-G IMUs, GPS, Radio, MicroSD)
│   ├── mid/                # Middleware (ring buffers, comms framing, RTOS abstractions)
│   └── tests/              # Native host unit tests and simulation mocks
├── ground-station/         # Real-time telemetry receiver, packet decoder, and mission UI
├── hardware/
│   ├── drc/                # KiCad Design Rule constraints and automated DRC check scripts
│   ├── libraries/          # Custom team footprint, symbol, and 3D model libraries
│   └── rev_a/              # KiCad v10 Flight Controller schematics, layouts, and manufacturing outputs
└── sim/                    # Software-in-the-Loop (SITL) and Hardware-in-the-Loop (HIL) simulators
```

---

## Hardware Overview (Rev A)

The Astro Avionics Flight Controller is designed in **KiCad v10** to withstand high acceleration, vibration, and thermal environments typical of supersonic high-power rocket flights.

* **Primary Processing Unit**: STM32F405RGT6 (Arm Cortex-M4 with FPU @ 168 MHz)
* **Inertial Sensing**:
  * High-G Triaxial Accelerometer (high-velocity boost phase acquisition)
  * Low-G 6-DOF IMU (apogee detection, attitude estimation, and descent tracking)
* **Barometric Altimetry**: High-precision barometric pressure sensor for altitude & apogee determination
* **Recovery & Pyrotechnics**: Dual-deployment pyro firing channels (Drogue @ Apogee, Main @ configured AGL altitude) with hardware interlocks and live continuity sensing
* **Telemetry & RF**: Long-range transceiver for live flight telemetry packet transmission to the ground station
* **Non-Volatile Logging**: MicroSD card interface logging sensor telemetry at high rates

For complete design files, see [`hardware/rev_a/`](hardware/rev_a/).

---

## Toolchain & Developer Prerequisites

### 1. Hardware Engineering (KiCad EDA)
* **KiCad v10** (or compatible KiCad 10 nightly build)
* KiCad CLI (`kicad-cli`) installed on system PATH for running local DRC/ERC exports

### 2. Embedded Firmware
* **ARM Embedded Toolchain**: `arm-none-eabi-gcc` (v10+ recommended)
* **Build Systems**: `cmake` (v3.22+) and `ninja-build` or GNU `make`
* **Static Analysis**: `clang-format` and `cppcheck`
* **Flashing & Debugging**: ST-LINK / J-Link with `openocd` or STM32CubeProgrammer

### 3. Simulation & Ground Station
* **Python**: Python 3.10+ with `pip` and virtual environment support

---

## Quickstart Guide

### Building Firmware Locally
```bash
# Clone the repository
git clone https://github.com/chanmeletio/Astro_Avionics.git
cd Astro_Avionics

# Configure and build firmware
cmake -B firmware/build -S firmware -DCMAKE_TOOLCHAIN_FILE=cmake/arm-none-eabi.cmake -GNinja
cmake --build firmware/build
```

### Running Hardware DRC & ERC Headless
```bash
# Run KiCad Electrical Rules Check
kicad-cli sch erc --output hardware/rev_a/output/erc_report.json hardware/rev_a/New_Flight_Controller.kicad_sch

# Run KiCad Design Rules Check
kicad-cli pcb drc --output hardware/rev_a/output/drc_report.json hardware/rev_a/New_Flight_Controller.kicad_pcb

# Parse violations with gatekeeper script
python hardware/drc/drc-ci-check.py --drc hardware/rev_a/output/drc_report.json --erc hardware/rev_a/output/erc_report.json
```

---

## Safety Protocol & Mission Rules

> [!CAUTION]
> **Pyrotechnic Safety Interlock Rule**: No live e-matches or pyrotechnic charges may be connected to the flight computer in the laboratory without the physical arming key / safety shunt removed and verified with a multimeter. Live fire testing must strictly adhere to [`docs/safety_procedures.md`](docs/safety_procedures.md).

---

## Contributing & Development Workflow

1. Create a feature branch from `develop` (`feat/driver-bmi088`, `hw/rev-a-power-trace-update`).
2. Ensure DRC/ERC passes with zero errors before opening a pull request.
3. Submit a Pull Request targeting `develop` using the provided [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md).

## License

This project is licensed under the [MIT License](LICENSE).
