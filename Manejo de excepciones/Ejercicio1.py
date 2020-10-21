try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("Error:\tNo es posible dividir entre cero,\n"
          "\tdebes introducir un número distinto.")