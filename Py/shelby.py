
"""
Motor de acciónes principales para Shelby

"""

import Voz	as voice
import Oido as ears
import tiempo as time
#import Manos as hands
from slugify import slugify #normaliza strings

voice.into_start()
voice.say('Iniciando sistema')
date=str(time.get_local_date())
tempo=str(time.get_local_time())
voice.say('Hoy es:'+ date)
voice.say('Son las:'+tempo)
voice.greet()
'''
comando=str(ears.listen()).lower()
comando_limpio=slugify(comando)#Normaliza la cadena de texto ingresada
lista_de_palabras=comando_limpio.split(" ")
print(lista_de_palabras)

voice.say("dijiste"+comando)

if 'busca' in lista_de_palabras:
	lista_de_palabras.remove('busca')
	hands.search(lista_de_palabras)

#if 'musica' in lista_de_palabras or 'videos'in lista_de_palabras or 'video' in lista_de_palabras:
print("ejecutando a yt")
hands.play_on_yt(comando)
'''




