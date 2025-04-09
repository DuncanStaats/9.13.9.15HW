import random

lotto_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

def ticket_maker():
    ticket = []
    while len(ticket) < 4:
        rando_lotto = random.randint(0, len(lotto_num) - 1)
        ticket_num = lotto_num[rando_lotto]
        if ticket not in ticket:
            ticket.append(ticket_num)
    return ticket

winning_ticket = ticket_maker()
my_ticket = ticket_maker()

print(f"Winning ticket: {winning_ticket}")
print(f"Your ticket: {my_ticket}")
print()

attempt = 0
while True:
    new_ticket = ticket_maker()
    attempt += 1
    if new_ticket == my_ticket:
        break

print(f"It took {attempt} attempts to get a winning ticket.")