#Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number.
favorite_numbers = {
    'manan': [42, 17],
    'akshi': [42, 39, 56],
    'kanika': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))
