# Day 63: The Mass Intel Harvester (Micro-ETL Pipeline) 🚀

## Overview
This project is a Micro-ETL (Extract, Transform, Load) pipeline built with Python. It automates the process of fetching live user data from an external REST API, parsing the complex JSON response, transforming the data into a clean structure, and securely loading it into a local CSV file.

## Features
* **Extract:** Utilizes the `requests` library to establish a secure connection and fetch live `JSON` data from a target API.
* **Transform:** Iterates through the raw data using a `for` loop, extracting deeply nested specific values (Name, Email, City) and structuring them into a clean `List` of `Dictionary` objects.
* **Load:** Employs the `csv.DictWriter` module for secure *File I/O* operations, automatically generating headers and writing the parsed dataset into `target_intel.csv`.

## Technologies Used
* Python 3.x
* `requests` Module
* `csv` Module
* JSON Parsing
* File I/O Operations

## How to Run
1. Ensure your `venv` is active.
2. Install dependencies: `pip install requests`
3. Execute the script: `python main.py`
4. The script will generate a `target_intel.csv` file in the root directory containing the harvested intelligence.