#ejercicio 1
numero=int(input("Ingrese numero: "))

for i in range(1,11):
    print(str(numero)+"*"+str(i)+"="+str(numero*i))

#ejercicio 2
num1=int(input("Ingrese numero 1: "))
num2=int(input("Ingrese numero 2: "))

print("Suma: "+ str(num1+num2))
print("Resta: "+str(num1-num2))
print("Multiplicacion: "+str(num1*num2))

if num2 != 0:
    print("Division: "+str(num1/num2))
else:
    print("No se puede dividir entre 0")

#ejercicio 3
pi=3.1416
radio = float(input("Ingrese el radio del circulo: "))
area=pi*radio*radio
print("Area del circulo "+str(area))