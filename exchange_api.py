import aiohttp
import asyncio
from datetime import datetime, timedelta


async def fetch_exchange_rate(session, date):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date.strftime('%d.%m.%Y')}"
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Request failed for date {date}: {e}")
        return None


async def fetch_exchange_rates(days):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for day in range(1, days + 1):
            date = datetime(2024, 3, 1) + timedelta(days=day - 1)
            tasks.append(fetch_exchange_rate(session, date))

        results = await asyncio.gather(*tasks)
        return [result for result in results if result is not None]


days_to_fetch = 10
exchange_rates = asyncio.run(fetch_exchange_rates(days_to_fetch))
for rate in exchange_rates:
    print(rate)
