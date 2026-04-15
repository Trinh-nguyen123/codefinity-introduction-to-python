vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
print(vegetables)
if "carrots" not in vegetables:
    vegetables.append("carrots")
    print(vegetables)
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
    print(vegetables)
vegetables.sort()
print("Updated Vegetable Inventory:", (vegetables))
if "carrots" in vegetables:
    print("Carrots are already in the list")
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list")