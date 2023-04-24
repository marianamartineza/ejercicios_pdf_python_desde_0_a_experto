#ejercicio 1
lista=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]

diccionario = {}

for item1 in lista:
    cont=0
    for item2 in lista:
        if item1==item2:
            cont+=1
    diccionario.update({item1:cont})

print(diccionario)

#ejercicio 2
diccionario={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,
'Maite': 5}

lista=[]

for value in diccionario.values():
    if value not in lista:
        lista.append(value)

print(lista)

#ejercicio 3
usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
     "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
     },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

cont=0
encontrado=False

while cont<3 and encontrado==False:

    usuario=input("Ingrese su usuario: ")
    contrasenia=input("Ingrese su contraseña: ")

    cont+=1

    for user,data in usuarios.items():
        if user == usuario and contrasenia == data["password"]:
            print("\n Bienvenido")
            print(" Nombre: "+data["nombre"])
            print(" Apellido: "+data["apellido"])
            encontrado=True
            break
    else:
        print(" Datos incorrectos. Quedan " + str(3-cont) + " intentos \n Ingrese nuevamente los datos")
        if cont==3:
            print("Fallo del ultimo intento")
            break

#ejercicio 4

estudiantes = {}

cant_estudiantes=3 #10
for i in range(1,cant_estudiantes+1):
    nombre=input("Ingrese el nombre del estudiante "+str(i)+" :")
    nota=float(input("Ingrese la nota del estudiante "+str(i)+" :"))
    estudiantes.update({str(i):{"nombre":nombre,"nota":nota}})

#print(estudiantes)

nota_aprobada=10

print("\n Lista estudiantes suspendidos")
for key,datos in estudiantes.items():
    if datos["nota"]<nota_aprobada:
        print(key+"\t "+datos["nombre"]+"\t "+str(datos["nota"]))

print("\n Lista estudiantes aprobados")
for key,datos in estudiantes.items():
    if datos["nota"]>=nota_aprobada:
        print(key+"\t "+datos["nombre"]+"\t "+str(datos["nota"]))

acumulador=0.0

for key,datos in estudiantes.items():
    acumulador+=datos["nota"]

nota_media=acumulador/cant_estudiantes
print("La nota media de la clase es " + str(nota_media))