# 🛡️ Day 93: FastAPI & Pydantic Data Validation

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This project demonstrates how to handle incoming `HTTP POST Request` payloads safely using the `Pydantic` library within the `FastAPI` framework.

### 🧠 Core Concepts Demonstrated
* **Pydantic Models:** Creating robust `DTO (Data Transfer Object)` equivalents in Python using `BaseModel` to ensure strict `Data Validation`.
* **POST Endpoints:** Setting up routes designed to receive, validate, and process incoming `JSON` payloads.
* **Automatic Error Handling:** Observing how `FastAPI` automatically intercepts invalid `Request` payloads and returns standardized `422 Unprocessable Entity` errors before the main logic executes.
* **Swagger UI:** Utilizing the auto-generated, interactive API documentation (at `/docs`) for seamless testing without external tools like Postman.

### 📂 File Structure
* `main.py`: Contains the `FastAPI` application instance, the `Pydantic` model (`DosyaTalebi`), and the routing logic.

### 🚀 Usage

Install the required dependencies:
```bash
pip install fastapi uvicorn pydantic

Run the local ASGI Server:
```bash
uvicorn main:app --reload