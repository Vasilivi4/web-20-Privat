import aiohttp
import asyncio


async def fetch_exchange_rates(days):
    async with aiohttp.ClientSession() as session:
        data = []
        for day in range(1, days + 1):
            async with session.get(
                f"https://api.privatbank.ua/p24api/exchange_rates?json&date=0{day}.03.2024"
            ) as response:
                response_json = await response.json()
                data.append(response_json)
        return data
