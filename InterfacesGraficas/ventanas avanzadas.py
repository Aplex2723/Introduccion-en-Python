from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser #Seleccion de color
from tkinter import filedialog as FileDialog

root = Tk()
def test():
    #color = ColorChooser.askcolor(title="Elije un color")
    #print(color)
    #ruta = FileDialog.askopenfile(title="Abrir fichero", initialdir="C:",
     #                             filetypes=(("Ficheros de texto", ".txt"),
      #                                       ("Ficheros de texto avanzados", ".txt2"),
       #                                      ("Todos los ficheros", ".")))#Abrir ciertos tipos de ficheros
    #print(ruta)
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="a+", defaultextension=".txt")#Equivale a open ruta en formato
    print(fichero)

Button(root, text="Cliqueame", command=test).pack()

root.mainloop()