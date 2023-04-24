#ej 2
class Robot():
    x:int
    y:int

    def __init__(self):
        self.x=0
        self.y=0

    def mueve(self,letra):
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

    def posicion_actual(self):
        print(self.x,self.y)

r=Robot()
r.mueve("A")
r.mueve("A")
r.mueve("I")
r.mueve("A")
r.mueve("D")
r.mueve("D")
r.mueve("D")
r.mueve("R")
r.mueve("I")




