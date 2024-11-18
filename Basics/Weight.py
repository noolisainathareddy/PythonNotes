weight = float(input("Enter your weight"))

units = input("Enter units (K or L)")

if units == "K":
    weight = weight * 2.205
    units = "Lbs."
    print(f"your weight is {round(weight,1)} {units}")
