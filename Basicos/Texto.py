print("Hola ""Mundo")
print("Una cadena")
print('otra cadena')
print('otra cadena mas')

#Tecto con Tabulacion (\t)
print("un texto con una \ttabulacion")
#Texto con nueva linea
print("un texto\ncon una linea")

#Cadena tipo "Raw"
print(r"C:\nombre\directorio")

#Textos con distintas linesas
print("""Una linea
otra linea
otra \ttabulacion""")

c = "Asignacion de texto"
print(c)
print(c+c)
s = "Una cadena compuesta " "de dos cadenas"
print(s)

#Tecnoca slizing
palabra = "phython"
#caracter en la posicion 0
print(palabra[-2])
print(palabra[0:2])
print(palabra[2:-1])
print(palabra[2:])
print(palabra[2:] + palabra[2:])
print(palabra[:99])
print(palabra[99:])

palabra = "N" + palabra[1:]
print(palabra)
