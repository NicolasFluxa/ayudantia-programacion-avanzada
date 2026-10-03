"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                    Entrada de Texto y Eco con Tkinter
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio combina los tres widgets más básicos de Tkinter: una caja de
texto para que el usuario escriba (`Entry`), un botón para disparar una acción
(`Button`) y una etiqueta para mostrar el resultado (`Label`).

1.  Crea una ventana raíz con un título y un tamaño (ej: "400x220").
2.  Crea una `Label` con una instrucción, como "Escribe algo y presiona «Repetir»".
3.  Crea un widget `Entry` (caja de texto de una línea) y empaquétalo.
4.  Crea una segunda `Label`, el «eco», con un texto inicial
    (ej: "El eco aparecerá aquí."). Aquí se mostrará lo que escriba el usuario.
5.  Define una función `repetir_texto()`:
    a.  Obtiene el texto de la caja con `entrada.get()`.
    b.  Si el texto no está vacío (ignorando espacios al inicio y al final),
        muestra en la etiqueta del eco: "Escribiste: [texto]".
    c.  Si está vacío, muestra un aviso, como "Aún no escribes nada.".
6.  Crea un botón «Repetir» que llame a `repetir_texto` (con `command`, y sin
    paréntesis, igual que en el ejercicio anterior).
7.  Crea un botón «Limpiar» que borre la caja (`entrada.delete(0, tk.END)`) y
    deje el eco con su texto inicial.
8.  (Extensión) Haz que presionar la tecla Enter dentro de la ventana también
    ejecute `repetir_texto`. Pista: `raiz.bind("<Return>", ...)`.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: practicar el ciclo básico de una interfaz: el usuario escribe
(`Entry`), presiona un botón (`Button`) y el programa responde cambiando una
`Label`.

Al ejecutar se abre una ventana con una caja de texto, un eco y dos botones:
  - al escribir «Hola» y presionar «Repetir» (o Enter), el eco dice
    «Escribiste: Hola» (y también se imprime en la consola);
  - con la caja vacía, el eco dice «Aún no escribes nada.»;
  - «Limpiar» borra la caja y devuelve el eco a su texto inicial.

-------------------------------------------------------------------------------
"""
import tkinter as tk

TEXTO_INICIAL_ECO = "El eco aparecerá aquí."

# 5. Función que lee la caja de texto y actualiza el eco
def repetir_texto():
    """Lee lo escrito en la caja y lo muestra en la etiqueta del eco."""
    texto = entrada.get().strip()  # .get() devuelve siempre un str; .strip() quita espacios sobrantes
    if texto:
        etiqueta_eco.config(text=f"Escribiste: {texto}", fg="black")
        print(f"Eco: {texto}")
    else:
        etiqueta_eco.config(text="Aún no escribes nada.", fg="gray")

# 7. Función que deja todo como al inicio
def limpiar():
    """Borra la caja de texto y restablece el eco."""
    entrada.delete(0, tk.END)  # Borra desde el carácter 0 hasta el final
    etiqueta_eco.config(text=TEXTO_INICIAL_ECO, fg="gray")
    entrada.focus()            # Deja el cursor listo para escribir de nuevo

# 1. Crear la ventana raíz
raiz = tk.Tk()
raiz.title("Entrada de texto y eco")
raiz.geometry("400x220")

# 2. Etiqueta con la instrucción
etiqueta_instruccion = tk.Label(raiz, text="Escribe algo y presiona «Repetir»", font=("Arial", 12))
etiqueta_instruccion.pack(pady=10)

# 3. Caja de texto (Entry). 'width' es el ancho medido en caracteres.
entrada = tk.Entry(raiz, width=35, font=("Arial", 12))
entrada.pack(pady=5)
entrada.focus()  # El cursor aparece directamente en la caja

# 4. Etiqueta del eco
etiqueta_eco = tk.Label(raiz, text=TEXTO_INICIAL_ECO, font=("Arial", 12), fg="gray")
etiqueta_eco.pack(pady=15)

# 6. y 7. Botones. Se ponen dentro de un Frame para que queden uno al lado del otro.
marco_botones = tk.Frame(raiz)
marco_botones.pack()
tk.Button(marco_botones, text="Repetir", command=repetir_texto).pack(side="left", padx=5)
tk.Button(marco_botones, text="Limpiar", command=limpiar).pack(side="left", padx=5)

# 8. (Extensión) La tecla Enter hace lo mismo que el botón «Repetir».
# bind() entrega un objeto «evento» a la función; como repetir_texto no lo recibe,
# lo envolvemos en una lambda que lo descarta.
raiz.bind("<Return>", lambda evento: repetir_texto())

print("Ventana lista. Escribe algo en la caja y presiona «Repetir» (o Enter).")
raiz.mainloop()
print("Aplicación cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué devuelve `entrada.get()`? ¿Qué tipo de dato es, aunque el usuario
    escriba un número? ¿Cómo lo convertirías a `int`?
2.  ¿Qué significan los dos argumentos de `entrada.delete(0, tk.END)`? ¿Qué
    pasaría si solo escribieras `entrada.delete(0)`?
3.  ¿Para qué sirve `.strip()` en `repetir_texto`? ¿Qué mostraría el eco si un
    usuario escribe solo espacios y no usáramos `.strip()`?
4.  `raiz.bind("<Return>", ...)` asocia un evento del teclado a una función.
    ¿Por qué hace falta la `lambda evento: ...`? ¿Qué error ocurriría si
    escribiéramos `raiz.bind("<Return>", repetir_texto)`?
5.  Las funciones `repetir_texto` y `limpiar` usan las variables `entrada` y
    `etiqueta_eco`, que son globales. ¿Cómo podrías evitarlo? (Mira las
    alternativas del final del archivo.)
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
    """`StringVar` compartida: el eco se actualiza SOLO, mientras escribes.

    El `Entry` y la `Label` comparten la misma variable de control
    (`textvariable`). No hace falta botón ni función: Tkinter sincroniza los
    widgets. Con `trace_add("write", ...)` se puede ejecutar código en cada cambio.
    Cuándo conviene: cuando quieres reaccionar en vivo (buscadores, contadores
    de caracteres). Con el botón, el usuario decide CUÁNDO se procesa el texto.
    """
    raiz = tk.Tk()
    raiz.title("Eco en vivo")
    texto = tk.StringVar(master=raiz)

    tk.Entry(raiz, textvariable=texto, width=35).pack(padx=20, pady=10)
    tk.Label(raiz, textvariable=texto, font=("Arial", 12)).pack(pady=10)   # se actualiza sola
    texto.trace_add("write", lambda *args: print(f"Eco: {texto.get()}"))

    raiz.mainloop()


def alternativa_2():
    """Sin variables globales: pasar los widgets a la función.

    `partial` (o una `lambda`) deja «preconfigurados» los argumentos de la
    función, así `command` sigue recibiendo una función sin parámetros pero la
    lógica ya no depende de globales.
    Cuándo conviene: scripts pequeños con varias ventanas o funciones. Para
    aplicaciones medianas, lo mejor es la clase (alternativa siguiente).
    """
    def repetir(entrada, etiqueta):
        texto = entrada.get().strip()
        etiqueta.config(text=f"Escribiste: {texto}" if texto else "Aún no escribes nada.")

    raiz = tk.Tk()
    raiz.title("Eco sin globales")
    entrada = tk.Entry(raiz, width=35)
    entrada.pack(padx=20, pady=10)
    eco = tk.Label(raiz, text="El eco aparecerá aquí.")
    eco.pack(pady=10)

    tk.Button(raiz, text="Repetir", command=partial(repetir, entrada, eco)).pack()
    # Equivalente con lambda: command=lambda: repetir(entrada, eco)

    raiz.mainloop()


def alternativa_3():
    """La aplicación como clase: los widgets son atributos (`self.entrada`...).

    Los métodos acceden a los widgets con `self`; no hacen falta globales y
    se pueden crear varias ventanas independientes.
    Cuándo conviene: en cuanto la aplicación tenga más de una ventana, mucho
    estado, o vaya a crecer (es el enfoque de la Semana 9).
    """
    class AppEco(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Eco con clase")
            self.entrada = tk.Entry(self, width=35)
            self.entrada.pack(padx=20, pady=10)
            self.eco = tk.Label(self, text="El eco aparecerá aquí.")
            self.eco.pack(pady=10)
            tk.Button(self, text="Repetir", command=self.repetir).pack()
            self.bind("<Return>", lambda evento: self.repetir())

        def repetir(self):
            texto = self.entrada.get().strip()
            self.eco.config(text=f"Escribiste: {texto}" if texto else "Aún no escribes nada.")

    AppEco().mainloop()


# alternativa_1()
# alternativa_2()
# alternativa_3()
