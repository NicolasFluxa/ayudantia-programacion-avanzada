"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                 Manejo de Errores Básico con `try-except`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que pida al usuario dos números y luego muestre el
resultado de la división del primer número por el segundo. Debes manejar
posibles errores que puedan surgir durante la entrada de datos o la operación.

1.  Usa un bucle `while` para permitir al usuario reintentar si ingresa datos inválidos.
2.  Dentro del bucle:
    a.  Usa un bloque `try` para intentar:
        i.  Pedir al usuario que ingrese el primer número (dividendo).
        ii. Convertirlo a `float`.
        iii.Pedir al usuario que ingrese el segundo número (divisor).
        iv. Convertirlo a `float`.
        v.  Realizar la división.
        vi. Imprimir el resultado de la división.
        vii.Si todo fue exitoso, salir del bucle `while` (usando `break`).
    b.  Usa un bloque `except ValueError`:
        i.  Si ocurre este error (ej: el usuario ingresa texto en lugar de un número),
            imprime un mensaje amigable como "Error: Debes ingresar números válidos."
    c.  Usa un bloque `except ZeroDivisionError`:
        i.  Si ocurre este error (el usuario intenta dividir por cero), imprime
            un mensaje como "Error: No se puede dividir por cero."
    d.  (Opcional) Añade un `except Exception as e:` genérico al final para
        capturar cualquier otro error inesperado e imprimirlo.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: que el programa no se caiga cuando el usuario escribe algo
inválido, sino que explique el problema y permita reintentar.

Al ejecutar:
  - el programa pide el dividendo y el divisor, y con datos válidos muestra
    el resultado con 4 decimales (ej.: 10 / 4 = 2.5000) y termina;
  - si escribes texto («abc») o divides por cero, muestra un mensaje de error
    específico y vuelve a preguntar desde el principio;
  - la solución limita los reintentos a 3 (así no queda en un bucle infinito);
    al agotarlos avisa y termina. La pregunta 5 propone quitar ese límite.

-------------------------------------------------------------------------------
"""

print("--- Calculadora de Divisiones Segura ---")
intentos_restantes = 3  # Limitar intentos para no quedar en bucle infinito si hay error persistente

while intentos_restantes > 0:
    try:
        # a.i, a.ii
        dividendo_str = input(f"\nIngresa el dividendo (número a dividir) [Intentos: {intentos_restantes}]: ")
        dividendo = float(dividendo_str)

        # a.iii, a.iv
        divisor_str = input("Ingresa el divisor (número por el cual dividir): ")
        divisor = float(divisor_str)

        # a.v
        resultado = dividendo / divisor

        # a.vi
        print(f"\nEl resultado de {dividendo} / {divisor} es: {resultado:.4f}")

        # a.vii (Si todo fue exitoso, salir del bucle)
        break

    # b. Manejar error si la conversión a float falla
    except ValueError:
        print("Error: Debes ingresar números válidos (ej: 10, 3.14). El texto no es un número.")
        intentos_restantes -= 1

    # c. Manejar error si se intenta dividir por cero
    except ZeroDivisionError:
        print("Error: ¡No se puede dividir por cero! Intenta con otro divisor.")
        intentos_restantes -= 1  # Podríamos no descontar aquí si solo fue el divisor

    # d. (Opcional) Capturar cualquier otro error
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        intentos_restantes -= 1

    if intentos_restantes == 0:
        print("\nHas agotado tus intentos. Por favor, reinicia el programa si deseas continuar.")

print("\n--- Fin del programa ---")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el propósito principal del bloque `try`? ¿Y del bloque `except`?
2.  ¿Por qué es útil especificar el tipo de error en la cláusula `except`
    (ej: `except ValueError:`) en lugar de usar solo `except:` (que capturaría todo)?
3.  Si el usuario ingresa "cero" (como texto) para el divisor, ¿qué bloque `except`
    se activaría primero y por qué?
4.  ¿Qué pasaría si el `break` dentro del bloque `try` no estuviera y el usuario
    ingresara datos correctos al primer intento?
5.  ¿Cómo podrías modificar el programa para que el bucle `while` sea infinito
    (`while True:`) y solo se rompa con `break` cuando la operación sea exitosa,
    sin un límite de intentos?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

def alternativa_1():
    """Función reutilizable para leer un número (separa «leer» de «dividir»).

    La solución principal mezcla entrada, conversión y cálculo en un solo
    bloque. Aquí `leer_numero` se encarga de pedir hasta recibir un número
    válido, y se puede reutilizar para cualquier dato numérico.
    Cuándo conviene: cuando vas a pedir varios números en el programa.
    """
    def leer_numero(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: debes ingresar un número válido.")

    dividendo = leer_numero("Dividendo: ")
    divisor = leer_numero("Divisor: ")
    try:
        print(f"{dividendo} / {divisor} = {dividendo / divisor:.4f}")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")


def alternativa_2():
    """Comprobar antes (`if divisor == 0`) en vez de capturar el error.

    Estilo «mirar antes de saltar»: se evita el error en lugar de manejarlo.
    Cuándo conviene: cuando la condición es simple y fácil de comprobar (cero).
    Para la conversión a número NO conviene: comprobar si un texto es
    convertible a `float` es más complicado que intentarlo y capturar
    `ValueError`. Python favorece «intentar y capturar» (EAFP).
    """
    while True:
        try:
            dividendo = float(input("Dividendo: "))
            divisor = float(input("Divisor: "))
        except ValueError:
            print("Error: debes ingresar números válidos.")
            continue
        if divisor == 0:                       # comprobación previa
            print("Error: el divisor no puede ser cero.")
            continue
        print(f"{dividendo} / {divisor} = {dividendo / divisor:.4f}")
        break


# alternativa_1()
# alternativa_2()
