# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

def calculate_revenue(prices, quantities_sold):
    return [prices[i] * quantities_sold[i] for i in range(len(prices))]

def formatted_output(products, revenues):
    # Pair products with revenues and sort by product name
    revenue_per_product = sorted(zip(products, revenues), key=lambda x: x[0])
    # Print each line
    for name, rev in revenue_per_product:
        print(f"{name} has total revenue of ${rev}")

revs = calculate_revenue(prices, quantities_sold)
formatted_output(products, revs)