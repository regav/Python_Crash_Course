alien_color = 'yellow'
green_message = "You earned 5 points!"
yellow_message = "You earned 10 points!"
red_message = 'You have earned 15 points!'

if alien_color == 'green':
   print(green_message) 
elif alien_color != 'green':
    print(yellow_message)

if alien_color == 'green':
    print(green_message)
elif alien_color == 'yellow':
    print(yellow_message)
else:
    print(red_message)
## The book wants me to write 3 versions of this program.
print("\n\n")

alien_color = 'red'
if alien_color == 'green':
    print(green_message)
elif alien_color == 'yellow':
    print(yellow_message)
elif alien_color == 'red':
    print(red_message)

print("\n\n")

alien_color = 'green'
if alien_color == 'green':
    print(green_message)
elif alien_color == 'yellow':
    print(yellow_message)
else:
    print(red_message)