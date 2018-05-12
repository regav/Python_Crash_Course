billy = {
    'first_name': 'billy',
    'last_name': 'smith',
    'age': '27',
    'birthday': '11-27-1990',
    'city': 'tucson'
}

print("My friend's first name is " + billy['first_name'].title() + ".")
print("My friend currently lives in " + billy['city'].title() + " with me.")
print("My friend is " + billy['age'] + " years old.")
print("My friend's full name is " + billy['first_name'].title() +
    " " + billy['last_name'].title() + ".")

# Copied and pasted from 6-1 lesson, as stated in lesson for 6-7

samuel = {
    'first_name': 'samuel',
    'last_name': 'william',
    'age': '25',
    'birthday': '02-11-1993',
    'city': 'austin'
}

rick = {
    'first_name': 'richard',
    'last_name': 'taylor',
    'age': '24',
    'birthday': '01-18-1994',
    'city': 'la'
}

people = []
people.append(billy)
people.append(samuel)
people.append(rick)

for person in people:
    print("My friend's name is " + person['first_name'].title() +  " " + person['last_name'].title() + ".")
    print("They were born in " + person['city'].title() + " on " + person['birthday'] + " which means they are " + person['age'] + " years old.")