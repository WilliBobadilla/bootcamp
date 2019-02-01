#_*_ coding:utf-8 _*_

"""autor: Williams bobadilla
   fecha de creacion: 28-enero-2019
   fecha de ultima edicion: 28-enero-2019 
   Descripcion: código para la segunda practica del botcamp, manejo de pulsador, 
   encendido y apagamos de de varios leds, control mediante un boton, cada vez que 
   se presiona el boton, es debe de encender un led a la vez, hasta apagarse, si se vuelve
   a presionar luego de apagarse todos los leds, se vuelve a encender el primer led, y asi sucesivamente
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
gpio.setup(entrada,gpio.IN)     #configuramos como entrada

contador=0                      #variable para manejo de los leds


while True:                             
   if gpio.input(entrada):              #si se presiona es True, entra en esa linea  
	  contador=contador+1               #aumentamos la variable contador
	  sleep(0.3)                         #agregamos una pausa para evitar que sume muy rapido
	  if contador==4:					#como solo tenemos 3 leds, contador debe tomar los valores 0,1,2
	  	 contador=0				 		#pero usamos el 3 para apagar todos los leds
	  	 						        #reinicimamos al primer led

   if contador==0:
   	  gpio.output(led1,True)            #encendemos el led 1
   	  gpio.output(led2,False)
   	  gpio.output(led3,False)
  
   if contador==1:
   	  gpio.output(led1,False)
   	  gpio.output(led2,True)           #encendemos el led 2
   	  gpio.output(led3,False)
  
   if contador==2:
   	  gpio.output(led1,False)
   	  gpio.output(led2,False)           #encendemos el led 3
   	  gpio.output(led3,True)

   if contador==3:
   	  gpio.output(led1,False)
   	  gpio.output(led2,False)           #apagamos todos los leds
   	  gpio.output(led3,False)
