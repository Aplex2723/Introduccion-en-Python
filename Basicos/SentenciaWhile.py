# Que es la iteracion?
# -Iterar es realizar una determinada accion varias veces.
# -Cada vez que se repite la accion de domina iteracion.
# Sentencia While (Mientras)
# Se basa en repetir un bloque a partir de evaluar una condicion logica, siempre que esta sea True.
# Nosotros como programadores, debemos planificar un momento que la condicion cambie a Falce y el while finalice su ejecucion.

c = 0
while c <= 5:
    c+=1
    print("el valor de C es: ",c)
else:
    print("El codigo a terminado y c vale: ",c)

c = 0
while c <= 5:
    c += 1
    if (c == 2):
        print("\nSe rompe el bucle ya que vale 2")
        break
    print("el valor de C es: ", c)
else:
    print("El codigo a terminado y c vale: ", c)

c = 0 # Valor continue
while c <= 5:
    c += 1
    if (c == 2):
        print("\nSe continua con la iteracion", c)
        continue
    print("el valor de C es: ", c)
else:
    print("El codigo a terminado y c vale: ", c)

print("\n\n\tBienvenido al menu interactivo")
while(True):
    print("""Que quieres hacer? Escribe una opcion
    1.) Saludar
    2.) Sumar numero
    3.) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola espero que te lo estes pasando chingon")
    elif opcion == '2':
        n1 = float(input("Introduce 1 dijito: "))
        n2 = float(input("Introduce otro numero: "))
        print("El resultado es: ",n1+n2)
    elif opcion == '3':
        print("Hasta luego!")
        break
    else:
        print("Comando desconocido, vuelva a intentarlo.")
