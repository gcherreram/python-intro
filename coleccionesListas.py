# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:37:22 2023

@author: Gabo0
"""
"""---------------------Caso practico 1----------------------------"""

cadena = input("Introduce una cadena: ")
vocales = ["a","e","i","o","u"]

for i in cadena:
    if i in vocales:
        print("El valor %s una vocal"%(i))
    else:
        print("El valor %s una consonante"%(i))
        

"""---------------------Caso practico 2----------------------------"""

lista = ["Madrid", "Malaga", "Barcelona"]

for i in lista:
    if i.lower().startswith('m'):
        print(i)
        
        
"""---------------------Caso practico 3----------------------------"""

lista = [2,3,4,5,6,7,10]
pares=[]

for i in lista:
    if i%2==0:
        pares.append(i)

print("Lista original", lista)
print("Lista de números pares", pares)

"""---------------------Caso practico 4----------------------------"""

lista = ["SGE",3.0,["A","B"],10,"FINAL"]

print(type(lista[2][1]))
print (lista[2][1])
print (lista[0:3:1])
print (lista[0:4])
lista[2][2]="z"
