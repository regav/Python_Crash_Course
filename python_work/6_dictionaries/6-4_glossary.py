# This was copied and pasted from lesson 6-3_glossary.py
glossary = {
    'print': "This is the 'print' keyword within Python, it is used to print out a string value to the screen or output onto the screen.",
    'list': "This is the 'list' varaible within Python. It can be used to store a list of values that can be called out individually or all together or one by one and even a certain group or other desired methods.",
    'loop': "This is the 'loop' action within Python. It is called by using the keyword 'for' it allows one to iterate over a list to do a certain action or many.",
    'for': "This is the 'for' keyword within Python to begin a loop statment. This can be used against a list dicitonary or other functions/methods built in Python.",
    '.title()': "This is the '.title()' method within Python. It is used to apply a certain format against a string, it will captialize each word within a string.",
    'dictionary': "This is the dictionary varaible within Python. It is used to create a list of key-pairs, meaning a Key with an assoicated value, to show realtionship between the two.",
    '.items()': "This is the '.items()' method within Python. It is used to pull both key and value (key-pair) of a dictionary. One uses this to iterate within a for loop.",
    '.keys()': "This is the .keys() method within Python. It is used to pull only the keys within a dictionary rather than both the key and value as done by a .items() method.",
    '.values()': "This is the .values() method within Python. It is used to pull only the values of the key-pair",
    'sorted()': "This is the sorted() function within Python. It is used to pull values from a list and sort them."
}
###
#print("print: " + glossary['print'] + "\n")
#print("list: " + glossary['list'] + "\n")
#print("loop: " + glossary['loop'] + "\n")
#print("for: " + glossary['for'] + "\n")
#print(".title(): " + glossary['.title()'] + "\n"
# removing print statments to use a for loop instead like problem 6-4 requestes
###

for word, definition in sorted(glossary.items()):
    print(word + ": " + definition)