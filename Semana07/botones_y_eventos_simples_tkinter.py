"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                  Botones y Manejo de Eventos Simples en Tkinter
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te enseñará a añadir botones a tu ventana y a hacer que
realicen una acción cuando se presionan (manejo de eventos).

1.  Crea una ventana raíz de Tkinter con un título y tamaño.
2.  Define una función Python (fuera de la lógica de la GUI principal por ahora,
    o como un método si estuvieras usando clases para la GUI) llamada `accion_boton()`:
    a.  Esta función, cuando se llame, debe imprimir un mensaje en la consola
        (ej: "¡El botón fue presionado!").
3.  Crea un widget `Label` con un texto inicial (ej: "Presiona el botón de abajo.").
    Empaquétalo.
4.  Crea un widget `Button` (botón):
    a.  Pásale la ventana raíz como padre.
    b.  Establece su texto (ej: "Haz Clic Aquí").
    c.  Usa la opción `command` para asociar el botón con tu función `accion_boton`.
        Importante: Pasa solo el nombre de la función, SIN paréntesis
        (ej: `command=accion_boton`, NO `command=accion_boton()`).
5.  Empaqueta el botón.
6.  Inicia el `mainloop`. Prueba presionar el botón y observa la consola.
7.  (Extensión) Modifica `accion_boton()` para que, en lugar de (o además de)
    imprimir en consola, cambie el texto de la `Label` creada en el paso 3.
    Para esto, la `Label` necesitará ser accesible desde la función, o puedes
    usar `StringVar` (que veremos más adelante) o configurar el texto directamente.
    Una forma simple es hacer la etiqueta una variable global o pasarla a la función
    si la defines de forma que pueda aceptarla (más avanzado con lambdas o clases).
    Para este ejercicio, intentemos cambiar su texto usando el método `config` o `configure`.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: conectar un evento (el clic) con una función, y que esa función
modifique la interfaz.

Al ejecutar se abre una ventana de 350x200 con una etiqueta («Presiona el
botón de abajo.»), el botón «Haz Clic Aquí» y el botón «Salir»:
  - cada clic en «Haz Clic Aquí» imprime «¡El botón fue presionado!» en la
    consola y cambia la etiqueta a «¡Gracias por presionar el botón!» en verde;
  - «Salir» cierra la ventana y el programa imprime «Aplicación cerrada.».

-------------------------------------------------------------------------------
"""
import tkinter as tk

# 2. Definir la función que se ejecutará al presionar el botón
def accion_boton():
    """Esta función se ejecuta cuando el botón es presionado."""
    mensaje_consola = "¡El botón fue presionado!"
    print(mensaje_consola) # Imprime en la consola

    # 7. (Extensión) Cambiar el texto de la etiqueta.
    # 'etiqueta_estado' se crea más abajo, a nivel de módulo; la función la encuentra
    # porque se ejecuta después, cuando el usuario presiona el botón.
    # (Usar variables globales es simple para este ejemplo, pero no es lo mejor en
    # apps grandes: mira las alternativas del final.)
    etiqueta_estado.config(text="¡Gracias por presionar el botón!", fg="green")

# 1. Crear la ventana raíz
raiz = tk.Tk()
raiz.title("Botones y Eventos")
raiz.geometry("350x200")

# 3. Crear una Label inicial
etiqueta_estado = tk.Label(raiz, text="Presiona el botón de abajo.", font=("Arial", 14))
etiqueta_estado.pack(pady=20)


# 4. Crear un widget Button
boton_accion = tk.Button(
    raiz,
    text="Haz Clic Aquí",
    font=("Arial", 12),
    bg="lightblue", # Color de fondo del botón
    fg="black",     # Color del texto del botón
    command=accion_boton  # Asociar la función (sin paréntesis)
)

# 5. Empaquetar el botón
boton_accion.pack(pady=10)

# Botón para salir de la aplicación
boton_salir = tk.Button(raiz, text="Salir", command=raiz.quit, bg="salmon")
boton_salir.pack(pady=5)

# 6. Iniciar el bucle principal
print("Ventana con botón lista. Esperando interacción...")
raiz.mainloop()
print("Aplicación cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el propósito de la opción `command` en un widget `Button`?
2.  ¿Por qué se pasa el nombre de la función a `command` (ej: `accion_boton`)
    en lugar de la llamada a la función (ej: `accion_boton()`)? ¿Qué pasaría
    si incluyeras los paréntesis?
3.  En la extensión del ejercicio, se modificó el texto de una `Label`.
    ¿Qué es `etiqueta_estado.config(text="...")`? ¿Para qué sirve `config` (o `configure`)?
4.  El ejemplo usa una variable global para `etiqueta_estado` para simplificar.
    ¿Por qué el uso extensivo de variables globales podría no ser una buena
    práctica en programas más grandes? ¿Qué alternativas existen (piensa en clases o
    funciones que pasan widgets como argumentos)?
5.  ¿Cómo añadirías otro botón que realice una acción diferente (ej: que imprima
    otro mensaje o cambie el texto de la etiqueta a algo distinto)?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

from functools import partial


def alternativa_1():
    """Sin variable global: `partial` (o `lambda`) pasa la etiqueta a la función.

    Cuándo conviene: la función necesita datos del entorno y quieres que sea
    reutilizable y fácil de probar. Si la acción es de una sola línea, una
    `lambda` basta: `command=lambda: etiqueta.config(text="¡Hola!")`.
    """
    def accion(etiqueta):
        print("¡El botón fue presionado!")
        etiqueta.config(text="¡Gracias por presionar el botón!", fg="green")

    raiz = tk.Tk()
    etiqueta = tk.Label(raiz, text="Presiona el botón de abajo.", font=("Arial", 14))
    etiqueta.pack(pady=20)
    tk.Button(raiz, text="Haz Clic Aquí", command=partial(accion, etiqueta)).pack(pady=10)
    raiz.mainloop()


def alternativa_2():
    """`StringVar`: la etiqueta muestra el valor de una variable de control.

    En vez de llamar a `etiqueta.config(text=...)`, se cambia la variable con
    `.set()` y todos los widgets que la usan se actualizan solos. Se ve en la
    Semana 8.
    Cuándo conviene: cuando varios widgets muestran o editan el mismo dato.
    """
    raiz = tk.Tk()
    mensaje = tk.StringVar(master=raiz, value="Presiona el botón de abajo.")
    tk.Label(raiz, textvariable=mensaje, font=("Arial", 14)).pack(pady=20)
    tk.Button(raiz, text="Haz Clic Aquí",
              command=lambda: mensaje.set("¡Gracias por presionar el botón!")).pack(pady=10)
    raiz.mainloop()


def alternativa_3():
    """La ventana como clase: la etiqueta es un atributo y el botón llama a un método.

    Cuándo conviene: es la forma estándar de organizar aplicaciones que
    crecen; evita los globales sin pasar argumentos a mano (Semana 9).
    """
    class Aplicacion(tk.Tk):
        def __init__(self):
            super().__init__()
            self.etiqueta = tk.Label(self, text="Presiona el botón de abajo.", font=("Arial", 14))
            self.etiqueta.pack(pady=20)
            tk.Button(self, text="Haz Clic Aquí", command=self.al_presionar).pack(pady=10)

        def al_presionar(self):
            print("¡El botón fue presionado!")
            self.etiqueta.config(text="¡Gracias por presionar el botón!", fg="green")

    Aplicacion().mainloop()


# alternativa_1()
# alternativa_2()
# alternativa_3()
