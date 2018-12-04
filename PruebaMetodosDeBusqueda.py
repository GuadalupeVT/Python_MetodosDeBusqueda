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
            return None
        else:
            print("Se encontro el elemento en")
            return id(self.table[hash])
    

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
        print (busquedaSecuencial(copy.copy(arregloDesordenado), datoBuscar))
    if menu==2:
        datoBuscar=int (input("Ingresa dato a buscar"))
        arr=copy.copy(arregloDesordenado)
        ordenamientoPorInsercion(arr)
        a=busquedaBinaria(arr,datoBuscar)
        if(a!=-1):
            print("Dato encontrado!")
    if menu==3:
        H=has_table()
        arr=copy.copy(arregloDesordenado)
        for i in range (0,len(arr)):
            H.Insert(str(arr[i]))
        datoBuscar=str (input("Ingresa dato a buscar"))
        print(H.Search(datoBuscar))
    