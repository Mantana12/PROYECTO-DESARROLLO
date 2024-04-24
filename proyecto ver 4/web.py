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
def recuperacionRegistrosID_libros():
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM LIBROS')
    datos = cursor.fetchall()
    conexion.close()
    return datos
@app.route('/crearLibro', methods=['GET', 'POST'])
def registrar_Libro():
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
        libros = recuperacionRegistrosID_libros()
        autores = recuperacionRegistros('autores')  
        editoriales = recuperacionRegistros('editoriales')  
        categorias = recuperacionRegistros('categorias') 
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        cursor.execute(l.listarLibros())
        rows = cursor.fetchall()
        return render_template('crearLibro.html',libros = libros,autores=autores, editoriales=editoriales, categorias=categorias, rows=rows)
    else:
        libros = recuperacionRegistros('libros')
        autores = recuperacionRegistros('autores')  
        editoriales = recuperacionRegistros('editoriales')  
        categorias = recuperacionRegistros('categorias') 
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        cursor.execute(l.listarLibros())
        rows = cursor.fetchall()
        return render_template('crearLibro.html',libros = libros, autores=autores, editoriales=editoriales, categorias=categorias, rows=rows)

'''
@app.route('/eliminarLibro', methods=['GET', 'POST'])
def eliminar_Libro():
    # Variable para el resultado, por defecto vacío
    resultado_eliminacion = ''

    if request.method == 'POST':
        libroid = request.form.get("idlibro", "")  # Obtiene el ID del libro, vacío si no se encuentra

        # Solo procede si libroid no está vacío
        if libroid:
            print("Libro a eliminar:", libroid)
            conexion = sql.connect('biblioteca.db')
            cursor = conexion.cursor()
            l = Libro()
            cursor.execute(*l.eliminarLibro(libroid))

            conexion.commit()
            conexion.close()
            print("Libro eliminado con éxito.")
            resultado_eliminacion = libroid
        else:
            print("No se proporcionó un ID de libro válido.")

    # Recupera los registros de libros para ambos casos, POST y GET
    libros = recuperacionRegistrosID_libros()
    return render_template('eliminarLibro.html', resultado=resultado_eliminacion, libros=libros)
'''

@app.route('/eliminarLibro', methods=['GET', 'POST'])
def eliminar_Libro():
    libroid = ""
    if request.method == 'POST':
        libroid = request.form.get("idlibro", "")
        if libroid:  
            print("Libro a eliminar:", libroid)
            conexion = sql.connect('biblioteca.db')
            cursor = conexion.cursor()
            l = Libro()
            cursor.execute(*l.eliminarLibro(libroid))
            conexion.commit()
            conexion.close()
            conexion = sql.connect('biblioteca.db')
            cursor = conexion.cursor()
            cadena = cursor.execute(*l.VerLibroEliminado(libroid)).fetchone()
            print(cadena)
            print("Libro eliminado con éxito.")
        else:
            print("No se proporcionó un ID de libro.")

        libros = recuperacionRegistrosID_libros()
        return render_template('eliminarLibro.html', resultado=libroid, libros=libros)
    else:
        libros = recuperacionRegistrosID_libros()
        return render_template('eliminarLibro.html', resultado=libroid, libros=libros)
if __name__ == '__main__':
    app.run(debug=True)
