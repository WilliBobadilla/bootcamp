
#_*_ coding: utf-8 _*_


"""autor: Williams Bobadilla
   fecha de creacion: 27-enero-2019
   fecha de ultima edicion:  27-enero-2019
   Descripcion: código para la primera practica del bootcamp. Manejo de leds, secuenciador de luces 3, encendido de un led a la vez

"""


import RPi.GPIO as gpio  		 # libreria para utilizar los puertos de entrada y salida
from time import sleep


led1=23       					#definimos los pines de GPIO a utilizar
led2=24
led3=25

gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi 
 
gpio.setup(led1,gpio.OUT)       #configuramos los puertos conectados a los leds como salida
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)



while True:
	gpio.output(led1,True)
	gpio.output(led3,False)
	sleep(1)                   #encendemos el primer led y apagamos el tercero, en el primer ciclo no hace falta pero luego si
	gpio.output(led2,True)
	gpio.output(led1,False)   #encendemos el segundo led y apagamos el primero 
	sleep(1)
	gpio.output(led3,True)
	gpio.output(led2,False)     #encendemos el tercer led y apagamos el segundo
	sleep(1)

	#Este programa finaliza cuando hay una interrupcion por teclado, CTRL+C
