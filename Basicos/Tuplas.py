tupla = (100,"Hola",[1,2,3,4],-60)
print(tupla[0])
print(tupla[1:3])
print(tupla[2][1])
print(len(tupla))
print(len(tupla[2]))

# Index para buscar un elemento y saber su hubicacion.
print(tupla.index(100))
print(tupla.index('Hola'))
print(tupla.count(100))
tupla = (100, 100, 100, 50, 60, 100)
print(tupla.count(100))
