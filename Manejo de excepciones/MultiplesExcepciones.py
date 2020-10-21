try:
    n = float(input("Introduce un numero: "))
    5/n
except TypeError:
    print("No se puede dividir el numero por una cadena")
except ValueError:
    print("Debes de introducir una cadena que sea un numero")
except ZeroDivisionError:
    print("No puedes dividir entre 0, prueba otro numero")
except Exception as e: # Conseguir nombre del error
    print(type(e).__name__)