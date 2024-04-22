from flask import Flask,request,render_template
from models.libro import Libro
import sqlite3 as sql

def recuperacionRegistrosAutores():
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM AUTORES')
    datos = cursor.fetchall()
    conexion.close()
    return datos

def recuperacionRegistros(tabla):
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM {tabla}')
    datos = cursor.fetchall()
    conexion.close()
    return datos
app = Flask(__name__)
@app.route('/crearLibro',methods = ['GET','POST'])
def registrar_Libro():
    if request.method == 'POST':
        editoriales = recuperacionRegistros('EDITORIALES')
        categorias = recuperacionRegistros('CATEGORIAS')

        editorial = request.form["ideditorial"]
        categoria  = request.form["categoriaf"]
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        isbn = request.form["isbn"]
        cantidad = request.form["cantidad"]
        año = request.form["año"]

        
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        l = Libro(editorial,categoria,titulo,descripcion,isbn,cantidad,año)
        cursor.execute(*l.agregarLibro())
        conexion.commit()
        conexion.close()
        # 'INSERT INTO LIBROS (IDEDITORIAL, IDCATEGORIA, LIBTITULO, LIBDESCRIPCION, LIBISBN, LIBCANTIDAD, LIBANOPUBLICACION) VALUES (?, ?, ?, ?, ?, ?, ?)'
        return render_template('crearLibro.html', editoriales = editoriales,categorias= categorias)
    else:
        editoriales = recuperacionRegistros('EDITORIALES')
        categorias = recuperacionRegistros('CATEGORIAS')
        return render_template('crearLibro.html', editoriales = editoriales,categorias= categorias)

@app.route('/listarLibro',methods = ['GET','POST'])
def listar_Libro():
    if request.method == 'POST':
        autores = recuperacionRegistrosAutores()
        editoriales = recuperacionRegistros('EDITORIALES')
        categorias = recuperacionRegistros('CATEGORIAS')
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        rows = cursor.execute(l.listarLibros())
        conexion.commit()
        return render_template('crearLibro.html',autores = autores,editoriales = editoriales,categorias = categorias, rows = rows)
    else:
        autores = recuperacionRegistrosAutores()
        editoriales = recuperacionRegistros('EDITORIALES')
        categorias = recuperacionRegistros('CATEGORIAS')

        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        rows = cursor.execute(l.listarLibros())
        conexion.commit()
        return render_template('listarLibro.html',autores = autores,editoriales = editoriales,categorias = categorias, rows = rows)
    


@app.route('/consultarLibro/<int:id>',methods = ['GET','POST'])
def consultar_Libro(id):
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    l = Libro()
    cursor.execute(*l.obtenerLibro(id))
    datos = cursor.fetchone()
    return render_template('actualizarLibro.html', idlibro = datos[0], ideditorial= datos[1], categoriaf = datos[2], titulo = datos[3],descripcion = datos[4],isbn = datos[5],cantidad = datos[7])


@app.route('/actualizarLibro/',methods = ['GET','POST'])
def actualizar_Libro():
   if request.method == 'POST':
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        l = Libro()

        
        idlibro = request.form["idlibro"]
        categoria  = request.form["categoriaf"]
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        #isbn = request.form["isbn"]
        cantidad = request.form["cantidad"]
        #año = request.form["año"]

        cursor.execute(*l.actualizar(titulo,descripcion,cantidad,idlibro))
        conexion.commit()
        conexion.close()

        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        rows = cursor.execute(l.listarLibros())
        conexion.commit()
        return render_template('listarLibro.html', rows = rows)
   else:
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        rows = cursor.execute(l.listarLibros())
        conexion.commit()
        return render_template('listarLibro.html', rows = rows)
if __name__ == '__main__':
    app.run( debug = True)