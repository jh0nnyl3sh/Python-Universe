import asyncio
import aiohttp
import time

# Fonksiyonun başına 'async' koyarak bunun bir 'Coroutine' olduğunu belirtiyoruz.
async def get_status(session, url):
    # 'await' diyerek Event Loop'a "Cevap gelene kadar sen git başka işlere bak" diyoruz (Non-blocking)
    async with session.get(url) as response:
        print(f"{url} - Status: {response.status}")

async def main():
    urls = ["https://google.com", "https://github.com", "https://vodafone.com"]
    
    async with aiohttp.ClientSession() as session:
        # Tüm task'leri hazırlıyoruz
        tasks = []
        for u in urls:
            tasks.append(get_status(session, u))
        
        # Event Loop'a tüm task'leri aynı anda ateşlemesini söylüyoruz
        await asyncio.gather(*tasks)

start = time.time()
# Programı Event Loop üzerinden başlatıyoruz
asyncio.run(main())
print(f"Geçen süre: {time.time() - start} saniye")