cities = {
    'tucson': {
        'country': 'united states',
        'population': 530000,
        'fact_sentence': 'famous for the Saguaro cactus.'
    },
    'la': {
        'country': 'united states',
        'population': 4000000,
        'fact_sentence': 'famous for the home of Hollywood.'
    },
    'Seattle': {
        'country': 'united states',
        'population': 3750000,
        'fact_sentence': 'famous for being the birthplace of Starbucks.'
    }
}

for city, city_info in cities.items():
    print("Here is a list of facts about " + city.title() + ".")
    print(city.title() + " is located in " + city_info['country'].title())
    print("The population is: " + str(city_info['population']) + ".")
    print("This city is " + city_info['fact_sentence'])
    print("\n")