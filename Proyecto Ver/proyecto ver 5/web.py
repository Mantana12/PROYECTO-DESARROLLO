 #Librerias y importaciones
from flask import Flask, request
import sqlite3 as sql
from models.Libro import Libro
from models.Autor import Autor
from models.Editorial import Editorial
from flask import Flask, request, render_template
from flask import redirect, url_for
from flask import jsonify
#Desarrollo del código fuente
app = Flask(__name__)
#Recuperación de registros
def recuperacionRegistros(tabla):
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM {tabla}')
    datos = cursor.fetchall()
    conexion.close()
    return datos
#Recuperacion de registros Libros
def recuperacionRegistrosID_libros():
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM LIBROS')
    datos = cursor.fetchall()
    conexion.close()
    return datos
#Recupercacion de registros autores
def recuperacionRegistrosID_autores():
    conexion = sql.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM AUTORES')
    datos = cursor.fetchall()
    conexion.close()
    return datos
#Método para validar ID
def es_valor_valido(valor):
    try:
        # Intenta convertir el valor a un entero
        valor_entero = int(valor)
        # Verifica si el valor es positivo (suponiendo que los IDs de autor sean números positivos)
        if valor_entero > 0:
            return True
        else:
            return False
    except ValueError:
        # Si no se puede convertir a entero, el valor no es válido
        return False

#Métodos para realizar Crud
#Crear Libros
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
        autores = recuperacionRegistros('autores') 
        libros = recuperacionRegistros('libros')
        editoriales = recuperacionRegistros('editoriales')  
        categorias = recuperacionRegistros('categorias') 
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        cursor.execute(l.listarLibros())
        rows = cursor.fetchall()
        return render_template('crearLibro.html',libros = libros, autores=autores, editoriales=editoriales, categorias=categorias, rows=rows)

# Crear Autor
@app.route('/crearAutor', methods=['GET', 'POST'])
def crearAutor():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        nacionalidad = request.form["nacionalidad"]
        fecha_nacimiento = request.form["fecha_nacimiento"]

        autor = Autor(nombre, apellido, nacionalidad, fecha_nacimiento)
        query, datos = autor.agregarAutor()
         # Realizar la inserción en la base de datos
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        cursor.execute(query, datos)
        conexion.commit()
        conexion.close()


        # Después de agregar el autor, redirige a la vista para crear otro autor
        return redirect(url_for('crearAutor'))

    else:
         # Recuperar los autores de la base de datos
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM AUTORES')
        autores = cursor.fetchall()  # Recuperar los datos de los autores
        conexion.close()  # Cerrar la conexión después de obtener los datos
        return render_template('crearAutor.html', autores=autores)
   
 #Eliminar Autores
@app.route('/eliminarAutor', methods=['GET', 'POST'])
def eliminarAutor():
    autorid = ""
    if request.method == 'POST':
        autorid = request.form.get("idautor", "")
        if autorid:  
            print("Autor a eliminar:", autorid)
            conexion = sql.connect('biblioteca.db')
            cursor = conexion.cursor()
            a = Autor()
            cursor.execute(*a.eliminarAutor(autorid))
            conexion.commit()
            conexion.close()
            conexion = sql.connect('biblioteca.db')
            cursor = conexion.cursor()
            cadena = cursor.execute(*a.VerAutorEliminado(autorid)).fetchone()
            print(cadena)
            print("Autor eliminado con éxito.")
        else:
            print("No se proporcionó un ID de autor.")

        autores = recuperacionRegistrosID_autores()
        return render_template('eliminarAutor.html', resultado=autorid, autores=autores)
    else:
        autores = recuperacionRegistrosID_autores()
        return render_template('eliminarAutor.html', resultado=autorid, autores=autores)
#Actualizar Autor
@app.route('/actualizarAutor', methods=['GET', 'POST'])
def actualizarAutor():
    if request.method == 'POST':
        autor_id = request.form.get("idautor", "")
        if autor_id:
            # Recuperar los datos del formulario de actualización
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            nacionalidad = request.form["nacionalidad"]
            fecha_nacimiento = request.form["fecha_nacimiento"]

            # Verificar si el ID del autor es un valor válido
            if es_valor_valido(autor_id):
                # Crear una instancia de la clase Autor y llamar al método actualizarAutor
                autor = Autor()
                autor.actualizarAutor(autor_id, nombre, apellido, nacionalidad, fecha_nacimiento)

                # Recuperar los autores actualizados
                autores = recuperacionRegistrosID_autores()
                # Devolver una respuesta JSON con el mensaje y la redirección
                return jsonify({"mensaje": "Autor actualizado correctamente", "redireccion": "/crearAutor"})
                
            else:
                 # Devolver un mensaje de error si el ID del autor no es válido
                return jsonify({"error": "ID de autor no válido"})
        else:
            # Devolver una respuesta de error si no se proporciona un ID de autor
            return jsonify({"error": "No se proporcionó un ID de autor para actualizar."})
    else:
          # Recuperar los autores de la base de datos
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM AUTORES')
        autores = cursor.fetchall()  # Recuperar los datos de los autores
        conexion.close()  # Cerrar la conexión después de obtener los datos
        return render_template('actualizarAutor.html', autores=autores)
#Eliminar Libros
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


@app.route('/actualizarLibro', methods=['GET', 'POST'])
def actualizar_Libro():
    if request.method == 'POST':
        libros = recuperacionRegistrosID_libros()
        editoriales = recuperacionRegistros('editoriales')
        categorias = recuperacionRegistros('categorias')

        idlibro = request.form["idlibro"]
        ideditorial = request.form["ideditorial"]
        idecategoria = request.form["categoriaf"]
        idtitulo = request.form["titulo"]
        iddescripcion  = request.form["descripcion"]
        cantidad = int(request.form["cantidad"])
        año = int(request.form["año"])
        l = Libro()
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        cursor.execute(*l.actualizarLibro(ideditorial,idecategoria,idtitulo,iddescripcion,cantidad,año,idlibro))
        conexion.commit()
        conexion.close()
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        cursor.execute(l.listarLibros())
        rows = cursor.fetchall()
        return render_template('actualizarLibro.html',rows = rows,libros = libros, editoriales = editoriales,categorias = categorias)
    else:
        libros = recuperacionRegistrosID_libros()
        editoriales = recuperacionRegistros('editoriales')
        categorias = recuperacionRegistros('categorias')
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        l = Libro()
        cursor.execute(l.listarLibros())
        rows = cursor.fetchall()
        return render_template('actualizarLibro.html',rows = rows,libros = libros, editoriales = editoriales, categorias = categorias)
    


@app.route('/crearEditorial',methods = ['GET','POST'])
def registrar_Editorial():
    if request.method == 'POST':
        autores = request.form["nombre"]
        telefono = request.form["telefono"]
        conexion = sql.connect('biblioteca.db')
        cursor = conexion.cursor()
        e = Editorial(autores,telefono)
        cursor.execute(*e.agregarEditorial())
        conexion.commit()
        conexion.close()
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        e = Editorial()
        cursor.execute(e.listarEditorial())
        editoriales = cursor.fetchall()
        return render_template('crearEditorial.html',editoriales = editoriales)
    else:
        conexion = sql.connect('biblioteca.db')
        conexion.row_factory = sql.Row
        cursor = conexion.cursor()
        e = Editorial()
        cursor.execute(e.listarEditorial())
        editoriales = cursor.fetchall()
        return render_template('crearEditorial.html',editoriales = editoriales)

@app.route('/', methods=['GET', 'POST'])
def Raiz():
    return render_template('Index.html')
if __name__ == '__main__':
    app.run(debug=True)

