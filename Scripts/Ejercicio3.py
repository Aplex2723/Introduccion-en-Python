import sys
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error - El numero es incorrecto")
        print("Ejemplo: Ejemplo3.py [0-9999]")
    else:
        cadena = str(numero)# Transformamos a cadena el numero que pusimos con str
        longitud = len(cadena) # Asignamos la longitud leyendo los valores de la cadena

        for i in range(longitud):                       # 10 x 0 = 1 = n1 * 1 = 000n1
            print("{:04d}".format(int(cadena[longitud-1-i])* 10 ** i)) #Transformando a numero entero la cadena ya aque si no, no actua el format

else:
    print("Los argumentos deben de ser definidos.")
    print("Ejemplo: python Ejercicio2.py [valor] [numero a descomponer]")