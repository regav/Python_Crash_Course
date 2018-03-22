major_rivers = {
    'amazon': "peru",
    'mississippi': "united states of america",
    'nile': "egypt"
}

for river, country in major_rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in major_rivers.keys():
    print(river.title() + " river.")

for country in major_rivers.values():
    print(country.title())