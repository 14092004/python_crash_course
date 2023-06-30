#: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
current_users = ['A', 'B', 'C', 'D', 'E']
new_users = ['F', 'B', 'G', 'E', 'H']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
