#ej 4
import math

class Triangulo():
    l1:float
    l2:float
    l3:float

    def __init__(self,l1,l2,l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3

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

    def mostrar(self):
        print(self.l1,self.l2,self.l3)

t1 = Triangulo(1,1,1)
t1.forma()
t1.area()
t1.perimetro()

t2 = Triangulo(3,4,5)
t2.forma()
t2.area()
t2.perimetro()

t3 = Triangulo(3,3,5)
t3.forma()
t3.area()
t3.perimetro()

t4 = Triangulo(3,4,3)
t4.forma()
t4.area()
t4.perimetro()

t5 = Triangulo(1,3,3)
t5.forma()
t5.area()
t5.perimetro()

t6 = Triangulo(2,5,7)
t6.forma()
t6.area()
t6.perimetro()

