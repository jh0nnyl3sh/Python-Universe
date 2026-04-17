import asyncio
import aiohttp
import time

# Aynı anda maksimum kaç Request atılacağını belirler.
CONCURRENCY_LIMIT = 5