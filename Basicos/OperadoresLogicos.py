# El 'Not' solo le a los logicos, sirve para negar una expresion logica
# Conjucion: sinonimo de unido, contiguo o cercano, agrupa uniendo (And)
# Dusyuncion: Sinonimo de separado, apartado o distante, Agrupa separando (Or)

print(not True)
print(not True == False)

print(True and True)
print(True and False)
print(False and False)
a = 13
print(a > 10  and a < 20)
a = 45
print(a > 10  and a < 20)

c = "Hola mundo"
print(len(c) >= 5 and c[0] == "H")
print(True or True)
print(True or False)
print(False or False)
c = "SALIR"
print(c == "EXIT" or c == "FIN" or c == "SALIR")
c = "OTRA COSA"
print(c == "EXIT" or c == "FIN" or c == "SALIR")
c = "Hector"
print(c[0] == "H" or c[0] == "h")