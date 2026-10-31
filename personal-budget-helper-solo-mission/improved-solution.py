
# Function 1: Calculate the remaining budget
def budget_remaining(budget, food, transport):
    remaining = budget - food - transport
    return remaining


# Function 2: Create a budget message
def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining."


# Test 1: Normal case
remaining = budget_remaining(2000, 900, 600)
print(remaining)  # Expected: 500

# Test 2: Zero expenses
remaining = budget_remaining(1500, 0, 0)
print(remaining)  # Expected: 1500

# Test 3: Overspend case
remaining = budget_remaining(1000, 800, 500)
print(remaining)  # Expected: -300

# Test 4: Test both functions together/message-format case
remaining = budget_remaining(2000, 900, 600)
message = budget_message("Ada", remaining)
print(message)  # Expected: Ada has 500 naira remaining.

# Test 5: Negative amount in the message
message = budget_message("Tobi", -300)
print(message)  # Expected: Tobi has -300 naira remaining.