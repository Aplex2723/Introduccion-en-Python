# Metodo tradicional
lista = []
for letra in 'casa':
    lista.append(letra)

print(lista)

# Metodo con comprecion de listas

lista = [letra for letra in 'casa']

print(lista)

# Metodo tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)
print(lista)

# Metodo con comprencion de listas 
lista = [numero**2 for numero in range(0,11)]
print(lista)

# Metodo tradicional
lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

# Metodo de comprencion de listas
lista = [numero for numero in range(0,11) if numero % 2 == 0]
print(lista)

# Metodo tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []
for numero in lista:
    if numero % 2 == 0:
        lista.append(numero)

print(pares)

# Metodo por comprencion de lista
pares = [numero for numero in [numero**2 for numero in range(0,11)] if numero % 2 == 0]
print(pares)

# Practica por comprencion de lista
# Metodo tradicional
lista2 = []
for numero in range(0,11):
    lista2.append(numero**2)
    
inpares = []   
for numero in lista2:
    if numero % 2 != 0:
        inpares.append(numero)
        
print(inpares)

inpares = [numero for numero in [numero**2 for numero in range(0,31)] if numero % 2 != 0 ]
print(inpares)