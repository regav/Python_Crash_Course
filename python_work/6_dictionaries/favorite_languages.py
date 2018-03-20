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