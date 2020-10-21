import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

#cursor.execute('''
#    CREATE TABLE usuarios (
#            dni VARCHAR(9) PRIMARY KEY,
#            nombre VARCHAR(100),
#            edad INTEGER,
#            email VARCHAR(100)
#            ) ''')

#usuarios = [
#    ('11111111A','Hector',27,'hector@ejemplo.com'),
#    ('22222222B','Mario',51,'mario@ejemplo.com'),
#    ('33333333C','Mercedez',38,'mercedez@ejemplo.com'),
#    ('44444444D','Juan',19,'juan@ejemplo.com'),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#cursor.execute('''
#    CREATE TABLE productos (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        nombre VARCHAR(100) NOT NULL,
#        marca VARCHAR(50) NOT NULL,
#        precio FLOAT NOT NULL
#    )
#    ''')

#productos = [
#    ('Teclado', 'Loguitech', 18.93),
#    ('Pantalla 18"', 'LG', 89.95)
#]
#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

#cursor.execute("SELECT * FROM productos")

#productos = cursor.fetchall()
#for producto in productos:
#    print(productos)

#CLAVEZ UNICAS                  ------           NO SE PUEDE REPETIR EL MISMO DNI
cursor.execute('''
    CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
        )
        ''')
usuarios = [
    ('11111111A','Hector',27,'hector@ejemplo.com'),
    ('22222222B','Mario',51,'mario@ejemplo.com'),
    ('33333333C','Mercedez',38,'mercedez@ejemplo.com'),
    ('44444444D','Juan',19,'juan@ejemplo.com'),
]

cursor.executemany("INSERT INTO usuarios VALUES (null, ?, ?, ?, ?)", usuarios)

conexion.commit()
conexion.close()