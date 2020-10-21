from tkinter import *
root =Tk()
root.config(bd=15)
def sumar():
    r.set (float(n1.get()) + float(n2.get()))
    borrar()

def rest():
    r.set (float(n1.get()) - float(n2.get()))
    borrar()

def multi():
    r.set (float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack() #Primer numero
Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack() #segundo numero
Label(root, text=" ").pack()
Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack() #resultado
Button(root, text = "Sumar", command=sumar).pack(side="left")
Button(root, text = "Restar", command=rest).pack(side="left")
Button(root, text = "Multiplicar", command=multi).pack(side="left")

root.mainloop()