
# _*_ coding: utf-8 _*_



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
 
gpio.setup(buzzer,gpio.OUT)       #configuramos los puertos conectador a los leds como salida

tono=gpio.PWM(buzzer,1000)        # inicializamos el objeto tono en el pi del buzzer , ademas especificamos la frecuencia 

tono.start(0)             #        comenzamos con el 0 %del ciclo de trabajo              
lista=[15,25,45,60,75]

while True:
     for i in range(len(lista)):    
         tono.ChangeDutyCycle(lista[i])     # cambiamos el ciclo de trabajo 
	 sleep(1)
	

