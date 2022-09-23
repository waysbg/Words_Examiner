from random import choice
from ast import literal_eval
from gtts import gTTS
from playsound import playsound
from pathlib import Path
from time import sleep
from deep_translator import GoogleTranslator

def play_string(string_toplay: str, language: str, exported_sound_name: str):
    sound_to_play = gTTS(text=string_toplay, lang=language)
    sound_to_play.save(exported_sound_name)
    sound_to_play = Path().cwd() / exported_sound_name
    playsound(sound_to_play)

welcome = Path().cwd() / "welcome.mp3"
playsound(welcome)
sleep(1)

translator = GoogleTranslator(source='en', target='bg')

file = open("dictionary.txt")
data = file.read()
data = literal_eval(data)
english_words = list(data)


while True:
    picked_word = choice(english_words)
    play_string(picked_word, "en", "word.mp3")
    decision = str(input(f"[t]ranslate, [n]ext or [e]xit           {picked_word}? "))

    if decision == "e":
        break
    elif decision == "t":
        translation = translator.translate(picked_word)
        print(f"{' ' * 40}{translation}\n")
        play_string(translation, "bg", "translation.mp3")
