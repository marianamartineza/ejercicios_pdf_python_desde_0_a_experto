#ejercicio 1
num=int(input("Ingrese un numero: "))

if num>0:
    print("Es un numero positivo")
elif num==0:
    print("Es igual a cero")
else:
    print("Es un numero negativo")

#ejercicio 2
num1=int(input("Ingrese numero 1: "))
num2=int(input("Ingrese numero 2: "))

sumador=0

for i in range(num1,num2+1):
    sumador+=i

print("Resultado: "+str(sumador))

#ejercicio 3
num1=int(input("Ingrese numero 1: "))
num2=int(input("Ingrese numero 2: "))

sumador_pares=0
sumador_impares=0

for i in range(num1,num2+1):
    if i%2==0:
        sumador_pares+=i
    else:
        sumador_impares+=i

total=sumador_pares+sumador_impares

print("Pares: "+str(sumador_pares))
print("Impares: "+str(sumador_impares))
print("Total: "+str(total))

#ejercicio 4
usuario=input("Ingrese su nombre de usuario: ")
contrasena=input("Ingrese su contrasena: ")

if usuario == "root" and contrasena == "toor":
    print("¡Bienvenido!")
else:
    print("Acceso fallido")

#ejercicio 5
intentos = 3

while intentos>0 and intentos<=3 :
    usuario=input("Ingrese su nombre de usuario: ")
    contrasena=input("Ingrese su contrasena: ")

    if usuario == "root" and contrasena == "toor":
        print("¡Bienvenido!")
        break
    else:
        intentos-=1
        print("Datos Incorrectos. Le quedan "+str(intentos)+" intentos")

        if intentos==0:
            print("Acceso Fallido")
            break

#ejercicio 6
mayor=-9999999

for i in range(1,6):
    num=int(input("Ingrese numero " + str(i) + ": "))
    if num>mayor:
        mayor=num

print("El mayor de todos los numeros es: " + str(mayor))

#ejercicio 7

temp = " "
cont=0
mayor=-9999999

while temp != "fin":
    cont+=1
    temp=input("Ingrese numero "+ str(cont)+" :")

    if temp != "fin":
        num=int(temp)
        if(num>mayor):
            mayor=num
    else:
        print("El mayor de todos los numeros es: "+str(mayor))
        break
