#alien_0 = {'color': 'green', 'points': 5}
#
#print(alien_0['color'])
#print(alien_0['points'])
#print(alien_0)
#
##How to add key-pairs to a dictionary
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)
## How to set an empty dictionary
#
#alien_1 = {}
#alien_1['color'] = 'green'
#alien_1['points'] = 5
#print(alien_1)
#
## How to modify EXISTING key-pairs
#print("This is what alien_1" + str(alien_1) + "\nHas in it's dictoinary")
#alien_1['color'] = 'yellow'
#print("This is what alien_1 now has in its dictionary\n" + str(alien_1))
#
## This is more code from pg 99
#print("\n\n")
#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print("Original x-position: " + str(alien_0['x_position']))
#
## Move alien to the right
## Determine how far to move the alien based on its current speed
#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    # This must be a fast alien.
#    x_increment = 3
## The new position is the old position plus the increment
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#
#print("New x-position: " + str(alien_0['x_position']))
#
## removing key-value pairs
#
#alien_0 = {'color': 'green', 'points': 5}
#print("\n\n")
#print(alien_0)
#
#del alien_0['points']
#print(alien_0)

## starting over for lesson taught in pg 109
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("\n\n")

# make an empty list for storing aliens
aliens = []

# make 30 green aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

#print("\n" + "This is all the aliens" + str(aliens))
print("\nThis is all the aliens.")
simple_counter = 0
for alien in aliens:
    simple_counter = simple_counter + 1
    print(str(simple_counter) + str(alien))