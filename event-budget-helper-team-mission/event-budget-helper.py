# Integrated components that makes a complete project.

# Candidate A: participant_cost
def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)


# Candidate B: event_total
def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    people_cost = participant_cost(attendees, food_per_person, transport_per_person) + venue_cost
    return people_cost


# Candidate C: budget_status
def budget_status(budget, total):
    if total < budget:
        return "Below budget"
    elif total == budget:
        return "Exact budget"
    else:
        return "Over budget"


# Candidate D: event_summary
def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."


""" 
Test cases for different components
Jerry     - candidate A
Vershima  - candidate B
Eucharia  - candidate C
Gabriel   - candidate D
"""

"""Test case for Candidate A: Participant cost"""
#Test 1: Normal attendee count
attendees1 = participant_cost(10, 800, 200)
print(attendees1) #Expected: 10000

#Test 2: Zero attendees
attendees2 = participant_cost(0, 800, 200)
print(attendees2) #Expected: 0


""" Test case for cadidate B: Event total"""
# Test 1: Normal attendees cost plus venue
total1 = event_total(10, 800, 200, 5000)
print(total1) # Expected: 15000


#Test 2: Zero attendance with non-zero venue
total2 = event_total(0, 800, 200, 5000)
print(total2) #Expected: 5000


""" Test case for candidate C: Budget status"""
#Test 1: Below Budget
status1 = budget_status(16000, 10000)
print(status1) #Expected 

#Test 2: Exact budget
status2 = budget_status(16000, 16000)
print(status2) #

#Test 3: Over budget
status3 = budget_status(16000, 17000)
print(status3)


""" Test case for candidate D: Event Summary"""
summary1 = event_summary("Study Day", total1, status1)
print(summary1) #Expected: Study Day: total 15000 naira. Within budget.

summary2 = event_summary("Learn2Earn Trials", total2,status2)
print(summary2) #Expected: Learn2Earn Trials: total 5000 naira. Within budget.