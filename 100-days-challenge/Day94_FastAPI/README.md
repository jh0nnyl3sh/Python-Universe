# ⚙️ Day 94: Full CRUD Operations in FastAPI

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This project completes the foundational lifecycle of a Web API by implementing a full CRUD (Create, Read, Update, Delete) architecture using an in-memory data store.

### 🧠 Core Concepts Demonstrated
* **CRUD Lifecycle:** Successfully mapping HTTP methods to data operations:
  * `POST` -> Create
  * `GET` -> Read
  * `PUT` -> Update
  * `DELETE` -> Delete
* **HTTP Exception Handling:** Using FastAPI's `HTTPException` to return appropriate status codes (`400 Bad Request`, `404 Not Found`) when constraints are violated.
* **In-Memory State:** Utilizing a Python Dictionary as a temporary, volatile database to test routing and logic without the overhead of an actual database connection.

### 📂 File Structure
* `main.py`: Contains the complete API architecture including the Pydantic data model and all four operational endpoints.

### 🚀 Usage

Run the local server:
```bash
uvicorn main:app --reload