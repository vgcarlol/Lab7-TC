
# Proyecto de Simplificación de Gramáticas

Este repositorio contiene la solución al **Laboratorio No. 7**, relacionado con la simplificación de gramáticas en teoría de la computación. El proyecto incluye la generación de un programa que simplifica gramáticas eliminando producciones-ε, producciones unarias, y muestra el resultado final sin redundancias. También se incluye un video de demostración de la ejecución del programa.

## Contenido del Repositorio

- `Ejercicio_2.py`: Código fuente del programa que realiza la simplificación de gramáticas.
- `gramatica1.txt`: Archivo de texto que contiene la primera gramática usada para las pruebas.
- `gramatica2.txt`: Archivo de texto que contiene la segunda gramática usada para las pruebas.
- `README.md`: Este archivo, con toda la documentación necesaria para entender y ejecutar el proyecto.
- `Ejercicio_1/`: Carpeta que contiene respuestas a los incisos que no involucran generación de código, en formato PDF y HTML.

## Requisitos

- Python 3.x
- Bibliotecas estándar de Python (`re`, `itertools`)

## Instrucciones para Ejecutar el Programa

1. **Clonar el Repositorio**:
   ```sh
   git clone https://github.com/vgcarlol/Lab7-TC
   ```
2. **Cambiar al Directorio del Proyecto**:
   ```sh
   cd Lab7-TC
   ```
3. **Archivos Necesarios**:
   Asegúrese de tener los archivos `gramatica1.txt` y `gramatica2.txt` en la raíz del repositorio. Estos archivos contienen las gramáticas de ejemplo que serán simplificadas.

4. **Ejecutar el Programa**:
   Para ejecutar el script de simplificación de gramáticas, use el siguiente comando:
   ```sh
   python Ejercicio_2.py
   ```

5. **Salida del Programa**:
   El programa mostrará:
   - Las gramáticas originales (cargadas desde `gramatica1.txt` y `gramatica2.txt`).
   - Las gramáticas resultantes después de eliminar producciones-𝜀.
   - Las gramáticas resultantes después de eliminar producciones unarias.
   - Las gramáticas finales simplificadas.

## Video de Demostración

He grabado un video de demostración donde muestro la ejecución del programa y explico brevemente cada paso del proceso de simplificación. Puedes ver el video en YouTube haciendo clic en el siguiente enlace:

- [Video de Demostración - Simplificación de Gramáticas](https://youtu.be/cZSwpsKyE4o)

## Estructura del Proyecto

- **Código Fuente**: El archivo principal `Ejercicio_2.py` contiene toda la lógica para cargar, validar y simplificar gramáticas.
- **Validación de Producciones**: Se utiliza una expresión regular mejorada para validar la sintaxis de cada producción, soportando palabras completas como terminales y no-terminales.
- **Eliminación de Producciones-𝜀**: El programa encuentra las producciones anulables y elimina las producciones que contienen `ε`, generando nuevas combinaciones de los cuerpos de producción.
- **Eliminación de Producciones Unarias**: También se eliminan producciones unarias (del tipo `A -> B`), consolidando las reglas que dependen de otras.

## Consideraciones

- El programa está diseñado para funcionar con gramáticas donde los no-terminales son letras mayúsculas y los terminales son letras minúsculas o palabras que empiezan con minúsculas.
- Cualquier error en la sintaxis de las gramáticas de entrada detendrá la ejecución del programa, indicando el error encontrado.

## Recomendaciones

- **Formato de Entrada**: Asegúrese de que las gramáticas de entrada sigan el formato especificado: cada producción debe estar en la forma `No-Terminal -> Cuerpo` y los cuerpos de producción deben estar separados por `|`.
- **Contribuciones**: Para contribuir al proyecto, por favor cree un "pull request" y explique claramente las mejoras o correcciones propuestas.

## Contacto

Para cualquier pregunta o sugerencia, puedes contactarme a través del repositorio o por medio de mi correo electrónico: `val221164@uvg.edu.gt`.

---

© 2024 Universidad del Valle de Guatemala - Facultad de Ingeniería - Ingeniería en Ciencia de la Computación y Tecnologías de la Información
