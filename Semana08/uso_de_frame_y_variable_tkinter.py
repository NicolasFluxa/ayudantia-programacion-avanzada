"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                 Uso de `Frame` y Variables de Control Tkinter (`StringVar`)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Los `Frame` son widgets contenedores que sirven para agrupar y organizar otros
widgets. Las `StringVar` (y otras como `IntVar`, `BooleanVar`) son variables
especiales de Tkinter que se pueden vincular a widgets para que se actualicen
automáticamente.

1.  Crea una ventana raíz de Tkinter.
2.  Crea una `StringVar` de Tkinter llamada `texto_compartido`. Inicialízala
    con un valor como "Texto inicial".
3.  Crea un `Frame` superior (`frame_arriba`). Empaquétalo en la raíz, haciendo
    que ocupe todo el ancho disponible (`fill='x'`).
    a.  Dentro de `frame_arriba`, crea una `Label` con el texto "Entrada:".
    b.  Dentro de `frame_arriba`, crea un `Entry` cuyo texto esté VINCULADO
        a `texto_compartido` usando la opción `textvariable`.
    c.  Empaqueta la Label y el Entry en `frame_arriba` (puedes usar `pack(side='left')`).

4.  Crea un `Frame` inferior (`frame_abajo`). Empaquétalo en la raíz (`fill='x'`).
    a.  Dentro de `frame_abajo`, crea una `Label` cuyo texto también esté VINCULADO
        a `texto_compartido` usando `textvariable`.
    b.  Empaqueta esta Label en `frame_abajo`.

5.  Define una función `actualizar_texto_variable()`:
    a.  Esta función debe cambiar el valor de `texto_compartido` usando su
        método `set()` (ej: a "Texto actualizado desde el botón!").
6.  Crea un `Button` en la ventana raíz (o en uno de los frames) con el texto
    "Actualizar Variable" y asócialo a la función `actualizar_texto_variable()`.
    Empaquétalo.

7.  Observa: Al escribir en el `Entry`, la `Label` de abajo se actualiza.
    Al presionar el botón, tanto el `Entry` como la `Label` se actualizan.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: agrupar widgets con `Frame` y mantenerlos sincronizados con una
`StringVar`, sin escribir código que copie el texto de uno a otro.

Al ejecutar se abre una ventana con dos recuadros (marcos) y un botón:
  - arriba, una caja de texto que parte con «Texto inicial en StringVar»;
  - abajo, una etiqueta (morada, en cursiva) que muestra lo MISMO y cambia a
    medida que escribes en la caja;
  - el botón «Actualizar Variable Programáticamente» cambia el texto de la
    variable desde el código y se actualizan las dos cosas a la vez; además
    imprime el nuevo valor en la consola.

-------------------------------------------------------------------------------
"""
import tkinter as tk

def actualizar_texto_variable():
    """Cambia el valor de la StringVar; el Entry y la Label vinculados se actualizan solos."""
    # 'texto_compartido' se crea más abajo; la función la encuentra porque solo se
    # ejecuta al presionar el botón, cuando ya existe.
    nuevo_valor = "¡Texto actualizado desde el botón!"
    texto_compartido.set(nuevo_valor)  # set() cambia la variable; get() la lee
    print(f"StringVar actualizada a: '{nuevo_valor}'")

# 1. Crear ventana raíz
raiz = tk.Tk()
raiz.title("Frames y StringVar")
raiz.geometry("450x200")

# 2. Crear una StringVar
texto_compartido = tk.StringVar()
texto_compartido.set("Texto inicial en StringVar") # Establecer valor inicial


# 3. Crear Frame superior y sus widgets
frame_arriba = tk.Frame(raiz, bd=2, relief="groove", padx=5, pady=5) # bd y relief para borde
frame_arriba.pack(pady=10, padx=10, fill="x") # fill="x" para que ocupe el ancho

# 3a. Label dentro de frame_arriba
label_instruccion_entry = tk.Label(frame_arriba, text="Entrada vinculada:")
label_instruccion_entry.pack(side="left", padx=5)

# 3b. Entry vinculado a texto_compartido
entry_vinculado = tk.Entry(frame_arriba, textvariable=texto_compartido, width=30, font=("Arial", 12))
entry_vinculado.pack(side="left", padx=5, expand=True, fill="x")


# 4. Crear Frame inferior y sus widgets
frame_abajo = tk.Frame(raiz, bd=2, relief="sunken", padx=5, pady=5)
frame_abajo.pack(pady=10, padx=10, fill="x")

# 4a. Label dentro de frame_abajo, vinculada a la misma StringVar
label_titulo_eco = tk.Label(frame_abajo, text="Eco de la entrada (Label vinculada):")
label_titulo_eco.pack(anchor="w") # anchor="w" para alinear a la izquierda (west)

label_eco_vinculada = tk.Label(frame_abajo, textvariable=texto_compartido, font=("Arial", 12, "italic"), fg="purple")
label_eco_vinculada.pack(pady=5, anchor="w")


# 6. Crear un Button para actualizar la StringVar
boton_actualizar = tk.Button(
    raiz, # Se añade directamente a la raíz, fuera de los frames
    text="Actualizar Variable Programáticamente",
    command=actualizar_texto_variable,
    bg="skyblue"
)
boton_actualizar.pack(pady=10)


# 7. Observar el comportamiento
print("Interfaz con Frames y StringVar lista.")
print(f"Valor inicial de StringVar: '{texto_compartido.get()}'")

raiz.mainloop()
print("Aplicación cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el propósito principal de un widget `Frame`? ¿Cómo ayuda a
    organizar interfaces más complejas?
2.  ¿Qué es una `StringVar` (o `IntVar`, `BooleanVar`, `DoubleVar`) en Tkinter?
    ¿Cuál es la principal ventaja de usarla con la opción `textvariable` de
    widgets como `Entry` o `Label`?
3.  ¿Cómo se obtiene el valor de una `StringVar` en Python? ¿Y cómo se establece
    o cambia su valor? (Ver `get()` y `set()`).
4.  Si modificas el texto directamente en el `Entry` que está vinculado a la
    `StringVar`, ¿por qué se actualiza automáticamente la `Label` que también
    está vinculada a la misma `StringVar`?
5.  ¿Podrías tener múltiples `Frame`s anidados (un `Frame` dentro de otro `Frame`)?
    ¿Para qué podría ser útil?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

def alternativa_1():
    """Frames con `grid()` en lugar de `pack()`.

    Cada `Frame` es un contenedor independiente: dentro de uno puedes usar
    `pack` y dentro de otro `grid`. Aquí el marco de arriba organiza su
    contenido en columnas con grid.
    Cuándo conviene: cuando el contenido de un marco es una tabla o formulario.
    """
    raiz = tk.Tk()
    texto = tk.StringVar(master=raiz, value="Texto inicial")
    marco = tk.Frame(raiz, bd=2, relief="groove", padx=5, pady=5)
    marco.pack(padx=10, pady=10, fill="x")
    tk.Label(marco, text="Entrada:").grid(row=0, column=0, sticky="w")
    tk.Entry(marco, textvariable=texto).grid(row=0, column=1, sticky="ew")
    tk.Label(marco, text="Eco:").grid(row=1, column=0, sticky="w")
    tk.Label(marco, textvariable=texto).grid(row=1, column=1, sticky="w")
    marco.columnconfigure(1, weight=1)
    raiz.mainloop()


def alternativa_2():
    """Sin `StringVar`: copiar el texto a mano con el evento de teclado.

    Cada vez que se suelta una tecla (`<KeyRelease>`) se lee el `Entry` y se
    actualiza la `Label`. Funciona, pero ahora eres TÚ quien mantiene los dos
    widgets sincronizados, y si olvidas un caso (pegar con el mouse, por
    ejemplo) quedan distintos; la `StringVar` lo hace por ti.
    Cuándo conviene: casi nunca para esto; sí si necesitas reaccionar a
    teclas específicas (Enter, Escape).
    """
    raiz = tk.Tk()
    entrada = tk.Entry(raiz)
    entrada.insert(0, "Texto inicial")
    entrada.pack(padx=10, pady=10)
    eco = tk.Label(raiz, text="Texto inicial")
    eco.pack(padx=10, pady=10)
    entrada.bind("<KeyRelease>", lambda evento: eco.config(text=entrada.get()))
    raiz.mainloop()


def alternativa_3():
    """`StringVar.trace_add`: ejecutar código cada vez que cambia la variable.

    Además de sincronizar los widgets, aquí se cuenta cuántos caracteres hay.
    Cuándo conviene: validar o reaccionar a cada cambio (límites de largo,
    habilitar/deshabilitar un botón) sin depender de qué widget originó el cambio.
    """
    raiz = tk.Tk()
    texto = tk.StringVar(master=raiz)
    contador = tk.StringVar(master=raiz, value="0 caracteres")
    texto.trace_add("write", lambda *args: contador.set(f"{len(texto.get())} caracteres"))
    tk.Entry(raiz, textvariable=texto).pack(padx=10, pady=10)
    tk.Label(raiz, textvariable=contador).pack(padx=10, pady=10)
    raiz.mainloop()


# alternativa_1()
# alternativa_2()
# alternativa_3()
