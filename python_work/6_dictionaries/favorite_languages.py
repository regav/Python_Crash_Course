favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
print("\n\n")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite lanugage is " +
    language.title() + ".")
print("\n\n")
friends = ['sarah', 'phil']

for name in favorite_languages.keys(): 
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our Poll!")

print("\n\n")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking our poll.")


print("\n\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# to produce a list without repeats by using the 'set' function
print("\n\n")

print("The following lanugages have been mentioned:")
for lanugage in set(favorite_languages.values()):
    print(lanugage.title())
    
# pg 112 changing structure of dictionary to allow more than one favorite 
# lanuguage by making the values into lists
print("\n\n")
favoite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
## THE CODE GOES WRONG BECAUSE I CALL OUT favorite_languages.items()
## BUT THE DICTIONARY IS MISSSPELLED favoite_languages
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
## I DID A SPELLING WRONG SOMEWHERE, THIS PRODUCES WEIRD OUTPUT
## ON THE CODE ABOVE... CORRECT CODE IS BELOW

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
