Number = int(input("What Number would you like to multiply up to 10?: "))
for multiplier in range(1, 11):
    result = Number * multiplier
    print(f"{Number} x {multiplier} = {result}")