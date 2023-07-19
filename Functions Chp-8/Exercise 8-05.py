# Write a function called describe_city() that accepts the name of a city and its country
def describe_city(city, country='chile'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
