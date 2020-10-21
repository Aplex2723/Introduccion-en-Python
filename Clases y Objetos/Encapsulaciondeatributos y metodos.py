class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde afuera "

    def __atributo_privado(self):
        print("Soy un metodo inalcanzable desde afuera")

e = Ejemplo()
# e.__atributo_privado si intentamos activarlo nos va a salir un error, ya que el atrubuto solo se puede usar desde adentro de la clase

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde afuera "

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde afuera")

    def atributo_publico(self):
        return self.__metodo_privado()

    def metodo_publico(self):
        return self.__metodo_privado()


e = Ejemplo()
e.atributo_publico()
e.metodo_publico()