# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

def calculate_revenue(prices, quantities_sold):
    return [prices[i] * quantities_sold[i] for i in range(len(prices))]
revs = calculate_revenue(prices, quantities_sold)
revenue_per_product = sorted(zip(products, revs),key = lambda x:x[0])
def formatted_output(list_to_print):
    for name, rev in list_to_print:
        print(f"{name} has total revenue of ${rev}")

formatted_output(revenue_per_product)