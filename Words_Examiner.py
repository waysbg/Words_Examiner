from random import choice
from ast import literal_eval

file = open("dictionary.txt")
data = file.read()
dictionary = literal_eval(data)
english_words = list(dictionary.keys())

while True:
    picked_word = choice(english_words)
    decision = str(input(f"o[p]en, [n]ext or [e]xit           {picked_word}? "))
    if decision == "e":
        break
    elif decision == "p":
        print(f"{' ' * 40}{dictionary[picked_word]}")




