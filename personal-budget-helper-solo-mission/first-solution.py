# Function to calculate remaining budget

def budget_remaining(budget,food, transport):
    remaining = budget - food - transport
    return remaining

#testing with normal case
money = budget_remaining(2000, 900, 600)
print(money)

#testing with zero case
money = budget_remaining(1500,0,0)
print(money)

#testing with overused case
money =budget_remaining(1000, 800, 500)
print(money)





# Second function
#Creating budget message
def budget_message(name, remaining):
    return f'{name} has {remaining} naira remaining.'

message = budget_message("Ada", 500)
print(message)

message = budget_message("Tobi", -300)
print(message)