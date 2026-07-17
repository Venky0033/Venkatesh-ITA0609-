distance = float(input("Enter trip distance (km): "))
mileage = float(input("Enter vehicle mileage (km/l): "))
price = float(input("Enter fuel price per liter: "))

fuel_needed = distance / mileage
cost = fuel_needed * price

print("Fuel Needed:", fuel_needed, "Cost:", cost)
