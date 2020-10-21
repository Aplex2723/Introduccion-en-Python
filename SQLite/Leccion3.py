import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

#cursor.execute("SELECT * FROM usuarios WHERE edad='27'")

#usuarios = cursor.fetchall()
#print(usuarios)

#MODIFICAR REGISTRO
#cursor.execute("UPDATE usuarios SET nombre='Hector Costa', edad=30 WHERE dni='11111111A'")

#ELIMINAR
cursor.execute("DELETE FROM usuarios WHERE dni='11111111A'")#No descuidar el where, si no se borra todo

conexion.commit()
conexion.close()