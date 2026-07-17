seats = int(input("Enter number of seats: "))
category = input("Enter category (Regular/Premium): ")

price = 150 if category.lower() == "regular" else 250
total = seats * price

discount = total * 0.1 if seats >= 5 else 0
final = total - discount

print("Total:", total, "Discount:", discount, "Final Payable:", final)
