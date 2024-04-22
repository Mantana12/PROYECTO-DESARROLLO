
#Clase Libro
class Libro:
    def __init__(self, autor=None, editorial=None, categoria=None, titulo=None, descripcion=None, isbn=None, cantidad=None, año=None, id_=None):
        self.identificador = id_
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria
        self.titulo = titulo
        self.descripcion = descripcion
        self.isbn = isbn  
        self.año = año
        self.cantidad = cantidad
    def agregarLibro(self):
        query = 'INSERT INTO LIBROS (IDAUTOR, IDEDITORIAL, IDCATEGORIA, LIBTITULO, LIBDESCRIPCION, LIBISBN, LIBANOPUBLICACION, LIBCANTIDAD) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        registros = (self.autor, self.editorial, self.categoria, self.titulo, self.descripcion, self.isbn, self.año, self.cantidad)
        return (query, registros)

    def listarLibros(self):
        query = '''SELECT DISTINCT LIBROS.IDLIBRO, AUTORES.AUNOMBRE, AUTORES.AUAPELLIDO, LIBROS.LIBTITULO, CATEGORIAS.CANOMBRE, LIBROS.LIBDESCRIPCION, LIBROS.LIBISBN, LIBROS.LIBCANTIDAD, LIBROS.LIBANOPUBLICACION
                   FROM LIBROS
                   INNER JOIN AUTORES ON LIBROS.IDAUTOR = AUTORES.IDAUTOR
                   INNER JOIN EDITORIALES ON LIBROS.IDEDITORIAL = EDITORIALES.IDEDITORIAL
                   INNER JOIN CATEGORIAS ON LIBROS.IDCATEGORIA = CATEGORIAS.IDCATEGORIA'''
        return query
    
    def eliminarLibro(self,id):
        query = 'DELETE FROM LIBROS WHERE IDLIBRO = (?)'
        dato = (id,)
        return (query, dato)
    def VerLibroEliminado(self,id):
        query = 'SELECT LIBTITULO FROM LIBROS WHERE IDLIBRO = (?)'
        dato = (id,)
        return (query, dato)
    def actualizarLibro(self,ideditorial,idecategoria,idtitulo,iddescripcion,cantidad,año,idlibro):
        query = f'''
        UPDATE LIBROS
        SET  IDEDITORIAL = ?, IDCATEGORIA = ?, LIBTITULO = ?, LIBDESCRIPCION = ?, LIBANOPUBLICACION = ?, LIBCANTIDAD = ?
        WHERE IDLIBRO = ?
        '''
        dato = (ideditorial, idecategoria, idtitulo, iddescripcion, cantidad, año,idlibro)
        return (query, dato)


