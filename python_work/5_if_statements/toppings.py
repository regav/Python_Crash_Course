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
