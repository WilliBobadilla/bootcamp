"""autor: Williams Bobadilla
   fecha de creacion: 24-enero-2019
   fecha de ultima edicion: 
   Descripcion: código para la primera practica del bootcamp. Manejo de leds, led intermitente (blink)

"""


import RPi.GPIO as gpio  	 # libreria para utilizar los puertos de entrada y salida
from time import sleep


led1=23      					 #definimos los pines de GPIO a utilizar


gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi (Broadcom SOC channel)
 
gpio.setup(led1,gpio.OUT)       #configuramos los puertos conectados a los leds como salida


while True:
	gpio.output(led1,True)     #encendemos el led1
	sleep(1)                   # pausa de un segundo
	gpio.output(led1,False)    #apagamos el led1
	sleep(1)                   # pausa de un segundo

	#Este programa finaliza cuando hay una interrupcion por teclado, CTRL+C
		