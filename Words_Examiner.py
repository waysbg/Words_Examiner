from random import choice
from ast import literal_eval
from gtts import gTTS
from playsound import playsound
from pathlib import Path

welcome = Path().cwd() / "welcome.mp3"
playsound(welcome)

file = open("dictionary.txt")
data = file.read()
dictionary = literal_eval(data)
english_words = list(dictionary.keys())

while True:
    picked_word = choice(english_words)
    word_to_play = gTTS(text=picked_word, lang='en')
    word_to_play.save("word.mp3")
    word_to_play = Path().cwd() / "word.mp3"
    playsound(word_to_play)
    decision = str(input(f"[t]ranslate, [n]ext or [e]xit           {picked_word}? "))
    if decision == "e":
        break
    elif decision == "t":
        print(f"{' ' * 40}{dictionary[picked_word]}\n")




