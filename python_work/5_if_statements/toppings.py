#requested_toppings = ['mushrooms', 'extra cheese']
#
#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni.")
#if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")
#
#print("\nFinished making your pizza!")
# doing a new version of this code PG 90

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry we are out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")
else:
    print("\n\nAre you sure you want a plain pizza?")

# This is the newest version of this program that has multiple lists pg 92
# I also added the intial if statement to check if requested_toppings is empty
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we do not have " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

print("\nFinished making your pizza!")