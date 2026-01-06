# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(5):
    day_name = weekdays[i]
    promotion = daily_promotions[i]
    print(f"{day_name}: Promotion on {promotion}")