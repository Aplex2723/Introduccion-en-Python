class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas ,velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad,self.cilindrada)


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", con carga de {} kg".format(self.carga)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        if (self.tipo == 'urbana' or 'deportiva'):
            return Vehiculo.__str__(self) + ", tipo {}".format(self.tipo)
        else:
            return "Escoja el tipo de Bicicleta, ya sea 'urbana' o 'deportiva'"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada ):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {} cc".format(self.velocidad,self.cilindrada)


def catalogar(Vehiculos, ruedas=None):
    #Primera pasada, mostrando recuento
    if ruedas != None:
        contador = 0
        for v in Vehiculos:
            if v.ruedas == ruedas:
                contador += 1
        print("\nSe han encontrado {} vehiculos con {} ruedas".format(contador, ruedas))

    #Segunda pasada, mostrar vehiculos
    for v in Vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)

lista = [
    Coche("azul", 4, 150, 1200),
    Camioneta("rojo", 4, 180, 2200, 1500),
    Bicicleta("amarilla", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)
