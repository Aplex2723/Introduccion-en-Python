def hola(arg):
    """Este es ek dockstring de la funcion"""
    print("hola", arg, "!")

print(help(hola))

class Clase:
    """Este es el dockstring de la clase"""
    def __init__(self):
        """Este es el dockstring del iniciador de la clase"""
        pass
    def metodo(self):
        """Este es el dockstring del metodo de la clase"""
        pass
o = Clase()
print(help(o))prin