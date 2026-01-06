start_number = 5
countdown_values = []

while start_number >= 1:
    # Append the current value to the list
    countdown_values.append(start_number)
    # Decrement so the loop makes progress
    start_number -= 1

print("Discount countdown complete!")
print(countdown_values)
    