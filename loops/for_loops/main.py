prices = [12.99, 8.50, 15.75, 23.00, 7.25]

# Write your code here
total = 0

# Use a for loop to iterate through each price in the prices list
# Add each price to the total variable inside the loop.
for price in prices:
    total = total + price # accu,mulate price inside loop
    
print ("Total price for products: ", total)
    