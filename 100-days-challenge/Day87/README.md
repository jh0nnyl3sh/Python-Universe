# 🏢 Department Salary Calculator

This project contains a Python `function` designed to calculate the total salary expenses of a specific department within a company. It acts as a foundational exercise for data processing and core programming logic.

### 🧠 Core Python Concepts Demonstrated
* Iterating through a `List` of `Dictionary` objects.
* Reading and matching specific `keys` and `values` from a `Dictionary`.
* Managing variable `Scope` correctly within a `function`.
* Using the `return` statement to output calculated data securely.

### 📂 File Structure
* `employees.py`: Contains the raw dataset (a `List` of employee `Dictionaries`).
* `main.py`: Contains the core logic, the iteration `loop`, and the calculation `function`.

### 🚀 Usage

1. Ensure your `employees.py` file contains the dataset in the following structure:
```python
employees = [
    {"name": "Ali", "department": "IT", "salary": 5000},
    {"name": "Ayse", "department": "HR", "salary": 4500},
    {"name": "Veli", "department": "IT", "salary": 5500},
    {"name": "Fatma", "department": "Finance", "salary": 6000}
]
```

2. Execute the main script from your terminal:
```bash
python main.py
```

### 📊 Example Output
```text
[IT] department total salary expense: 10500
```