#ej 3
class Robot():
    x:int
    y:int
    movimientos:list

    def __init__(self):
        self.x=0
        self.y=0
        self.movimientos=[]

    def mueve_letra(self,letra):
        match letra:
            case "A":
                self.x+=1
            case "R":
                self.x-=1
            case "I":
                self.y-=1
            case "D":
                self.y+=1
            case _:
                print('No es una opcion valida')
        self.posicion_actual()

    def mueve(self,secuencia):
        print('\n secuencia recibida: ' + secuencia)
        for letra in secuencia:
            self.mueve_letra(letra)
        self.movimientos.append(secuencia)

    def posicion_actual(self):
        print(self.x,self.y)

    def listar_ordenes(self):
        print('\n listar ordenes recibidas: ')
        for orden in self.movimientos:
            print(orden)

    def posicion_inicial(self):
        print("\n secuencia volver a 0,0")
        secuencia=""
        x=self.x
        y=self.y
        while(x!=0 or y!=0):
            if x>0:
                x-=1
                secuencia+="R"
            if x<0:
                x+=1
                secuencia+="A"
            if y>0:
                y-=1
                secuencia+="I"
            if y<0:
                y+=1
                secuencia+="D"

        print(secuencia)

r=Robot()
r.mueve("AADDADIR") # (2,2)
r.listar_ordenes()
r.posicion_inicial()
r.mueve("RIRI")

