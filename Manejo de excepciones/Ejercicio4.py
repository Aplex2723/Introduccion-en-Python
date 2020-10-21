try:
    resultado = 15 + "20"
except TypeError:
    print("Error:\tSólo es posible sumar datos del mismo tipo,\n"
          "\tdebes transformar el número a cadena o viceversa.")