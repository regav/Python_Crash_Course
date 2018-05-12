# the tasks in this lesson says to make dictionaries then add them to a list
steel = {
    'name': 'steel',
    'animal': 'dog',
    'breed': 'husky',
    'owner': 'brea',
}

guero = {
    'name': 'guero',
    'animal': 'dog',
    'breed': 'mutt',
    'owner': 'lex',
}

maxwell = {
    'name': 'max',
    'animal': 'dog',
    'breed': 'german-shepard',
    'owner': 'lex',
}

pets = []
pets.append(steel)
pets.append(guero)
pets.append(maxwell)

for pet in pets:
    pet_name = pet['name'].title()
    pet_animal = pet['animal']
    pet_breed = pet['breed'].title()
    pet_owner = pet['owner'].title()

    print(pet_name + " is a " + pet_animal + " that is a " + pet_breed + " and their owner is " + pet_owner + ".")