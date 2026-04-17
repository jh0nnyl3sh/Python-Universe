# Async-URL-Scanner-Pro

A high-performance, asynchronous URL status scanner built with Python's `asyncio` and `aiohttp`. Designed for security researchers and developers who need to perform large-scale reconnaissance without overwhelming network resources.

## 🏗 Architecture & Features

This tool is not just a simple script; it's built with modern architectural patterns:

- **Asynchronous I/O:** Utilizes `asyncio` and `aiohttp` for non-blocking network requests, allowing hundreds of tasks to run concurrently.
- **Concurrency Control (Semaphore):** Implements `asyncio.Semaphore` to limit concurrent connections. This prevents socket exhaustion and reduces the risk of being flagged by WAFs (Web Application Firewalls).
- **Connection Pooling:** Uses `aiohttp.ClientSession` for persistent TCP connections, significantly boosting performance.
- **Fault Tolerance:** Basic exception handling and timeout management for reliable execution in unstable network conditions.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual Environment (Recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/Async-URL-Scanner-Pro.git](https://github.com/YOUR_GITHUB_USERNAME/Async-URL-Scanner-Pro.git)
   cd Async-URL-Scanner-Pro