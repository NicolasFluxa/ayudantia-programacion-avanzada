"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                          Factorial Recursivo
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
El factorial de un número entero no negativo `n`, denotado como `n!`, es el
producto de todos los enteros positivos menores o iguales a `n`.
Por ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.
Por definición, 0! = 1 y 1! = 1.

Escribe una función recursiva llamada `factorial_recursivo(n)` que calcule
el factorial de un número `n`.

La función debe:
1.  Validar que `n` sea un entero no negativo. Si es negativo, debe lanzar
    un `ValueError`. Si no es entero, también (o manejarlo adecuadamente).
2.  Identificar el caso base: si `n` es 0 o 1, el factorial es 1.
3.  Identificar el caso recursivo: si `n > 1`, el factorial es `n` multiplicado
    por el factorial de `n-1`.
4.  Probar la función con varios números (ej: 0, 1, 5, 7) y también con un
    número negativo para ver la validación.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: resolver un problema definiéndolo en términos de una versión más
pequeña de sí mismo (n! = n * (n-1)!) hasta llegar a un caso que se responde
directo (0! = 1! = 1).

Al ejecutar verás los factoriales de 0, 1, 5, 7 y 3 (1, 1, 120, 5040 y 6) y
después dos mensajes de error controlados: uno para -3 (negativo) y otro para
3.5 (no es entero). Para trazar las llamadas, descomenta el `print` de
depuración dentro de la función.

-------------------------------------------------------------------------------
"""

def factorial_recursivo(n):
    """
    Calcula el factorial de un número n de forma recursiva.

    Args:
        n (int): Un número entero no negativo.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es negativo o no es un entero.
    """
    # 1. Validar la entrada
    if not isinstance(n, int):
        raise ValueError("El factorial solo está definido para números enteros.")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    # 2. Caso base
    if n == 0 or n == 1:
        return 1
    # 3. Caso recursivo
    else:
        # print(f"Calculando {n} * factorial_recursivo({n-1})") # Para depuración y ver las llamadas
        return n * factorial_recursivo(n - 1)

# 4. Pruebas de la función
print("--- Calculando Factoriales Recursivamente ---")
numeros_prueba = [0, 1, 5, 7, 3]

for num in numeros_prueba:
    try:
        resultado = factorial_recursivo(num)
        print(f"El factorial de {num} ({num}!) es: {resultado}")
    except ValueError as e:
        print(f"Error al calcular factorial de {num}: {e}")

# Prueba con un número negativo
print("\nIntentando calcular factorial de un número negativo (-3):")
try:
    factorial_recursivo(-3)
except ValueError as e:
    print(f"Error: {e}")

# Prueba con un no entero
print("\nIntentando calcular factorial de un no entero (3.5):")
try:
    factorial_recursivo(3.5)
except ValueError as e:
    print(f"Error: {e}")

print("-------------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es un "caso base" en una función recursiva? ¿Por qué es crucial tenerlo?
    ¿Cuál es el caso base en `factorial_recursivo`?
2.  ¿Qué es un "caso recursivo" (o paso recursivo)? ¿Cómo se define en esta función?
3.  Si llamaras a `factorial_recursivo(3)`, traza mentalmente (o en papel) las
    llamadas recursivas que se harían hasta llegar al caso base y cómo se
    construye el resultado final.
4.  ¿Qué sucedería si el caso base estuviera incorrecto o ausente (por ejemplo,
    si el caso base fuera `n == -1`)?
5.  La recursividad a veces puede ser menos eficiente que una solución iterativa
    (con bucles) debido a la sobrecarga de llamadas a funciones. ¿Podrías
    escribir una versión iterativa de la función factorial?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

import math
from functools import reduce


def alternativa_1():
    """Versión iterativa (con un bucle).

    Hace lo mismo sin llamadas apiladas, así que no tiene límite de recursión:
    con n grande la versión recursiva falla con `RecursionError` y esta no.
    Cuándo conviene: cuando n puede ser grande, o cuando el problema se
    describe naturalmente como una repetición (no como un problema que
    contiene un problema más pequeño).
    """
    def factorial_iterativo(n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("El factorial requiere un entero no negativo.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    print(factorial_iterativo(5))                           # 120
    print(len(str(factorial_iterativo(1500))), "dígitos")   # funciona con n grande
    try:
        factorial_recursivo(1500)                           # la recursiva se pasa del límite
    except RecursionError:
        print("La versión recursiva excedió el límite de recursión (≈ 1000 llamadas).")


def alternativa_2():
    """`math.factorial`: lo que ya trae la biblioteca estándar.

    Está escrita en C, es rápida y valida la entrada por ti.
    Cuándo conviene: en código real, siempre que exista una función de la
    biblioteca estándar que haga lo que necesitas. La versión recursiva es
    para aprender la técnica.
    """
    print(math.factorial(5))                                # 120
    try:
        math.factorial(-3)
    except ValueError as error:
        print(f"Error: {error}")


def alternativa_3():
    """Producto con `math.prod` o `reduce` (estilo funcional).

    Cuándo conviene: cuando prefieres expresar «multiplica todos estos
    números» en una línea, sin escribir bucle ni recursión.
    """
    n = 5
    print(math.prod(range(1, n + 1)))                       # 120
    print(reduce(lambda acumulado, i: acumulado * i, range(1, n + 1), 1))   # 120


# alternativa_1()
# alternativa_2()
# alternativa_3()
