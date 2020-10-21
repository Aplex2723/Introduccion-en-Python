def restar(a,b):
    return a-b
print(restar(14,2))

print(restar(b=2,a=1))

def restar2(a=None,b=None):
    if a == None or b == None:
        print("Error, debes enviar dos numeros a la funcion")
        return
    else:
        return a-b
print(restar2(4,6))