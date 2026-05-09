# 🌐 Day 92: Introduction to Web APIs with FastAPI

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This project marks the transition from standard console applications to Web-based API development using Python's modern `FastAPI` framework.

### 🧠 Core Concepts Demonstrated
* **REST API Fundamentals:** Setting up a basic web server that responds to HTTP GET requests.
* **FastAPI Framework:** Initializing an API instance and defining routing decorators (`@app.get`).
* **Uvicorn ASGI Server:** Running a local server to host the API and dynamically reloading it during development.
* **Path Parameters:** Extracting dynamic variables from the URL endpoint (e.g., `/dosya/{dosya_id}`) and returning them within a structured JSON response.

### 🚀 Usage

Install the required dependencies:
```bash
pip install fastapi uvicorn


Run the local server:
```bash
uvicorn main:app --reload


📊 Expected Endpoints & JSON Output
GET / -> {"status": "success", "message": "FastAPI sunucusu basariyla calisiyor!"}

GET /dosya/1453 -> {"dosya_numarasi": 1453, "islem_durumu": "Beklemede", "aciklama": "1453 numarali dosya kuyruga alindi."}