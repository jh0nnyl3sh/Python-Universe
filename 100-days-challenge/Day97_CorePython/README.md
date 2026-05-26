# 💾 Day 97: JSON Export & Persistent Storage

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This project demonstrates how to transition data from volatile memory (`RAM`) into persistent storage using standard data formats (`JSON`), enabling cross-system communication.

### 🧠 Core Concepts Demonstrated
* **Persistent Storage:** Moving grouped data from a Python `Dictionary` into a physical file on the disk.
* **JSON Serialization:** Using Python's built-in `json` module to convert native objects into universally readable `JSON` strings.
* **Data Formatting:** Utilizing the `indent=4` parameter within `json.dump()` to generate human-readable, beautifully structured output.
* **System Interoperability:** Creating a data export format that can be easily parsed by other backend systems (e.g., C# / .NET) or frontend interfaces.

### 📂 File Structure
* `main.py`: The script handling the parsing, grouping, and exporting logic.
* `raw_data/`: Directory containing raw `.txt` files.
* `classification_report.json`: The generated output file containing the structured data.

### 🚀 Usage

Run the script:
```bash
python main.py