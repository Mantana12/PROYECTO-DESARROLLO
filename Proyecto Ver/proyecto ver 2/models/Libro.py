
class Libro:
    def __init__(self, autor=None, editorial=None, categoria=None, titulo=None, descripcion=None, cantidad=None, año=None, id_=None):
        self.identificador = id_
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria
        self.titulo = titulo
        self.descripcion = descripcion
        self.año = año
        self.cantidad = cantidad
    def agregarLibro(self):
        query = 'insert into libros (IDAUTOR, IDEDITORIAL, IDCATEGORIA, LIBTITULO, LIBDESCRIPCION, LIBANOPUBLICACION,LIBCANTIDAD)values(?,?,?,?,?,?,?)'
        registros = (self.autor,self.editorial,self.categoria,self.titulo,self.descripcion,self.año,self.cantidad)
        return (query,registros)
    def listarLibros(self):
        query = '''SELECT DISTINCT libros.IDLIBRO, AUTORES.AUNOMBRE, AUTORES.AUAPELLIDO, libros.LIBTITULO, CATEGORIAS.CANOMBRE, libros.LIBDESCRIPCION, libros.LIBCANTIDAD, libros.LIBANOPUBLICACION
                   FROM libros
                   INNER JOIN AUTORES ON libros.IDAUTOR = AUTORES.IDAUTOR
                   INNER JOIN EDITORIALES ON libros.IDEDITORIAL = EDITORIALES.IDEDITORIAL
                   INNER JOIN CATEGORIAS ON libros.IDCATEGORIA = CATEGORIAS.IDCATEGORIA'''
        return query
