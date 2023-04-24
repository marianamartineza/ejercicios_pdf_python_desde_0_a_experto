#ejercicio 1

def esPrimo(a):
    primo=True

    for i in range (2,a):
        if a%i==0:
            primo=False
            break
    return primo


num=int(input("Ingrese el numero: "))

if esPrimo(num) == True:
    print("El numero es primo")
else:
    print("El numero no es primo")

#ejercicio 2

import random

def respuesta(num,usuario):

    if usuario<num:
        print("El numero es mas alto")
    elif usuario>num:
        print("El numero es mas bajo")
    else:
        print("¡Acertaste!")


num=random.randint(1,10)
print("Numero aleatorio generado!")

max_intentos=3
cont=0

while cont<max_intentos:
    cont+=1
    print("\n Intento " + str(cont))
    usuario=int(input("\n Ingrese el numero: "))
    respuesta(num,usuario)

#Ejercicio 3

def enRango(num):
    return num in range(1,21)

def enLista(num):
    lista=[6,14,11,3,2,1,15,19]
    return num in lista


num=int(input("Ingrese el numero: "))
print("num 1-20: "+ str(enRango(num)))
print("Dentro de la lista: "+ str(enLista(num)))
