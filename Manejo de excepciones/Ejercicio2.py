lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error:\tEl índice se encuentra fuera del rango,\n"
          "\tdebes utilizar un número mayor o igual que cero\n"
          "\ty menor que la longitud de la lista.")