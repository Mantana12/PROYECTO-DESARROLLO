from flask import Flask, request, render_template
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
        autor = request.form["idautor"]
        editorial = int(request.form["ideditorial"])
        categoria = int(request.form["categoriaf"])
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        isbn = request.form["isbn"]  
        año = int(request.form["año"])
        cantidad = int(request.form["cantidad"])
        
       
        libro = Libro(autor, editorial, categoria, titulo, descripcion, isbn, cantidad, año)
        
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        cursor.execute(*libro.agregarLibro())
        conexion.commit()
        conexion.close()
        autores = recuperacionRegistros('autores')  
        editoriales = recuperacionRegistros('editoriales')  
        categorias = recuperacionRegistros('categorias') 
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        cursor.execute(l.listarLibros())
        rows = cursor.fetchall()
        return render_template('crearLibro.html', autores=autores, editoriales=editoriales, categorias=categorias, rows=rows)
   
    else:
        autores = recuperacionRegistros('autores')  
        editoriales = recuperacionRegistros('editoriales')  
        categorias = recuperacionRegistros('categorias') 
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        cursor.execute(l.listarLibros())
        rows = cursor.fetchall()
        return render_template('crearLibro.html', autores=autores, editoriales=editoriales, categorias=categorias, rows=rows)



if __name__ == '__main__':
    app.run(debug=True)
