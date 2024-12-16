# -*- coding: utf-8 -*-
"""
Created on Sun May 28 08:16:18 2023

@author: Gabo0
"""

""" ------------------------ FUNCIONES DE PRIMER ORDEN------------------------------------"""

def multiplicar(num1,num2):
    return num1*num2

print(multiplicar(3,2))

#Determinar valor por defecto, siempre al final del
def multiplicar(num1,num2=2):
    return num1*num2

print(multiplicar(3))


"""Retornar"""
def elemento_quimico(símbolo):
    elementos = {'H':'1-Hidrógeno', 'He':'2-Helio', 'Li':'3-Litio'}
    elemento = elementos[símbolo]
    lista = elemento.split('-')
    return (lista[0], lista[1])

num_atomico, denomina = elemento_quimico('He')
print('Núm. Atómico:', num_atomico)
print('Denominación:', denomina)

"""------------------------------- PÁRAMETROS ARBITRARIOS -------------------------------"""

"""CASO 1.
Estos argumentos llegarán a la función en forma de LISTA. Si una función espera
recibir parámetros fijos y arbitrarios, los arbitrarios siempre deben suceder a los
fijos."""

#Con el asterico se toma ese elemento o los elementos como listas
def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print (parametro_fijo)
    for argumento in arbitrarios:
        print (argumento)

recorrer_parametros_arbitrarios('Fixed', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3')


#Con el doble asterico se toma ese elemento o los elementos como diccionarios
"""CASO 2.
Como diccionario."""
def varios(param1, param2, **otros):
    for i in otros.items():
        print (i)
        print (param1)
        print (param2)
varios(1, 2, tercero = 3)
#En el diccionario hay que pasar clave(solo un string) = valor (puede ser un
#numero o un string).}


"""Funcionaes lambda"""

print((lambda x:x*2)(3))

"""Funciones de alto orden"""

"""• map (func, lista) → Devuelve una lista aplicando func a cada elemento.
• reduce (func, lista, (primero)) → Devuelve un valor aplicando la
operación binaria func.
• filter (pred, lista) → Devuelve una lista filtrando con el predicado."""
#Ejemplo map:
lista=[2,4,6,8]
print(list(map(lambda x:x*2,lista)))
#Para que devuelva la lista debemos castear.

"""reduce (func, lista, (primero)) → Devuelve un valor aplicando la operación
binaria func.
• filter (pred, lista) → Devuelve una lista filtrando con el predicado.
Ejemplo reduce:"""

import functools
lista=[2,4,6,8]
print(functools.reduce(lambda x,y:x+y,lista))

"""• filter (pred, lista) → Devuelve una lista filtrando con el predicado.
Ejemplo filter:"""
def positivos(numeros):
    return list(filter(lambda n: n >= 0, numeros))
print (positivos([2,3,-4,5,6]))

