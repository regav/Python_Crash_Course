#i am to test quality and inquality with strings
#test using lower() function
#numerical tests using quality, inquality, ==, >=, <=, !=
#test using 'and' and 'or' keywords
#test whether an item is in a list
#test whether an item is not in a list
#this is supposed to be using same tests from 5-1, I will just do new ones

name_1 = 'bob'
name_2 = 'billy'
num_1 = 15
num_2 = 5
names = ['andy', 'ron', 'andrew']

print("Is name_1.lower() == 'bob'? I predict True")
print(name_1.lower() == 'bob')
print("\nIs name_2.lower() != 'billy'? I predict False")
print(name_2 != 'billy')
print("\nIs num_1 >= 20? I predict False")
print(num_1 >= 20)
print("\nIs num_2 <= 25? I predict True")
print(num_2 <= 25)
print("\nIs name_1 == 'bob' and name_2 == 'billy'? I predict True")
print(name_1 == 'bob' and name_2 == 'billy')
print("\nIs the name 'nick' in names? I predict False")
print('nick' in names)
print("\nIs the name 'ryan' not in names? I predict True")
print('ryan' not in names)