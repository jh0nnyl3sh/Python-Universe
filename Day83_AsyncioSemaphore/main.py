import asyncio
import aiohttp
import time

# Aynı anda maksimum kaç Request atılacağını belirler.
CONCURRENCY_LIMIT = 5

async def fetch_url(session, url, semaphore, task_id):
    # Task buraya geldiğinde Semaphore'dan boş bir slot bekler.
    # Eğer 5 slot da doluysa, kod burada pause edilir.
    async with semaphore:
        try:
            # 10 saniyelik Timeout ekliyoruz. Asılı kalan requestler sistemi tıkamasın
            async with session.get(url, timeout=10) as response:
                status = response.status
                print(f"[Task {task_id}] {url} -> Status: {status}")
        except Exception as e:
            print(f"[Task {task_id}] {url} -> Error: {e}")
            