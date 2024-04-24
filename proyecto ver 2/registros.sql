INSERT INTO AUTORES (IDAUTOR, AUNOMBRE, AUAPELLIDO, AUNACIONALIDAD, AUFECHANACIMIENTO) VALUES
(1, 'Joanne', 'Rowling', 'Británica', '1965-07-31'),
(2, 'George', 'Orwell', 'Británica', '1903-06-25'),
(3, 'Gabriel', 'García Márquez', 'Colombiana', '1927-03-06'),
(4, 'Haruki', 'Murakami', 'Japonesa', '1949-01-12'),
(5, 'Jane', 'Austen', 'Británica', '1775-12-16'),
(6, 'Mark', 'Twain', 'Estadounidense', '1835-11-30'),
(7, 'Leo', 'Tolstoy', 'Rusa', '1828-09-09'),
(8, 'Virginia', 'Woolf', 'Británica', '1882-01-25'),
(9, 'Fyodor', 'Dostoevsky', 'Rusa', '1821-11-11'),
(10, 'Charles', 'Dickens', 'Británica', '1812-02-07');
INSERT INTO CATEGORIAS (IDCATEGORIA, CANOMBRE, CADESCRIPCION) VALUES
(1, 'Fantasía', 'Libros que contienen elementos mágicos y sobrenaturales.'),
(2, 'Distopía', 'Obras que exploran sociedades utópicas fallidas.'),
(3, 'Realismo mágico', 'Narrativa que incorpora elementos mágicos en entornos realistas.'),
(4, 'Literatura contemporánea', 'Obras literarias escritas desde la segunda mitad del siglo XX hasta la actualidad.'),
(5, 'Romance', 'Historias centradas en las relaciones románticas entre personajes.'),
(6, 'Aventura', 'Narrativas que cuentan las vivencias de personajes en situaciones de riesgo y descubrimiento.'),
(7, 'Histórica', 'Ficción que recrea eventos históricos o períodos específicos.'),
(8, 'Psicológica', 'Literatura que explora la psicología de los personajes, sus emociones y su mente.'),
(9, 'Crimen', 'Narrativa centrada en crímenes, su investigación y sus consecuencias.'),
(10, 'Clásicos', 'Obras literarias reconocidas por su mérito artístico y universalidad.');
INSERT INTO EDITORIALES (IDEDITORIAL, EDNOMBRE, EDTELEFONO) VALUES
(1, 'Bloomsbury', 123456789),
(2, 'Secker & Warburg', 987654321),
(3, 'Editorial Sudamericana', 567890123),
(4, 'Shinchosha', 321098765),
(5, 'T. Egerton', 654321098),
(6, 'American Publishing Company', 456789012),
(7, 'The Russian Messenger', 789012345),
(8, 'Hogarth Press', 234567890),
(9, 'The Russian Messenger', 890123456),
(10, 'Richard Bentley', 123789456);
INSERT INTO LIBROS (IDLIBRO, IDAUTOR, IDEDITORIAL, IDCATEGORIA, LIBTITULO, LIBDESCRIPCION, LIBANOPUBLICACION, LIBCANTIDAD) VALUES
(1, 1, 1, 1, 'Harry Potter y la piedra filosofal', 'El primer libro de la serie Harry Potter, donde Harry descubre que es un mago.', 1997, 50),
(2, 2, 2, 2, '1984', 'Una distopía sobre una sociedad bajo vigilancia constante.', 1949, 30),
(3, 3, 3, 3, 'Cien años de soledad', 'La historia de la familia Buendía a lo largo de siete generaciones.', 1967, 40),
(4, 4, 4, 4, 'Kafka en la orilla', 'Una compleja novela que entrelaza diferentes historias.', 2002, 25),
(5, 5, 5, 5, 'Orgullo y prejuicio', 'Una de las primeras comedias románticas en la historia de la novela.', 1813, 45),
(6, 6, 6, 6, 'Las aventuras de Tom Sawyer', 'Las aventuras de un joven en el sur de Estados Unidos.', 1876, 35),
(7, 7, 7, 7, 'Guerra y paz', 'Una de las obras más importantes de la literatura rusa, sobre la invasión napoleónica.', 1869, 20),
(8, 8, 8, 8, 'Al faro', 'Una reflexión sobre la familia, la pérdida y los recuerdos.', 1927, 15),
(9, 9, 9, 9, 'Crimen y castigo', 'La historia de un joven estudiante que comete un asesinato.', 1866, 50),
(10, 10, 10, 10, 'Oliver Twist', 'La vida de un huérfano en Londres y su lucha por la supervivencia.', 1838, 30);
