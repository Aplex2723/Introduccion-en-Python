print("Hola")
l = [1,2,3]
l.pop()
l.pop()
l.pop()
print(l)

l = [1,2,3]
if len(l) > 0:
    l.pop()
print(l)

n = float(input("Introduce un numro: ")) #Para que no de error hay que cambiarlo a numero flotante o entero ya que por defecto es una cadena str
m = 4
print("{}/{}={}".format(n,m,n/m))