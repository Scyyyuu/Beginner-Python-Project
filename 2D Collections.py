groceries = ({"Apple", "Orange", "Banana", "Chicken",},
             {"Celery", "Milk", "Potatoes"},
             {"Pork", "Snacks", "Fish"})

for collection in groceries:
    for food in collection:
        print (food, end=" ")
    print()