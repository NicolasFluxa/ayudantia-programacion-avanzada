"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                       Mi Primera Ventana con Tkinter
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te guiará para crear tu primera ventana básica usando Tkinter
y añadir un simple mensaje.

1.  Importa el módulo `tkinter` (comúnmente como `tk`).
2.  Crea la ventana principal de la aplicación (la ventana raíz).
    Generalmente se hace con `raiz = tk.Tk()`.
3.  Establece un título para la ventana (ej: "Mi Primera Ventana").
    Usa el método `title()` de la ventana raíz.
4.  Define las dimensiones iniciales de la ventana (ej: "300x200" para
    300 píxeles de ancho y 200 de alto). Usa el método `geometry()`.
5.  Crea un widget `Label` (etiqueta) para mostrar un texto.
    a.  El primer argumento del constructor `Label` es la ventana padre (tu raíz).
    b.  Usa el argumento `text` para especificar el mensaje (ej: "¡Hola, Tkinter!").
6.  "Empaqueta" el widget `Label` en la ventana para que sea visible.
    Usa el método `pack()` del widget Label. Este es el gestor de geometría más simple.
7.  Inicia el bucle principal de eventos de Tkinter (`mainloop()`). Esto mantiene
    la ventana visible y receptiva a eventos hasta que se cierre.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: conocer las piezas mínimas de toda aplicación Tkinter: la ventana
raíz, un widget dentro de ella y el bucle de eventos que la mantiene viva.

Al ejecutar se abre una ventana de 400x250 con el título «Mi Primera Ventana
con Tkinter» y dos etiquetas: «¡Hola, Tkinter! Bienvenido/a.» y «Este es un
ejemplo básico de GUI con Python.». En la consola aparecen mensajes de
avance; el último («El bucle principal ha terminado...») solo sale cuando
cierras la ventana. Si omites `mainloop()`, la ventana se abre y se cierra al
instante.

-------------------------------------------------------------------------------
"""

# 1. Importar el módulo tkinter
import tkinter as tk

# 2. Crear la ventana principal (raíz)
raiz = tk.Tk()

# 3. Establecer el título de la ventana
raiz.title("Mi Primera Ventana con Tkinter")

# 4. Definir las dimensiones iniciales de la ventana (ancho x alto)
raiz.geometry("400x250") # Ancho de 400px, Alto de 250px

# Configuración adicional opcional: hacer que la ventana no sea redimensionable
# raiz.resizable(False, False) # El primer False es para ancho, el segundo para alto

print("Ventana raíz creada. Añadiendo widgets...")

# 5. Crear un widget Label (etiqueta)
#   a. El primer argumento es el widget padre (la ventana raíz 'raiz')
#   b. 'text' es el texto que mostrará la etiqueta
etiqueta_saludo = tk.Label(raiz, text="¡Hola, Tkinter! Bienvenido/a.", font=("Arial", 16))

# 6. Empaquetar el widget Label en la ventana para hacerlo visible
# pack() es un gestor de geometría que organiza los widgets en bloques.
etiqueta_saludo.pack(pady=20) # pady añade un poco de espacio vertical alrededor de la etiqueta

# Crear otra etiqueta para demostrar el empaquetado
etiqueta_info = tk.Label(raiz, text="Este es un ejemplo básico de GUI con Python.", font=("Helvetica", 12))
etiqueta_info.pack(pady=10)

print("Widgets añadidos y empaquetados. Iniciando bucle principal...")
# 7. Iniciar el bucle principal de eventos de Tkinter
# Esto mantiene la ventana abierta y receptiva hasta que el usuario la cierre.
raiz.mainloop()

print("El bucle principal ha terminado (ventana cerrada).")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el propósito de `import tkinter as tk`? ¿Podrías importar tkinter
    de otra forma? ¿Cuál es la convención?
2.  ¿Qué es la "ventana raíz" en una aplicación Tkinter? ¿Cuántas puedes tener
    normalmente en una aplicación simple?
3.  ¿Qué hace el método `pack()`? ¿Qué sucedería si olvidaras llamar a `.pack()`
    (u otro método de gestor de geometría como `.grid()` o `.place()`) en un widget?
4.  ¿Para qué sirve `raiz.mainloop()`? ¿Qué ocurre si omites esta línea?
5.  ¿Cómo podrías cambiar el color de fondo de la ventana raíz o el color del
    texto de la `Label`? (Investiga las opciones `bg` y `fg`).
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

import tkinter.ttk as ttk


def alternativa_1():
    """La ventana como subclase de `tk.Tk` (en vez de una variable `raiz`).

    La ventana ES la aplicación: los widgets se crean en `__init__` con
    `self` como padre. Es la base de la organización en clases de la Semana 9.
    Cuándo conviene: en cuanto el programa tenga más que un par de widgets.
    """
    class MiVentana(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Mi Primera Ventana con Tkinter")
            self.geometry("400x250")
            tk.Label(self, text="¡Hola, Tkinter! Bienvenido/a.", font=("Arial", 16)).pack(pady=20)

    MiVentana().mainloop()


def alternativa_2():
    """Widgets `ttk` (aspecto nativo del sistema) en lugar de los clásicos `tk`.

    `ttk.Label` se parece a `tk.Label`, pero toma los colores y fuentes desde
    un tema; por eso opciones como `bg` o `fg` no existen, y se usa `style`
    o `foreground`/`background`. Se importa como `tkinter.ttk`.
    Cuándo conviene: cuando quieres que la aplicación se vea moderna sin
    esfuerzo. Los widgets clásicos (`tk`) son más fáciles de personalizar.
    """
    raiz = tk.Tk()
    raiz.title("Ventana con ttk")
    raiz.geometry("400x250")
    ttk.Label(raiz, text="¡Hola, Tkinter!", font=("Arial", 16)).pack(pady=20)
    raiz.mainloop()


def alternativa_3():
    """Centrar la ventana y ubicar con `place` en lugar de `pack`.

    `pack` acomoda los widgets en bloques; `place` los coloca en coordenadas
    exactas (píxeles o fracciones del tamaño de la ventana). Con
    `relx=0.5, rely=0.5, anchor="center"` la etiqueta queda al medio aunque
    se cambie el tamaño de la ventana.
    Cuándo conviene: `pack` casi siempre; `place` para un elemento flotante
    (una etiqueta centrada, un botón de cierre en la esquina). La Semana 8
    presenta `grid`, el más cómodo para formularios.
    """
    raiz = tk.Tk()
    raiz.title("Centrado con place")
    ancho, alto = 400, 250
    x = (raiz.winfo_screenwidth() - ancho) // 2
    y = (raiz.winfo_screenheight() - alto) // 2
    raiz.geometry(f"{ancho}x{alto}+{x}+{y}")                 # tamaño + posición en pantalla
    tk.Label(raiz, text="¡Hola, Tkinter!", font=("Arial", 16)).place(relx=0.5, rely=0.5, anchor="center")
    raiz.mainloop()


# alternativa_1()
# alternativa_2()
# alternativa_3()
