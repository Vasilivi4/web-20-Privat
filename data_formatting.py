def format_exchange_rates(data, additional_currencies=None):
    formatted_data = []
    for day_data in data:
        formatted_day_data = {}
        if "date" in day_data:
            date = day_data["date"]
            for currency in day_data.get("exchangeRate", []):
                if currency["currency"] in ["EUR", "USD"] or (
                    additional_currencies
                    and currency["currency"] in additional_currencies
                ):
                    formatted_day_data[date] = {
                        currency["currency"]: {
                            "sale": currency["saleRate"],
                            "purchase": currency["purchaseRate"],
                        }
                    }
        formatted_data.append(formatted_day_data)
    return formatted_data
