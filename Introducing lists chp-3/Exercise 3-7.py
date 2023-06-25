#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests
guests = ['Biswajit','Akshi','Rohan','Kanika','Manan','Aviral']
message = "\n" + guests[0] + ", please come to the dinner."
print(message)
message = guests[1] + ", please come to the dinner."
print(message)
message = guests[2] + ", please come to the dinner."
print(message)
message = guests[3] + ", please come to the dinner."
print(message)
message = guests[4] + ", please come to the dinner."
print(message)
message = guests[5] + ", please come to the dinner."
print(message)
message = ("\nSorry, we can only invite two people to dinner.")
print(message)

name = "guests.pop()"
print("\nSorry " + guests.pop() + " I can't invite you to dinner.")
print("Sorry " + guests.pop() + " I can't invite you to dinner.")
print("Sorry " + guests.pop() + " I can't invite you to dinner.")
print("Sorry " + guests.pop() + " I can't invite you to dinner.")
print(guests)
message = "\n" + guests[0] + ", you're still invited."
print(message)
message = "\n" + guests[1] + ", you're still invited."
print(message)
print("\n",guests)
del(guests)
print(guests)
