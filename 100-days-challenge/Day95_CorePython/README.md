# 🔍 Day 95: Dynamic Entity Classification & File I/O

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This project focuses on `Core Python` capabilities, specifically moving away from unreliable `Folder Path` assumptions and instead dynamically classifying data based on internal `Keyword` analysis.

### 🧠 Core Concepts Demonstrated
* **File I/O Operations:** Using the `Context Manager` (`with open()`) to safely read files without causing memory leaks.
* **String Manipulation:** Standardizing raw text data using `.lower()` to ensure case-insensitive matching.
* **Dynamic Routing:** Implementing logic that classifies entities (e.g., "Judge" vs. "Prosecutor") strictly based on content `Keywords` rather than physical directory structures.
* **Exception Handling:** Wrapping the file reading process in a `try-except` block to gracefully handle missing files or read permission errors.

### 📂 File Structure
* `main.py`: The main script containing the classification logic.
* `raw_data/`: A dummy directory containing `.txt` files to simulate raw, unclassified data drops.

### 🚀 Usage

Run the script directly via terminal:
```bash
python main.py