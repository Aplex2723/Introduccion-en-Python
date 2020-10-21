#Sentencia If
if not False:
    print("Se cumple la condicion")
    print("Tambien se muestra este print")

a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("Vale 5")

a = 5
b = 10
if a == 5:
    print("\na vale ",a)
    if b == 10:
        print("y b vale ",b)

if a == 5 and b == 10:
    print("\na vale ",a," b vale ",b)

n = 10
if n % 2 == 0:
    print(n, " es un numero par")
else:
    print(n," es un numero impar")

# Sentencia Elif (Sino si), se encadena a un if para comprobar otra posible condicion, siempre que la anterior no se cumpla
comando = "ENTRAR"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola espero que estes chido")
elif comando == "SALIR":
    print("Saliendo del sistema")
else:
    print("Este comando no es reconocido")

nota = float(input("\n\tIntroduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Suficiente")
elif nota < 5:
    print("Reporbado")

if True:
    pass