#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""autor: Williams bobadilla
   fecha de creacion: 24-enero-2019
   fecha de ultima edicion: 
   Descripcion: Es un codigo para la lectura del sensor de temperatura Dht_22


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

from time import sleep
import Adafruit_DHT as dht   #renombramos la libreria com dht
import RPi.GPIO as gpio  	 # libreria para utilizar los puertos de entrada y salida


     				
gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi


def DHT22_data():
	# leemos los datos del sensor, la humedad y la temperatura
	humi, temp = dht.read_retry(dht.DHT22, 23)    #pin data conectado al GPIO23, si se usa el DHT11, usamos dht.DHT11
	return humi, temp 

while True:
	try:
		humedad,temperatura=DHT22_data()               						    # llamamos a una funcion que nos retorna los datos del sensor

		if humedad is not None and temperatura is not None:    					#comprobamos si hay datos, si hay hacemos esto 
			print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperatura, humedad)) #str.format() es utilizado 
                                                                                       #el numero entre la llaves es la posicion de la variable a mostar
		else:
			print ("Error en la lectura del sensor")
		# esperamos un tiempo para volver a leer el sensor, lo recomendable es 2 segundos como minimo
		sleep(20)
	except KeyboardInterrupt:  											 # Se ha pulsado CTRL+C!!
		 gpio.cleanup()          										 # Limpiamos los pines GPIO y salimos	
		 print("Programa terminado")
		 break          												 # con esto finalizamos por completo el programa
		
