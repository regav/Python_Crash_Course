user_names = ['billy', 'eric', 'daniel', 'randy', 'david', 'admin']

for user_name in user_names:
    if user_name == 'admin':
        print("Hello " + user_name.title() + ", would you like to see a status report?")
    else:
        print("Hello " + user_name.title() + ", thank you for logging in again.")
