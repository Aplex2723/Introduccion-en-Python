n = int("10")
f = float("10.5")
c = "Un texto y un numero" + str(10) + " " + str(4.12)
print(bin(10))
print(hex(10))
print(int('0b1010', 2))
print(int('0xa',16))
print(abs(-10))
print(round(5.5))
print(round(5.4))
print(eval('2+5'))
n = 10
print(eval('n*10-5'))
print(len("Una cadena"))
print(len([1,2,4,56,6]))

def test(num):
    return num, num*2, num*4
print(test(5))
print(type(test(5)))