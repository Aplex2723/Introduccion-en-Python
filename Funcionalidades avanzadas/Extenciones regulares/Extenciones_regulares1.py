import re

texto = "En esta cadena se encuentra una palabra mágica"

re.search('mágica', texto)

palabra = "mágica"

encontrado = re.search(palabra,  texto)

if encontrado is not None:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra)

print( encontrado.start() )  # Posición donde empieza la coincidencia
print( encontrado.end() )    # Posición donde termina la coincidencia
print( encontrado.span() )   # Tupla con posiciones donde empieza y termina la coincidencia
print( encontrado.string )   # Cadena sobre la que se ha realizado la búsqueda

# El re.match: busca un patron al principio de otra cedena
texto = "Hola mundo"
print(re.match("Hola", texto))

# re.slplit: divide una cadena a partir de un patron
texto = "vamos a dividir esta cadena"

print(re.split(' ', texto))

# re.sub: sustituye rodas las coincidencias en una cadena
texto = "Hola amigo"
print(re.sub("amigo", "amiga", texto))

# re.findall: buscar todas las coinmcidencias en una cadena
texto = "hola adios hola hola"
print(len(re.findall("hola", texto)))

texto = "hola adios hello hola bye"
print(re.findall("(hola)(hello)", texto))
