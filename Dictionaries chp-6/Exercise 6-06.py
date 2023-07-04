#Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
favorite_languages = {
    'biswajit': 'python',
    'kanika': 'c',
    'akshi': 'ruby',
    'manan': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['manan', 'rohan', 'avi', 'ruhi', 'kanika', 'mdkkd', 'lowkw']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
