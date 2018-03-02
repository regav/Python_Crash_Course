# The lines below are from book
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
# The lines below is my code, I need to write 10 conditonal tests

num_1 = 10
num_2 = 5
num_3 = 5.5
num_4 = 10.5

print("\nIs num_1 >= 12? I predict False")
print(num_1 >= 12)
print("\nIs num_1 >= num_2? I predict True")
print(num_1 >= num_2)
print("\nIs num_3 <= num_1? I predict True.")
print(num_3 <= num_1)
print("\nIs num_4 >= num_3? I predict True")
print(num_4 >= num_3)

print("Let's test and, or, not conditionals")
print("\nIs num_1 >= num_2 and num_2 == 10? I predict True")
print(num_1 >= num_2 and num_1 == 10)
print("\nIs num_2 >= 6 or num_4 == 10? I predict False")
print(num_2 >= 6 or num_4 == 10)
#print("\nIs num_1 not == 10? I predict False")
#print(num_1 not == 10)
#I got an invalid syntax on line 29 for the 'not ==' section
#Proper syntax is using != 
print("\nIs num_1 != 10? I predict False")
print(num_1 != 10)
# we are at 7 tests. lets add string tests
car_1 = 'mustang'
car_2 = 'beetle'
car_3 = 'stingray'

print("\nIs car_1 == 'beetle'? I predict False.")
print(car_1 == 'beetle')
print("\nIs car_1 == 'mustang' and car_2 == beetle? I predict True")
print(car_1 == 'mustang' and car_2 == 'beetle')
print("\nIs car_1 == car_3? I predict False.")
print(car_1 == car_3)

