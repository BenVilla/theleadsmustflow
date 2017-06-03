import math


sitter_info = [{'name': 'Rob', 'spots': 2,'leads': 10, 'rev': 40, 'bookrate':0.40},
               {'name': 'Jane', 'spots': 1,'leads': 4, 'rev': 40, 'bookrate':0.33},
               {'name': 'Rose', 'spots': 3, 'leads': 6, 'rev': 40, 'bookrate': 0.25}]

sitter_marginal_ev = {}

for sitter in sitter_info:

    vacancies = sitter['spots']
    initial_leads = sitter['leads']
    additional_leads = initial_leads + 1
    booking_rate = sitter['bookrate']
    revenue = sitter['rev']

    wins = 0 #these would be 'booked stays'
    ev = 0


    #ev: initial expected value: this is the expected value if we don't send over the next lead to this sitter
    while wins <= initial_leads:
        if wins > vacancies:
            effective_stays = vacancies
        else:
            effective_stays = wins

        combinations = math.factorial(initial_leads)/ (math.factorial(wins) * math.factorial(initial_leads - wins))

        ev += (booking_rate ** wins)  * ((1 - booking_rate) ** (initial_leads - wins)) * (revenue * effective_stays) * combinations

        wins += 1


    #ev2: this gets us the expected_value if we send the next lead to this sitter -- we'll take ev2 - ev to get marginal ev
    wins = 0
    ev2 = 0

    while wins <= additional_leads:
        if wins > vacancies:
            effective_stays = vacancies
        else:
            effective_stays = wins

        combinations = math.factorial(additional_leads)/ (math.factorial(wins) * math.factorial(additional_leads - wins))

        ev2 += (booking_rate ** wins)  * ((1 - booking_rate) ** (additional_leads - wins)) * (revenue * effective_stays) * combinations

        wins += 1


    marginal_ev = (ev2 - ev)


    sitter_marginal_ev[sitter['name']] = marginal_ev


#this prints out the sitters in the order in which they should be displayed, as well as the marginal expected value they provide
#if they get the next lead
sorted_sitters = sorted(sitter_marginal_ev.items(), key=lambda x: x[1], reverse=True)

print(sorted_sitters)



