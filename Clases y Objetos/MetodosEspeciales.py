class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se a creado la pelicula: ", self.titulo)

    # Destrucotr de clase
    def __del__(self):
        print("Se esta borrando la pelicula: ", self.titulo)


p = Pelicula("El Padrino", 175, 1972)
str(p)


class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se a creado la pelicula: ", self.titulo)

    # Destrucotr de clase
    def __del__(self):
        print("Se esta borrando la pelicula: ", self.titulo)

    # Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)


p = Pelicula("El Padrino", 175, 1972)
print(str(p))


class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se a creado la pelicula: ", self.titulo)

    # Destrucotr de clase
    def __del__(self):
        print("Se esta borrando la pelicula: ", self.titulo)

    # Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    #Redefinimos metodo Length
    def __len__(self):
        return self.duracion
p = Pelicula("El Padrino", 175, 1972)
print(len(p))
