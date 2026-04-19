import asyncio
import aiohttp
import time

# Gişedeki bilet sayısı. Aynı anda maksimum kaç Request atılacağını belirler.
CONCURRENCY_LIMIT = 5

async def fetch_url(session, url, semaphore, task_id):
    # Task buraya geldiğinde Semaphore'dan boş bir bilet (slot) bekler.
    # Eğer 5 bilet de doluysa, kod burada pause edilir (Non-blocking).
    async with semaphore:
        try:
            # 10 saniyelik Timeout ekliyoruz. Asılı kalan Request'ler sistemi tıkamasın.
            async with session.get(url, timeout=10) as response:
                status = response.status
                print(f"[Task {task_id}] {url} -> Status: {status}")
        except Exception as e:
            print(f"[Task {task_id}] {url} -> Error: {e}")

async def main():
    # Test için 5 URL'lik bir listeyi 4 ile çarpıp 20 elemanlı bir hedef listesi yaratıyoruz.
    urls = [
        "https://github.com",
        "https://google.com",
        "https://vodafone.com",
        "https://hackerone.com",
        "https://bugcrowd.com"
    ] * 4 

    # Semaphore objesini limitimizle başlatıyoruz.
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    # aiohttp ile tek bir ClientSession açıyoruz. (Connection Pooling için kritik).
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for i, url in enumerate(urls):
            # Her bir URL için bir Task oluşturup listeye ekliyoruz.
            task = asyncio.create_task(fetch_url(session, url, semaphore, i + 1))
            tasks.append(task)
        
        # Tüm Task'leri Event Loop'a fırlatıyoruz. 
        # Hepsi aynı anda yola çıkıyor ama Semaphore onlara gişede dur diyecek.
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    
    # Event Loop'u başlatıyoruz.
    asyncio.run(main())
    
    print(f"\n--- Toplam Süre: {time.time() - start_time:.2f} saniye ---")