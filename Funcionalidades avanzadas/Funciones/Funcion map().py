#Funcion map
numeros = [2,5,10,23,50,33]

def doblar(numero):
    return numero*2

print(map(doblar, numeros) )

m = map(doblar, numeros)
print(m)
print(m)

print(list(map(lambda x: x*2, numeros)))

a = [1,2,3,4,5]
b = [6,7,8,9,10]

print(list(map(lambda x,y: x*y, a, b)))

c = [11,12,13,14,15]
print(list(map(lambda x,y,z: x*y*z, a, b, c)))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)

personas = [
    Persona("Miranda", 25),
    Persona("Eduardo", 12),
    Persona("Maria", 17),
    Persona("Javier", 76),
    Persona("Anahi", 11)
]
#Incrementando 1 año de edad
def incrementar(persona):
    persona.edad += 1
    return persona

personas = map(incrementar, personas)
for persona in personas:
    print(persona)

#aciendolo con lambda
personas = [
    Persona("Miranda", 25),
    Persona("Eduardo", 12),
    Persona("Maria", 17),
    Persona("Javier", 76),
    Persona("Anahi", 11)
]
#Creando nuevamente Persona con la informacion actualizada
#Todo este codigo equivale a linea 38-45
personas = map(lambda persona: Persona(persona.nombre, persona.edad + 1), personas)
for persona in personas:
    print(personas)