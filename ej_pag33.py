# ej 1
lista=[6,14,11,3,2,1,15,19]

try:
    num=int(input('ingrese la posicion de la lista a acceder: '))
    print('lista['+str(num)+'] = '+str(lista[num]))
except IndexError:
    print('La posicion ingresada no existe en la lista')
finally:
    print('programa finalizado')

#ej 2
diccionario = {
    "nombre":"RAE",
    "paginas":900,
    "pais":"España"
}

try:
    key=input('Ingrese la clave a buscar en el diccionario: ')
    print(diccionario[key])
except KeyError:
    print('La llave introducida ('+key+') no se encuentra en el diccionario')
finally:
    print('programa finalizado')