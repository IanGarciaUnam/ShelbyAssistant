
import pywhatkit as kit
import Voz
import Mensaje
from datetime import datetime,timedelta


kit.add_driver_path("/home/iangarcia/Documentos/Shelby/resources/chromeDriver/chromedriver")



#Nos envía la ayuda necesaria para esta versión de pywhatkit
def help():
	kit.help()

#Abre el navegador y reproduce en youtube el primer video relacionado a este
def play_on_yt(busqueda):
	kit.playonyt(str(busqueda))

def search(busqueda):
	kit.search(str(busqueda))#Will give information about the topic

def send_whats(contacto, contenido):
	now = datetime.now()
	#sendwhatmsg("contacto", "mensaje", hora de envio, minuto de envio )
	now= now + timedelta(minutes=3)
	kit.sendwhatmsg(str(contacto), str(contenido), now.hour, now.minute)

