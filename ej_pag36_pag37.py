#ej 1
import string


class Coche():
    matricula: string
    marca: string
    kilometros_recorridos: float
    gasolina: float

    def __init__(self,matricula,marca,kilometros_recorridos,gasolina):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos= kilometros_recorridos
        self.gasolina=gasolina

    def recorrer(self,km_conducir):
        if self.gasolina-km_conducir*0.1>0:
            self.kilometros_recorridos+=km_conducir
            self.gasolina-=km_conducir*0.1
        else:
            print('Es necesario repostar para recorrer la cantidad indicada de kilometros')

    def repostar(self,lt_gasolina):
        self.gasolina+=lt_gasolina

    def mostrar(self):
        print('kilometros_recorridos = ' + str(self.kilometros_recorridos) + ', gasolina='+ str(self.gasolina))

c1 = Coche('A123C','Aveo',0,0)
print(c1.matricula,c1.marca,c1.kilometros_recorridos,c1.gasolina)
c1.repostar(50)
c1.mostrar()
c1.recorrer(100)
c1.mostrar()
c1.recorrer(40)
c1.mostrar()
c1.recorrer(180)
c1.mostrar()
c1.recorrer(200)
c1.mostrar()