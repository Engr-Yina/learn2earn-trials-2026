"""
Learn2Earn Day 1
Git Fundamentals Practical Demonstration

This program demonstrates:
1. Python functions
2. Return values
3. Conditional statements
4. Basic calculations
"""


def calculate_total(price, quantity):
    """Calculate the total cost of items."""
    return price * quantity


def check_budget(budget, total):
    """Determine whether a purchase is under, within or over budget."""

    if total < budget:
        return "Under budget"
    elif total == budget:
        return "Exact budget"
    else:
        return "Over budget"


# Sample data
item_price = 500
quantity = 4
budget = 2500

# Calculate purchase total
total_cost = calculate_total(item_price, quantity)

# Determine budget status
budget_status = check_budget(budget, total_cost)

# Display results
print("LEARN2EARN - DAY 1 PRACTICAL")
print("-----------------------------")
print(f"Item Price: ₦{item_price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ₦{total_cost}")
print(f"Budget: ₦{budget}")
print(f"Budget Status: {budget_status}")