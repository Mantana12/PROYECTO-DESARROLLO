from flask import Flask,request,render_template
import sqlite3 as sql
from models.Libro import Libro

app = Flask(__name__)

def recuperacionRegistros(tabla):
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM {tabla}')
    datos = cursor.fetchall()
    conexion.close()
    return datos
@app.route('/crearLibro', methods=['GET', 'POST'])
def libro():
    if request.method == 'POST':
        autor_id = request.form["idautor"]
        editorial_id = int(request.form["ideditorial"])
        categoria_id = int(request.form["categoriaf"])
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        año = int(request.form["año"])
        cantidad = int(request.form["cantidad"])
        
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        
        # Obtener nombre y apellido del autor
        cursor.execute('SELECT IDAUTOR, AUNOMBRE, AUAPELLIDO FROM AUTORES WHERE IDAUTOR = ?', (autor_id,))
        autor_data = cursor.fetchone()
        autor_nombre = autor_data[1]  # Índice 1 para el nombre del autor
        autor_apellido = autor_data[2]  # Índice 2 para el apellido del autor
        
        # Obtener ID de editorial y categoría si es necesario
        cursor.execute('SELECT IDEDITORIAL FROM EDITORIALES WHERE IDEDITORIAL = ?', (editorial_id,))
        editorial_id = cursor.fetchone()[0]
        
        cursor.execute('SELECT IDCATEGORIA FROM CATEGORIAS WHERE IDCATEGORIA = ?', (categoria_id,))
        categoria_id = cursor.fetchone()[0]
        
        libro = Libro(autor_nombre, autor_apellido, editorial_id, categoria_id, titulo, descripcion, año, cantidad)
        cursor.execute(*libro.agregarLibro())
        conexion.commit()
        conexion.close()
        return 'Libro agregado'
    
    else:
        autores = recuperacionRegistros('autores')  
        editoriales = recuperacionRegistros('editoriales')  
        categorias = recuperacionRegistros('categorias') 
        return render_template('crearLibro.html', autores=autores, editoriales=editoriales, categorias=categorias)

@app.route('/listarLibro')
def listado_libros():
    conexion = sql.connect('biblioteca.db')
    conexion.row_factory = sql.Row  # Esto hace que los resultados sean accesibles como diccionarios
    cursor = conexion.cursor()
    l = Libro()
    cursor.execute(l.listarLibros())
    rows = cursor.fetchall()
    return render_template('listarLibro.html', rows=rows)




if __name__ == '__main__':
    app.run(debug=True)





