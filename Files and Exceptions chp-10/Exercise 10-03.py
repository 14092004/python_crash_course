# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
