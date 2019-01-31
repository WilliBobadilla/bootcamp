
# _*_ coding: utf-8 -*-

"""autor: Williams Bobadilla
   fecha de creacion: 24-enero-2019
   fecha de ultima edicion: 27-enero-2019
   Descripcion: código para la primera practica del bootcamp. Manejo de leds, secuenciador de luces 1

"""


import RPi.GPIO as gpio  	 # libreria para utilizar los puertos de entrada y salida
from time import sleep


led1=23       #definimos los pines de GPIO a utilizar
led2=24
led3=25

gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi
 
gpio.setup(led1,gpio.OUT)       #configuramos los puertos conectados a los leds como salida
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)

while True:
	gpio.output(led1,True)     #encendemos el led1
	sleep(1)                   # pausa de un segundo
	gpio.output(led2,True)    #encendemos el led2 
	sleep(1)                   # pausa de un segundo
	gpio.output(led3,True)     #encendemos el led3
	sleep(1)
	gpio.output(led1,False)     #apagamos el led1
	sleep(1)                   # pausa de un segundo
	gpio.output(led2,False)    #apagamos el led2 
	sleep(1)                   # pausa de un segundo
	gpio.output(led3,False)     #apagamos el led3
	sleep(1)

	#Este programa finaliza cuando hay una interrupcion por teclado, CTRL+C
gpio.cleanup()
