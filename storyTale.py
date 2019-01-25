from gerardolib import translate
from fairyTaleText import text


mynewdict = {"fish":input("Enter a new word for fish")}
new_text = translate(text, mynewdict).split(".")
for sentence in new_text:
    print(sentence, end= ".\n")