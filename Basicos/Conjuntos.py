conjunto = set()
print(conjunto)
conjunto = {1,2,3}
print(conjunto)
conjunto.add(4)
print(conjunto)
conjunto.add(0)
print(conjunto)
conjunto.add('H')
print(conjunto)
conjunto.add('A')
conjunto.add('Z')
print(conjunto)

grupo = {'Hector', 'Mario', 'Juan'}
print('Hector' in grupo)
print('Maria' in grupo)
print('Hector' not in grupo)
test = {'Hector', 'Hector', 'Hector'}
print(test) # Se eliminan los repetidos

# Eliminando numeros repetidos mediente lista y grupos
l = [1,2,3,3,2,1]
print(l)
c = set(l)
print(c)
l = list(c)
print(l)
l = [1,2,3,3,2,1]
l = list(set(l))
print(l)

s = "Al pan pan y al vino vino"
print(set(s))