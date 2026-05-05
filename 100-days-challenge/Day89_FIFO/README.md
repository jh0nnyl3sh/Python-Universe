# ⏳ Day 89: Task Scheduler (Queue & FIFO Architecture)

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This script demonstrates the Queue data structure and FIFO (First In, First Out) methodology using Python's optimized `collections.deque` module.

This project focuses on building high-performance task scheduling mechanisms, a core concept in operating systems and backend architectures.

### 🧠 Core Concepts Demonstrated
* **Queue Architecture:** Implementing a robust queuing system for background tasks.
* **FIFO (First In, First Out):** Ensuring tasks are processed in the exact order they arrive.
* **collections.deque:** Utilizing Double-Ended Queues for maximum performance.
* **Time Complexity Optimization:** Using `.popleft()` for `Dequeue` operations to achieve **O(1)** time complexity, avoiding the heavy **O(n)** memory shifting of standard `List` objects.

### 📂 File Structure
* `main.py`: Contains the core logic, including `Enqueue` (`.append()`) and `Dequeue` (`.popleft()`) operations simulating a realistic task scheduler.

### 🚀 Usage

Execute the main script from your terminal:
```bash
python main.py