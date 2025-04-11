# Pistas adicionales para resolver el reto

Si en algún momento te quedas bloqueado, aquí tienes algunas sugerencias y pasos detallados para abordar cada apartado del reto:

---

## 1. Crear la base de datos SQLite3

- Usa la librería `sqlite3` para conectarte a la base de datos. Si no existe el archivo `biblioteca.db`, se creará automáticamente.
- Crea la tabla `libros` con una consulta SQL como esta:

```sql
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    anio INTEGER NOT NULL,
    estado TEXT NOT NULL,
    usuario TEXT
);
```

- Usa `cursor.execute()` para ejecutar las consultas SQL y asegúrate de llamar a `connection.commit()` para guardar los cambios.

---

## 2. Diseñar las clases

- Crea una clase `Libro` que represente cada libro. Por ejemplo:

```python
class Libro:
    def __init__(self, titulo, autor, anio, estado="disponible", usuario=None):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.estado = estado
        self.usuario = usuario
```

- Crea una clase `Biblioteca` que gestione las operaciones principales (añadir libros, consultar libros, prestar y devolver). Esta clase debe interactuar con la base de datos.

---

## 3. Registrar un nuevo libro

- En la clase `Biblioteca`, crea un método llamado `registrar_libro()` que:
  - Reciba los datos del libro como parámetros.
  - Inserte el libro en la base de datos usando una consulta SQL como esta:

```sql
INSERT INTO libros (titulo, autor, anio, estado) VALUES (?, ?, ?, ?);
```

    - Usa `cursor.execute()` con los valores proporcionados por el usuario.

---

## 4. Consultar la lista de libros disponibles

- En la clase `Biblioteca`, crea un método llamado `consultar_libros()` que:
  - Ejecute una consulta SQL para obtener todos los libros de la tabla:

```sql
SELECT * FROM libros;
```

    - Devuelva los resultados como una lista de objetos `Libro`.

- Usa un bucle para imprimir cada libro en formato legible por consola.

---

## 5. Registrar el préstamo de un libro

- En la clase `Biblioteca`, crea un método llamado `prestar_libro()` que:
  - Reciba el título del libro y el nombre del usuario.
  - Verifique si el libro está disponible con una consulta SQL como esta:

```sql
SELECT * FROM libros WHERE titulo = ? AND estado = 'disponible';
```

    - Si está disponible, actualiza su estado a "prestado" y guarda el nombre del usuario con una consulta SQL como esta:

```sql
UPDATE libros SET estado = 'prestado', usuario = ? WHERE titulo = ?;
```

    - Si no está disponible, muestra un mensaje indicando que no se puede prestar.

---

## 6. Registrar la devolución de un libro

- En la clase `Biblioteca`, crea un método llamado `devolver_libro()` que:
  - Reciba el título del libro.
  - Verifique si el libro está prestado con una consulta SQL como esta:

```sql
SELECT * FROM libros WHERE titulo = ? AND estado = 'prestado';
```

    - Si está prestado, actualiza su estado a "disponible" y elimina el nombre del usuario con una consulta SQL como esta:

```sql
UPDATE libros SET estado = 'disponible', usuario = NULL WHERE titulo = ?;
```

    - Si ya está disponible, muestra un mensaje indicando que no estaba prestado.

---

## 7. Manejo de excepciones

- Usa bloques `try-except` para manejar errores comunes:
  - Por ejemplo, si intentas prestar o devolver un libro que no existe, puedes capturar el error y mostrar un mensaje al usuario.

```python
try:
    # Código que puede generar un error
    cursor.execute("SELECT * FROM libros WHERE titulo = ?", (titulo,))
    resultado = cursor.fetchone()
    if resultado is None:
        raise ValueError("El libro no existe.")
except ValueError as e:
    print(f"Error: {e}")
```

---

## 8. Persistencia de datos

- Asegúrate de cargar los datos desde la base de datos al iniciar el programa. Esto puede hacerse en el constructor de la clase `Biblioteca`.
- Guarda automáticamente los cambios en la base de datos después de cada operación (por ejemplo, registrar un préstamo o devolver un libro).

---

## 9. Implementar el menú principal

- Usa un bucle infinito (`while True`) para mostrar el menú principal hasta que el usuario decida salir.
- Crea funciones independientes para cada opción del menú y llama a estas funciones desde el bucle principal.
- Maneja entradas incorrectas (por ejemplo, si el usuario introduce una opción no válida) mostrando mensajes claros.

Ejemplo básico del menú principal:

```python
def menu_principal():
    continuar = True
    while continuar:
        print("\nMenú principal:")
        print("1. Registrar un nuevo libro")
        print("2. Consultar la lista de libros disponibles")
        print("3. Registrar el préstamo de un libro")
        print("4. Registrar la devolución de un libro")
        print("5. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                biblioteca.registrar_libro()
            elif opcion == 2:
                biblioteca.consultar_libros()
            elif opcion == 3:
                biblioteca.prestar_libro()
            elif opcion == 4:
                biblioteca.devolver_libro()
            elif opcion == 5:
                print("¡Gracias por usar el sistema!")
                continuar = False
            else:
                print("Opción no válida. Inténtalo nuevamente.")
        except ValueError:
            print("Error: Por favor introduce un número válido.")
```

---

## Consejo final

Si te sientes atascado en algún momento, divide el problema en partes más pequeñas y resuélvelas una por una. Por ejemplo:

1. Primero asegúrate de que puedes conectar a SQLite3 y crear la tabla.
2. Luego prueba insertar y consultar datos en la base de datos.
3. Después implementa las clases y métodos uno por uno.

Recuerda: ¡programar es resolver problemas paso a paso! 😊
