#creamos un archivo nuevo 
#guardamos en la carpeta del repositorio
#con la extension .py
#uso de numeros aleatorios

#importamos la libreria randint
from random import randint 
aleatorio=randint(0,20) #creamos una variable 
#y generamos un numero aleatorio entre 0 y 20
print(aleatorio) #imprimimos el numero generado
#ejercicio 
# escribir una funcion sorteo() que reciba 
# una lista de participantes, y elegir a uno 
#de los participantes aleatoriamente, y 
# retornar esa persona elegida 
#desafio: no volver a retornar una persona
#  ya sorteada

#soluciones 
#importamos la funcion randint de libreria random
from random import randint 
def sorteo_fin_de_anho(lista): #definimos una funcion
    #utilizamos len() para saber la cantidad de personas 
    # que hay en la lista y guardamos en cant
    #para que no salga del rango
    cant=len(lista)-1 
    indice=randint(0,cant) #generamos un indice aleatorio
    #seleccionamos un elemento de la lista
    #y guardamos en variable ganador
    ganador=lista[indice] 
    return ganador   #retornamos ganador
    print(ganador)  #esto no se ejecuta
#creamos la lista de los participantes
participantes=["Kami","Lucas","Vale","Sarita","Fede"]
#llamamos a la funcion y guardamos en una variable 
#el resultado retornado por la funcion
ganar=sorteo_fin_de_anho(participantes)
print(ganar)#imprimimos el ganador 
