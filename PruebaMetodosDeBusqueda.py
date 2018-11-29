'''
Created on 29/11/2018

@author: GVT
'''
import random
import copy
from getpass import _raw_input
def busquedaSecuencial(unaLista,datoBuscar):
    pos=0
    encontrado=False
    
    while pos<len(unaLista)and not encontrado:
        if unaLista[pos]==datoBuscar:
            encontrado=True
        else:
            pos=pos+1
    return encontrado
menu=0
arregloDesordenado = [0]  * 1000
for i in range(1000):
    arregloDesordenado[i] = random.randint(0, 100)
while(menu!=2):
    print ("_________MENU__________")
    print ("1. Busqueda Secuencial")
    menu=int(_raw_input("2. Salir"))
    
    if menu==1:
        datoBuscar=int(_raw_input("Ingresa dato a buscar"))
        busquedaSecuencial(copy.copy(arregloDesordenado), datoBuscar)
    