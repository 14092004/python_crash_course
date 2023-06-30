#Make a list of five or more usernames, including the name 'admin'
usernames = ['manan', 'akshi', 'kanika', 'rohan', 'ruhi']

for username in usernames:
    if username == 'kanika':
        print("Hello kanika, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")
