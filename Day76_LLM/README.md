# AI-Powered Audit Data Extractor

## 📌 Overview
This project demonstrates an industry-standard `Pipeline` for extracting structured financial data from unstructured, messy audit logs using Large Language Models (LLMs). It effectively eliminates the "hallucination" risk of AI by enforcing strict `Data Validation` rules before any data reaches the `Database`.

Instead of letting the AI generate unstructured `Spaghetti Code` or free-text responses, this tool imposes a strict `Architecture` using **Pydantic**, ensuring that the extracted data strictly adheres to predefined `Type Hinting` rules (e.g., forcing financial amounts to be `Float` and compliance status to be `Boolean`).

## ⚙️ Architecture & Technologies
* **Python 3.x**
* **Google GenAI SDK:** For accessing high-performance LLMs (`gemini-2.5-flash` / `gemini-3.1-pro-preview`).
* **Pydantic:** Acting as the strict gatekeeper for `Data Validation` and schema enforcement.

## 🚀 Features
* **Structured Output generation:** Converts complex `Independent Audit` texts into clean `JSON` objects.
* **Zero-Tolerance Validation:** Automatically raises a `ValidationError` (`Exception`) if the LLM attempts to return invalid data types.
* **Domain-Specific:** Tailored specifically for `Compliance`, financial analysis, and audit workflows.

## 🛠️ Installation & Setup

1. Clone the `Repository` and navigate to the directory:
   ```bash
   git clone <your-repo-url>
   cd Day76_LLM