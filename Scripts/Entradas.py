''' SCRIPTS
Guiones con instrucciones en codigo fuente que se ejecutan de arriba a abajo,
guardados en un fichero con una nombre unico y ejecutados desde el interprete.

Puede tomar datos (Argumentos) en el momento de la ejecucion
'''

import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce los argumentos correctamente")
    print("Ejemplo: SCRIPT.py 'Texto' 5")
