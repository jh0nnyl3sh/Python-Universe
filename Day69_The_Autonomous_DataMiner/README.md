# Day 69: The Autonomous DataMiner (Micro-ETL Object) ⛏️

## Overview
This project demonstrates the integration of Object-Oriented Programming (OOP) with external API requests and File I/O operations. The `DataMiner` class acts as an autonomous agent capable of extracting user data from a target REST API, parsing the JSON payload, and dynamically exporting the refined intelligence into a CSV file.

## Features
* **OOP Architecture:** Encapsulates data (`intel_data`) and capabilities within a reusable `DataMiner` class.
* **Extract & Transform:** Uses the `requests` module to fetch JSON data and strategically extracts specific nested attributes (Name, Email, City, Phone).
* **Dynamic Load:** Utilizes `csv.DictWriter` to export the in-memory data into a CSV file, accepting dynamic filenames to prevent hardcoding.

## Execution
Ensure your `venv` is active and dependencies are installed.
```bash
python main.py