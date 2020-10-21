import math

class Punto():
    def __init__(self,x=0 ,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x,self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} Se situa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se situa sobre el eje Y".format(self))
        else:
            print("esta sobre el origen")

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y))

    def distancia(self,p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print("La distancia entre 2 puntos de {} y {} es ({})".format(self, p, d))


class Rectangulo:
    def __init__(self, inicial=Punto(), final=Punto()):
        self.inicial = inicial
        self.final = final

        #Hago los calculos, pero no llamo los atributos igual
        #que los metodos porque sino podriamos sobreescribirlos
        self.vBase = abs(self.final.x - self.inicial.x)
        self.vAltura = abs(self.final.y - self.inicial.y)
        self.vArea = self.vBase * self.vAltura

    def base(self):
        print("La base del triangulo es {}".format(self.vBase))

    def altura(self):
        print("La altura del rectangulo es {}".format(self.vAltura))

    def area(self):
        print("El area del rectangulo es {}".format(self.vArea))

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()