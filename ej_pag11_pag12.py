print("Hola mundo")

#ejercicio 1
nombre = "Kobe Bryant"
edad = 45
media_puntos = 28.5
activo = False

print(str(type(nombre)) + ' ' + nombre)
print(str(type(edad)) + ' ' + str(edad))
print(str(type(media_puntos)) + ' ' + str(media_puntos))
print(str(type(activo)) + ' ' + str(activo))

#ejercicio2
nombre = input("Ingrese su nombre: ")
DNI=int(input("Ingrese su DNI: "))
edad=int(input("Ingrese su edad: "))

print(nombre)
print(DNI)
print(edad)

#ejercicio 3
cadena=input("Ingrese su string: ")
substring=cadena[:3]+cadena[-3:]
print(substring)

#ejercicio 4
inicio=int(input("Ingrese posicion inicio de cadena: "))
longitud=int(input("Ingrese longitud del substring: "))
cadena=input("Ingrese su cadena: ")
fin=inicio+longitud
substring=cadena[inicio:fin]
print(substring)

#ejercicio 5
frase=input("Ingrese su frase: ")
letra=input("Ingrese la letra a buscar: ")
reemplazar=input("Ingrese reemplazo: ")

contador=frase.count(letra)

if(contador>0):
    nueva_frase=''
    print("Resultado: "+str(contador)+" apariciones")

    for l in frase:
        if l == letra:
            nueva_frase=nueva_frase+reemplazar
        else:
            nueva_frase=nueva_frase+l

    print(nueva_frase)
else:
    print("Resultado: "+str(contador)+" apariciones")
    print("No se encontro "+letra+" en "+frase)

