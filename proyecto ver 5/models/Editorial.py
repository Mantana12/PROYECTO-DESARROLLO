class Editorial:
    def __init__(self,nombre=None,telefono=None):
        self.nombre = nombre
        self.telefono = telefono
    def agregarEditorial(self):
        query = 'insert into editoriales (EDNOMBRE,EDTELEFONO) values(?,?)'
        datos = (self.nombre,self.telefono)
        return (query,datos)
    def listarEditorial(self):
        query = 'select IDEDITORIAL,EDNOMBRE,EDTELEFONO from editoriales'
        return query