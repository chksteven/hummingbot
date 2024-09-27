import asyncio

class DAAPIThrottler:
    def __init__(self, rate_limit=10):
        self.rate_limit = rate_limit
        self.semaphore = asyncio.Semaphore(rate_limit)

    async def throttle(self):
        async with self.semaphore:
            await asyncio.sleep(1)
