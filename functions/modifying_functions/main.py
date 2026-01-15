# Define function and return price after applying discount
def apply_discount(price, discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price

#Define functio and return price after adding tax
def apply_tax(price, tax=0.07):
    taxed_price = price * (1 + tax)
    return taxed_price

# Define calculate_total, use apply_discount and apply_tax
# to return the total price with both discount and tax applied.
def calculate_total(price, discount=0.05, tax=0.07):
    # First apply the discount
    discounted = apply_discount(price, discount)
    # Apply tax to discounted amount
    total_price = apply_tax(discounted, tax)
    return total_price

#Call calculate_total using default discount and tax
total_price_default = calculate_total(price=120)
print(f"Total cost with default discount and tax: ${total_price_default}")

#Call calculate_total using custom values
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")

