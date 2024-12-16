import pandas as pd

count = 0

while count < 5:
    print(count, ' is Less than 5')
    count = count +1


"""Contador en for range primera forma"""

for contador in range(5):
    print(contador)
    

"""Contador en for range segunda forma"""
"""El primer digito marca el inicio, el segundo marca el final"""

for contador in range(3,10):
    print(contador)

"""Contador en for range segunda forma"""
"""El primer digito marca el inicio, el segundo marca el final y el tercero representa el salto"""

for contador in range(0,30,3):
    print(contador)
    
    
"""----------------------------CASO PRACTICO 1--------------------------"""
i = 1
h = ''
while i<=25:
    if i%2 != 0:
        h += ' %i' % i
    i+=1
print(h)


"""----------------------------CASO PRACTICO 2--------------------------"""
cont = 0
for i in range(0,5):
    numero = float(input("Introduce un numero: "))
    cont = cont+numero
media=cont/5

print("La media es %.2f"%(media))


"""----------------------------CASO PRACTICO 3 V1--------------------------"""
valor = 0
cont = int(input("Cuantos valores deseas introducir: "))
for i in range(0,cont):
    numero = float(input("Introduce un numero: "))
    if numero < 0:
        valor += 1

print("Los números negativos son %.f"%(valor))

"""----------------------------CASO PRACTICO 3 V2--------------------------"""
numero = int(input("Cuantos valores deseas introducir: "))
i = 0
cont = 0
while i<=numero:
    valor=int(input("Valores a comprobar: "))
    if valor < 0:
        cont += 1
    i += 1
    

print("El número de valores negativos es", cont)

"""----------------------------CASO PRACTICO 4--------------------------"""
for i in range(1,21):
    print(i,end=' ')
    
