"""autor: Williams Bobadilla
   fecha de creacion: 27-enero-2019
   fecha de ultima edicion: 27-enero-2019 
   Descripcion: código para la primera practica del bootcamp. Manejo de leds, secuenciador de luces 2

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

lista=[led1,led2,led3]          #creamos una lista con los leds que tenemos

while True:
	for i in range(len(lista)):       #recorremos la lista, len(lista) devuelve el tamaño de la lista
		gpio.output(lista[i],True)    # seleccioamos los leds con lista[i], donde i es la posicion del led a seleccionar, encendemos en este caso
		sleep(1)                      #pausa de 1 segundo
	for i in range(len(lista)):
		gpio.output(lista[i],False)   # con esto vamos apagando los leds
		sleep(1)

	


	#Este programa finaliza cuando hay una interrupcion por teclado, CTRL+C