import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()
#Una vez creadaa la base de datos, no se puede ejecutar nuevamente por que dara error, debe de cambiar los valores
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuarios VALUES ('Hector',27,'hector@ejemplo.com')")

#Recuperando registros
#cursor.execute("SELECT * FROM usuarios")
#usuario = cursor.fetchone()
#print(usuario)

#usuarios = [
#    ('Mario',51,'mario@ejemplo.com'),
#    ('Mercedez',38,'mercedez@ejemplo.com'),
#    ('Juan',19,'juan@ejemplo.com'),
#]
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

#Recuperando varios registros
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuarios)

#confirmar cambios
conexion.commit()
conexion.close()