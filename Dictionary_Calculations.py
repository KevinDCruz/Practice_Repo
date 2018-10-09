stocks = {
    'GOOG': 545,
    'AAPL': 234,
    'FB': 459,
    'AMZN': 152,
    'UBR': 347,
    'MSFT': 200
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
