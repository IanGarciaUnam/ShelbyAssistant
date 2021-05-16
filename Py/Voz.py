import os
import random
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import tiempo as time
"""
 	Voz 
	Conversion de Texto a Voz motor del habla de shelby 


"""
def say(word:str):
	"""
	Litteraly , it says the String gotten
	"""
	my_word=str(word)
	tts=gTTS(my_word, lang = 'es-us')
	tts.save("resources/speaking.mp3")	
	playsound("resources/speaking.mp3")

def say_slow(word):
	my_word=str(word)
	tts=gTTS(my_word, lang = 'es-us', slow = True)
	tts.save("resources/speaking.mp3")	
	playsound("resources/speaking.mp3")

def save_audio(word):
	my_word=str(word)
	tts=gTTS(my_word, lang = 'es-us')
	tts.save("resources/saved.mp3")

def say_saved_audio():
	playsound("resources/saved.mp3")

def into_start():
	path='resources/starting/'
	songs_list=os.listdir(path)
	chosen=str(random.choice(songs_list))
	playsound(path+chosen)

def sing():
	path='resources/music/'
	songs_list=os.listdir(path)
	chosen=str(random.choice(songs_list))
	playsound(path+chosen)
def greet():
	if time.get_sun() == 'AM':
		saludo = open("resources/greeting/greeting_morning.txt","r")
		text=saludo.read().split(',')
		saludo.close()
		chosen=str(random.choice(text))
		say(chosen)
	if time.get_sun() == 'PM':
		saludo = open("resources/greeting/greeting_afternoon.txt","r")
		text=saludo.read().split(',')
		saludo.close()
		chosen=str(random.choice(text))
		say(chosen)