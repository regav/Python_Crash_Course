guests = ['Albert Wesker', 'Chris Redfield', 'Lois lane']
invitation = ', will you attend my dinner party this weekend?'
cant_arrive = ' cannot attend the party.'
larger_table_message = 'Good news all, more can join the party!'
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[0] + cant_arrive)
guests[0] = 'John Lennon'
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
guests.insert(0, 'Steve Nash')
guests.insert(2, 'Jim Carrey')
guests.append('Johnny Cash')
print('The new list of people is ' + str(guests))
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print(guests[5] + invitation)
print("I am sorry but I can only invite two people to the party")
not_coming_lists = [guests.pop()]
print(not_coming_lists)
not_coming_lists.append(guests.pop())
print(not_coming_lists)
not_coming_lists.append(guests.pop())
print(str(not_coming_lists) + " are not able to attend.")
not_coming_lists.append(guests.pop())
print(str(not_coming_lists) + " are not able to attend the party.")
print(str(guests) + ' will be attending the party.')
del guests[0]
del guests[0]
print('Are coming' + str(guests))