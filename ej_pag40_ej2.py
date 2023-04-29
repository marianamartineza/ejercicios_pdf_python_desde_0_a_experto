import math

class Poligono():
    l1:float
    l2:float
    l3:float
    color:str

    def __init__(self,color,l1,l2,l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3
        self.color=color

    def mostrar(self):
        print(self.color,self.l1,self.l2,self.l3)


class Triangulo(Poligono):

    def area(self):
        s = self.perimetro()/2
        a = math.sqrt(s*(s-self.l1)*(s-self.l2)*(s-self.l3))
        print ("\n area = " + str(a))
        return a

    def forma(self):
        if self.l1 == self.l2 and self.l2==self.l3 and self.l3==self.l1:
            print("\n Triangulo equilatero")
        elif (self.l1 == self.l2 and self.l1!=self.l3) or (self.l1 == self.l3 and self.l1!=self.l2) or (self.l3 == self.l2 and self.l1!=self.l3):
            print("\n triangulo isosceles")
        else:
            print("\n triangulo escaleno")
        self.mostrar()

    def perimetro(self):
        p=self.l1+self.l2+self.l3
        print ("\n perimetro = " + str(p))
        return p


class Cuadrado(Poligono):
    l4: float

    def __init__(self,color,l1,l2,l3,l4):
        Poligono.__init__(self,color,l1,l2,l3)
        self.l4 = l4

    def area(self):
        if self.l1==self.l2 and self.l2==self.l3 and self.l1==self.l4:
            a= math.pow(self.l1,2)
            print ("\n area = " + str(a))
            return a
        else:
            print("El cuadrado no tiene todos los lados iguales")


    def perimetro(self):
        if self.l1==self.l2 and self.l2==self.l3 and self.l1==self.l4:
            p=self.l1*4
            print ("\n perimetro = " + str(p))
            return p
        else:
            print("El cuadrado no tiene todos los lados iguales")

    def mostrar(self):
        Poligono.mostrar(self)
        print(self.l4)

t1=Triangulo('Azul',3,4,5)
t1.forma()
t1.area()
t1.perimetro()

t2=Triangulo('Azul',10,20,20)
t2.forma()
t2.area()
t2.perimetro()


c1=Cuadrado('Rojo',10,10,10,10)
c1.mostrar()
c1.area()
c1.perimetro()

c2=Cuadrado('Verde',30,10,10,10)
c2.mostrar()
c2.area()
c2.perimetro()

