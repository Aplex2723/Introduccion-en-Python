import re

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

texto = "hala hela hila hola hula" 
patrones = ['h[ou]la', 'h[aeiou]la']
print(buscar(patrones, texto))

texto = "hala heeela hiiiila hooooola " 
patrones = ['h[ae]la', 'h[ae]*la']
print(buscar(patrones, texto))

#Excliusion en conjuntpo [^] para busquedas contrarias
texto = "hala hela hila hola hula" 
patrones = ['h[o]la', 'h[^o]la']
print(buscar(patrones, texto))

#Rangos [-] ejemplo [A-z] [A-Z] [a-Z]
texto = "hola h0la Hola mola m0la M0la fyhd asSa"

patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}']
print(buscar(patrones, texto))

#Caracteres escapados \
texto = "Este curso de python 3 se publico en el año 2016"
patrones = [r'\d', r'\d+', r'\D', r'\D+', r'\s', r'\S', r'\S+']
print(buscar(patrones, texto))