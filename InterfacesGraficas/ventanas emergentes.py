from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

def test():
    #MessageBox.showinfo("Hola!","Hola mundo!")
    #MessageBox.showwarning("Alerta", "Seccion solo para admins")
    #MessageBox.showerror("Error","A ocurrido un error inesperado")
    #resultado = MessageBox.askquestion("Salir", "Estas seguro que quieres salir sin guardar")
    #if resultado == "yes":
     #   root.destroy()
    #resultado = MessageBox.askokcancel("Salir", "¿Sobrescribir el fichero actual?")
    #if resultado == True:
     #   root.destroy()
    #resultado = MessageBox.askyesno("Salir", "Estas seguro que quieres salir sin guardar")
    #if resultado:
     #   root.destroy()
    resultado=MessageBox.askretrycancel("Reintentar", "No es posible la conexion")
    if resultado:
        root.destroy()

Button(root, text="Clicame", command=test).pack()

root.mainloop()