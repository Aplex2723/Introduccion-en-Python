from tkinter import *

root = Tk()#creando raiz

root.title("Hola mundo")
root.resizable(1,1)#Evita redimencionar la ventana (cambiarle el tamano)
root.iconbitmap('tkp.ico')#Poner icono alado del titulo

frame = Frame(root, width=480, height=320)#Asignando la anchura y el alto del frame y Creandolo un frame
frame.pack(fill='both', expand=1)#haciendo visible el frame
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)#anadiendo un borde
frame.config(relief="sunken")#anadiendo tipo de borde para que aparezca

#Cambiandole las configuraciones pero a la base root
root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")



#Abajo de todo
root.mainloop()