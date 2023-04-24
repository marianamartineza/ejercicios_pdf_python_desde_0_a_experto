#Dada la siguiente lista [12, 23, 5, 29, 92, 64] realiza las siguientes operaciones y vete mostrando
#la lista resultante por pantalla:

lista = [12, 23, 5, 29, 92, 64]

#1. Elimina el último número y añádelo al principio.

item = lista[-1]
lista.pop()
lista.insert(0,item)
print(lista)

#2. Mueve el segundo elemento a la última posición.
item = lista[1]
lista.remove(item)
lista.append(item)
print(lista)

#3. Añade el número 14 al comienzo de la lista.
lista.insert(0,14)
print(lista)

#4. Suma todos los números de la lista y añade el resultado al final de la lista.

sumador=0
for item in lista:
    sumador+=item

lista.append(sumador)
print(lista)

#5. Comina la lista actual con la siguiente: [4, 11, 32]

lista2=[4, 11, 32]

lista.extend(lista2)
print(lista)

#6. Elimina todos los números impares de la lista.
lista2=[ ]

for item in lista:
    if item%2==0:
        lista2.append(item)

lista.clear()
lista.extend(lista2)
print(lista)

#7. Ordena los números de la lista de forma ascendente.

lista.sort()
print(lista)

#8. Vacía la lista.

lista.clear()
print(lista)

#ejercicio 2
lista1=[]

print("Ingrese 5 numeros de la lista 1: ")
for i in range (1,6):
    num=int(input("Ingrese numero "+str(i)+" :"))
    lista1.append(num)

lista2=[]

print("Ingrese 5 numeros de la lista 2: ")
for i in range (1,6):
    num=int(input("Ingrese numero "+str(i)+" :"))
    lista2.append(num)

lista=[]

for item1 in lista1:
    for item2 in lista2:
        if item1==item2:
            lista.append(item1)
print(lista)
