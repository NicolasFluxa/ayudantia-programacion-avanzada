"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
          Serie de Fibonacci Recursiva y Optimización con Memoización
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
La secuencia de Fibonacci es una serie de números donde cada número es la suma
de los dos anteriores, usualmente comenzando con 0 y 1.
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) para n > 1.

1.  Escribe una función recursiva `fibonacci_recursivo(n)` que calcule el
    n-ésimo número de Fibonacci.
    a.  Debe manejar los casos base para n=0 y n=1.
    b.  Debe manejar el caso recursivo F(n) = F(n-1) + F(n-2).
    c.  Asegúrate de que `n` sea un entero no negativo.

2.  Prueba la función para valores pequeños de `n` (ej: 0, 1, 2, 7, 10).
3.  Intenta calcular `fibonacci_recursivo(30)` o `fibonacci_recursivo(35)`.
    Observa el tiempo que tarda. Esta implementación es ineficiente porque
    recalcula los mismos valores de Fibonacci múltiples veces.

4.  **Optimización con Memoización (caché):**
    a.  Crea una nueva función `fibonacci_memoizado(n, cache={})`.
        El `cache` es un diccionario que se pasará (y modificará) entre llamadas
        recursivas para almacenar resultados ya calculados.
    b.  Antes de calcular F(n), verifica si `n` ya está en el `cache`. Si es así,
        retorna el valor cacheado.
    c.  Si no está en el `cache`, calcula F(n) (usando los casos base o la
        llamada recursiva CON memoización).
    d.  Antes de retornar el resultado calculado, guárdalo en el `cache` con `n` como clave.
    e.  Prueba `fibonacci_memoizado(30)`, `fibonacci_memoizado(35)` e incluso valores
        más altos como `fibonacci_memoizado(50)`. Compara el rendimiento.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: comprobar por qué una recursión «ingenua» puede ser lentísima (calcula
los mismos valores una y otra vez) y cómo la memoización (guardar resultados
ya calculados) lo arregla.

Al ejecutar verás:
  - F(0), F(1), F(2), F(7) y F(10) = 0, 1, 1, 13 y 55, con ambas versiones;
  - la comparación para F(30) = 832040: la recursiva simple tarda del orden de
    décimas de segundo a segundos (según tu computador) y la memoizada,
    microsegundos. Prueba con n = 35 y verás que la diferencia crece.

-------------------------------------------------------------------------------
"""
import time


# 1. Fibonacci recursivo (ineficiente)
def fibonacci_recursivo(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fibonacci solo está definido para enteros no negativos.")

    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    else:
        # print(f"Calculando F({n-1}) + F({n-2})") # Para ver la cantidad de llamadas
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# 4. Fibonacci con memoización
def fibonacci_memoizado(n, cache={}):
    """
    Calcula el n-ésimo número de Fibonacci usando recursión con memoización.
    El caché se pasa como un argumento por defecto mutable, lo que puede tener
    implicaciones si la función se llama múltiples veces desde el mismo scope
    sin resetear el caché explícitamente para una nueva "serie" de cálculos.
    Una forma más robusta es inicializar el caché fuera o pasarlo como None
    e inicializarlo dentro si es None.
    Para este ejercicio, el comportamiento por defecto es aceptable.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fibonacci solo está definido para enteros no negativos.")

    # Verificar si el resultado ya está en el caché
    if n in cache:
        return cache[n]

    # Casos base
    if n == 0:
        resultado = 0
    elif n == 1:
        resultado = 1
    # Caso recursivo
    else:
        # print(f"Memoizado: Calculando F({n-1}) + F({n-2})")
        resultado = fibonacci_memoizado(n - 1, cache) + fibonacci_memoizado(n - 2, cache)

    # Guardar el resultado en el caché antes de retornarlo
    cache[n] = resultado
    return resultado


# Pruebas
print("--- Calculando Fibonacci ---")
numeros_fib_pequenos = [0, 1, 2, 7, 10]
print("\nFibonacci recursivo (simple):")
for num in numeros_fib_pequenos:
    print(f"F({num}) = {fibonacci_recursivo(num)}")

print("\nFibonacci memoizado (debería dar los mismos resultados):")
for num in numeros_fib_pequenos:
    # Reseteamos el caché para cada prueba independiente si queremos un caché limpio
    # o usamos uno persistente si llamamos secuencialmente.
    # Para este ejemplo, un caché persistente en llamadas sucesivas es ok.
    print(f"F_memo({num}) = {fibonacci_memoizado(num, {})} ")  # Pasamos caché vacío

# Comparación de rendimiento para un número más grande
n_grande = 30  # Prueba con 30, luego puedes intentar 35

print(f"\nComparando rendimiento para F({n_grande}):")

# Recursivo simple
start_time = time.time()
try:
    res_recursivo = fibonacci_recursivo(n_grande)
    end_time = time.time()
    print(f"  Recursivo simple F({n_grande}) = {res_recursivo} (tomó {end_time - start_time:.4f} segundos)")
except ValueError as e:
    print(f"  Error recursivo: {e}")

# Memoizado
# Es importante resetear el caché si se quiere medir desde cero para la misma 'n'
# o si se sospecha que el caché por defecto mutable persiste entre llamadas no relacionadas.
# Aquí, para una comparación justa, usamos un caché nuevo.
cache_para_n_grande = {}
start_time = time.time()
try:
    res_memoizado = fibonacci_memoizado(n_grande, cache_para_n_grande)
    end_time = time.time()
    print(f"  Memoizado F({n_grande})      = {res_memoizado} (tomó {end_time - start_time:.4f} segundos)")
except ValueError as e:
    print(f"  Error memoizado: {e}")

# Para n_grande = 35 o más, la diferencia es aún más dramática.
# La versión recursiva simple se vuelve muy lenta.

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Por qué la implementación recursiva simple de Fibonacci es ineficiente para
    valores de `n` relativamente grandes (ej: n > 30)? (Piensa en cuántas veces
    se recalculan los mismos subproblemas).
2.  ¿Qué es la "memoización" (o memorización)? ¿Cómo ayuda a optimizar la función
    recursiva de Fibonacci?
3.  En `fibonacci_memoizado(n, cache={})`, ¿qué rol juega el diccionario `cache`?
    ¿Por qué se usa como un argumento con valor por defecto?
4.  El valor por defecto `cache={}` para un argumento de diccionario es una
    característica de Python que puede llevar a comportamientos inesperados si la
    función se llama múltiples veces y modifica el diccionario, ya que el mismo
    diccionario se reutiliza. ¿Cómo podrías modificar la función para asegurar
    que el caché se inicie vacío en cada "primera llamada" a una secuencia de
    Fibonacci si no se proporciona explícitamente un caché?
    (Pista: `if cache is None: cache = {}`).
5.  ¿Cuál es el límite práctico de la recursividad en Python (profundidad máxima
    de recursión)? ¿Qué error ocurre si se excede?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

from functools import lru_cache


def alternativa_1():
    """`@lru_cache`: memoización automática con un decorador.

    Es exactamente la misma recursión simple, más una línea. La biblioteca
    estándar guarda los resultados por ti, sin diccionario manual y sin el
    problema del argumento por defecto mutable (`cache={}`).
    Cuándo conviene: casi siempre que necesites memoizar una función pura en
    código real.
    """
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print(fib(30))                                          # 832040, al instante
    print(fib(90))                                          # 2880067194370816120
    print(fib.cache_info())                                 # cuántos aciertos del caché hubo


def alternativa_2():
    """Versión iterativa: sin recursión ni caché.

    Va guardando solo los dos últimos valores. Es la más eficiente: tiempo
    proporcional a n y memoria constante.
    Cuándo conviene: cuando solo necesitas el n-ésimo valor y n puede ser
    muy grande (sin riesgo de `RecursionError`).
    """
    def fib(n):
        anterior, actual = 0, 1
        for _ in range(n):
            anterior, actual = actual, anterior + actual
        return anterior

    print([fib(i) for i in range(11)])                      # 0, 1, 1, 2, 3, 5, 8, ...
    print(fib(30))                                          # 832040


def alternativa_3():
    """Generador: producir la serie de a un término por vez.

    Cuándo conviene: cuando necesitas VARIOS términos seguidos (los primeros
    20, o hasta superar cierto valor) y no solo uno.
    """
    def fibonacci():
        anterior, actual = 0, 1
        while True:
            yield anterior
            anterior, actual = actual, anterior + actual

    from itertools import islice
    print(list(islice(fibonacci(), 11)))                    # los primeros 11 términos


# alternativa_1()
# alternativa_2()
# alternativa_3()
