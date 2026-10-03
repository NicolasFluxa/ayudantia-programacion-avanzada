"""
-------------------------------------------------------------------------------
                        PROYECTO OPCIONAL 01
                 Juego "Adivina el Número" con Interfaz Gráfica
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Reimplementa el clásico juego de "Adivina el Número" (donde la computadora
"piensa" un número y el usuario intenta adivinarlo) pero esta vez con una
interfaz gráfica de usuario (GUI) utilizando Tkinter.

**Funcionalidades Requeridas:**

1.  **Generación del Número Secreto:**
    * Al iniciar la aplicación (o al presionar un botón "Nuevo Juego"), la
        computadora debe generar un número aleatorio secreto entre 1 y 100.
        (Usa el módulo `random`: `random.randint(1, 100)`).
2.  **Interfaz Gráfica:**
    * Una `Label` para dar instrucciones al usuario (ej: "Adivina un número entre 1 y 100").
    * Un `Entry` para que el usuario ingrese su intento.
    * Un `Button` "Adivinar" para enviar el intento.
    * Una `Label` para mostrar retroalimentación (ej: "Muy alto", "Muy bajo",
        "¡Correcto!", "Ingresa un número válido.").
    * (Opcional) Una `Label` para mostrar el número de intentos realizados.
3.  **Lógica del Juego:**
    * Cuando el usuario presiona "Adivinar":
        a.  Obtener el número del `Entry`. Validar que sea un número entero.
        b.  Incrementar el contador de intentos.
        c.  Comparar el intento con el número secreto.
        d.  Actualizar la `Label` de retroalimentación:
            * Si el intento es menor: "Muy bajo. Intenta de nuevo."
            * Si el intento es mayor: "Muy alto. Intenta de nuevo."
            * Si es correcto: "¡Felicidades! Adivinaste en [X] intentos."
                En este caso, el `Entry` y el botón "Adivinar" podrían deshabilitarse
                hasta que se inicie un "Nuevo Juego".
4.  **Botón "Nuevo Juego":**
    * Debe resetear el juego: generar un nuevo número secreto, limpiar el
        `Entry`, resetear la `Label` de retroalimentación y el contador de
        intentos, y rehabilitar los controles si estaban deshabilitados.
5.  **Estructura:**
    * Organiza la aplicación usando una clase.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: un juego completo con interfaz gráfica que combine todo lo visto:
una clase con estado (número secreto, intentos), variables de control,
validación de la entrada, eventos de teclado y widgets que se habilitan o
deshabilitan.

Al ejecutar se abre una ventana de 400x300. El programa elige un número entre
1 y 100 (la consola lo muestra «para depuración»: no mires si quieres jugar).
  - escribe un número y presiona «Adivinar» (o Enter): la etiqueta dice si es
    muy bajo o muy alto y se actualiza el contador de intentos;
  - un texto no numérico, o fuera de 1 a 100, muestra un aviso y NO cuenta
    como intento;
  - al acertar, se muestra un mensaje con los intentos usados, y la caja y
    el botón «Adivinar» se deshabilitan;
  - «Nuevo Juego» reinicia todo con otro número secreto.

-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox
import random


class JuegoAdivinaNumeroGUI:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número")
        master.geometry("400x300")
        master.configure(padx=15, pady=15)

        self.numero_secreto = 0
        self.intentos_realizados = 0

        # Variables de control de Tkinter
        self.var_intento_usuario = tk.StringVar()
        self.var_retroalimentacion = tk.StringVar()
        self.var_contador_intentos = tk.StringVar()

        self.crear_widgets()
        self.iniciar_nuevo_juego()  # Inicia el primer juego automáticamente

    def crear_widgets(self):
        """Crea y posiciona los widgets de la interfaz."""
        tk.Label(self.master, text="He pensado un número entre 1 y 100.", font=("Arial", 12)).pack(pady=5)

        frame_entrada = tk.Frame(self.master)
        frame_entrada.pack(pady=10)

        tk.Label(frame_entrada, text="Tu intento:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.entry_intento = tk.Entry(frame_entrada, textvariable=self.var_intento_usuario, width=10,
                                      font=("Arial", 10))
        self.entry_intento.pack(side=tk.LEFT, padx=5)
        self.entry_intento.focus()
        # Bind Enter key to a adivinar_numero method
        self.entry_intento.bind("<Return>", lambda event: self.procesar_intento())

        self.boton_adivinar = tk.Button(self.master, text="Adivinar", command=self.procesar_intento,
                                        font=("Arial", 10, "bold"), bg="lightblue")
        self.boton_adivinar.pack(pady=5)

        self.label_retroalimentacion = tk.Label(self.master, textvariable=self.var_retroalimentacion,
                                                font=("Arial", 11, "italic"), fg="navy")
        self.label_retroalimentacion.pack(pady=10)

        self.label_contador_intentos = tk.Label(self.master, textvariable=self.var_contador_intentos,
                                                font=("Arial", 10))
        self.label_contador_intentos.pack(pady=5)

        self.boton_nuevo_juego = tk.Button(self.master, text="Nuevo Juego", command=self.iniciar_nuevo_juego,
                                           font=("Arial", 10), bg="lightgreen")
        self.boton_nuevo_juego.pack(pady=10)

    def iniciar_nuevo_juego(self):
        """Resetea el estado del juego para una nueva partida."""
        self.numero_secreto = random.randint(1, 100)
        self.intentos_realizados = 0

        self.var_intento_usuario.set("")  # Limpiar Entry
        self.var_retroalimentacion.set("Ingresa tu primer intento.")
        self.var_contador_intentos.set("Intentos: 0")

        self.entry_intento.config(state=tk.NORMAL)  # Habilitar Entry
        self.boton_adivinar.config(state=tk.NORMAL)  # Habilitar Botón
        self.entry_intento.focus()
        print(f"Nuevo juego iniciado. Número secreto (para depuración): {self.numero_secreto}")

    def procesar_intento(self):
        """Procesa el intento del usuario."""
        try:
            intento = int(self.var_intento_usuario.get())
            if not (1 <= intento <= 100):
                self.var_retroalimentacion.set("Por favor, ingresa un número entre 1 y 100.")
                messagebox.showwarning("Entrada Inválida", "El número debe estar entre 1 y 100.")
                self.var_intento_usuario.set("")
                return

            self.intentos_realizados += 1
            self.var_contador_intentos.set(f"Intentos: {self.intentos_realizados}")

            if intento < self.numero_secreto:
                self.var_retroalimentacion.set(f"'{intento}' es MUY BAJO. ¡Intenta de nuevo!")
            elif intento > self.numero_secreto:
                self.var_retroalimentacion.set(f"'{intento}' es MUY ALTO. ¡Intenta de nuevo!")
            else:  # ¡Correcto!
                palabra = "intento" if self.intentos_realizados == 1 else "intentos"  # concordancia
                mensaje_exito = (f"¡CORRECTO! Adivinaste el número {self.numero_secreto} "
                                 f"en {self.intentos_realizados} {palabra}.")
                self.var_retroalimentacion.set(mensaje_exito)
                messagebox.showinfo("¡Felicidades!", mensaje_exito)
                self.entry_intento.config(state=tk.DISABLED)  # Deshabilitar Entry
                self.boton_adivinar.config(state=tk.DISABLED)  # Deshabilitar Botón

        except ValueError:
            self.var_retroalimentacion.set("Entrada inválida. Ingresa solo NÚMEROS enteros.")
            messagebox.showerror("Error de Entrada", "Debes ingresar un número entero.")

        self.var_intento_usuario.set("")  # Limpiar Entry para el siguiente intento
        self.entry_intento.focus()


# --- Bloque Principal ---
if __name__ == "__main__":
    print("Iniciando Juego 'Adivina el Número' con GUI...")
    ventana_raiz = tk.Tk()
    juego_app = JuegoAdivinaNumeroGUI(ventana_raiz)
    ventana_raiz.mainloop()
    print("Juego cerrado.")

"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  **Estado del Juego:** ¿Qué variables de instancia (`self.numero_secreto`,
    `self.intentos_realizados`) son cruciales para mantener el estado del juego?
2.  **Variables de Control Tkinter:** ¿Cómo se usan `StringVar` para actualizar
    dinámicamente el texto de las `Label`s y obtener el texto del `Entry`?
3.  **Flujo del Juego:** Describe el flujo lógico que ocurre cuando el usuario
    ingresa un número y presiona "Adivinar".
4.  **Reinicio del Juego:** ¿Qué acciones realiza la función `iniciar_nuevo_juego()`
    para preparar una nueva partida?
5.  **Deshabilitar Widgets:** ¿Por qué y cómo se deshabilitan el `Entry` y el botón
    "Adivinar" una vez que el usuario adivina correctamente? ¿Cómo se vuelven a
    habilitar? (Ver la opción `state` de los widgets).
6.  **Manejo de Errores:** ¿Qué tipo de error se maneja con `try-except` en
    `procesar_intento()`? ¿Qué otros errores podrían considerarse?
7.  **Mejora (Binding de Evento):** La línea `self.entry_intento.bind("<Return>", lambda event: self.procesar_intento())`
    permite que el usuario presione Enter en el Entry para adivinar. Explica brevemente
    cómo funciona `bind` y qué es `lambda event: ...` en este contexto.
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

import random


def alternativa_1():
    """`Spinbox`: evitar el error en vez de validarlo.

    Un `Spinbox` solo ofrece números de 1 a 100 (con flechas), así que casi no
    se pueden ingresar valores fuera de rango. Aun así se debe validar si el
    usuario escribe a mano.
    Cuándo conviene: cuando el rango es pequeño y conocido; para rangos
    amplios (1 a 1.000.000) la caja de texto es más práctica.
    """
    raiz = tk.Tk()
    secreto = random.randint(1, 100)
    caja = tk.Spinbox(raiz, from_=1, to=100, width=6)
    caja.pack(padx=20, pady=10)
    mensaje = tk.Label(raiz, text="Adivina un número entre 1 y 100")
    mensaje.pack(pady=5)

    def probar():
        try:
            intento = int(caja.get())
        except ValueError:
            mensaje.config(text="Escribe un número entero.")
            return
        mensaje.config(text="¡Correcto!" if intento == secreto else "Muy bajo" if intento < secreto else "Muy alto")

    tk.Button(raiz, text="Adivinar", command=probar).pack(pady=5)
    raiz.mainloop()


def alternativa_2():
    """Validación en vivo con `validatecommand`: solo deja escribir dígitos.

    Tkinter pregunta a la función ANTES de aceptar cada tecla (`%P` es el texto
    que quedaría). Si devuelve `False`, la tecla se rechaza. Así nunca llega
    texto inválido a `int()`.
    Cuándo conviene: campos con formato estricto (números, códigos, RUT).
    Ojo: para el usuario es menos claro «por qué no me deja escribir» que un
    mensaje de error; úsalo con una instrucción visible.
    """
    raiz = tk.Tk()
    solo_digitos = (raiz.register(lambda texto_nuevo: texto_nuevo == "" or texto_nuevo.isdigit()), "%P")
    tk.Entry(raiz, validate="key", validatecommand=solo_digitos, width=10).pack(padx=20, pady=20)
    raiz.mainloop()


def alternativa_3():
    """Lógica del juego como funciones puras (sin Tkinter).

    `evaluar_intento` se puede probar sin abrir una ventana, y permite hacer
    algo imposible en la interfaz: dejar que un programa juegue solo con
    búsqueda binaria. Siempre acierta en 7 intentos o menos (2^7 = 128 > 100).
    Cuándo conviene: cuando la lógica empieza a tener reglas propias; la
    interfaz queda como una capa delgada que solo muestra resultados.
    """
    def evaluar_intento(intento, secreto):
        if intento < secreto:
            return "bajo"
        if intento > secreto:
            return "alto"
        return "correcto"

    secreto = random.randint(1, 100)
    minimo, maximo, intentos = 1, 100, 0
    while True:
        intento = (minimo + maximo) // 2
        intentos += 1
        resultado = evaluar_intento(intento, secreto)
        if resultado == "correcto":
            break
        if resultado == "bajo":
            minimo = intento + 1
        else:
            maximo = intento - 1
    print(f"El número era {secreto}; la búsqueda binaria lo halló en {intentos} intentos.")


# alternativa_1()
# alternativa_2()
# alternativa_3()
