
class Mensaje:

	from datetime import datetime
	now = datetime.time

def __init__(self, contacto, contenido):
	self.contacto=str(contacto)
	self.contenido=str(contenido)
	time=now + timedelta(minutes=3)

contacto=""
contenido=""

def set_contacto(contacto):
	contacto=str(contacto)

def set_contenido(contenido):
	contenido=str(contenido)

def get_contacto():
	return str(contacto)

def get_contenido():
	return str(contenido)

def get_time_to_send():
	now = now +timedelta(minutes=3)
	return now