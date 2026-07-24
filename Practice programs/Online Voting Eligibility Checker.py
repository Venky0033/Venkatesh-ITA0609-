age = int(input("Enter age: "))
nationality = input("Enter nationality: ")

if age >= 18 and nationality.lower() == "indian":
    print("Eligible to Vote")
else:
    print("Not Eligible")
