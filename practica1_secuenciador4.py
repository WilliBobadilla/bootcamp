#_*_ coding: utf-8 _*_



"""autor: Williams bobadilla
   fecha de creacion: 27-enero-2019
   fecha de ultima edicion: 27-enero-2019 
   Descripcion: código para la primera practica del bootcamp. Manejo de leds, secuenciador de luces 4,
    encendido de un led a la vez, es el mismo codigo que el anterior a diferencia que se hace con ciclos

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

lista=[led1,led2,led3]          #creamos una lista con los leds 



while True:
	for i in range(len(lista)):         
		if i>0:
			gpio.output(lista[i-1],False)         #apagamos el led anterior al i
			gpio.output(lista[i],True)            #encendemos el led en la posicion i
		else: 
			gpio.output(lista[i],True)
		sleep(1)                                  #pausa de 1 segundo 
	gpio.output(lista[i],False)
	#Este programa finaliza cuando hay una interrupcion por teclado, CTRL+C
