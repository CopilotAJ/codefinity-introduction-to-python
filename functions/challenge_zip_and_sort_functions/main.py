# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = list(zip(products, prices, quantities_sold))
print("Product: ", products, "Price: ", prices, "Quantity Sold: ", quantities_sold)

sorted_products = sorted(combined_list)
print(sorted_products)

#Loop through sorted_products and print each productsname, price and quantities_sold
for name, price, qty in sorted_products:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {qty}")


