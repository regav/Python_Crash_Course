pizzas = ['mushroom pizza','no-cheese pizza','pepperoni pizza']

for pizza in pizzas:
   print ("I like " + pizza + ".")

print("I really like pizza.\nI really like pizza, such as:")
for pizza in pizzas:
   print("pizza")
print("I really love pizza!")
# to follow instructions in book I am manually printing the for loop

print("I really like pizza, such as:\nmushroom pizza\nno-cheese pizza\nand pepperoni pizza\nI really love pizza!")
#Lesson 4-11 is below
friend_pizzas = pizzas[:]
pizzas.append('sausage pizza')
friend_pizzas.append('chicken pizza')
print("My favorite pizzas are:")
for pizza in pizzas:
   print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
   print(pizza)