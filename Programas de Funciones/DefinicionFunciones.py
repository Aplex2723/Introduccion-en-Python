def saludar():
    print("Hola! Este print se llama desde la funcion saludar()")

print(saludar())

def dibujar_tabla_del_5():
    for i in range(10):
        print("5 *",i,"=",i*5)
print(dibujar_tabla_del_5())

'''def test():
    n = 10
print(test())
Las variables solo abarcan desntro de la funcion test
'''
# Aqui definimos primero la variable y luego la imprimimos dentro de la funcioncion para
# que se pueda reflejar con un print fuera de la funcion.
m = 10
def test2():
    print(m)
print(test2())

# Tambien se puede declarar despues siempre y cuando se declare antes de imprimir la funcion test2
def test2():
    print(l)
l = 5
print(test2())

def test():
    o = 5 # Se define a la variable 'o' con el valor de 5
    print(o)
print(test())# se imprime el valor de 'o' osea 5
o = 10# Se asigna a 'o' un nuevo valor el cual es 10
print(test)# Se imprime la funcion test pero da como resultado 5 ya que en la funcion se le declaro la 'o'.
print(o)# Se imrpime la 'o' como valor 10

