#forma inncorrecta

numero = 35
if numero >= 0 and numero <= 100:
    print("El numero {} se encuentra entre 0 y 100".format(numero))
else:
    print("El numero {} no se encuentra entre 0 y 100".format(numero))

#forma correcta

numero = 35 
if 0 <= numero <= 100:
    print("El numero {} se encuentra entre 0 y 100".format(numero))
else:
    print("El numero {} no se encuentra entre 0 y 100".format(numero))