weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("BMI:", bmi, "Status:", status)
