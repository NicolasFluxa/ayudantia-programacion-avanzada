"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                 Layout con `grid()` - Calculadora Simple (Suma)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
El gestor de geometría `grid()` permite organizar widgets en una estructura
de filas y columnas, ofreciendo más control que `pack()`.
Crearemos una interfaz muy simple para una calculadora que solo sume dos números.

1.  Crea una ventana raíz de Tkinter.
2.  Crea los siguientes widgets:
    a.  Una `Label` con el texto "Primer número:".
    b.  Un `Entry` para que el usuario ingrese el primer número.
    c.  Una `Label` con el texto "Segundo número:".
    d.  Un `Entry` para el segundo número.
    e.  Una `Label` para el texto "Resultado:".
    f.  Una `Label` (inicialmente vacía o con "0") para MOSTRAR el resultado.
    g.  Un `Button` con el texto "Sumar".
3.  Organiza estos widgets usando el método `grid()`:
    * La primera Label y el primer Entry en la fila 0.
    * La segunda Label y el segundo Entry en la fila 1.
    * El botón "Sumar" en la fila 2 (puede ocupar varias columnas o estar centrado).
    * La Label "Resultado:" y la Label para el resultado en la fila 3.
    Usa opciones como `row`, `column`, `sticky` (para alineación), `padx`, `pady`.
4.  Define una función `realizar_suma()`:
    a.  Debe obtener los valores de los dos `Entry` (recordar convertirlos a número).
    b.  Calcular la suma.
    c.  Actualizar el texto de la `Label` del resultado.
    d.  Manejar posibles `ValueError` si la entrada no es numérica.
5.  Asocia `realizar_suma()` al `command` del botón "Sumar".
6.  Inicia el `mainloop`.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: ordenar widgets en una cuadrícula de filas y columnas con `grid()`,
y leer/convertir datos de `Entry` con manejo de errores.

Al ejecutar se abre una ventana de 300x200 con dos cajas de texto, el botón
«Sumar» (que ocupa todo el ancho) y el resultado, que parte en «0.00»:
  - con 2 y 3.5 el resultado pasa a «5.50»;
  - con una caja vacía aparece el aviso «Por favor, ingresa ambos números.»;
  - con texto (ej.: «abc»), aparece el error «Por favor, ingresa solo números
    válidos.» y el resultado muestra «Error».
Observa que los decimales deben ir con PUNTO (3.5): «3,5» da error. La
alternativa 3 del final muestra cómo aceptar también la coma.

-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox  # Para mostrar errores de forma más visual

# Los widgets 'entry_num1', 'entry_num2' y 'label_resultado_valor' se crean más abajo, a
# nivel de módulo. La función puede leerlos sin 'global' porque solo se ejecuta cuando
# el usuario presiona el botón, momento en que ya existen. (Para evitar variables
# globales, mira las alternativas del final.)

def realizar_suma():
    """Obtiene los números de los Entry, los suma y muestra el resultado."""
    try:
        num1_str = entry_num1.get()
        num2_str = entry_num2.get()

        if not num1_str or not num2_str:  # Verificar si están vacíos
            messagebox.showwarning("Entrada Vacía", "Por favor, ingresa ambos números.")
            return

        num1 = float(num1_str)
        num2 = float(num2_str)

        suma = num1 + num2
        label_resultado_valor.config(text=f"{suma:.2f}")  # Mostrar con 2 decimales

    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, ingresa solo números válidos.")
        label_resultado_valor.config(text="Error")
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")
        label_resultado_valor.config(text="Error")


# 1. Crear ventana raíz
raiz = tk.Tk()
raiz.title("Calculadora de Suma con grid()")
raiz.geometry("300x200")  # Ajustar tamaño según necesidad

# Configurar padding general para la ventana raíz para que los widgets no estén pegados a los bordes
raiz.configure(padx=10, pady=10)

# 2. Crear widgets y 3. Organizar con grid()

# Fila 0
label_num1 = tk.Label(raiz, text="Primer número:")
label_num1.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # sticky="w" (west) para alinear a la izquierda

entry_num1 = tk.Entry(raiz, width=15)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# Fila 1
label_num2 = tk.Label(raiz, text="Segundo número:")
label_num2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry_num2 = tk.Entry(raiz, width=15)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Fila 2
boton_sumar = tk.Button(raiz, text="Sumar", command=realizar_suma, width=10)
# columnspan=2 para que el botón ocupe el espacio de dos columnas
# sticky="ew" para que se expanda horizontalmente (east-west)
boton_sumar.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# Fila 3
label_resultado_texto = tk.Label(raiz, text="Resultado:")
label_resultado_texto.grid(row=3, column=0, padx=5, pady=5, sticky="w")

label_resultado_valor = tk.Label(raiz, text="0.00", width=15, relief="sunken",
                                 anchor="e")  # anchor="e" (east) para alinear texto a la derecha
label_resultado_valor.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

# Configurar pesos de las columnas para que el Entry se expanda si la ventana se redimensiona
# La columna 1 (donde están los Entry) se expandirá
raiz.columnconfigure(1, weight=1)

# 6. Iniciar bucle principal
print("Calculadora simple (suma) lista.")
raiz.mainloop()
print("Calculadora cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la diferencia principal entre `pack()` y `grid()` como gestores de geometría?
    ¿En qué situaciones `grid()` podría ser más ventajoso?
2.  Explica qué hacen las opciones `row`, `column`, `columnspan` y `sticky` en el método `grid()`.
    ¿Qué significan valores como `sticky="w"` o `sticky="ew"`?
3.  En la función `realizar_suma()`, ¿por qué es importante usar `try-except` al
    convertir las entradas de los `Entry` a números?
4.  La línea `raiz.columnconfigure(1, weight=1)` se usa para el comportamiento de redimensión.
    ¿Qué efecto tiene `weight=1` en una columna (o fila con `rowconfigure`)?
5.  ¿Cómo modificarías esta calculadora para que también tenga un botón "Restar" y
    realice la resta de los dos números, mostrando el resultado en la misma etiqueta?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

def alternativa_1():
    """Mismo diseño con `pack()` y un `Frame` por fila.

    `pack` no tiene filas ni columnas: para alinear «etiqueta + caja» lado a
    lado hay que agrupar cada par en un `Frame` y empaquetar con `side="left"`.
    Cuándo conviene: pack, para barras de botones o columnas simples apiladas;
    grid, para cualquier cosa que deba alinearse en columnas (formularios,
    calculadoras, tablas). No se pueden mezclar `pack` y `grid` en el MISMO
    contenedor (Tkinter se queda trabado), pero sí en contenedores distintos.
    """
    raiz = tk.Tk()
    raiz.title("Suma con pack()")
    entradas = []
    for texto in ("Primer número:", "Segundo número:"):
        fila = tk.Frame(raiz)
        fila.pack(fill="x", padx=10, pady=5)
        tk.Label(fila, text=texto, width=15, anchor="w").pack(side="left")
        entrada = tk.Entry(fila, width=15)
        entrada.pack(side="left")
        entradas.append(entrada)

    resultado = tk.Label(raiz, text="0.00", relief="sunken")

    def sumar():
        try:
            resultado.config(text=f"{float(entradas[0].get()) + float(entradas[1].get()):.2f}")
        except ValueError:
            resultado.config(text="Error")

    tk.Button(raiz, text="Sumar", command=sumar).pack(fill="x", padx=10, pady=10)
    resultado.pack(fill="x", padx=10, pady=5)
    raiz.mainloop()


def alternativa_2():
    """La calculadora como clase, con una tabla de operaciones.

    Los widgets son atributos (`self.entrada1`...), sin variables globales,
    y las operaciones viven en un diccionario: agregar «Restar» o «Multiplicar»
    es agregar una línea (pregunta 5 de las preguntas de comprensión).
    Cuándo conviene: cuando la calculadora crece (más operaciones, historial).
    """
    import operator

    class Calculadora(tk.Tk):
        OPERACIONES = {"Sumar": operator.add, "Restar": operator.sub, "Multiplicar": operator.mul}

        def __init__(self):
            super().__init__()
            self.title("Calculadora con clase")
            self.entrada1 = tk.Entry(self, width=15)
            self.entrada2 = tk.Entry(self, width=15)
            self.resultado = tk.Label(self, text="0.00", relief="sunken", width=15, anchor="e")
            tk.Label(self, text="Primer número:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
            self.entrada1.grid(row=0, column=1, padx=5)
            tk.Label(self, text="Segundo número:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
            self.entrada2.grid(row=1, column=1, padx=5)
            for columna, (nombre, funcion) in enumerate(self.OPERACIONES.items()):
                tk.Button(self, text=nombre, command=lambda f=funcion: self.calcular(f)).grid(row=2, column=columna, pady=8)
            tk.Label(self, text="Resultado:").grid(row=3, column=0, sticky="w", padx=5)
            self.resultado.grid(row=3, column=1, padx=5)

        def calcular(self, operacion):
            try:
                valor = operacion(float(self.entrada1.get()), float(self.entrada2.get()))
                self.resultado.config(text=f"{valor:.2f}")
            except ValueError:
                self.resultado.config(text="Error")

    Calculadora().mainloop()


def alternativa_3():
    """Aceptar la coma decimal (3,5) además del punto (3.5).

    En Chile se escribe la coma, pero `float("3,5")` falla. Una función
    pequeña normaliza el texto antes de convertir; la lógica de errores no cambia.
    Cuándo conviene: siempre que los usuarios escriban números a mano.
    """
    def leer_numero(texto):
        return float(texto.strip().replace(",", "."))

    for ejemplo in ("3,5", "2.25", " 10 ", "abc"):
        try:
            print(f"{ejemplo!r} -> {leer_numero(ejemplo)}")
        except ValueError:
            print(f"{ejemplo!r} -> no es un número")


# alternativa_1()
# alternativa_2()
# alternativa_3()
