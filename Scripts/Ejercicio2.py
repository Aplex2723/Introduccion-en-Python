import sys
if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or columnas < 1 or filas > 9 or columnas > 9:
        print("Error - Filas o columnas incorrectas")
        print("Ejemplo: Ejemplo2.py [1-9] [1-9]")
    else:
        for s in range(filas):
            print(" ")
            for n in range(columnas):
                print(" * ", end='')

else:
    print("Error en los valores, intente aplicar el siguiente formato: ")
    print("Ejemplo: Ejercicio2.py [1-9] [1-9]")