import sqlite3
from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()
root.title("Administracion de restaurante")
root.resizable(0,0)
root.config(bd=15)

def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL
                )
        ''')
    except sqlite3.OperationalError:
        print("La categoria ya ha sido creada anteriormente.")

    else:
        print("Se ha creado correctamente la categoria.")

    try:
        cursor.execute('''
            CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        ''')
    except sqlite3.OperationalError:
        MessageBox.showerror("Error", "La categoria ya ha sido creada anteriormente, prueba a usar otro nombre.")
        print("La categoria ya ha sido creada anteriormente.")

    else:
        MessageBox.showwarning("Categoria", "La categoria se ha creado correctamente")
        print("Se ha creado correctamente la categoria.")

    conexion.close()

def agregar_categoria():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES(null, '{}')".format(categoria.get()))
    except sqlite3.IntegrityError:
        MessageBox.showerror("Error", "La categoria ya ha sido creada anteriormente, prueba a usar otro nombre.")
        print("La categoria ya ha sido creada anteriormente.")
    else:
        MessageBox.showwarning("Categoria", "La categoria se ha creado correctamente")
        print("Se ha creado correctamente la categoria.")


def agregar_plato():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()

    tl = Toplevel(root, bg="Orange")
    tl.title("Modificar Datos")
    tl.geometry('600x400')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = IntVar(tl)
    label1 = Label(tl, text='Selecciona una categoria para añadir el plato:')
    label1.grid(row=0, column=0)

    for categoria in categorias:
        label2 = Label(tl, text="[{}] {}".format(categoria[0], categoria[1]))
        label2.grid(row=1, column=0)

    #categoria_usuario = int(input("> "))
    categoria_usuario = Entry(tl, textvariable=inf)
    categoria_usuario.grid(row=0, column=1)

    plat = StringVar()
    #plato = input("¿Nombre del nuevo plato?\n> ")
    plato = Label(tl, text="¿Nombre del nuevo plato?")
    nombre_plato = Entry(tl, textvariable=plat)
    nombre_plato.grid(row=1, column=0)

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(
            plat, categoria_usuario))
    except sqlite3.IntegrityError:
        MessageBox.showerror("El plato '{}' ya existe.".format(plato))
        print("El plato '{}' ya existe.".format(plato))
    else:
        MessageBox.showinfo("Plato '{}' creado correctamente.".format(plato))
        print("Plato '{}' creado correctamente.".format(plato))

    conexion.commit()
    conexion.close()


def mostrar_menu():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    tl = Toplevel(root, bg="Yellow")
    tl.title("Menú del restaurante")
    tl.geometry('600x400')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        #print(categoria[1])
        label = Label(tl, text="[{}]".format(categoria[1]))
        label.grid(row=4, column=0)
        platos = cursor.execute(
            "SELECT * FROM plato WHERE categoria_id={}".format(
                categoria[0])).fetchall()
        for plato in platos:
            Label(tl, text="\t{}".format(plato[1]))
            #print("\t{}".format(plato[1]))

    conexion.close()

categoria = StringVar()
Label(root, text="Ingrese un nombre para una nueva categoria:").pack()
Entry(root, justify="center", textvariable=categoria).pack()  # Primer numero
Label(root, text="").pack()

Button(root, text="Ingresar", command=agregar_categoria).pack(side="left")
Button(root, text="Agregar plato", command=agregar_plato).pack(side="left")
Button(root, text="Menu", command=mostrar_menu).pack(side="left")

crear_db()
root.mainloop()