import sqlite3


class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """

    def __init__(self, titulo, autor, anyo, estado="disponible", usuario=None):
        """
        Constructor de la clase Libro.

        :param titulo: Título del libro.
        :param autor: Autor del libro.
        :param anyo: Año de publicación del libro.
        :param estado: Estado del libro ("disponible" o "prestado").
        :param usuario: Nombre del usuario que tiene prestado el libro (opcional).
        """
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.estado = estado
        self.usuario = usuario

    def __str__(self):
        """
        Representación en texto de un objeto Libro.

        :return: Cadena con los detalles del libro.
        """
        # Si el libro está prestado, incluye el nombre del usuario en la representación
        usuario_info = f" - Prestado a: {self.usuario}" if self.estado == "prestado" else ""
        return f"{self.titulo} - {self.autor} ({self.anyo}) - {self.estado}{usuario_info}"


class Biblioteca:
    """
    Clase que gestiona las operaciones de la biblioteca, incluyendo la persistencia de datos en SQLite3.
    """

    def __init__(self):
        """
        Constructor de la clase Biblioteca. Conecta a la base de datos SQLite3 y crea la tabla si no existe.
        """
        # Conexión a la base de datos SQLite3
        self.conexion = sqlite3.connect("biblioteca.db")
        self.cursor = self.conexion.cursor()

        # Crea la tabla 'libros' si no existe
        self._crear_tabla()

    def _crear_tabla(self):
        """
        Crea la tabla 'libros' en la base de datos si no existe.
        """
        # Ejecuta una consulta SQL para crear la tabla
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL COLLATE NOCASE,
                autor TEXT NOT NULL,
                anyo INTEGER NOT NULL,
                estado TEXT NOT NULL,
                usuario TEXT
            )
        ''')

        # Guarda los cambios en la base de datos
        self.conexion.commit()

    def registrar_libro(self):
        """
        Registra un nuevo libro en la base de datos. Solicita los datos al usuario por consola.
        """
        try:
            # Solicita los datos del libro al usuario
            titulo = input("Introduce el título del libro: ").strip()
            autor = input("Introduce el autor del libro: ").strip()
            anyo = int(input("Introduce el año de publicación: "))

            # Inserta el nuevo libro en la base de datos con estado "disponible"
            self.cursor.execute('''
                INSERT INTO libros (titulo, autor, anyo, estado)
                VALUES (?, ?, ?, ?)
            ''', (titulo, autor, anyo, "disponible"))

            # Guarda los cambios en la base de datos
            self.conexion.commit()

            print("\n¡Libro registrado con éxito!")

        except ValueError:
            # Maneja errores si el año no es un número entero
            print("Error: El año debe ser un número entero")

    def consultar_libros(self):
        """
        Consulta y muestra todos los libros registrados en la base de datos.
        """
        # Ejecuta una consulta SQL para obtener todos los libros
        self.cursor.execute("SELECT * FROM libros")

        # Recupera todos los resultados como una lista
        libros = self.cursor.fetchall()

        if not libros:
            # Si no hay libros registrados, muestra un mensaje
            print("\nNo hay libros registrados en la biblioteca.")
            return

        print("\nLista de libros:")

        # Itera sobre los resultados y muestra cada libro con su información
        for libro in libros:
            print(
                f"- {libro[1]} - {libro[2]} ({libro[3]}) - {libro[4]}", end="")

            # Si el libro está prestado, muestra el nombre del usuario que lo tiene
            if libro[5]:
                print(f" - Prestado a: {libro[5]}")
            else:
                print()

    def prestar_libro(self):
        """
        Registra el préstamo de un libro. Solicita el título y el nombre del usuario por consola.

        Verifica que el libro esté disponible antes de realizar el préstamo.
        """
        # Solicita al usuario el título del libro a prestar
        titulo = input("Introduce el título del libro a prestar: ").strip()

        # Verifica si el libro existe y está disponible en la base de datos
        self.cursor.execute(
            "SELECT * FROM libros WHERE titulo = ? AND estado = 'disponible'", (titulo,))

        # Recupera el resultado de la consulta
        libro = self.cursor.fetchone()

        if libro:
            # Solicita al usuario el nombre del prestatario
            usuario = input("Introduce el nombre del usuario: ").strip()

            # Actualiza el estado del libro a "prestado" y registra el nombre del usuario en la base de datos
            self.cursor.execute('''
                UPDATE libros 
                SET estado = 'prestado', usuario = ?
                WHERE titulo = ?
            ''', (usuario, titulo))

            # Guarda los cambios en la base de datos
            self.conexion.commit()

            print("\n¡Préstamo registrado con éxito!")

        else:
            # Si no se encuentra o no está disponible, muestra un mensaje de error
            print("\nError: El libro no existe o no está disponible")

    def devolver_libro(self):
        """
        Registra la devolución de un libro. Solicita el título por consola.

        Verifica que el libro esté prestado antes de realizar la devolución.
        """
        # Solicita al usuario el título del libro a devolver
        titulo = input("Introduce el título del libro a devolver: ").strip()

        # Verifica si el libro existe y está prestado en la base de datos
        self.cursor.execute(
            "SELECT * FROM libros WHERE titulo = ? AND estado = 'prestado'", (titulo,))

        # Recupera el resultado de la consulta
        libro = self.cursor.fetchone()

        if libro:
            # Actualiza el estado del libro a "disponible" y elimina el nombre del usuario en la base de datos
            self.cursor.execute('''
                UPDATE libros 
                SET estado = 'disponible', usuario = NULL
                WHERE titulo = ?
            ''', (titulo,))

            # Guarda los cambios en la base de datos
            self.conexion.commit()

            print("\n¡Devolución registrada con éxito!")

        else:
            # Si no se encuentra o ya está disponible, muestra un mensaje de error
            print("\nError: El libro no existe o ya estaba disponible")


def main():
    """
    Función principal que ejecuta el menú interactivo para gestionar la biblioteca.
    """
    biblioteca = Biblioteca()  # Crea una instancia de Biblioteca

    print("¡Bienvenido al sistema de gestión de la Biblioteca Municipal de Alguazas!")

    continuar = True
    while continuar:
        # Menú principal para seleccionar opciones
        print("\nMenú principal:")
        print("1. Registrar un nuevo libro")
        print("2. Consultar la lista de libros disponibles")
        print("3. Registrar el préstamo de un libro")
        print("4. Registrar la devolución de un libro")
        print("5. Salir")

        try:
            # Solicita al usuario que seleccione una opción
            opcion = int(input("\nSelecciona una opción: "))

            if opcion == 1:
                # Llama al método para registrar un nuevo libro
                biblioteca.registrar_libro()
            elif opcion == 2:
                # Llama al método para consultar todos los libros
                biblioteca.consultar_libros()
            elif opcion == 3:
                # Llama al método para registrar el préstamo de un libro
                biblioteca.prestar_libro()
            elif opcion == 4:
                # Llama al método para registrar la devolución de un libro
                biblioteca.devolver_libro()
            elif opcion == 5:
                # Sale del programa y cierra la conexión a la base de datos
                print("\n¡Gracias por usar el sistema! Hasta pronto 👋")
                biblioteca.conexion.close()  # Cierra la conexión a la base de datos antes de salir
                continuar = False
            else:
                # Muestra un mensaje si el usuario introduce una opción no válida
                print("Opción no válida. Introduce un número del 1 al 5.")

        except ValueError:
            # Maneja errores si el usuario introduce algo que no sea un número entero
            print("Error: Debes introducir un número válido (1-5)")


if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta directamente
