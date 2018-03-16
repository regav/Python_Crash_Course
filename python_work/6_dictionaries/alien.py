alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

#How to add key-pairs to a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# How to set an empty dictionary

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# How to modify EXISTING key-pairs
print("This is what alien_1" + str(alien_1) + "\nHas in it's dictoinary")
alien_1['color'] = 'yellow'
print("This is what alien_1 now has in its dictionary\n" + str(alien_1))

# This is more code from pg 99
print("\n\n")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# removing key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print("\n\n")
print(alien_0)

del alien_0['points']
print(alien_0)