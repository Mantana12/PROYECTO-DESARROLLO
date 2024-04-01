from flask import Flask, request, render_template
import sqlite3 as sql
from models.Libro import Libro  # Importa la clase Libro desde el módulo models.Libro

app = Flask(__name__)  # Crea una instancia de Flask

# Función para recuperar registros de una tabla específica en la base de datos
def recuperacionRegistros(tabla):
    conexion = sql.connect('biblioteca.db')  # Conecta a la base de datos SQLite
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM {tabla}')  # Ejecuta una consulta SQL para obtener todos los registros de la tabla
    datos = cursor.fetchall()  # Obtiene todos los registros como una lista de tuplas
    conexion.close()
    return datos  # Devuelve los datos obtenidos
# Ruta para servir archivos estáticos (CSS, JS, imágenes, etc.)
@app.route('/static/<path:path>')
def static_files(path):
    return app.send_static_file(path)

#crear Libro
@app.route('/crearLibro', methods=['GET', 'POST'])
def libro():
    if request.method == 'POST':
        # Obtiene los datos del formulario enviado por el usuario
        autor = request.form["idautor"]
        editorial = int(request.form["ideditorial"])
        categoria = int(request.form["categoriaf"])
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        año = int(request.form["año"])
        cantidad = int(request.form["cantidad"])
        
        # Establece conexión con la base de datos
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        
        # Consulta para obtener el ID real del autor
        cursor.execute('SELECT IDAUTOR FROM AUTORES WHERE IDAUTOR = ?', (autor,))
        autor = cursor.fetchone()[0]  # Obtiene el ID real del autor
        
        # Consulta para obtener el ID real de la editorial
        cursor.execute('SELECT IDEDITORIAL FROM EDITORIALES WHERE IDEDITORIAL = ?', (editorial,))
        editorial = cursor.fetchone()[0]  # Obtiene el ID real de la editorial
        
        # Consulta para obtener el ID real de la categoría
        cursor.execute('SELECT IDCATEGORIA FROM CATEGORIAS WHERE IDCATEGORIA = ?', (categoria,))
        categoria = cursor.fetchone()[0]  # Obtiene el ID real de la categoría
        
        # Crea una instancia de la clase Libro con los datos proporcionados
        libro = Libro(autor, editorial, categoria, titulo, descripcion, cantidad, año)
        
        # Ejecuta el método para agregar un libro en la base de datos
        cursor.execute(*libro.agregarLibro())
        
        # Confirma la transacción en la base de datos
        conexion.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        return 'Libro Agregado Exitosamente!...'  # Devuelve un mensaje de éxito
        
    else:
        # Recupera los registros de autores, editoriales y categorías para mostrar en el formulario
        autores = recuperacionRegistros('autores')  
        editoriales = recuperacionRegistros('editoriales')  
        categorias = recuperacionRegistros('categorias') 
        
        # Renderiza el template 'crearLibro.html' y pasa los datos de autores, editoriales y categorías al template
        return render_template('crearLibro.html', autores=autores, editoriales=editoriales, categorias=categorias)


# Ruta para listar los libros disponibles en la biblioteca
@app.route('/listarLibro')
def listado_libros():
    conexion = sql.connect('biblioteca.db')  # Conecta a la base de datos SQLite
    conexion.row_factory = sql.Row  # Esto hace que los resultados sean accesibles como diccionarios
    cursor = conexion.cursor()
    l = Libro()  # Crea una instancia de la clase Libro
    cursor.execute(l.listarLibros())  # Ejecuta la consulta para listar los libros
    rows = cursor.fetchall()  # Obtiene todos los registros como una lista de diccionarios (filas)
    return render_template('listarLibro.html', rows=rows)  # Renderiza el template 'listarLibro.html' y pasa los datos de los libros al template

# Ruta para servir archivos estáticos (en este caso, tu archivo CSS)
@app.route('/Front-End/<path:path>')
def static_proxy(path):
    return app.send_static_file(f'Front-End/{path}')

# Punto de entrada principal para ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
