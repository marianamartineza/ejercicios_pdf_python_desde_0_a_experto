# Taller Mariana Martinez Araque CI 28.396.879 - Taller POO - SID2D
class Persona:
    def __init__(self):
        self.nombre=''
        self.edad=''
        self.cedula=''

    #setters
    def set_nombre(self,nombre:str):
        self.nombre=nombre

    def set_edad(self,edad:int):
        self.edad=edad

    def set_cedula(self,cedula:int):
        self.cedula=cedula

    def mostrar(self):
        diccionario={
            "nombre":self.nombre,
            "edad": self.edad,
            "cedula": self.cedula,
        }
        return diccionario

    def es_mayorde_edad(self):
        if self.edad>=18:
            return True
        else:
            return False

class Cuenta(Persona):
    def __init__(self):
        self.__Titular = Persona()
        self.__cantidad_dinero:float=0

    def set_titular(self,nombre:str,edad:int,cedula:int):
        self.__Titular.set_nombre(nombre)
        self.__Titular.set_edad(edad)
        self.__Titular.set_cedula(cedula)

    def set_cantidad(self,cantidad:float):
        if cantidad>=0:
            self.__cantidad_dinero=cantidad

    def get_titular(self):
        return self.__Titular

    def get_cantidad(self):
        return self.__cantidad_dinero

    def mostrar(self):
        diccionario = {
            "Titular": self.__Titular.mostrar(),
            "Cantidad": self.get_cantidad()
        }
        return diccionario

    def depositar(self,cantidad:float):
        if cantidad>0:
            self.__cantidad_dinero+=cantidad

    def retirar(self,cantidad:float):
        self.__cantidad_dinero-=cantidad

# instanciar objeto de tipo cuenta
cuenta = Cuenta()

# asignar titular y cantidad
cuenta.set_titular("mariana",22,28396879)
cuenta.set_cantidad(20.05)

# mostrar la cuenta instanciada
print(cuenta.mostrar())

# probar depositar
cuenta.depositar(10)
print(cuenta.mostrar())

# si el numero a depositar es negativo no haga nada
cuenta.depositar(-2)
print(cuenta.mostrar())

# retirar incluso si queda en numeros rojos (negativos)
cuenta.retirar(5)
print(cuenta.mostrar())

cuenta.retirar(100)
print(cuenta.mostrar())

# mostrar por pantalla si el titular es mayor o menor de edad
titular=cuenta.get_titular()

if titular.es_mayorde_edad():
    print("El titular de la cuenta es mayor de edad")
else:
    print("El titular de la cuenta no es mayor de edad")



