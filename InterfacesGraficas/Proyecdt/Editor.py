from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open

ruta = "" #Se utilizara para almacenar un fichero

def nuevo():
    global ruta
    result = MessageBox.askokcancel("Nuevo", "¿Desea crear un archivo nuevo?")
    if result == True:
        mensaje.set("Nuevo fichero")
        ruta = ""
        text.delete(1.0, "end")
        root.title(" EdT - Text editor")
    else:
        return

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(title="Abrir fichero de texo", initialdir='.', filetype=(("Ficheros de texto", "*.txt"),))
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        text.delete(1.0, 'end')
        text.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - EdT ")

def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = text.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente.")
    else:
        guardarcomo()

def guardarcomo():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar como", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = text.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente.")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

root = Tk()
root.title(" EdT - Editor de texto")

#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Nuevo", command = nuevo)
filemenu.add_command(label = "Abrir", command = abrir)
filemenu.add_command(label = "Guardar", command = guardar)
filemenu.add_command(label = "Guardar como", command = guardarcomo)
filemenu.add_separator()
filemenu.add_command(label = "Salir", command = root.quit)
menubar.add_cascade(menu = filemenu, label = "Archivo")

#Caja de texto central
text = Text(root)
text.pack(fill = "both", expand = 1)
text.config(bd = 0, padx = 6, pady = 4, font = ("Consolas", 12))

#Monitor inferior
mensaje = StringVar()
mensaje.set("EdT editor de texto.")
monitor = Label(root, textvar =mensaje, justify = "left" )
monitor.pack(side = "left")

root.config(menu = menubar)
root.mainloop()