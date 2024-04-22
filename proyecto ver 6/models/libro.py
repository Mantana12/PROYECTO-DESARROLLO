class Libro:
    def __init__(self,editorial = None,categoria= None,titulo = None,descripcion = None,isbn = None, año  = None,cantidad = None,id_ = None):
        self.editorial = editorial
        self.categoria = categoria
        self.titulo = titulo
        self.descripcion = descripcion
        self.isbn = isbn  
        self.año = año
        self.cantidad = cantidad
        self.identificador = id_
    def agregarLibro(self):
        query ='INSERT INTO LIBROS (IDEDITORIAL, IDCATEGORIA, LIBTITULO, LIBDESCRIPCION, LIBISBN, LIBCANTIDAD, LIBANOPUBLICACION) VALUES (?, ?, ?, ?, ?, ?, ?)'
        registros = (self.editorial, self.categoria, self.titulo, self.descripcion, self.isbn, self.cantidad, self.año)
        return (query, registros)
    
    def listarLibros(self):
        query = '''
        SELECT Libros.IDLIBRO,Autores.AUNOMBRE,Autores.AUAPELLIDO,Libros.LIBTITULO,Libros.LIBDESCRIPCION,Categorias.CANOMBRE,Editoriales.EDNOMBRE,Libros.LIBISBN,Libros.LIBCANTIDAD,Libros.LIBANOPUBLICACION,CASE WHEN Libros.LIBACTIVO = 1 THEN 'ACTIVO'WHEN Libros.LIBACTIVO = 0 THEN 'INACTIVO'END AS 'ESTADO'
        FROM Libros
    LEFT JOIN AutoresLibros ON Libros.IDLIBRO = AutoresLibros.IDLIBRO
    LEFT JOIN Autores ON AutoresLibros.IDAUTOR = Autores.IDAUTOR
    LEFT JOIN Categorias ON Libros.IDCATEGORIA = Categorias.IDCATEGORIA
    LEFT JOIN Editoriales ON Libros.IDEDITORIAL = Editoriales.IDEDITORIAL
    UNION
    SELECT Libros.IDLIBRO,Autores.AUNOMBRE,Autores.AUAPELLIDO,Libros.LIBTITULO,Libros.LIBDESCRIPCION,Categorias.CANOMBRE,Editoriales.EDNOMBRE,Libros.LIBISBN,Libros.LIBCANTIDAD,Libros.LIBANOPUBLICACION,CASE WHEN Libros.LIBACTIVO = 1 THEN 'ACTIVO'WHEN Libros.LIBACTIVO = 0 THEN 'INACTIVO'END AS 'ESTADO'
    FROM AutoresLibros
    LEFT JOIN Libros ON AutoresLibros.IDLIBRO = Libros.IDLIBRO
    LEFT JOIN Autores ON AutoresLibros.IDAUTOR = Autores.IDAUTOR
    LEFT JOIN Categorias ON Libros.IDCATEGORIA = Categorias.IDCATEGORIA
    LEFT JOIN Editoriales ON Libros.IDEDITORIAL = Editoriales.IDEDITORIAL
    WHERE
    Libros.IDLIBRO IS NULL;
                    '''
        return query
    
    def obtenerLibro(self,id):
        query = f'''
        select Libros.IDLIBRO,Editoriales.EDNOMBRE,Categorias.CANOMBRE,Libros.LIBTITULO,Libros.LIBDESCRIPCION,Libros.LIBISBN,Libros.LIBANOPUBLICACION,Libros.LIBCANTIDAD
            from Libros
            inner join Editoriales
            on Libros.IDEDITORIAL = Editoriales.IDEDITORIAL
            inner JOIN Categorias
            on Categorias.IDCATEGORIA = Libros.IDCATEGORIA
            where Libros.IDLIBRO = (?)
        '''
        dato = (id,)
        return (query, dato)
    def actualizar(self, titulo, descripcion, cantidad, identificador):
        query = '''
            UPDATE libros SET LIBTITULO = ?, LIBDESCRIPCION = ?, LIBCANTIDAD = ? WHERE IDLIBRO = ?
        '''
        datos = (titulo, descripcion, cantidad, identificador)
        return (query, datos)


'''
select Libros.IDLIBRO,Editoriales.EDNOMBRE,Categorias.CANOMBRE,Libros.LIBTITULO,Libros.LIBDESCRIPCION,Libros.LIBISBN,Libros.LIBANOPUBLICACION,Libros.LIBCANTIDAD
from Libros
inner join Editoriales
on Libros.IDEDITORIAL = Editoriales.IDEDITORIAL
inner JOIN Categorias
on Categorias.IDCATEGORIA = Libros.IDCATEGORIA
where Libros.IDLIBRO = 11
'''