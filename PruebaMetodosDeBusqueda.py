'''
Created on 29/11/2018

@author: GVT
'''
def busquedaSecuencial(unaLista,datoBuscar):
    pos=0
    encontrado=False
    
    while pos<len(unaLista)and not encontrado:
        if unaLista[pos]==datoBuscar:
            encontrado=True
        else:
            pos=pos+1
    return encontrado

listaPrueba=[1,2,32,8,17,19,42,13,0]
print (busquedaSecuencial (listaPrueba,32) )