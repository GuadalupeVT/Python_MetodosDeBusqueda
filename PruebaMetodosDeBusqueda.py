'''
Created on 29/11/2018

@author: GVT
'''
import random
import copy
from time import time

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
    comparaciones=0
    recorridos=0
    start_time = time()
    pos=0
    encontrado=False
    while pos<len(unaLista)and not encontrado:
        comparaciones=comparaciones+1
        if unaLista[pos]==datoBuscar:
            encontrado=True
        else:
            pos=pos+1
        recorridos=recorridos+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Comparaciones: "+str (comparaciones))
    return encontrado

def busquedaBinaria(unaLista,elemento):
    primero=0
    ultimo=len(unaLista)-1
    comparaciones=0
    recorridos=0
    start_time = time()
    while(primero<=ultimo):
        comparaciones=comparaciones+1
        recorridos=recorridos+1
        centro=int ((primero+ultimo)/2)
        valorCentro=unaLista[centro]
        
        if(elemento==valorCentro):
            comparaciones=comparaciones+1
            elapsed_time = time() - start_time
            print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
            print ("Recoridos: "+str (recorridos))
            print ("Comparaciones: "+str (comparaciones))
            return centro
        elif elemento<valorCentro:
            comparaciones=comparaciones+1
            ultimo=centro-1
        else:
            primero=centro+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Comparaciones: "+str (comparaciones))
    return -1

class has_table:
    def __init__(self):
        self.table=[None]*127
        
    def Hash_func(self,value):
        key=0
        for i in range (0,len(value)):
            key+=ord(value[i])
        return key%127
    
    def Insert(self,value):
        hash=self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash]=value
        
    def Search(self,value):
        hash=self.Hash_func(value)
        if self.table[hash] is None:
            return "No se encontro el elemento!"
        else:
            return "Se encontro el elemento!"
    

menu=0
arregloDesordenado = [0]  * 1000
for i in range(1000):
    arregloDesordenado[i] = random.randint(0, 100)
while(menu!=4):
    print ("_________MENU__________")
    print ("1. Busqueda Secuencial")
    print ("2. Busqueda Binaria")
    print ("3. Funciones Hash")
    menu=int(input("4.Salir"))
    
    if menu==1:
        datoBuscar=int (input("Ingresa dato a buscar"))
        if(busquedaSecuencial(copy.copy(arregloDesordenado), datoBuscar)):
            print("Dato encontrado")
        else:
            print("Dato no encontrado!")
    if menu==2:
        datoBuscar=int (input("Ingresa dato a buscar"))
        arr=copy.copy(arregloDesordenado)
        ordenamientoPorInsercion(arr)
        if(busquedaBinaria(arr,datoBuscar)!=-1):
            print("Dato encontrado!")
        else:
            print("Dato no encontrado!")
    if menu==3:
        H=has_table()
        arr=copy.copy(arregloDesordenado)
        for i in range (0,len(arr)):
            H.Insert(str(arr[i]))
        datoBuscar=str (input("Ingresa dato a buscar"))
        start_time = time()
        print(H.Search(datoBuscar))
        elapsed_time = time() - start_time
        print("No hace recorridos ni comparaciones")
        print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    