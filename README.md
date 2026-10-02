# Ayudantía de Programación Avanzada en Python

Material de apoyo de la ayudantía del ramo **Programación Avanzada en Python**
(Universidad Autónoma de Chile, sede Talca), año 2025. Son ejercicios resueltos y
comentados, desde programación orientada a objetos hasta interfaces gráficas con Tkinter.

## Contenido

Hay una carpeta por semana (`Semana01` a `Semana10`). Los ejercicios principales están
en la carpeta de la semana y los complementarios, en su subcarpeta `Opcional/`.

| Carpeta | Tema | Ejercicios | Opcional |
| --- | --- | --- | --- |
| `Semana01` | Clases y objetos: atributos, constructor `__init__` y métodos | `mi_primera_clase_objeto.py`<br>`clase_con_constructor_y_metodo.py` | `clase_rectangulo_calculos.py` |
| `Semana02` | Encapsulamiento y herencia simple (`super()`, sobrescritura de métodos) | `encapsulamiento_basico_cuenta_bancaria.py`<br>`herencia_simple_animal.py` | `herencia_con_vehiculo.py` |
| `Semana03` | Polimorfismo (con herencia y *duck typing*) y abstracción | `polimorfismo_con_herencia_figuras.py`<br>`duck_typing_y_protocolos.py` | `clases_abstractas_conceptuales_instrumentos.py` |
| `Semana04` | Excepciones: `try`/`except`/`else`/`finally`, `raise` y excepciones propias | `manejo_de_errores_try_except.py`<br>`try_except_else_finally_archivo.py` | `validacion_con_raiz_y_excepciones_personalizadas.py` |
| `Semana05` | Recursividad: caso base y caso recursivo, memoización | `factoria_recursivo.py`<br>`suma_lista_recursivo.py` | `fibonacci_recursivo_y_memoizacion.py` |
| `Semana06` | Propiedades (`@property`), métodos de clase y métodos estáticos | `propiedades_getter_setter_deleter.py`<br>`metodo_clase_y_estaticos.py` | `clase_configuracion_app_completa.py` |
| `Semana07` | Tkinter I: ventana, `Label`, `Button` y eventos | `primer_ventana _tkinter.py`<br>`botones_y_eventos_simples_tkinter.py` | `entrada_texto_y_eco_tkinter.py` (pendiente) |
| `Semana08` | Tkinter II: `grid()`, `Frame` y variables de control (`StringVar`) | `layout_con_grid_calculadora_simple.py`<br>`uso_de_frame_y_variable_tkinter.py` | `formulario_basico_varios_widget.py` |
| `Semana09` | Tkinter III: diálogos, menús y aplicaciones estructuradas con clases | `dialogos_y_menus_tkinter.py`<br>`app_tkinter_con_clases_oop.py` | `editor_texto_simple.py` |
| `Semana10` | Proyecto final: Mini Paint con Tkinter | `mini_paint_basico_tkinter.py`<br>`mejorando_mini_paint.py` | `juego_adivina_numero_gui.py` |

## Cómo está armado cada archivo

Cada `.py` es independiente y sigue la misma estructura:

1. **Enunciado**: el problema a resolver, al comienzo del archivo.
2. **Código**: una solución comentada.
3. **Preguntas de comprensión**: preguntas para reflexionar, al final del archivo
   (en la Semana 10 se llaman «Puntos clave y preguntas guía»).

Si estás cursando el ramo, intenta resolver el enunciado por tu cuenta antes de leer el código.

## Cómo ejecutar los ejemplos

**Requisitos:** Python 3.10 o superior (el material se desarrolló con Python 3.13 y se
verificó con 3.11 y 3.14). Solo usa la biblioteca estándar, así que no hay nada más que
instalar. Se asume que ya manejas los fundamentos de Python, los del ramo introductorio
de Programación.

1. Descarga el repositorio (botón verde **Code**, luego **Download ZIP**) o clónalo:

   ```bash
   git clone https://github.com/NicolasFluxa/ayudantia-programacion-avanzada.git
   cd ayudantia-programacion-avanzada
   ```

2. Ejecuta cualquier archivo desde la carpeta del repositorio:

   ```bash
   python Semana01/mi_primera_clase_objeto.py
   ```

   En Windows también puedes usar `py` en lugar de `python`.

Ten en cuenta:

- Las semanas 7 a 10 abren ventanas con Tkinter. Viene incluido con Python en Windows y
  macOS; en Ubuntu o Debian se instala con `sudo apt install python3-tk`.
- El archivo de la Semana 07 se llama `primer_ventana _tkinter.py` (con un espacio antes
  de `_tkinter`), así que hay que escribirlo entre comillas:
  `python "Semana07/primer_ventana _tkinter.py"`.
- `Semana04/manejo_de_errores_try_except.py` te pide datos por teclado.
- `Semana04/try_except_else_finally_archivo.py` crea un archivo `datos_prueba.txt` en la
  carpeta desde la que lo ejecutas (el repositorio lo ignora).

## Autoría

Material preparado por Nicolás Fluxá, ayudante de Programación Avanzada en Python.
Perfil profesional: [LinkedIn](https://www.linkedin.com/in/nflux%C3%A1/).
