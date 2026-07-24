age = int(input("Enter age: "))
weight = float(input("Enter weight (kg): "))
hb = float(input("Enter hemoglobin level: "))

if age >= 18 and weight >= 50 and hb >= 12.5:
    print("Eligible to Donate Blood")
else:
    print("Not Eligible")

