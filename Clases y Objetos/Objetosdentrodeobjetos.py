class Peliculas:
    def __init__(self, nombre, duracion, lanzamiento):
        self.nombre = nombre
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula:", self.nombre)

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.lanzamiento)


class Catalogo:
    peliculas = []
    def __init__(self, pelicualas=[]):
        self.peliculas = pelicualas

    def agregar(self,p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)

p = Peliculas("El Padrino",175,1972)
c = Catalogo([p])
c.mostrar()
c.agregar(Peliculas("El Padrino P2",202,1974))# Añadiendo otra pelicula al catalogo desde la funcion agregar
c.mostrar()