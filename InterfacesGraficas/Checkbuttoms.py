from tkinter import *

def Seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += " Con leche"
    else:
        cadena += " y sin leche"

    if (azucar.get()):
        cadena += " Con azucar"
    else:
        cadena += " y sin azucar"

    monitor.config(text=cadena)

root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar() # 1 si 0 no
azucar = IntVar()

frame = Frame(root)
frame.pack()
Label(frame, text="¿Como quieres el cafe?").pack()
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=Seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=Seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()