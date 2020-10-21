numeros = [2,5,10,23,50,33]

def multiple():
    if numeros %5 == 0:
        return True

print(filter(multiple, numeros))

#trasformando a lambda
print(list(filter(lambda numero: numero %5 == 0, numeros)))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)

personas = [
    Persona("juan", 15),
    Persona("Manuel", 25),
    Persona("Javier", 13),
    Persona("Miranda", 54),
    Persona("Paco", 55)
]
print(personas)

menores = filter(lambda persona: persona.edad < 18, personas)
for menor in menores:
    print(menor)