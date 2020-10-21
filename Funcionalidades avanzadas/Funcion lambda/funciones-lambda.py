#Funcion mas potente de python (anonima)

def doblar(n):
    result = n * 2
    return result

print(doblar(5))
#simplificado
def doblar2(n): return n * 2
print(doblar(4))

#con funcion lambda (funcion anonima simplificada)
doblar = lambda n: n * 2
print(doblar(2))

inpar = lambda num : num%2 != 0

print(inpar(5))

revertir = lambda cadena: cadena[::-1]

print(revertir("hola"))

sumar = lambda x,y: x+y
print(sumar(5,6))