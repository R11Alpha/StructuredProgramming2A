order = float(input("How much is your order?\n"))

bank = float(input("How much do you have in your plastic?\n"))

if bank >= order:
    print("Paid with plastic")
else:
    print("Plastic rejected")