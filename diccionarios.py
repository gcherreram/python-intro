# -*- coding: utf-8 -*-
"""
Created on Sat May 27 10:22:21 2023

@author: Gabo0
"""

clase = {}

mi_diccionario = {'SVG':'Fotos1','AD':'Fotos3'}

for clave in mi_diccionario:
    print(clave,":",mi_diccionario[clave])
    
#Validar si una llave existe en el diccionario
clave in mi_diccionario

#Añadir elemento al diccionario
clase['clave nueva'] ='valor nuevo'

#Borrar elementos
del mi_diccionario[clave]

#Borrar contenido del diccionario pero dejandolo instanciado
mi_diccionario.clear()

#borrar diccionario entero
#del mi_diccionario


"""------------------------ FOR PARA DICCIONARIOS ------------------------"""

for clave in mi_diccionario:
    print(clave, ":", mi_diccionario[clave])

#Usando el método items(), obtenemos una lista de tuplas (clave, valor),
#que podemos usar en el for:

for(clae,valor) in mi_diccionario.items():
    print(clave,":",valor)
    

#Usando enumerate se puede obtener el indice de posición junto a su clave correspondiente:
for i, v in enumerate(mi_diccionario):
    print(i,v)
    
"""------------------------ ORDENACIÓN PARA DICCIONARIOS ------------------------"""

# POR CLAVES
sorted(mi_diccionario)
sorted(mi_diccionario, reverse=True)
print(clave,":", mi_diccionario[clave])

# POR SUS VALORES
from operator import itemgetter
compra ={'leche':2.19,'pan':3.09,'cafe':4.59,'huevos':1.79}
print(sorted(compra.items(), key=itemgetter(1)))


"""------------------------ CASO PRÁCTICO 1 ------------------------"""

print("La palabra más larga")
palabra = input("Dime una palabra (Intro para salir): ").lower()
longitudMax = 0

while (palabra.isalpha()):
    palabra = input("Dime una palabra: ")
    if len(palabra) > longitudMax:
        palabraMax = palabra
        longitudMax = len(palabra)
    
print("Y la palabra más larga es ... !"+ palabraMax + "!")