class Producto:
    def __init__(self, referencia, tipo, nombre, pvp, descripccion,productor=None, dristribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.pvp = pvp
        self.tipo = tipo
        self.nombre = nombre
        self.descripccion = descripccion
        self.productor = productor
        self.distribuidor = dristribuidor
        self.isbn = isbn
        self.autor = autor

adorno = Producto('000A', 'ADORNO', 'Vaso Adornado', 15, 'Vaso de porcelana con dibujos')
print(adorno.tipo)



class Producto:
    def __init__(self, referencia, nombre, pvp, descripccion):
        self.referencia = referencia
        self.pvp = pvp
        self.nombre = nombre
        self.descripccion = descripccion

    def __str__(self):
        return """
REFERENCIA  \t{}
NOMBRE  \t\t{}
PVP     \t\t{}
DESCRIPCCION  \t{}""".format(self.referencia,self.nombre,self.pvp,self.descripccion)


class Adorno(Producto):
    pass

a= Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con arboles")
print(a)

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """
REFERENCIA  \t{}
NOMBRE  \t\t{}
PVP     \t\t{}
DESCRIPCCION  \t{}
PRODUCTOR     \t{}
DISTRIBUIDOR  \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripccion,self.productor,self.distribuidor)


al = Alimento(5034, "Botella de Aceite",5,"250 ml")
al.productor = "Aceitera2344"
al.distribuidor = "Distribuciones S.A"
print(al)


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """
REFERENCIA  \t{}
NOMBRE  \t\t{}
PVP     \t\t{}
DESCRIPCCION  \t{}
ISBN        \t{}
AUTOR     \t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripccion,self.isbn,self.autor)

li = Libro(7352, "Cocina mediterrania",9,"Recetas sanas y buenas")
li.isbn = "0-1234535-1"
li.autor = "Juana Dominquez"
print(li)

productos = [a , al]
productos.append(li)
print(productos)

for p in productos:
    print(p.referencia, p.nombre) # Recortando los datos

print("\n")
for p in productos:
    if ( isinstance(p, Adorno) ):
        print(p.referencia, "\/" ,p.nombre)

    elif ( isinstance(p, Alimento) ):
        print(p.referencia, "\/" ,p.nombre, "\/" ,p.productor)

    elif ( isinstance(p, Libro) ):
        print(p.referencia, "\/" ,p.nombre, "\/" ,p.isbn)**

def rebajar_producto(p, rebaja):
    '''Devuelve un producto con una rebaja en procentaje en su precio'''
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

al_rebajado = rebajar_producto(al, 10)
print(al_rebajado)

l = [1,2,3]
l2 = l
l2.append(4)
print(l2)

import copy # En este apartado copiamos los datos desde una clase para no joder lo demas
copia_a = copy.copy(a)
print(copia_a)