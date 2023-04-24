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
        print ("area = " + str(a))
        return a

    def forma(self):
        if self.l1 == self.l2 and self.l2==self.l3:
            print("Triangulo equilatero")

    def perimetro(self):
        p=self.l1+self.l2+self.l3
        print ("perimetro = " + str(p))
        return p

    def mostrar(self):
        print("lados: "+str(self.l1,self.l2,self.l3))