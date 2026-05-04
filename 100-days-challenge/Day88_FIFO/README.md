# ⏳ Day 88: Task Scheduler (Queue / FIFO Architecture)

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This script demonstrates the Queue data structure and FIFO (First In, First Out) methodology using Python's optimized `collections.deque` module.

This project focuses on building high-performance task scheduling mechanisms, a core concept in operating systems and backend architectures.

### 🧠 Core Concepts
* **Queue Architecture:** Implementing a robust queuing system for background tasks.
* **FIFO (First In, First Out):** Ensuring tasks are processed in the exact order they arrive.
* **collections.deque:** Utilizing Double-Ended Queues for maximum performance during `append` and `popleft` operations, avoiding the heavy memory shifting of standard `List` objects.

### 🚀 Current State (Part 1)
Currently, the script successfully initializes the `Queue` and performs `Enqueue` operations (adding tasks to the queue). The `Dequeue` (processing) operations are scheduled for the next update.

### ⚙️ Usage
```bash
python task_scheduler.py