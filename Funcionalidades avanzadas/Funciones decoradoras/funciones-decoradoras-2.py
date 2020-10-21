#def hola():
#    print("Hola!")

#def adios():
#    print("Adios!")

def monitorizar(funcion):

    def decorar():
        print("\n\t Se esta apunto de ejecutar la funcion: ", funcion.__name__)

        funcion()

        print("\t Se ha finalizado la ejecucion de la funcion: ", funcion.__name__)

    return decorar

def monitorizar_args(funcion):

    def decorar(*args, **kwargs):
        print("\n\t Se esta apunto de ejecutar la funcion: ", funcion.__name__)

        funcion(*args, **kwargs)

        print("\t Se ha finalizado la ejecucion de la funcion: ", funcion.__name__)

    return decorar

#monitorizar(hola)()

@monitorizar
def hola():
    print("Hola!")

@monitorizar
def adios():
    print("Adios!")

@monitorizar_args
def saludar(hombre):
    print("Hola!!! {}".format(hombre))

@monitorizar_args
def bienvenido(nombre):
    print("Bienvenido {}!".format(nombre))

hola()
adios()
saludar("Hector")
bienvenido("Javier")