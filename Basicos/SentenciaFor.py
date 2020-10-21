# Sentencia For
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while(indice < len(numeros)):
    print(numeros[indice])
    indice += 1


for numeros in numeros:
    print(numeros)

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for indice2,numeros in enumerate(numeros):
 #   numeros[indice2] *= 10
  #  print(numeros)

cadena = "Hola Amigps"
for caracter in cadena:
    print(caracter)

#for i,c in enumerate(cadena):
 #   cadena[i] = "*"

cadena2 = ""
for caracter in cadena:
    cadena2 += caracter*2
    print(cadena2)

for i in range(10):
    print(i)

print(list(range(10)))