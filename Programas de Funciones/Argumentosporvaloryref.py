def doblar_valor(numero):
    numero *= 2
n = 10
doblar_valor(n)
print(n)

def doblar_valores(numeros): # Se reflejan los valores al exterior
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [50,10,100]
doblar_valores(ns)
print(ns)

def doblar_valor(numero):
    return numero * 2
n = 10
n = doblar_valor(n)
print(n)

def doblar_valores(numeros): # Crear una copia para prevenir modificar una lista
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [50,10,100]
doblar_valores(ns[:])# Inca que queremos devolver una sublista
print(ns)