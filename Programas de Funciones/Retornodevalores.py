def test():
    return "Una cadena retornada"
print(test())
c = test()
print(c)

def test2():
    return [1,2,3,4,5]
print(test2())
print(test2()[-1])
print(test2()[1:4])
l = test2()
print(l)

def test(): # En esta parte se parece a las tuplas
    return "una cadena", 20, [12,52,1]
print(test())
c,n,l = test()
print(c)
print(n)
print(l)