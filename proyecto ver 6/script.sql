CREATE TABLE Nacionalidades
(
   IDNACIONALIDAD INTEGER PRIMARY KEY,
   NANOMBRE CHAR(100),
   NAPAIS CHAR(100)
);
CREATE TABLE Autores
(
   IDAUTOR INTEGER PRIMARY KEY,
   AUNOMBRE CHAR(100),
   AUAPELLIDO CHAR(100),
   IDNACIONALIDAD INTEGER,
   AUFECHANACIMIENTO CHAR(100),
   FOREIGN KEY (IDNACIONALIDAD) REFERENCES Nacionalidades(IDNACIONALIDAD)
);
CREATE TABLE Categorias
(
   IDCATEGORIA INTEGER PRIMARY KEY,
   CANOMBRE CHAR(40),
   CADESCRIPCION CHAR(200)
);

CREATE TABLE Comentarios
(
   IDUSUARIO INTEGER NOT NULL,
   IDLIBRO INTEGER NOT NULL,
   IDCOMENTARIO INTEGER PRIMARY KEY,
   COCOMENTARIO CHAR(400),
   COVALORACION INTEGER,
   FOREIGN KEY(IDUSUARIO) REFERENCES Usuarios(IDUSUARIO),
   FOREIGN KEY(IDLIBRO) REFERENCES Libros(IDLIBRO)
);

CREATE TABLE Editoriales
(
   IDEDITORIAL INTEGER PRIMARY KEY,
   EDNOMBRE CHAR(100),
   EDTELEFONO INTEGER
);

CREATE TABLE Empleados
(
   IDEMPLEADO INTEGER PRIMARY KEY,
   EMNOMBRE CHAR(100),
   EMAPELLIDO CHAR(100),
   EMCORREO CHAR(100),
   EMCONTRASENA CHAR(100)
);

CREATE TABLE Libros
(
   IDLIBRO INTEGER PRIMARY KEY,
   IDEDITORIAL INTEGER,
   IDCATEGORIA INTEGER,
   LIBTITULO CHAR(100),
   LIBDESCRIPCION CHAR(500),
   LIBISBN CHAR(20) UNIQUE,
   LIBANOPUBLICACION INTEGER,
   LIBACTIVO BOOLEAN DEFAULT TRUE,
   LIBCANTIDAD INTEGER,
   FOREIGN KEY(IDEDITORIAL) REFERENCES Editoriales(IDEDITORIAL),
   FOREIGN KEY(IDCATEGORIA) REFERENCES Categorias(IDCATEGORIA)
);
CREATE TABLE AutoresLibros
(
   IDAUTOR INTEGER,
   IDLIBRO INTEGER,
   PRIMARY KEY (IDAUTOR, IDLIBRO),
   FOREIGN KEY (IDAUTOR) REFERENCES Autores(IDAUTOR),
   FOREIGN KEY (IDLIBRO) REFERENCES Libros(IDLIBRO)
);


CREATE TABLE Multas
(
   IDEMPLEADO INTEGER NOT NULL,
   IDLIBRO INTEGER NOT NULL,
   IDPRESTAMOS INTEGER NOT NULL,
   IDMULTA INTEGER PRIMARY KEY,
   MUVALOR INTEGER,
   MUFECHAGENERACION DATE,
   MUESTADO CHAR(11),
   FOREIGN KEY(IDEMPLEADO) REFERENCES Empleados(IDEMPLEADO),
   FOREIGN KEY(IDLIBRO) REFERENCES Libros(IDLIBRO),
   FOREIGN KEY(IDPRESTAMOS) REFERENCES Prestamos(IDPRESTAMOS)
);

CREATE TABLE Prestamos
(
   IDEMPLEADO INTEGER NOT NULL,
   IDLIBRO INTEGER NOT NULL,
   IDPRESTAMOS INTEGER PRIMARY KEY,
   IDUSUARIO INTEGER,
   PRFECHAPRESTAMO DATE,
   PRFECHADEVOLUCION DATE,
   PRESTADO BOOLEAN,
   FOREIGN KEY(IDEMPLEADO) REFERENCES Empleados(IDEMPLEADO),
   FOREIGN KEY(IDLIBRO) REFERENCES Libros(IDLIBRO),
   FOREIGN KEY(IDUSUARIO) REFERENCES Usuarios(IDUSUARIO)
);

CREATE TABLE Reservas
(
   IDRESERVA INTEGER PRIMARY KEY,
   IDLIBRO INTEGER,
   IDUSUARIO INTEGER,
   REFECHA DATE,
   FOREIGN KEY(IDLIBRO) REFERENCES Libros(IDLIBRO),
   FOREIGN KEY(IDUSUARIO) REFERENCES Usuarios(IDUSUARIO)
);

CREATE TABLE Usuarios
(
   IDUSUARIO INTEGER PRIMARY KEY,
   USNOMBRE CHAR(100),
   USAPELLIDO CHAR(100),
   USCORREO CHAR(100),
   USCONTRASENA CHAR(100)
);