ticket_price = 10
num_ticket = int(input("how many tickets do you want to buy"))
if  num_ticket == 5:
    print(ticket_price * num_ticket)
else:
    new_price = ticket_price * 0.7
    old_price = new_price * num_ticket
    print("The total price with a 30% discount for", num_ticket, "tickets is:", old_price, "GEL")