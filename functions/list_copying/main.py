def apply_discount(prices):
    #Create a copy of the prices list
    prices_copy = prices.copy()
    #Iterate through the list of prices using indexing
    for i in range(len(prices_copy)):
        #Apply a 10% discount if prices is gretaer than 2.0
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.9
        
    return prices_copy


# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: {updated_prices}")