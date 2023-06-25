#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
guests = ['Akshi','Kanika','Manan']
message = guests[0] + ", please come to the dinner."
print(message)
message = guests[1] + ", please come to the dinner."
print(message)
message = guests[2] + ", please come to the dinner."
print(message)
message = ("\nKanika, cannot come to the dinner")
print(message)
del(guests[1])
guests.insert(1, "Biswajit")
message = ("\n" + guests[1] + ", please come to the dinner.")
print(message)
message = guests[0] + ", please come to the dinner."
print(message)
message = guests[2] + ", please come to the dinner."
print(message)
