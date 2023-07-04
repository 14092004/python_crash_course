#Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
people = []

person = {
    'first_name': 'manan',
    'last_name': 'dhall',
    'age': 18,
    'city': 'new delhi',
    }
people.append(person)

person = {
    'first_name': 'x',
    'last_name': 'dhall',
    'age': 5,
    'city': 'new delhi',
    }
people.append(person)

person = {
    'first_name': 'y',
    'last_name': 'dhall',
    'age': 8,
    'city': 'new delhi',
    }
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")
