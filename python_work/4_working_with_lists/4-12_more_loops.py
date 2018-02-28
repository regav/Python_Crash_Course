my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

my_foods.append('cannoli')
friends_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

print(my_foods + friends_foods)

example_friend_foods = my_foods
example_friend_foods.append('bananas')
print("This is my favorite foods:")
print(my_foods)
print("\nThis is 'example_friend_food list of favorite foods:")
print(example_friend_foods)
print("\nBy setting a varaible to = another list, it only makes the varaible point to the same list as the original list")
print(" to really make a copy you must use the slice notation [:].")

#The code below is for 4-12 lesson
print("\nWe will now print the list of foods within a for loop.")
for food in my_foods:
   print(food)
print("\n")
for food in friends_foods:
   print(food)