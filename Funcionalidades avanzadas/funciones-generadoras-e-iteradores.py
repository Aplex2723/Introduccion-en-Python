# Porrgla general:
[numero for numero in [0,2,3,4,5] if numero % 2 == 0]

[numero for numero in range(0,6) if numero % 2 == 0]

#Crear una funcion generadora manual
def pares(n):
    for numero in range(n+1):
        if numero %2 == 0:
            yield numero #Remplaza el pares.append(numero)

for numero in pares(10):
    print(numero)

[numero for numero in pares(10)]
pares = pares(3)

print(next(pares))
print(next(pares))

#No puedes convertir cadenas o listas ya que no son iteradores
#lista = [1,2,3,4,5]
#next(lista)

#Funcion iter para convertir a interadores
lista = [1,2,3,4,5]
lista_iterable = iter(lista)
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))

cadena = "hola"
cadena_iterable = iter(cadena)
print(next(cadena_iterable))
print(next(cadena_iterable))
print(next(cadena_iterable))
print(next(cadena_iterable))