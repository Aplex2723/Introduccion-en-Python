class Galleta:
    pass
una_galleta = Galleta()
una_galleta.sabor = "Salado"
una_galleta.color = "Marron"
print("El sabor de esta galleta es:", una_galleta.sabor)

class Galleta:
    chocolate = True

una_galleta = Galleta()
print(una_galleta.chocolate)

class Galleta():
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta")
    def chocolatear(self):
        self.chocolate = True # Cambiando el atributo interno a True con el self.
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta con chocolate")
        else:
            print("Soy una galleta sin chocolate")

g = Galleta()
print(g.tiene_chocolate())# Mostrando la galleta antes de chocolatearla
g.chocolatear()
print(g.tiene_chocolate())# Mostrando la galleta despues de chocolatearla

class Galleta():
    chocolate = False
    def __init__(self, sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print("Se acaba de crear una galleta {} y {}".format(sabor, forma))
    def chocolatear(self):
        self.chocolate = True # Cambiando el atributo interno a True con el self.
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta con chocolate")
        else:
            print("Soy una galleta sin chocolate")
g = Galleta("salada", "cuadrada")
g = Galleta()# Como esta vacio no pasa ninguna informacion, por lo tanto no imprime nada