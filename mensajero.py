from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import settings
import platform
import pywhatkit as kit

'''
For each time that we init our programawe should know what OS we're using, 
so, It just gonna be adjusted when it start
'''
driver =webdriver.Chrome()
def iniciar_mensajero():
	# Checks if on Mac or Windows
    print("Opening Chrome")
    if platform.system() == "Windows":
        driver = webdriver.Chrome('chromedriver.exe')
    else:
       	driver = webdriver.Chrome('/home/iangarcia/Documentos/Shelby/resources/chromeDriver/chromedriver')


def send_whatssapp_message(friend_name):
	settings.friend_name=friend_name
# Opens Whatsapp
	driver.get('https://web.whatsapp.com/')
	# Waits for you to scan the whatsapp QR code
def page_load():
	get_users = driver.find_elements_by_xpath("//*[contains(text(), '" + settings.friend_name + "')]")
	if len(get_users) > 0:        # waits 4 seconds to make sure page is loaded
		sleep(4)
		get_users[0].click()
		settings.found_page = 1
#Send messages from our own file
def start_sending_messages(my_script, iteraciones):
	settings.script=my_script
	settings.iterations=iteraciones
	print("Starting messages...")
	with open(settings.script, "r") as f:
		for line in f.readlines():
			for i in range(settings.iterations):
				for word in line.split():
					print("Sending: " + word)
					# Types words and submits
					actions = ActionChains(driver)
					actions.send_keys(word, Keys.ENTER)
					actions.perform()
					sleep(float(settings.delay))
def sending_message(mensaje):
	message=str(mensaje)
	print("Sending" + message)
	actions= ActionChains(driver)
	actions.send_keys(message, Keys.ENTER)
	actions.perform()
	sleep(float(settings.delay))

def mensajea_por_whatsapp_directo(nombre_contacto, mensaje, iteraciones):
	nombre_contacto=str(nombre_contacto)
	mi_mensaje=str(mensaje)
	mis_iteraciones=int(iteraciones)
	send_whatssapp_message(nombre_contacto)
	page_load()
	while settings.found_page==0:
		page_load()
		print("PLEASE SCAN QR CODE WITH PHONE")
		sleep(2)
	for i in range(mis_iteraciones):
		sending_message(mi_mensaje)






#Envia mensajes desde un archivo de Texto
def mensajea_por_whatssapp(nombre_del_contacto, archivo, iteraciones):
	nombre_contacto=str(nombre_del_contacto)
	nombre_archivo=str(archivo)
	
	send_whatssapp_message(nombre_contacto)#Busca el contacto en Whatssapp Web
	page_load()
	while settings.found_page == 0:
          	page_load()
          	print("PLEASE SCAN QR CODE WITH PHONE")
          	sleep(2)
	start_sending_messages(nombre_archivo, int(iteraciones))

def send_message_by_messenger(friend):
	settings.friend_name=str(friend)
	# Opens Facebook Messenger
	settings.source='Messenger'
	driver.get('https://www.messenger.com/')
	sleep(5)
	# Login
	driver.find_element_by_xpath('//*[@id="email"]').send_keys(settings.username_email)
	driver.find_element_by_xpath('//*[@id="pass"]').send_keys(settings.password)
	sleep(10)
	driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
	# Waits 8 seconds to finish loading page
	print("Waiting for a few seconds...")
	sleep(8)
	if settings.source != "Whatsapp":
		driver.find_element_by_xpath("//*[contains(text(), '" + settings.friend_name + "')]").click()
	if settings.source == "Messenger":
		driver.refresh()
		sleep(5)
	sending_message("Hola paps, ai loviu")

send_message_by_messenger('Carlos Andrade Hdez')