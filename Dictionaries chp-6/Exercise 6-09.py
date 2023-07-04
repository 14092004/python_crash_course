#Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
favorite_places = {
    'Manan': ['bear mountain', 'death valley', 'tierra del fuego'],
    'Akshi': ['hawaii', 'iceland'],
    'Kanika': ['mt. verstovia', 'the playground', 'south carolina']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
