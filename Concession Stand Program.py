Menu = {"FRIES": 39.99,
        "CHICKEN": 100.00,
        "COLA": 20.00,
        "NUGGETS": 67.99,
        "JUICE": 20.00,
        "SPAGHETTI": 55.99,
        "CHICKEN BUCKET": 519.99,
        "CHICKEN FILLET": 59.99,
        "ICE CREAM": 39.99,
        }


orders_list = []
total = 0
values = Menu.values()

print ("===================")
print ("       Menu        ")
print ("===================")


for key, value in Menu.items():
    print (f"{key}: {value}")
    print ("---------------")

while True:
    orders = input ("Enter your Exact Order within the Menu (Press X to exit / A to add / R to remove ): ").upper()

    if orders == "A":
        add_order = input ("Enter your Exact Order within the Menu (Press X to exit / A to add / R to remove ): ").upper()
        orders_list.append(add_order)
        print (f"You ordered: {orders_list}")
        

    elif orders == "FRIES":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "CHICKEN":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "COLA":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "NUGGETS":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "JUICE":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "SPAGHETTI":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "CHICKEN BUCKET":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "CHICKEN FILLET":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "ICE CREAM":
        orders_list.append(orders)
        print (f"You ordered: {orders_list}")
        

    elif orders == "R":
        remove_list = input (f"Choose an Item to Remove {orders_list}: ").upper()
        if remove_list in orders_list:
            orders_list.remove(remove_list)
        else:
            print(f"{remove_list} wasn't found in the list you've ordered. Try again ")

    elif orders == "X":
        break

print ("--------------------")
print ("       RECEIPT      ")

for order in orders_list:
    print ("--------------------")
    print (order)

total += values

print (f"Your Total Price: P{total}") 