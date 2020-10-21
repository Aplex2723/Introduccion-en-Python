from tkinter import *

root = Tk()#creando raiz

root.title("Hola mundo")
root.resizable(1,1)#Evita redimencionar la ventana (cambiarle el tamano)
root.iconbitmap('tkp.ico')#Poner icono alado del titulo

frame = Frame(root)

#Abajo de todo
root.mainloop()