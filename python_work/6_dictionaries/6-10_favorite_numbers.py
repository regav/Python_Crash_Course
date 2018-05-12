bob = {'name': 'bob', 'favorite_number': [10, 11] }
samuel = {'name': 'samuel', 'favorite_number': [45, 12] }
billy = {'name': 'billy', 'favorite_number': [11, 34] }
kelly = {'name': 'kelly', 'favorite_number': [9, 65] }
dave = {'name': 'dave', 'favorite_number': [7, 43] }

friend_message = "My friend's name is "
number_message = " their favorite number is: "

print(friend_message + bob['name'].title() + number_message + str(bob['favorite_number']))
print(friend_message + samuel['name'].title() + number_message + str(samuel['favorite_number']))
print(friend_message + billy['name'].title() + number_message + str(billy['favorite_number']))
print(friend_message + kelly['name'].title() + number_message + str(kelly['favorite_number']))
print(friend_message + dave['name'].title() + number_message + str(dave['favorite_number']))

# copied and pasted from lesson 6-2 

print("\n\n")
friends = []
friends.append(bob)
friends.append(samuel)
friends.append(billy)
friends.append(kelly)
friends.append(dave)

for friend in friends:
    name = friend['name']
    print("My name " + name.title() + " favorite numbers are:")
    for number in friend['favorite_number']:
        print("\t" + str(number))