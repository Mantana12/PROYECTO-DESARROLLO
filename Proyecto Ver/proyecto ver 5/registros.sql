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
INSERT INTO LIBROS (IDLIBRO, IDAUTOR, IDEDITORIAL, IDCATEGORIA, LIBTITULO, LIBDESCRIPCION, LIBISBN, LIBANOPUBLICACION, LIBCANTIDAD) VALUES
(1, 1, 1, 1, 'Harry Potter y la piedra filosofal', 'El primer libro de la serie Harry Potter, donde Harry descubre que es un mago.', '9788478884452', 1997, 50),
(2, 2, 2, 2, '1984', 'Una distopía sobre una sociedad bajo vigilancia constante.', '9780451524935', 1949, 30),
(3, 3, 3, 3, 'Cien años de soledad', 'La historia de la familia Buendía a lo largo de siete generaciones.', '9780307474728', 1967, 40),
(4, 4, 4, 4, 'Kafka en la orilla', 'Una compleja novela que entrelaza diferentes historias.', '9781400079278', 2002, 25),
(5, 5, 5, 5, 'Orgullo y prejuicio', 'Una de las primeras comedias románticas en la historia de la novela.', '9781503290563', 1813, 45),
(6, 6, 6, 6, 'Las aventuras de Tom Sawyer', 'Las aventuras de un joven en el sur de Estados Unidos.', '9780486400778', 1876, 35),
(7, 7, 7, 7, 'Guerra y paz', 'Una de las obras más importantes de la literatura rusa, sobre la invasión napoleónica.', '9780307389640', 1869, 20),
(8, 8, 8, 8, 'Al faro', 'Una reflexión sobre la familia, la pérdida y los recuerdos.', '9780156030472', 1927, 15),
(9, 9, 9, 9, 'Crimen y castigo', 'La historia de un joven estudiante que comete un asesinato.', '9780486415871', 1866, 50),
(10, 10, 10, 10, 'Oliver Twist', 'La vida de un huérfano en Londres y su lucha por la supervivencia.', '9780486424538', 1838, 30);
INSERT INTO USUARIOS (IDUSUARIO, USNOMBRE, USAPELLIDO, USCORREO, USCONTRASENA) VALUES
(1, 'Elena', 'Gomez', 'elena.gomez@gmail.com', 'Elena#2024!'),
(2, 'Carlos', 'Fernandez', 'carlos.fernandez@puce.edu.ec', 'Car123!fernandez'),
(3, 'Lucia', 'Martinez', 'lucia.martinez@hotmail.com', 'Lucia2024$$'),
(4, 'Miguel', 'Lopez', 'miguel.lopez@gmail.com', 'MLopez!4032'),
(5, 'Ana', 'Ruiz', 'ana.ruiz@puce.edu.ec', 'ARuiz%9876'),
(6, 'David', 'Jimenez', 'david.jimenez@hotmail.com', 'DJ2024*hotmail'),
(7, 'Laura', 'Vazquez', 'laura.vazquez@gmail.com', 'LauraVz2024!'),
(8, 'Daniel', 'Moreno', 'daniel.moreno@puce.edu.ec', 'DanM2024!'),
(9, 'Sara', 'Alvarez', 'sara.alvarez@hotmail.com', 'SaraAlva$234'),
(10, 'Pablo', 'Dominguez', 'pablo.dominguez@gmail.com', 'PDom#4753');
INSERT INTO EMPLEADOS (IDEMPLEADO, EMNOMBRE, EMAPELLIDO, EMCORREO, EMCONTRASENA) VALUES
(1, 'Roberto', 'Sánchez', 'roberto.sanchez@gmail.com', 'RobSan2024#'),
(2, 'Marta', 'Díaz', 'marta.diaz@gmail.com', 'MDiaz!7891'),
(3, 'Antonio', 'Morales', 'antonio.morales@gmail.com', 'AntMor2024$$'),
(4, 'Carmen', 'Jiménez', 'carmen.jimenez@gmail.com', 'CarmenJ2024*'),
(5, 'Francisco', 'Navarro', 'francisco.navarro@gmail.com', 'FNavarro%2024'),
(6, 'Laura', 'Gil', 'laura.gil@gmail.com', 'LauraG123!'),
(7, 'Sergio', 'Vega', 'sergio.vega@gmail.com', 'SVega#2024!'),
(8, 'Clara', 'Lorenzo', 'clara.lorenzo@gmail.com', 'ClaraL2024$'),
(9, 'Fernando', 'Hernández', 'fernando.hernandez@gmail.com', 'FerH2024&'),
(10, 'Alicia', 'Romero', 'alicia.romero@gmail.com', 'AliRo2024!');
INSERT INTO COMENTARIOS (IDUSUARIO, IDLIBRO, IDCOMENTARIO, COCOMENTARIO, COVALORACION) VALUES
(1, 1, 1, 'Increíble inicio de serie, totalmente recomendado!', 5),
(2, 2, 2, 'Un clásico que sigue siendo relevante hoy en día.', 4),
(3, 3, 3, 'Una obra maestra del realismo mágico.', 5),
(4, 4, 4, 'Murakami en su mejor momento, surrealista y cautivador.', 4),
(5, 5, 5, 'Romance y crítica social, una combinación perfecta.', 5),
(6, 6, 6, 'Divertido y aventurero, ideal para jóvenes lectores.', 4),
(7, 7, 7, 'Profundo análisis de la sociedad y la guerra.', 5),
(8, 8, 8, 'Un viaje introspectivo a la mente y recuerdos.', 4),
(9, 9, 9, 'Intenso y psicológico, una narrativa impresionante.', 5),
(10, 10, 10, 'Una historia conmovedora sobre la injusticia y la esperanza.', 4);
INSERT INTO PRESTAMOS (IDEMPLEADO, IDLIBRO, IDPRESTAMOS, IDUSUARIO, PRFECHAPRESTAMO, PRFECHADEVOLUCION, PRESTADO) VALUES
(1, 1, 1, 1, '2023-04-01', '2023-04-15', TRUE),
(2, 2, 2, 2, '2023-04-02', '2023-04-16', TRUE),
(3, 3, 3, 3, '2023-04-03', '2023-04-17', TRUE),
(4, 4, 4, 4, '2023-04-04', '2023-04-18', TRUE),
(5, 5, 5, 5, '2023-04-05', '2023-04-19', TRUE),
(6, 6, 6, 6, '2023-04-06', '2023-04-20', TRUE),
(7, 7, 7, 7, '2023-04-07', '2023-04-21', TRUE),
(8, 8, 8, 8, '2023-04-08', '2023-04-22', TRUE),
(9, 9, 9, 9, '2023-04-09', '2023-04-23', TRUE),
(10, 10, 10, 10, '2023-04-10', '2023-04-24', TRUE);
INSERT INTO RESERVAS (IDRESERVA, IDLIBRO, IDUSUARIO, REFECHA) VALUES
(1, 1, 2, '2023-04-25'),
(2, 2, 3, '2023-04-26'),
(3, 3, 4, '2023-04-27'),
(4, 4, 5, '2023-04-28'),
(5, 5, 6, '2023-04-29'),
(6, 6, 7, '2023-04-30'),
(7, 7, 8, '2023-05-01'),
(8, 8, 9, '2023-05-02'),
(9, 9, 10, '2023-05-03'),
(10, 10, 1, '2023-05-04');
INSERT INTO MULTAS (IDEMPLEADO, IDLIBRO, IDPRESTAMOS, IDMULTA, MUVALOR, MUFECHAGENERACION, MUESTADO) VALUES
(1, 1, 1, 1, 15, '2023-04-16', 'Pendiente'),
(2, 2, 2, 2, 20, '2023-04-17', 'Pagada'),
(3, 3, 3, 3, 25, '2023-04-18', 'Pendiente'),
(4, 4, 4, 4, 30, '2023-04-19', 'Pagada'),
(5, 5, 5, 5, 35, '2023-04-20', 'Pendiente'),
(6, 6, 6, 6, 10, '2023-04-21', 'Pagada'),
(7, 7, 7, 7, 15, '2023-04-22', 'Pendiente'),
(8, 8, 8, 8, 20, '2023-04-23', 'Pagada'),
(9, 9, 9, 9, 25, '2023-04-24', 'Pendiente'),
(10, 10, 10, 10, 30, '2023-04-25', 'Pagada');
