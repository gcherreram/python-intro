# -*- coding: utf-8 -*-
"""
Created on Sat May 27 09:23:06 2023

@author: Gabo0
"""

""" --------------- OPERADOR CONCATENAR ------------------"""

mensaje1 = 'Hola' + ' ' + 'Mundo'
print(mensaje1)

""" -------------- Multiplicar --------------------------- """

mensaje2a = 'Hola ' * 3
mensaje2b = 'Mundo'
print(mensaje2a+mensaje2b)

""" -------------- AÑADIR --------------------------- """

mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)


""" -------------- .FIND ENCONTRAR --------------------------- """

mensaje5a = "Hola Mundo"
mensaje5a = mensaje5a.find("Mundo")
print(mensaje5a)

""" -------------- .FIND ENCONTRAR --------------------------- """

mensaje7 = "Hola Mundo"
mensaje8 = mensaje7.replace("l","pizza")
print(mensaje8)

""" -------------- LONGITUD --------------------------- """

print(len(mensaje8))

""" -------------- STRIP, RSTRIP, LSTRIP --------------------------- """

#Elimina los espacios en blanco del inicio y del final

""" -------------- swapcase() --------------------------- """

#Devuelve una copia de la cadena con las máyusculas pasadas a minúsculas y viceversa

mensaje9 = "Hola Mundo"
mensaje10 = mensaje9.swapcase()
print(mensaje10)

""" -------------- title() --------------------------- """

#Devuelve una versión con formato título, es decir, con todas las palabras
#en minúsculas excepto la primera letra, que va en mayusculas

mensaje10 = "Hola MUNDO"
mensaje11 = mensaje10.title()
print(mensaje11)

""" -------------- endswith() --------------------------- """

#Devuelve el valor booleano si una cadena termina con una cadena especificada
S = "Hola Mundo"
print(S.endswith("do"))


""" -------------- startswith() --------------------------- """

#Devuelve el valor booleano si una cadena inicia con una cadena especificada

S = "Hola Mundo"
print(S.startswith("do"))
print(S.startswith("Hola"))

""" -------------------------------- CASO PRACTICO 1 ------------------------------------ """

linea = 'a: b: c: d: e: f:gh '

','.join(x.strip() for x in linea.split(':'))


""" -------------------------------- CASO PRACTICO 2 ------------------------------------ """

s = 'www.afuera.es'
i = s.split('.',1)
domain_name=i[1]
print(domain_name)

""" -------------------------------- CASO PRACTICO 3 ------------------------------------ """

Frutafresca = [' banana', ' mora de Logan ', 'maracuyá']

List = []

for i in Frutafresca:
    res=i.strip()
    List.append(res)

print(List)

""" -------------------------------- CASO PRACTICO 4 ------------------------------------ """

String = "blah, lots, of, spaces, here"
print(len(String))

a=String.split(',')
print(a)
print(len(a))

""" -------------------------------- CASO PRACTICO 5 ------------------------------------ """

Frase = "0000000000000000 es un ejemplo de string con zeros ¡!! 00000000"
print(Frase.strip('0'))
print(Frase.rstrip('0'))
print(Frase.lstrip('0'))

""" -------------------------------- CASO PRACTICO 6 ------------------------------------ """

linea = 'a: b: c: d: e: f:gh '

#resultado =linea.split(':')
#print(resultado)

print(','.join(linea.split(':')))

""" -------------------------------- CASO PRACTICO 7 ------------------------------------ """

cadena = "intro cadena"
vocales = ['a','e','i','o','u']
for i in cadena:
    if i in vocales:
        print(i, 'es una vocal')
    else:
        print(i, 'no es una vocal')
        
if 'la' in 'hola': print ('¡Está!')
