

text = "my favorite fruits are oranges and bananas ,"\
    "Because it makes me feel great and smart"
list_text = text.split()
print(list_text)



#build a dictionary
myDictionary = {'oranges':input("somefruit"), 'bananas':input("some other fruit or thing"),
                'great':input("An adjective"), 'smart':input('another adjecive')}
#print(mydictionary.keys())
###print




from gerardolib import translate

print(translate(text,myDictionary))