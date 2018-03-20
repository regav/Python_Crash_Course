bob = {'name': 'bob', 'favorite_number': 10 }
samuel = {'name': 'samuel', 'favorite_number': 45 }
billy = {'name': 'billy', 'favorite_number': 11 }
kelly = {'name': 'kelly', 'favorite_number': 9 }
dave = {'name': 'dave', 'favorite_number': 7 }

friend_message = "My friend's name is "
number_message = " their favorite number is: "

print(friend_message + bob['name'].title() + number_message + str(bob['favorite_number']))
print(friend_message + samuel['name'].title() + number_message + str(samuel['favorite_number']))
print(friend_message + billy['name'].title() + number_message + str(billy['favorite_number']))
print(friend_message + kelly['name'].title() + number_message + str(kelly['favorite_number']))
print(friend_message + dave['name'].title() + number_message + str(dave['favorite_number']))