"""-----------------------------------Ejemplo 1--------------------------------------"""

edad=23
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Evaluar en linea

print('par' if edad % 2 ==0 else 'impar')

# Evaluar si un valor está entre varios posibles

tecla = 'S'

if tecla in('s','S','y','Y'):
    print('Ha seleccionado: Si')
else:
    print('Es falso')
    


#Evaluar variables booleanas

respuesta = True
if respuesta:
    print('Si, es verdad')
else:
    print('Es falso')
    

#Evaluar variables por tipo de dato que contienen 
var1 = "Python 3 para impacientes"
var2=3
var3=3.14
var4=True
if type(var1) is str:
    print("'var1' es una cadena")

if type(var2) is int:
    print("'var2' es un número entero")
    
if type(var3) is float:
    print("'var3' es un número float")
    
if type(var4) is bool:
    print("'var4' es un bool")




"""---------------------------Caso práctico 1-------------------------------"""

import random

num=random.randint(1,20)
print("El numero aleatorio generado es %f" %(num))

if num<10:
    print('El valor generado tiene un digito')
else:
    print('El valor generado tiene dos digitos')
    

"""---------------------------Caso práctico 2-------------------------------"""

print('Comparador de años')
fecha1=int(input('¿En que año estamos?:'))
fecha2=int(input('Escriba un años cualquiera:'))

if fecha1 > fecha2:
    print("Desde el año", fecha2, "han pasado", fecha2 - fecha1, "años")
    
if fecha1 < fecha2:
    print("Para llegar al año", fecha2, "faltan", fecha2 - fecha1, "años")
    
if fecha1 == fecha2:
    print("¡Son el mismo año!")


"""---------------------------Caso práctico 3-------------------------------"""


print('Comparador de valores')
valor1=int(input('Ingrese el primer valor:'))
valor2=int(input('Ingrese el segundo valor:'))

if valor1 > valor2:
    print("Segundo menor")
elif valor1 < valor2:
    print("primero menor")
else:
    print("Son iguales")

"""---------------------------Caso práctico 4-------------------------------"""

num=int(input('Ingrese un número:'))
print('El número es par' if num % 2 ==0 else 'El número es impar')