current_users = ['grizzly', 'grizzlyray', 'grizzlyray93', 
'grizzlybear', 'grizzlybear93']

new_users = ['grizzlybear', 'grizz', 'shutthedoor', 'raymond', 'GRIZZLY']

#if new_users:
#    for new_user in new_users:
#        if new_user.lower() in current_users:
#            print("This username is not avivable.")
#        else:
#            print("This username is avivable.")
#else:
#    print("There is no new usernames requested.")


if new_users:
    copy_current_users = []
    for current_user in current_users:
        copy_current_users.append(current_user.lower())
    for new_user in new_users:
        if new_user.lower() in copy_current_users:
            print("You cannot use this username: " + new_user + ", please use another one.")
        else:
            print("You may use this username: " + new_user + ".")
else:
    print("There is no new username requests.")

print("\n\n\n")
if new_users:
    for new_user in new_users:
        for current_user in current_users:
            if new_user.lower() == current_user.lower():
                print("You cannot use this username: " + new_user + ", please use another.")
    else:
        print("You may use this username: " + new_user + ".")
else:
    print("There is no new username requests.")