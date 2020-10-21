# Stacks
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)
pila.pop()# Sacando de la pila
print(pila)

#Dequeue (colas)
from _collections import deque
cola = deque(['Hector', 'Juan', 'Miuel'])
print(cola)

cola.append('Maria')
cola.append('Arnaldo')
print(cola)

p = cola.popleft() # Guardando a Juan antes de eliminarlo
cola.popleft() # Eliminando un dato desde la izquierda
print(cola)
