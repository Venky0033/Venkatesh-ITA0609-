age = int(input("Enter age: "))
cls = input("Enter class (Sleeper/AC): ")

fare = 500 if cls.lower() == "sleeper" else 1000
if age < 12:
    fare *= 0.5
elif age > 60:
    fare *= 0.7

print("Ticket Fare:", fare)
