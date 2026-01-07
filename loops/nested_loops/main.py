produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

#Combine the 2 lists to a single list
groceries = [produce, dairy]

for section in groceries:
    for item in section:
        print("Item name: ", item)

