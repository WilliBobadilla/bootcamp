"""autor: Williams bobadilla
   fecha de creacion: 24-enero-2019
   fecha de ultima edicion: 
   Descripcion: Es un codigo para el proyecto final de clase, una mini incubadora que utiliza el sensor DHT22, una 
   raspberry pi y la plataforma thinsgpeak.com .
   
   Instrucciones para instalar la libreria
   Para descargar la libreria
   		git clone https://github.com/adafruit/Adafruit_Python_DHT.git
   Luego entrar al directorio 
   		cd Adafruit_Python_DHT
   Despues instalar las herramientas necesarias para la instalacion de la libreria
  	 sudo apt-get install build-essential python-dev
   por ultimo instalar la libreria 
   		sudo python setup.py install

  Con eso ya tenemos instalado la libreria


"""

import sys
import urllib.request 
from time import sleep
import Adafruit_DHT as dht   #renombramos la libreria com dht
import RPi.GPIO as gpio  	 # libreria para utilizar los puertos de entrada y salida

buzzer= 25     					# pin a conectar al led
gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi
gpio.setup(25, GPIO.OUT)  		# gpio N°25 usado como salida
# Acá debe ir el API KEY, dado por la plataforma
myAPI = '8QWHS6O1IKEOTWOU' 

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI # URL donde enviaremos los datos, no borrar esto!
def DHT22_data():
	# leemos los datos del sensor, la humedad y la temperatura
	humi, temp = dht.read_retry(dht.DHT22, 23) #puerto data conectado al GPIO23
	return humi, temp 

while True:
	try:
		humedad,temperatura=DHT22_data()  # llamamos a una funcion que nos retorna los datos del sensor
		# si la lectura es valida, hacemos todo esto
		while temperatura<24 or temperatura>27:  		#si no está en el rango normal, suena una alarma
			gpio.output(buzzer,True)			 # encendemos un led en modo de advertencia
			humedad,temperatura=DHT22_data()  # volvemos a leer los sensores
		
		gpio.output(buzzer,False)              #apagamos el aviso

		if isinstance(humi, float) and isinstance(temp, float):  #comprueba si hay datos del sensor
			#enviamos datos a la API, a thingspeak
			conn = urllib.request.urlopen(baseURL + '&field1=%s&field2=%s'  % (temperatura,humedad))
			print (conn.read())	
			conn.close()			#cerramos la conexion
		else:
			print ("Error en la lectura del sensor")
		# esperamos un tiempo para volver a leer el sensor
		sleep(20)
	except KeyboardInterrupt:   # Se ha pulsado CTRL+C!!
		 gpio.cleanup()          # Limpiamos los pines GPIO y salimos	
		 print("Programa terminado")
		 break          # con esto finalizamos por completo el programa
		