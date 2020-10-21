from tkinter import *

root = Tk()#creando raiz

#Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

root.title("Hola mundo")
root.resizable(1,1)#Evita redimencionar la ventana (cambiarle el tamano)
root.iconbitmap('tkp.ico')#Poner icono alado del titulo

Label(root, text="Hola mundo!!!").pack(anchor="nw")
label = Label(root, text="Otra etiqueta")
label.pack(anchor="center")
Label(root, text="ultima etiqueta").pack(anchor="se")

#añadir propiedades graficas
label.config(bg="green",fg="blue", font=("Verdana", 24))
label.config(textvariable = texto)


#Abajo de todo
root.mainloop()