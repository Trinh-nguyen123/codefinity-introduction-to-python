prices = [29.99, 45.50, 12.75, 38.20]
discount = [10, 20, 15, 5]
for index in range(len(prices)):
    new_price = prices[index] * (1-discount[index]/100)
    prices[index] = new_price
    print(f"Update price for item {index}: ${new_price:.2f}")