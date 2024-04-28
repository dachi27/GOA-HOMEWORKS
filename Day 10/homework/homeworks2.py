price = float(input("enter the price of the item: "))
budget = float(input("enter your budget here: "))
if budget >= price:
    print("you can buy that item")
else:
    print("you can't buy the item")