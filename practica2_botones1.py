"""autor: Williams bobadilla
   fecha de creacion: 28-enero-2019
   fecha de ultima edicion: 28-enero-2019 
   Descripcion: código para la segunda practica del botcamp, manejo de pulsador, 
   encendido y apagado de led

"""


import RPi.GPIO as gpio  		 # libreria para utilizar los puertos de entrada y salida
from time import sleep


led1=23       					#definimos los pines de GPIO a utilizar
led2=24
led3=25
entrada=22



gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi
 
gpio.setup(led1,gpio.OUT)       #configuramos los puertos conectados a los leds como salida
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)
gpio.setup(entrada,gpio.IN)     #configuramos como entrada el gpio 22

while True:
   if gpio.input(entrada):              #si se presiona es True, entra en la siguiente linea  
      gpio.output(led1, True)             
   else:
      gpio.output(led1, False)      