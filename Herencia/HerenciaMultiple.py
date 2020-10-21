class A:
    def __init__(self):
        print("Soy de clase A")

    def a(self):
        print("Este metodo lo heredo de A")


class B:
    def __init__(self):
        print("Soy de clase B")

    def b(self):
        print("Este metodo lo heredo de B")


class C(A,B):
    def c(self):
        print("Esye merodo es de C")

C=C()# Imprime el primer valor de derecha a izquierda en este caso la A

C.a()
C.b()
C.c()