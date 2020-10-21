
'''while(True):
    try:
        n = float(input("Introduce un numero: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
        break # Importante romper la iteracion si todo sale bien
    except:
        print("Ha ocurrido un erro, introduce bien el numero.")
'''
'''while(True):
    try:
        n = float(input("Introduce un numero: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un erro, introduce bien el numero.")
    else:
        print("Todo funciono bien")
        break  # Importante romper la iteracion si todo sale bien'''

while(True):
    try:
        n = float(input("Introduce un numero: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un erro, introduce bien el numero.")
    else:
        print("Todo funciono bien")
        break  # Importante romper la iteracion si todo sale bien
    finally: #se ejecuta si el codigo esta bien o mal
        print("Fin de la iteracion...")