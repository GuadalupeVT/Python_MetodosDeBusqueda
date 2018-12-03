'''
Created on 29/11/2018

@author: GVT
'''
import random
import copy

def ordenamientoPorInsercion(numeros):
    for i in range(1,len(numeros)):
        aux=numeros[i]
        j=i-1
        while j>=0:
            if(aux<numeros[j]):
                numeros[j+1]=numeros[j]
                numeros[j]=aux
                j=j-1
            else:
                break

def busquedaSecuencial(unaLista,datoBuscar):
    pos=0
    encontrado=False
    
    while pos<len(unaLista)and not encontrado:
        if unaLista[pos]==datoBuscar:
            encontrado=True
        else:
            pos=pos+1
    return encontrado

def busquedaBinaria(unaLista,elemento):
    primero=0
    ultimo=len(unaLista)-1
    while(primero<=ultimo):
        centro=int ((primero+ultimo)/2)
        valorCentro=unaLista[centro]
        
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
while(menu!=3):
    print ("_________MENU__________")
    print ("1. Busqueda Secuencial")
    print ("2. Busqueda Binaria")
    menu=int(input("3.Salir"))
    
    if menu==1:
        datoBuscar=int (input("Ingresa dato a buscar"))
        print (busquedaSecuencial(copy.copy(arregloDesordenado), datoBuscar))
    if menu==2:
        datoBuscar=int (input("Ingresa dato a buscar"))
        arr=copy.copy(arregloDesordenado)
        ordenamientoPorInsercion(arr)
        a=busquedaBinaria(arr,datoBuscar)
        if(a!=-1):
            print("Dato encontrado!")  