age = 22
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

ticket_price = "Ticket Price for you is: ${}"

print(ticket_price.format(price))