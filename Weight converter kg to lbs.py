weight = float(input("Weight: "))
unit = str(input("(K)g or (L)bs: "))
if unit == "k" or unit == "K":
    lbs = weight * 2.2046
    print("Weight in Lbs: " + str(round(lbs, 2)))
elif unit == "l" or unit == "L":
    kg = weight / 2.2046
    print("Weight in Kg: " + str(round(kg, 2)))