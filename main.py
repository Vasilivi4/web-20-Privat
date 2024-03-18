import sys
import json
import asyncio
import argparse

from exchange_api import fetch_exchange_rates
from data_formatting import format_exchange_rates


async def main():
    parser = argparse.ArgumentParser(
        description="Fetch exchange rates from PrivatBank API"
    )
    parser.add_argument(
        "days", type=int, help="Number of days to fetch exchange rates for"
    )
    parser.add_argument(
        "currencies", nargs="*", default=[], help="Additional currencies to include"
    )
    args = parser.parse_args()

    days = args.days
    additional_currencies = args.currencies

    if days > 10:
        print("Error: You can only get exchange rates for up to 10 days.")
        return

    data = await fetch_exchange_rates(days)
    formatted_data = format_exchange_rates(data)
    print(json.dumps(formatted_data, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
