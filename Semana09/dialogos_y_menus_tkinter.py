"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                      Diálogos Estándar y Menús en Tkinter
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te mostrará cómo usar diálogos estándar (messagebox) para
interactuar con el usuario y cómo crear una barra de menú básica en una
aplicación Tkinter.

1.  Importa `tkinter` y `tkinter.messagebox`. (`tkinter.filedialog`, para abrir y
    guardar archivos, se usa recién en el ejercicio opcional.)
2.  Crea la ventana raíz.
3.  Define funciones "comando" para las opciones del menú:
    a.  `mostrar_acerca_de()`: Debe mostrar un diálogo `showinfo` con información
        básica de la "aplicación" (ej: "Mi Aplicación v1.0, Creada con Tkinter").
    b.  `confirmar_salida()`: Debe mostrar un diálogo `askyesno` preguntando
        "¿Estás seguro de que quieres salir?". Si el usuario dice sí, cierra la
        ventana (`raiz.quit()` o `raiz.destroy()`).
    c.  `abrir_info_dummy()`: Simplemente muestra un `showinfo` diciendo "Funcionalidad 'Abrir Info' aún no implementada."

4.  **Creación del Menú Principal:**
    a.  Crea un objeto `Menu` asociado a la ventana raíz. Este será la barra de menú.
    b.  Configura la ventana raíz para que use esta barra de menú (`raiz.config(menu=barra_menu)`).

5.  **Creación del Menú "Archivo":**
    a.  Crea un nuevo objeto `Menu` (ej: `menu_archivo`) asociado a `barra_menu`.
        Importante: `tearoff=0` para que el menú no se pueda "desprender".
    b.  Añade comandos a `menu_archivo`:
        i.  "Abrir Información" que llame a `abrir_info_dummy`.
        ii. Un separador (`add_separator()`).
        iii."Salir" que llame a `confirmar_salida`.
    c.  Añade `menu_archivo` a `barra_menu` con la etiqueta "Archivo"
        (`barra_menu.add_cascade(label="Archivo", menu=menu_archivo)`).

6.  **Creación del Menú "Ayuda":**
    a.  Crea otro objeto `Menu` (ej: `menu_ayuda`) asociado a `barra_menu` (`tearoff=0`).
    b.  Añade un comando "Acerca de..." que llame a `mostrar_acerca_de`.
    c.  Añade `menu_ayuda` a `barra_menu` con la etiqueta "Ayuda".

7.  (Opcional) Añade un botón a la ventana principal que, al ser presionado,
    muestre un diálogo `askquestion` y luego imprima la respuesta ("yes" o "no")
    en la consola.
8.  Inicia el `mainloop`.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: usar los diálogos estándar de `tkinter.messagebox` para informar y
preguntar al usuario, y construir una barra de menú con submenús.

Al ejecutar se abre una ventana de 500x300 con la barra «Archivo» / «Ayuda»
y un botón «Haz una Pregunta»:
  - Archivo > Abrir Información: avisa que aún no está implementado;
  - Archivo > Salir: pregunta «¿Estás seguro...?»; solo con «Sí» se cierra;
  - Ayuda > Acerca de...: muestra los datos de la aplicación;
  - el botón abre una pregunta sí/no, imprime la respuesta en consola y la comenta.
Cada diálogo bloquea la ventana principal hasta que lo cierres.

-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox # Para diálogos estándar

# Ventana Raíz
raiz = tk.Tk()
raiz.title("Diálogos y Menús")
raiz.geometry("500x300")

# --- 3. Funciones Comando para el Menú ---
def mostrar_acerca_de():
    """Muestra un diálogo 'showinfo' con información de la aplicación."""
    messagebox.showinfo(
        title="Acerca de Mi Aplicación",
        message="Mi Súper Aplicación\nVersión 1.0\nCreada con Python y Tkinter\n(c) 2025 Tu Nombre"
    )

def confirmar_salida():
    """Muestra un diálogo 'askyesno' y cierra la app si la respuesta es sí."""
    if messagebox.askyesno(title="Confirmar Salida", message="¿Estás seguro de que quieres salir?"):
        print("Saliendo de la aplicación...")
        raiz.destroy() # .quit() también funciona, .destroy() es más definitivo.

def abrir_info_dummy():
    """Función placeholder para una opción de menú."""
    messagebox.showinfo(title="Información", message="Funcionalidad 'Abrir Información' aún no implementada.")

def preguntar_algo():
    """Muestra un diálogo 'askquestion' y procesa la respuesta."""
    respuesta = messagebox.askquestion(
        title="Pregunta Importante",
        message="¿Te está gustando Tkinter?",
        icon='question' # 'info', 'warning', 'error', 'question'
    )
    if respuesta == 'yes':
        print("Respuesta a la pregunta: ¡Sí!")
        messagebox.showinfo("Respuesta", "¡Genial que te guste Tkinter!")
    else: # respuesta == 'no'
        print("Respuesta a la pregunta: No...")
        messagebox.showinfo("Respuesta", "Oh, bueno, ¡quizás le encuentres el gusto!")


# --- 4. Creación de la Barra de Menú Principal ---
barra_menu_principal = tk.Menu(raiz)
raiz.config(menu=barra_menu_principal) # Asignar la barra de menú a la ventana

# --- 5. Creación del Menú "Archivo" ---
menu_archivo = tk.Menu(barra_menu_principal, tearoff=0) # tearoff=0 para que no se pueda "desprender"

# 5b. Añadir comandos a menu_archivo
menu_archivo.add_command(label="Abrir Información", command=abrir_info_dummy)
menu_archivo.add_separator() # Añade una línea separadora
menu_archivo.add_command(label="Salir", command=confirmar_salida)

# 5c. Añadir menu_archivo a la barra_menu_principal
barra_menu_principal.add_cascade(label="Archivo", menu=menu_archivo)


# --- 6. Creación del Menú "Ayuda" ---
menu_ayuda = tk.Menu(barra_menu_principal, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=mostrar_acerca_de)
barra_menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)


# --- 7. (Opcional) Botón para probar otro diálogo ---
frame_contenido = tk.Frame(raiz, pady=20)
frame_contenido.pack(expand=True)

label_info = tk.Label(frame_contenido, text="Explora los menús de arriba o presiona el botón.", font=("Arial", 12))
label_info.pack(pady=10)

boton_pregunta = tk.Button(frame_contenido, text="Haz una Pregunta", command=preguntar_algo, font=("Arial", 10), bg="lightyellow")
boton_pregunta.pack(pady=10)


# --- 8. Iniciar Bucle Principal ---
print("Aplicación con menús y diálogos lista.")
raiz.mainloop()
print("Aplicación cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la diferencia entre `tk.Menu(raiz)` y `tk.Menu(barra_menu_principal)`?
    ¿Para qué se usa cada uno en la creación de menús?
2.  ¿Qué hace la opción `tearoff=0` al crear un `Menu`?
3.  ¿Cómo se añade un submenú (como "Archivo" o "Ayuda") a la barra de menú principal?
    (Ver `add_cascade`).
4.  Nombra al menos tres tipos diferentes de diálogos que proporciona `tkinter.messagebox`
    y describe brevemente para qué se usaría cada uno.
5.  Si quisieras añadir un atajo de teclado (ej: Ctrl+Q para Salir) a una opción
    del menú, ¿cómo podrías hacerlo? (Investiga la opción `accelerator` y el
    método `bind` o la configuración de eventos del menú).
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

def alternativa_1():
    """Atajo de teclado (Ctrl+Q) y confirmar también al cerrar con la «X».

    `accelerator` solo MUESTRA el texto «Ctrl+Q» en el menú; el atajo real lo
    crea `bind`. `protocol("WM_DELETE_WINDOW", ...)` intercepta el botón de
    cerrar de la ventana para que también pida confirmación (en la solución
    principal, la «X» cerraría sin preguntar).
    Cuándo conviene: en toda aplicación con datos que se podrían perder.
    (Esta es la respuesta a la pregunta 5.)
    """
    raiz = tk.Tk()
    raiz.title("Atajos y cierre seguro")

    def salir(evento=None):                       # 'evento' permite usarla en bind() y en command
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir?"):
            raiz.destroy()

    barra = tk.Menu(raiz)
    raiz.config(menu=barra)
    menu = tk.Menu(barra, tearoff=0)
    menu.add_command(label="Salir", accelerator="Ctrl+Q", command=salir)
    barra.add_cascade(label="Archivo", menu=menu)

    raiz.bind("<Control-q>", salir)
    raiz.protocol("WM_DELETE_WINDOW", salir)
    raiz.mainloop()


def alternativa_2():
    """Construir el menú a partir de una estructura de datos.

    En vez de una línea `add_command` por opción, el menú se describe con un
    diccionario y se arma con un bucle; agregar una opción es agregar una
    entrada. `None` representa un separador.
    Cuándo conviene: menús largos o que se generan según el contexto
    (por ejemplo, la lista de archivos recientes).
    """
    raiz = tk.Tk()
    raiz.title("Menú desde datos")
    estructura = {
        "Archivo": [("Abrir Información", lambda: messagebox.showinfo("Info", "Aún no implementado")),
                    None,
                    ("Salir", raiz.destroy)],
        "Ayuda": [("Acerca de...", lambda: messagebox.showinfo("Acerca de", "Mi Aplicación v1.0"))],
    }
    barra = tk.Menu(raiz)
    raiz.config(menu=barra)
    for titulo, opciones in estructura.items():
        menu = tk.Menu(barra, tearoff=0)
        for opcion in opciones:
            if opcion is None:
                menu.add_separator()
            else:
                texto, accion = opcion
                menu.add_command(label=texto, command=accion)
        barra.add_cascade(label=titulo, menu=menu)
    raiz.mainloop()


def alternativa_3():
    """`askyesno` vs `askquestion` vs `askokcancel`: qué devuelve cada uno.

    - `askyesno`      -> True / False        (el más cómodo en un `if`)
    - `askquestion`   -> "yes" / "no"        (texto: hay que comparar con ==)
    - `askokcancel`   -> True / False        (para «Aceptar / Cancelar»)
    - `askyesnocancel`-> True / False / None (tres respuestas posibles)
    Cuándo conviene: `askyesno` para decisiones sí/no; `askyesnocancel` cuando
    «no» y «cancelar» significan cosas distintas (guardar antes de salir).
    """
    print("askyesno ->", repr(messagebox.askyesno("Pregunta", "¿Continuar?")))
    print("askquestion ->", repr(messagebox.askquestion("Pregunta", "¿Continuar?")))
    print("askokcancel ->", repr(messagebox.askokcancel("Pregunta", "¿Continuar?")))
    print("askyesnocancel ->", repr(messagebox.askyesnocancel("Pregunta", "¿Guardar antes de salir?")))


# alternativa_1()
# alternativa_2()
# alternativa_3()
