from random import choice
from ast import literal_eval
from gtts import gTTS
from playsound import playsound
from pathlib import Path
from time import sleep

welcome = Path().cwd() / "welcome.mp3"
playsound(welcome)
sleep(1)

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
    sleep(1)

    if decision == "e":
        break
    elif decision == "t":
        translation = dictionary[picked_word]
        print(f"{' ' * 40}{translation}\n")
        translation_to_play = gTTS(text=translation, lang='bg')
        translation_to_play.save("translation.mp3")
        translation_to_play = Path().cwd() / "translation.mp3"
        playsound(translation_to_play)
        sleep(1)