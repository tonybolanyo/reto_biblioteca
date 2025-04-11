# Características clave de la solución

1. **Programación orientada a objetos**:
    - Clase `Libro` para modelar los datos
    - Clase `Biblioteca` para la lógica de negocio y persistencia
2. **Persistencia con SQLite3**:
    - Base de datos automáticamente creada al iniciar
    - Transacciones gestionadas con `commit()`
    - Consultas parametrizadas para seguridad
3. **Manejo de errores**:
    - Validación de tipos de datos
    - Control de libros no existentes
    - Prevención de operaciones inválidas
4. **Interfaz intuitiva**:
    - Menú interactivo con feedback claro
    - Formato legible para mostrar libros
    - Mensajes de éxito/error descriptivos

---

## Cómo probar el programa

1. Ejecuta el script y selecciona la opción 1 para registrar libros
2. Usa la opción 2 para verificar que se guardaron correctamente
3. Prueba a prestar y devolver libros (opciones 3 y 4)
4. Cierra y vuelve a abrir el programa para comprobar la persistencia
5. Experimenta con entradas incorrectas para ver el manejo de errores

Este modelo implementa todos los requisitos del reto y sirve como referencia para comparar con la solución del alumno. 😊
