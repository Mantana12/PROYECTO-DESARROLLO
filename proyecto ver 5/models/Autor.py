import sqlite3 as sql
#Clase Autor
class Autor:
    def __init__(self, nombre=None, apellido=None, nacionalidad=None, fecha_nacimiento=None, id_=None):
        self.id = id_
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
#Clase para Agregar el autor
    def agregarAutor(self):
        query = 'INSERT INTO AUTORES (AUNOMBRE, AUAPELLIDO, AUNACIONALIDAD, AUFECHANACIMIENTO) VALUES (?, ?, ?, ?)'
        datos = (self.nombre, self.apellido, self.nacionalidad, self.fecha_nacimiento)
        return query, datos
    
#Clase para poder ver los autores creados
    def listarAutores(self):
        query = '''SELECT AUTORES.IDAUTOR, AUTORES.AUNOMBRE, AUTORES.AUAPELLIDO, AUTORES.AUNACIONALIDAD, AUTORES.FECHANACIMIENTO
                   FROM AUTORES'''
        return query

#Clase para eliminar autores
    def eliminarAutor(self, id):
        query = 'DELETE FROM AUTORES WHERE IDAUTOR = ?'
        dato = (id,)
        return query, dato
    
# Método para obtener el título de un libro eliminado
    def VerAutorEliminado(self, id):
        query = 'SELECT AUNOMBRE, AUAPELLIDO FROM AUTORES WHERE IDAUTOR = (?)'
        dato = (id,)
        return (query, dato)

# Método para actualizar un autor
    def actualizarAutor(self, autor_id, nombre, apellido, nacionalidad, fecha_nacimiento):
        # Consulta SQL para actualizar los datos del autor
        query = "UPDATE AUTORES SET AUNOMBRE=?, AUAPELLIDO=?, AUNACIONALIDAD=?, AUFECHANACIMIENTO=? WHERE IDAUTOR=?"
        
        # Conexión a la base de datos y ejecución de la consulta
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        cursor.execute(query, (nombre, apellido, nacionalidad, fecha_nacimiento, autor_id))
        
        # Confirmar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()

