#Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city
cities = {
    'New Delhi': {
        'country': 'India',
        'population': 6158080,
        'nearby mountains': 'himalaya',
        },
    'Paris': {
        'country': 'France',
        'population': 87600,
        'nearby mountains': 'x',
        },
    'melbourne': {
        'country': 'Australia',
        'population': 1003,
        'nearby mountains': 'y',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")
    
