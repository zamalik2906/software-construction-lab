<div align="center">

# 🛠️ Software Construction Lab

**A continuously improving Python project built lab by lab for the _Software Construction & Development_ course.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)
![Linter](https://img.shields.io/badge/linter-ruff-D7FF64?logo=ruff&logoColor=black)
![Types](https://img.shields.io/badge/types-mypy-2A6DB2)
![Status](https://img.shields.io/badge/status-in%20progress-orange)

</div>

---

## 📖 About

This repository holds my work for **Software Construction & Development** at **Sir Syed CASE Institute of Technology, Islamabad**.

Every lab in the semester extends the same codebase, so the project grows step by step: from a simple setup, to clean and readable code, and onwards. The focus is not only on making code _work_, but on making it **readable, testable and easy to change**.

## ✨ What's Inside

| Module          | Description                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| `src/hello.py`  | A small, fully typed `greet()` function used to verify the toolchain (Lab 1)                                   |
| `src/orders.py` | Order-total calculation refactored into small functions with clear names, guard clauses and type hints (Lab 2) |
| `tests/`        | Automated tests written with **pytest**                                                                        |

## 🧰 Tech Stack

- **Python 3.12**: language
- **pytest**: unit testing
- **ruff**: linting
- **mypy**: static type checking
- **Git and GitHub**: version control
- **Visual Studio Code**: editor

## 📁 Project Structure

```text
software-construction-lab/
├── src/
│   ├── hello.py          # Lab 1: greet() function
│   └── orders.py         # Lab 2: refactored order processing
├── tests/
│   ├── test_hello.py     # Tests for hello.py
│   └── test_orders.py    # Tests for orders.py
├── .gitignore            # Keeps .venv out of version control
├── requirements.txt      # Project dependencies
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/software-construction-lab.git
cd software-construction-lab
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## 💻 Usage

Run these from the project root, inside the virtual environment.

**Greeting (Lab 1)**

```python
>>> from src.hello import greet
>>> greet("World")
'Hello, World!'
```

**Order total (Lab 2)**

```python
>>> from src.orders import calculate_order_total
>>> order = {
...     "items": [
...         {"price": 25.0, "qty": 2},
...         {"price": 40.0, "qty": 1},
...         {"price": -5.0, "qty": 3},   # ignored: invalid price
...     ],
...     "member": True,
...     "country": "PK",
... }
>>> calculate_order_total(order)
86.0
```

> 💡 The total is `subtotal (90.0) − member discount (9.0) + shipping (5.0) = 86.0`.

## ✅ Code Quality Checks

| Purpose               | Command            |
| --------------------- | ------------------ |
| Run all tests         | `python -m pytest` |
| Lint the code         | `ruff check .`     |
| Type-check the source | `mypy src/`        |

Run all three before every commit to keep the codebase clean.

## 🗺️ Lab Progress

| Lab    | Topic                                                                                 | Status      |
| ------ | ------------------------------------------------------------------------------------- | ----------- |
| Lab 1  | Development environment: Python, Git, GitHub, virtual environment, ruff, mypy, pytest | ✅ Done     |
| Lab 2  | Naming, function design and decomposition (refactoring)                               | ✅ Done     |
| Lab 3+ | Coming soon                                                                           | ⏳ Upcoming |

## 🧠 Key Concepts Practised

- **Meaningful naming**: `snake_case`, descriptive nouns for data and verb phrases for functions
- **Extract Function**: splitting one long function into small, single-purpose functions
- **Guard clauses**: returning early instead of nesting `if`/`else` chains
- **Type hints**: every parameter and return value is typed and verified with `mypy`
- **Refactoring safely**: changing structure without changing behaviour, backed by a test

## 📚 References

- Fowler, M. _Refactoring: Improving the Design of Existing Code_
- McConnell, S. _Code Complete_, Chapter 11

## 👤 Author

**Zeeshan Ahmed Malik**
Computer Science student, Sir Syed CASE Institute of Technology, Islamabad

---

<div align="center">

⭐ _Built one lab at a time._

</div>
