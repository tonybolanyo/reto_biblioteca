# Reto: Biblioteca

## **Reto: La Biblioteca del Sabio Codificador**

Te doy la bienvenida a este reto de programación en Python. En este ejercicio, te convertirás en la persona principal del equipo de desarrollo del sistema de gestión de una pequeña biblioteca. La biblioteca necesita un programa que permita a los bibliotecarios gestionar los libros y registrar los préstamos de los usuarios. ¡Es tu momento para brillar!

### **Historia**

En un pequeño pueblo llamado **Algoritmia**, existe una biblioteca muy especial conocida como **"La Biblioteca del Sabio Codificador"**. Esta biblioteca guarda libros mágicos que contienen secretos ancestrales sobre la programación y el desarrollo de software. Sin embargo, el bibliotecario que la gestionaba ha decidido retirarse, y ahora necesitan un sistema moderno para organizar los libros y ayudar a los habitantes del pueblo a acceder a ellos.

Tu misión es crear un **programa en Python** que gestione esta biblioteca. El sistema debe permitir:

1. Registrar nuevos libros en su inventario.
2. Consultar la lista de libros disponibles.
3. Registrar préstamos de libros a usuarios.
4. Devolver libros prestados.
5. Guardar toda la información en una base de datos para que no se pierda al cerrar el programa.

La bibliotecaria principal, Ada Scriptoria, está muy emocionada por ver cómo tu programa hará su trabajo más fácil.

---

### **Requisitos del programa**

Tu programa debe implementar las siguientes funcionalidades:

#### 1. **Menú principal**

El programa debe mostrar un menú principal que permita al usuario elegir entre las siguientes opciones:

- Registrar un nuevo libro.
- Consultar la lista de libros disponibles.
- Registrar el préstamo de un libro.
- Registrar la devolución de un libro.
- Salir del programa.

#### 2. **Registrar un nuevo libro**

Cuando el usuario elija esta opción, se le pedirá que introduzca:

- El título del libro.
- El autor del libro.
- El año de publicación.

El libro se añadirá a la base de datos y estará disponible para ser prestado.

#### 3. **Consultar la lista de libros disponibles**

Esta opción debe mostrar todos los libros registrados en la base de datos junto con su estado (disponible o prestado).

#### 4. **Registrar el préstamo de un libro**

Cuando el usuario seleccione esta opción:

- Se le pedirá que introduzca el título del libro que desea prestar.
- Se le pedirá el nombre del usuario que toma prestado el libro.

Si el libro está disponible, se actualizará su estado a "prestado" y se registrará el nombre del usuario que lo tomó prestado. Si no está disponible, se mostrará un mensaje indicando que no puede ser prestado.

#### 5. **Registrar la devolución de un libro**

Cuando el usuario seleccione esta opción:

- Se le pedirá que introduzca el título del libro que desea devolver.

Si el libro está marcado como "prestado", se actualizará su estado a "disponible". Si ya estaba disponible, se mostrará un mensaje indicando que no estaba prestado.

#### 6. **Persistencia de datos**

Toda la información sobre los libros y sus estados debe guardarse en una base de datos SQLite3 llamada `biblioteca.db`. La base de datos debe contener una tabla llamada `libros` con las siguientes columnas:

- `id` (entero, clave primaria).
- `titulo` (texto).
- `autor` (texto).
- `anio` (entero).
- `estado` (texto: "disponible" o "prestado").
- `usuario` (texto, opcional; solo se llena si el libro está prestado).

Los datos deben cargarse desde la base de datos al iniciar el programa y guardarse automáticamente cada vez que se realice una operación.

#### 7. **Gestión de errores**

El programa debe manejar excepciones básicas, como:

- Intentar prestar un libro que no existe.
- Intentar devolver un libro que no existe o ya está disponible.
- Introducir datos incorrectos (por ejemplo, texto donde se espera un número).

---

### **Pistas para resolverlo**

1. Utiliza programación orientada a objetos para organizar tu código:
    - Crea una clase `Libro` para representar cada libro.
    - Crea una clase `Biblioteca` para gestionar todas las operaciones relacionadas con los libros y los préstamos.
2. Usa funciones para dividir las tareas del menú principal y evitar repetir código.
3. Implementa bucles para mantener el menú principal activo hasta que el usuario decida salir.
4. Utiliza SQLite3 para gestionar la persistencia de datos:
    - Crea la tabla `libros` si no existe al iniciar el programa.
    - Usa consultas SQL para insertar, actualizar y recuperar información.
5. Maneja excepciones con bloques `try-except` para evitar que errores inesperados detengan tu programa.

---

### **Ejemplo del flujo del programa**

```plaintext
¡Bienvenido a La Biblioteca del Sabio Codificador!

Menú principal:
1. Registrar un nuevo libro
2. Consultar la lista de libros disponibles
3. Registrar el préstamo de un libro
4. Registrar la devolución de un libro
5. Salir

Selecciona una opción: 1

Introduce el título del libro: El Quijote
Introduce el autor del libro: Miguel de Cervantes
Introduce el año de publicación: 1605

¡Libro registrado con éxito!

Menú principal:
1. Registrar un nuevo libro
2. Consultar la lista de libros disponibles
3. Registrar el préstamo de un libro
4. Registrar la devolución de un libro
5. Salir

Selecciona una opción: 2

Lista de libros:
1. El Quijote - Miguel de Cervantes (1605) - Disponible

Menú principal:
1. Registrar un nuevo libro
2. Consultar la lista de libros disponibles
3. Registrar el préstamo de un libro
4. Registrar la devolución de un libro
5. Salir

Selecciona una opción: 3

Introduce el título del libro a prestar: El Quijote
Introduce el nombre del usuario: Juan Pérez

¡Préstamo registrado con éxito!

...
```

---

### **Objetivo**

El objetivo es aplicar todo lo aprendido durante este curso: clases, funciones, bucles, manejo de excepciones, entrada/salida por consola y persistencia con SQLite3.

¡Buena suerte! Don Manuel confía en ti para modernizar su biblioteca 😊
