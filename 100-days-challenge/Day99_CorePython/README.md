# 🏗️ Day 99: Object-Oriented Programming (OOP) Refactoring

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This phase transforms a procedural data-parsing script into a robust, reusable Object-Oriented module.

### 🧠 Core Concepts Demonstrated
* **Encapsulation:** Grouping related state (`target_dir`, `classified_data`) and behavior (`process_directory`, `export_report`) into a single cohesive `Class`.
* **Constructors (`__init__`):** Dynamically initializing object instances with specific configurations (directories, file names) at runtime.
* **Internal Routing (`self`):** Properly accessing internal class methods and properties using the `self` keyword, replacing global variables.
* **Modularity:** Creating a structure that can be easily imported and consumed by other Python applications or external API triggers.

### 📂 File Structure
* `main.py`: Contains the `DocumentClassifier` class and the instantiation logic.
* `raw_data/`: Dummy data for testing.
* `system.log`: Runtime audit logs (Ignored by Git).
* `classification_report.json`: Parsed output data (Ignored by Git).

### 🚀 Usage

Run the script:
```bash
python main.py