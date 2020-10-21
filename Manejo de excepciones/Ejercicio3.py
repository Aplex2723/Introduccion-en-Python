colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    colores['blanco']
except KeyError:
    print("Error:\tLa clave del diccionario no se encuentra,\n"
          "\tdebes probar con otra que sí exista.")