tea_prices = {
    "Masala Tea": 40,
    "Lemon Tea": 20,
    "Elaichi Tea": 50,
    "Vanilla Tea": 100
}

tea_prices_usd = { tea:round(price/88,2) for tea,price in tea_prices.items() }
print(tea_prices_usd)