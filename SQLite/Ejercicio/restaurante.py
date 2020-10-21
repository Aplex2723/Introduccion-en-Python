import sqlite3

def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)''')

    except sqlite3.OperationalError:
        print("La tabla de la categoria ya existe")

    else:
        print("La tabla de Categorias se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")

    else:
        print("La tabla de Platos se ha creado")
    conexion.close()

def agregar_categoria():
    categoria = input("Nombre de la nueva categoria:\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya ha sido creada anteriormente".format(categoria))
    else:
        print("La categoria '{}' se ha creado correctamente".format(categoria))
    conexion.commit()
    conexion.close()

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria para añadir el plato: ")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))
    
    categoria_usuario = int(input("> "))
    plato = input("Nombre del plato nuevo?:\n>")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario))
    except sqlite3.OperationalError:
        print("El plato {} ya ha sido creado anteriormente.".format(plato))
    else:
        print("El plato {} ha sido creado exitosamente.".format(plato))
    conexion.commit()
    conexion.close()

def mostrar_menu():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM categoria WHERE categoria_id={}".format(categorias[0])).fetchall()

        for plato in platos:
            print("\t{}".format(plato[1]))
    conexion.close()

crear_db()

while True:
    print("\nMenu del restaurante")
    opcion = input(
        "\nIntroduce una categoria: " \
        "\n[1] Agregar categoria" \
        "\n[2] agregar plato" \
        "\n[3] Mostrar menu" \
        "\n[4] Salir\n\n> ")
    
    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        print("Saliendo del programa")
        break

    else:
        print("Opccio incorrecta")