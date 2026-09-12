Weight = float (input ("Enter your weight in kg: "))
Height = float (input ("Enter your height in m: "))
BMI = Weight / (Height * Height)
print (f"Your BMI: {BMI}")
if BMI <= 19:
    print ("Category: Underweight")
elif BMI <= 25:
    print ("Category: Normal")
elif BMI <= 30:
    print ("Category: Overweight")
else: 
    print ("Category: Obese")