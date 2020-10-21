import re
#Patrones con sintaxis repetida
texto = "hla hola hoola hooola hoooooola"
print(re.findall("hla", texto))

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

patrones = ['hla', 'hola', 'hoola', 'hooooola']
print(buscar(patrones, texto))

#Meta-caracter *: ninguna o mas repeticiones de la letra a su izquierda

patrones = ['hla', 'hola', 'hoola', 'hooooola']
                                #ninguna o mas veces
patrones = ["ho", "ho*", "ho*la", "hu*la"]
print(buscar(patrones , texto))

#Metacaracter +: una o mas repeticiones de la letra a su izquierda
patrones = ['hla', 'hola', 'hoola', 'hooooola']
patrones = ["ho", "ho+"]
print(buscar(patrones , texto))

#Metacaracter ?: una o ninguna repeticion de la letra a su izquierda
patrones = ['hla', 'hola', 'hoola', 'hooooola']
patrones = ["ho", "ho?", "ho?la"]
print(buscar(patrones , texto))

#syntaxis con {n}: indica u numero de repeticiones explicito de la letra a su izquierda
patrones = ['hla', 'hola', 'hoola', 'hooooola']
patrones = ["ho{0}", "hol{1}a", "ho{3}la"]
print(buscar(patrones , texto))

patrones = ['hla', 'hola', 'hoola', 'hooooola']
patrones = ["ho{0,1}", "ho{1,2}la", "ho{2,10}la"]
print(buscar(patrones , texto))