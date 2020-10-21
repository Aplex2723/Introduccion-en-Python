a = 5
a *= 2 # suma en asignacion
print(a)
a /= 2
print(a)
a %= 2
print(a)
a = 5
a **= 10
print(a)

n = 0
while n < 10:
    if (n % 2) == 0:
        print(n,'es un numero par')
    else:
        print(n,'es un numero impar')
    n += 1 # expresion aritmetica n = n + 1equivalente a operacion de asignacion n+=1