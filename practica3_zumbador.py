"""autor: Williams bobadilla
   fecha de creacion: 28-enero-2019
   fecha de ultima edicion: 28-enero-2019 
   Descripcion: código para la segunda practica del botcamp, manejo de pulsador, 
   encendido y apagamos de de varios leds, control mediante un boton, cada vez que 
   se presiona el boton, es debe de encender un led a la vez, hasta apagarse, si se vuelve
   a presionar luego de apagarse todos los leds, se vuelve a encender el primer led, y asi sucesivamente.
   Este codigo es el mismo que el anterior a diferencia que es mas optimizado
"""

import RPi.GPIO as gpio  		 # libreria para utilizar los puertos de entrada y salida
from time import sleep


buzzer=25                 #conectado al gpio 25 



gpio.setmode(gpio.BCM) 			# modo BCM  de la raspberry pi
 
gpio.setup(buzzer,gpio.out)       #configuramos los puertos conectador a los leds como salida

tono=gpio.PWM(buzzer,100)        # inicializamos el objeto tono en el pin del buzzer con 

tono.start(5)                    # iniciamos el tono en 5 
while True: 
	tono.ChangeDutyCicle(15)     # cambiamos el ciclo de trabajo
	sleep(1)
	tono.ChangeDutyCicle(90)
	sleep(1)
	

