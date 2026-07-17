stock = int(input("Enter current stock: "))
min_stock = int(input("Enter minimum required stock: "))

if stock < min_stock:
    print("Stock Low! Reorder Needed")
else:
    print("Stock Sufficient")
