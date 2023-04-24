#ej 1

class Vehiculo():
    marca: str
    kilometros_recorridos: float

    def __init__(self,marca,kilometros_recorridos: float):
        self.marca=marca
        self.kilometros_recorridos=kilometros_recorridos
    
    def recorrer(self,km_conducir: float):
        self.kilometros_recorridos += km_conducir

    def mostrar(self):
        print('\nmarca = ' + str(self.marca) + ' kilometros_recorridos = ' + str(self.kilometros_recorridos))


class Coche(Vehiculo):
    matricula: str
    gasolina: float

    def __init__(self,marca,kilometros_recorridos,matricula,gasolina):
        Vehiculo.__init__(self,marca,kilometros_recorridos)
        self.matricula = matricula
        self.gasolina=gasolina

    def recorrer(self,km_conducir: float):
        if self.gasolina-km_conducir*0.1>0:
            Vehiculo.recorrer(self,km_conducir)
            self.gasolina-=km_conducir*0.1
        else:
            print('Es necesario repostar para recorrer la cantidad indicada de kilometros')

    def repostar(self,lt_gasolina):
        self.gasolina+=lt_gasolina

    def mostrar(self):
        Vehiculo.mostrar(self)
        print('gasolina='+ str(self.gasolina))

class Bicicleta(Vehiculo):

    ruedas_llenas: bool

    def __init__(self, marca, kilometros_recorridos):
        Vehiculo.__init__(self,marca, kilometros_recorridos)
        self.ruedas_llenas=True

    def recorrer(self,km_conducir):
        # km + new < km + 50 
        if ((self.kilometros_recorridos+km_conducir<50) or (self.kilometros_recorridos+km_conducir<self.kilometros_recorridos+50)) and self.ruedas_llenas:
            Vehiculo.recorrer(self,km_conducir)
            self.mostrar()
        else:
            self.ruedas_llenas = False
            print("Es necesario hinchar las ruedas para poder avanzar \n")

    def hinchar_ruedas(self):
        self.ruedas_llenas=True
        print("\nSe hincharon las ruedas de la bicicleta")

    def mostrar(self):
        Vehiculo.mostrar(self)
        print('ruedas_llenas='+ str(self.ruedas_llenas) + '\n')

c1 = Coche('Aveo',0,'A123C',0)
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

b1 = Bicicleta("bmx",0)
b1.recorrer(10)
b1.recorrer(40)
b1.recorrer(50)
b1.hinchar_ruedas()
b1.recorrer(10)