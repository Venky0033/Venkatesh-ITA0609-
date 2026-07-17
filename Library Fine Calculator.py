days = int(input("Enter overdue days: "))
if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = 5*2 + (days-5)*5
else:
    fine = 5*2 + 5*5 + (days-10)*10

print("Library Fine:", fine)
