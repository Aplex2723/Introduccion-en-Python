'''Ejemplo de implementacion con programacion Estructurada'''

clientes = [
    {'Nombre' : 'Hector', 'Apellido' : 'Costa Guzman', 'ine' : '111111111A'},
    {'Nombre' : 'Pedro', 'Apellido' : 'Casillas Torres', 'ine' : '222222222B'}
]

def mostrar_clientes(clientes, ine):
    for c in clientes:# le asignamos a c que buesque en clientes
        if (ine == c['ine']):
            print('{} {}'.format(c['Nombre'], c['Apellido']))
            return

    print("Cliente no encontrado")

print(mostrar_clientes(clientes, '111111111A'))

def borrar_cliente(clientes, ine):
    for i,c in enumerate(clientes):# Asignamos a 'i' la numeracion de cliente
        if (ine == c['ine']):
            del(clientes[i])# Si no borramos el valor 'i' no se borra el diccionario
            print(str(c), "> BORRADO")
            return
    print("Cliente no encontrado")

print(borrar_cliente(clientes, '222222222B'))
print(clientes)