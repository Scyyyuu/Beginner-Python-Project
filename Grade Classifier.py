try:
    Score = int (input ("What Grade number would you like to classify?: "))
except:
    print ("Please enter a valid number")
if Score >= 90:
    print ("Grade: A")
elif Score >= 80:
    print ("Grade: B")
elif Score >= 70:
    print ("Grade: C")
elif Score >= 60:
    print ("Grade: D")
else:
    print ("Grade: F")