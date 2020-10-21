def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boom")
    print("Fin de la funcion", num)
print(cuenta_atras(5))

def factorial(num):
    print("valor inicial =",num)
    if num > 1:
        num = num * factorial(num-1)
    print("valor final =",num)
    return num
print(factorial(5))