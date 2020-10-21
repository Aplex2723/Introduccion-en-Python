v = "otro texto"
n = 10
print("Un texto",v,"y un numero",n)
c = "Un texto {} y un numro {}".format(v,n) # Lo mismo de arriba
print(c)

c = "Un texto {} y un numero {}".format(v,n) # Pasadno numeros
print("Un texto {1} y un numero {0}".format(v,n))# Cambiando los valores donde 1 = n y 0 = v
print("\tUn texto {texto} y un numero {numero}".format(texto=v,numero=n))
print("{texto}, {texto}, {texto}".format(texto=v))

print("{:>30}".format("Palabra"))# Alineamiento a la derecha en 30 caracteres
print("{:30}".format("Palabra"))# Alineamiento a la izquierda en 30 caracteres
print("{:^30}".format("Palabra"))# Alineamiento al centro en 30 caracteres
print("{:.3}".format("Palabra"))# Truncamiento a 3 caracteres
print("{:>30.3}".format("Palabra"))# Alineamiento a la derecha en 30 caracteres con truncamiento de 3

# Formateo de numero enteros, rellenados con espacios
print(" ")
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
# Formateo de numero enteros, rellenados con ceros
print(" ")
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

# Formateo de numeros flotanbtes, rellenados con espacios
print(" ")
print("{:7.3f}".format(3.1415983))
print("{:7.3f}".format(123.23))

# Formateo de numeros flotanbtes, rellenados con ceros
print(" ")
print("{:07.3f}".format(3.1415983))
print("{:07.3f}".format(123.23))