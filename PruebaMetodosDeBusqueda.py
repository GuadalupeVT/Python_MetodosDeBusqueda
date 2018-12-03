'''
Created on 29/11/2018

@author: GVT
'''
import random
import copy
def busquedaSecuencial(unaLista,datoBuscar):
    pos=0
    encontrado=False
    
    while pos<len(unaLista)and not encontrado:
        if unaLista[pos]==datoBuscar:
            encontrado=True
        else:
            pos=pos+1
    return encontrado

def busquedaBinaria(self,unaLista,elemento):
    primero=0
    ultimo=len(unaLista)-1
    while(primero<=ultimo):
        centro=int ((primero+ultimo)/2)
        valorCentro=unaLista(centro)
        print("Comparando "+str(elemento)+" con "+str(unaLista[centro]))
        
        if(elemento==valorCentro):
            return centro
        elif elemento<valorCentro:
            ultimo=centro-1
        else:
            primero=centro+1
    return -1
        
        

menu=0
arregloDesordenado = [0]  * 1000
for i in range(1000):
    arregloDesordenado[i] = random.randint(0, 100)
while(menu!=2):
    print ("_________MENU__________")
    print ("1. Busqueda Secuencial")
    menu=int(input("2.Salir"))
    
    if menu==1:
        datoBuscar=int (input("Ingresa dato a buscar"))
        print (busquedaSecuencial(copy.copy(arregloDesordenado), datoBuscar))
    