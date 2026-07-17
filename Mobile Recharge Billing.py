amount = float(input("Enter recharge amount: "))
cashback = amount * 0.05
final = amount - cashback

print("Recharge Amount:", amount, "Cashback:", cashback, "Final Payable:", final)
