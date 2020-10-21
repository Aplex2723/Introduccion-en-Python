import sqlite3
from tkinter import *

root = Tk()
root.title("Restaurante Panchito  --  Menu")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="      Restaurante     ", fg="darkgreen", font=("Time New Roman", 28, "bold italic")).pack()
Label(root, text="       Panchito        ", fg="darkgreen", font=("Time New Roman", 28, "bold italic")).pack()
Label(root, text="Menu del dia", fg="green", font=("Time New Roman", 24, "bold italic")).pack()

Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

categoria = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categoria:
    Label(root, text=categoria[1], fg="black", font=("Time New Roman", 20, "bold italic")).pack()

    platos = cursor.execute(
        "SELECT *FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()

    for plato in platos:
        Label(root, text=plato[1], fg="gray", font=("Time New Roman", 15, "italic")).pack()

    Label(root, text="").pack()
conexion.close()

Label(root, text="12$ (IVA Incluido)", fg="darkgreen", font=("Time New Roman", 15, "bold italic")).pack(side="right")
root.mainloop()

