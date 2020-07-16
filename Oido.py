"""
	Esta implementación permite el ingreso por voz a Shelby


"""
import os
import random
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import Voz




#Escucha a través del microfono y devuelve lo escuchado o su aproximado en string
def listen():
		my_words="espera"
		r = sr.Recognizer()
		with sr.Microphone() as source:
			Voz.say("Te estoy escuchando")
			print("Esperando al usuario")
			audio = r.listen(source)
			print("escuchado")
			try:
				text = r.recognize_google(audio, language = "es-ES")
				print("convertido a texto")	
				my_words=str(text)
				print("Dijiste: {}".format(text))
			except:
				Voz.say("Lo siento, no logré escucharte")
				print("No pude escucharte")
				my_words="ExcepcionVacia" 
		return my_words
