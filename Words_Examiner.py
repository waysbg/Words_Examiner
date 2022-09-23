from random import choice
from ast import literal_eval
from gtts import gTTS
from playsound import playsound
from pathlib import Path
from time import sleep

def play_string(string_toplay:str, language: str, exported_sound_name: str):
    sound_to_play = gTTS(text=string_toplay, lang=language)
    sound_to_play.save(exported_sound_name)
    sound_to_play = Path().cwd() / exported_sound_name
    playsound(sound_to_play)


welcome = Path().cwd() / "welcome.mp3"
playsound(welcome)
sleep(1)

file = open("dictionary.txt")
data = file.read()
dictionary = literal_eval(data)
english_words = list(dictionary.keys())

while True:
    picked_word = choice(english_words)
    play_string(picked_word, "en", "word.mp3")

    decision = str(input(f"[t]ranslate, [n]ext or [e]xit           {picked_word}? "))
    sleep(1)

    if decision == "e":
        break
    elif decision == "t":
        translation = dictionary[picked_word]
        print(f"{' ' * 40}{translation}\n")
        play_string(translation, "bg", "translation.mp3")
        sleep(1)