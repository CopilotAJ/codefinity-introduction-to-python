# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, values in products.items():
    #Convert price to a float
    price = float(values[0])
    #Convert the quantity sold to an int
    quantity = int(values[1])
    # Multiply them to get the total sales
    total_sales = price * quantity
    print(f"Total sales for {product}: ${total_sales}")
    # Append the total sales to total_sales_list
    total_sales_list.append(total_sales)

# calculate sum of all sales
total_sum = sum(total_sales_list)
print(f"Total sum of all sales:  ${total_sum}")

min_sales = min(total_sales_list)
print(f"Minimum sales: ${min_sales}")

max_sales = max(total_sales_list)
print(f"Maximum sales: ${max_sales}")
