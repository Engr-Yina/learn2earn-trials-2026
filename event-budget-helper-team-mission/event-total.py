from participant import participant_cost

# Candidate B: event_total
def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    people_cost = participant_cost(attendees, food_per_person, transport_per_person) + venue_cost
    return people_cost 

#Test cases

# Test 1: Normal attendees cost plus venue
total = event_total(10, 800, 200, 5000)
print(total) # Expected: 15000


#Test 2: Zero attendance with non-zero venue
total = event_total(0, 800, 200, 5000)
print(total) #Expected: 5000
