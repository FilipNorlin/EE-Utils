# EE-Utils

A collection of reusable electrical engineering utilities and mathematical tools written in Python.

The goal of **EE-Utils** is to provide accurate, easy-to-use implementations of common electrical engineering equations and calculations that can be reused across projects instead of being rewritten every time.

---

## Features

Current modules include:

* 🌡️ **NTC Thermistors**

  * Steinhart–Hart equation
  * Temperature ↔ Resistance conversion
  * Beta equation
  * Resistance interpolation

More utilities are planned, including:

* 🔌 Voltage divider calculations
* ⚡ Ohm's Law
* 📈 RC, RL and RLC filter equations
* 🎚️ Op-amp gain calculations
* 🔋 Battery calculations
* 🔥 Power dissipation
* 🧲 Inductor calculations
* 🧮 Unit conversions
* 📊 Electrical constants and helper functions

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<username>/EE-Utils.git
```

or install locally:

```bash
pip install -e .
```

---

## Example

```python
from ee_utils.ntc import NTC

ntc = NTC(
    r25=10000,
    beta=3950
)

temperature = ntc.temperature_from_resistance(5230)
print(f"{temperature:.2f} °C")

resistance = ntc.resistance_from_temperature(50)
print(f"{resistance:.0f} Ω")
```

---

## Project Structure

```
EE-Utils/
│
├── ee_utils/
│   ├── ntc.py
│   ├── filters.py
│   ├── resistors.py
│   ├── converters.py
│   └── ...
│
├── examples/
├── tests/
├── README.md
└── pyproject.toml
```

---

## Philosophy

Electrical engineering projects often require the same equations and calculations repeatedly. This library aims to collect them in one well-tested, documented, and reusable package.

The focus is on:

* Readability
* Accuracy
* Reusability
* Minimal dependencies
* Well-documented code

---

## Contributing

Contributions are welcome.

If you'd like to add a new electrical engineering utility or improve an existing one, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.
