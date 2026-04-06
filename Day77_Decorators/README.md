# 🛡️ Day 77: Pythonic Security & Clean Architecture with Decorators

## 📌 Overview
This project demonstrates how to implement **Role-Based Access Control (RBAC)** and **Security Logging** using Python `Decorators`. 

Instead of writing repetitive `if/else` checks for user roles inside every single function (which leads to `Spaghetti Code`), this project utilizes a strict `Pythonic` approach. By wrapping core functions with a custom `@require_admin` decorator, we achieve a robust `Clean Architecture` where the `Business Logic` is completely isolated from security and logging layers.

## ⚙️ Architecture & Concepts
* **Advanced Python:** `Decorators`, `Higher-Order Functions`, `*args` and `**kwargs`.
* **Security:** `Role-Based Access Control (RBAC)` simulation.
* **Monitoring:** Automated `Logging` of both `GRANTED` and `DENIED` access attempts with timestamps into a local file (`security_logs.txt`).
* **Design Principles:** `DRY (Don't Repeat Yourself)` and `Separation of Concerns`.

## 🚀 How It Works
The system evaluates a simulated `current_user` dictionary. The `@require_admin` decorator acts as a strict gatekeeper:
1. It intercepts the function call and checks the `role` of the current user.
2. If the user is an `admin`, it executes the wrapped function and logs the successful access.
3. If the user lacks permissions, it blocks the execution, returns an `Access Denied` warning, and logs the unauthorized attempt.

### 💻 Code Example
```python
@require_admin
def delete_database_record(record_id):
    # Core Business Logic only. No security checks inside!
    print(f"🗑️ Record {record_id} deleted!")