class Animal():
    __tiene_patas:bool

    def __init__(self,color:str,tipo:str):
        self.__color = color
        self.__tipo = tipo

    def set_tiene_patas(self,tiene_patas:bool):
        self.__tiene_patas = tiene_patas

    def get_diccionario(self):
        diccionario = {
            "color": self.__color,
            "tipo": self.__tipo,
            "tiene_patas":self.__tiene_patas,
        }
        return diccionario

    def get_tiene_patas(self):
        return self.__tiene_patas

    def get_tipo(self):
        return self.__tipo

a1=Animal("verde","serpiente")
a1.set_tiene_patas(False)
print(a1.get_diccionario())

a2=Animal("marron","perro")
a2.set_tiene_patas(True)
print(a2.get_diccionario())

animales = [a1,a2]

for animal in animales:
    if animal.get_tiene_patas():
        print("El animal de tipo ",animal.get_tipo()," tiene patas")
    else:
        print("El animal de tipo ",animal.get_tipo()," no tiene patas")

