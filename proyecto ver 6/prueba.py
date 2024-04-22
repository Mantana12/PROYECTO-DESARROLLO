from models.libro import Libro
import sqlite3 as sql
conexion = sql.connect('biblioteca.db')
cursor = conexion.cursor()
l = Libro()
cursor.execute(*l.obtenerLibro(11))
datos = cursor.fetchone()
print(datos[0])
print(datos[1])
print(datos[2])
