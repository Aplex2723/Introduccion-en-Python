
def indeterminados_posicion(*args):#Creamos una funcion con argumentos indeterminados
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola",[1,5,2,7]) # Lo  que imprimiria un tipo de tupla

def indeterminados_nombre(**kwargs):# Clave y valor
    print(kwargs)

indeterminados_nombre(n=5,c="Hola",l=[1,5,2,7]) # Esto se imprime como un diccionario

def indeterminados_nombre(**kwargs):# Clave y valor
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])# pasando los valores para que se impriman
indeterminados_nombre(n=5,c="Hola",l=[1,5,2,7]) # Por reglas de diccionarios nadamas muestra claves

def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("\nSumatorio ideterminado es: ", t)
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])

super_funcion(10,50,-1,4.23,300,Nombre="Hexctor",Edad=27)
