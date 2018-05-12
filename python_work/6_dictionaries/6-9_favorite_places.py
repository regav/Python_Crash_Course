favorite_places = {
    'ray': ['rome', 'tucson', 'disney-land'],
    'preston': ['japan', 'korea', 'texas'],
    'dd': ['paris', 'new-york', 'hawaii']
}

for person, places in favorite_places.items():
    name = person.title()
    print(name + " favorite places are:")
    for place in places:
        location = place.title()
        print("\t" + location)