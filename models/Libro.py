class Libro:
    def __init__(self, autor=None, editorial=None, categoria=None, titulo=None, descripcion=None, cantidad=None, año=None, id_=None):
        # Constructor de la clase Libro con atributos opcionales para inicializar los valores de cada propiedad
        self.identificador = id_  # Identificador del libro
        self.autor = autor  # Autor del libro
        self.editorial = editorial  # Editorial del libro
        self.categoria = categoria  # Categoría del libro
        self.titulo = titulo  # Título del libro
        self.descripcion = descripcion  # Descripción del libro
        self.año = año  # Año de publicación del libro
        self.cantidad = cantidad  # Cantidad de ejemplares del libro
    
    def agregarLibro(self):
        # Método para generar la consulta SQL de inserción para agregar un libro a la base de datos
        query = 'insert into libros (IDAUTOR, IDEDITORIAL, IDCATEGORIA, LIBTITULO, LIBDESCRIPCION, LIBANOPUBLICACION, LIBCANTIDAD) values (?,?,?,?,?,?,?)'
        registros = (self.autor, self.editorial, self.categoria, self.titulo, self.descripcion, self.año, self.cantidad)
        return (query, registros)  # Devuelve la consulta SQL y los valores a insertar como una tupla
    
    def listarLibros(self):
        # Método para generar la consulta SQL para listar los libros de la base de datos
        query = '''SELECT DISTINCT libros.IDLIBRO, AUTORES.AUNOMBRE, AUTORES.AUAPELLIDO, libros.LIBTITULO, CATEGORIAS.CANOMBRE, libros.LIBDESCRIPCION, libros.LIBCANTIDAD, libros.LIBANOPUBLICACION
                   FROM libros
                   INNER JOIN AUTORES ON libros.IDAUTOR = AUTORES.IDAUTOR
                   INNER JOIN EDITORIALES ON libros.IDEDITORIAL = EDITORIALES.IDEDITORIAL
                   INNER JOIN CATEGORIAS ON libros.IDCATEGORIA = CATEGORIAS.IDCATEGORIA'''
        return query  # Devuelve la consulta SQL para listar los libros
