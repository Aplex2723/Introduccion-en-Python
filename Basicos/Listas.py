numero = [1,2,3,4]
datos = [4,"una cadena", -15, 3.14, "otra cadena"]
print(datos[0])
print(datos[-2:])
print(numero + [3, 6, 7, 8])
pares = [0,2,4,5,8,10]
pares[3] = 6
print(pares)
pares.append(12) #añadir numeros a una cadena
pares.append(7*2)
print(pares)

letras = ['a','b','c','d','e','f']
letras[:3] = ['A','B', 'C']
print(letras)
letras[:3] = []
print(letras)

#Unir listas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print(r)
print(r[1])
print(r[2][0])
print(r[-1][-1])