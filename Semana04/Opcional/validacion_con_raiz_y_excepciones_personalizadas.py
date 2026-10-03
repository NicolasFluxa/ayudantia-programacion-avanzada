"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
        Validaciones con `raise` y Excepciones Personalizadas (Básico)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te permitirá practicar cómo "lanzar" (raise) excepciones
cuando ciertas condiciones no se cumplen en tu código, y cómo definir
excepciones personalizadas para errores específicos de tu aplicación.

1.  Define una excepción personalizada simple llamada `SaldoInsuficienteError`
    que herede de la clase base `Exception`. Puedes dejar su cuerpo vacío (`pass`).

2.  Retoma la clase `CuentaBancaria` del ejercicio de Encapsulamiento (Semana 2)
    o una versión simplificada de ella.
    a.  En el constructor `__init__(self, titular, saldo_inicial=0)`:
        Si `saldo_inicial` es negativo, en lugar de solo imprimir una advertencia,
        lanza un `ValueError` con un mensaje descriptivo.
    b.  Modifica el método `depositar(self, cantidad)`:
        Si `cantidad` no es positiva, lanza un `ValueError`.
    c.  Modifica el método `retirar(self, cantidad)`:
        i.  Si `cantidad` no es positiva, lanza un `ValueError`.
        ii. Si `cantidad` es mayor que el saldo actual, lanza tu excepción
            personalizada `SaldoInsuficienteError`, pasándole un mensaje
            que incluya el saldo actual y el monto del intento de retiro.

3.  En el código principal (fuera de la clase):
    a.  Intenta crear una `CuentaBancaria` con saldo inicial negativo, usando
        un `try-except ValueError` para capturar y mostrar el error.
    b.  Con una cuenta válida, intenta depositar una cantidad negativa, usando
        `try-except ValueError`.
    c.  Intenta retirar una cantidad negativa, usando `try-except ValueError`.
    d.  Intenta retirar más dinero del que hay en la cuenta, usando
        `try-except SaldoInsuficienteError` para capturar tu excepción personalizada.
    e.  Realiza una operación válida de retiro y muestra el saldo.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: en vez de imprimir un aviso y seguir, la cuenta se NIEGA a hacer
una operación inválida lanzando una excepción, y quien la usa decide qué
hacer. Además se define una excepción propia para el caso «saldo insuficiente».

Al ejecutar verás cinco pruebas, cada una con su resultado:
  - crear una cuenta con saldo negativo -> `ValueError` capturado;
  - depositar -50 y retirar -20 -> `ValueError` capturado, el saldo no cambia (200.00);
  - retirar 300 (saldo + 100) -> `SaldoInsuficienteError` con el detalle de saldo y monto;
  - retirar 50 -> operación válida, saldo final 150.00.

-------------------------------------------------------------------------------
"""


# 1. Definir una excepción personalizada
class SaldoInsuficienteError(Exception):
    """Excepción para cuando se intenta retirar más saldo del disponible."""
    pass


# 2. Clase CuentaBancaria modificada
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.__titular = titular
        if saldo_inicial < 0:
            # a. Lanzar ValueError si saldo_inicial es negativo
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__saldo = float(saldo_inicial)
        print(f"Cuenta creada para {self.__titular} con saldo ${self.__saldo:.2f}")

    def obtener_saldo(self):
        return self.__saldo

    def obtener_titular(self):
        return self.__titular

    def depositar(self, cantidad):
        cantidad_float = float(cantidad)
        if cantidad_float <= 0:
            # b. Lanzar ValueError si cantidad no es positiva
            raise ValueError("La cantidad a depositar debe ser un número positivo.")
        self.__saldo += cantidad_float
        print(f"Depósito de ${cantidad_float:.2f} realizado. Nuevo saldo: ${self.__saldo:.2f}")

    def retirar(self, cantidad):
        cantidad_float = float(cantidad)
        if cantidad_float <= 0:
            # c.i. Lanzar ValueError si cantidad no es positiva
            raise ValueError("La cantidad a retirar debe ser un número positivo.")
        if cantidad_float > self.__saldo:
            # c.ii. Lanzar SaldoInsuficienteError
            mensaje_error = (f"No se puede retirar ${cantidad_float:.2f}. "
                             f"Saldo disponible: ${self.__saldo:.2f}")
            raise SaldoInsuficienteError(mensaje_error)

        self.__saldo -= cantidad_float
        print(f"Retiro de ${cantidad_float:.2f} realizado. Nuevo saldo: ${self.__saldo:.2f}")


# --- Código Principal para Probar ---
if __name__ == "__main__":
    print("--- Probando Validaciones y Excepciones en CuentaBancaria ---")

    # 3a. Intentar crear cuenta con saldo inicial negativo
    print("\nIntentando crear cuenta con saldo negativo...")
    try:
        cuenta_error = CuentaBancaria("Usuario Error", -100)
    except ValueError as e:
        print(f"Capturado Error al crear cuenta: {e}")

    # Crear una cuenta válida para las siguientes pruebas
    try:
        mi_cuenta = CuentaBancaria("Juan Valiente", 200.0)
    except ValueError as e:  # No debería ocurrir aquí
        print(f"Error inesperado al crear mi_cuenta: {e}")
        mi_cuenta = None  # Para evitar errores si la creación falla

    if mi_cuenta:
        # 3b. Intentar depositar cantidad negativa
        print("\nIntentando depositar cantidad negativa...")
        try:
            mi_cuenta.depositar(-50)
        except ValueError as e:
            print(f"Capturado Error al depositar: {e}")
        print(f"Saldo actual de {mi_cuenta.obtener_titular()}: ${mi_cuenta.obtener_saldo():.2f}")

        # 3c. Intentar retirar cantidad negativa
        print("\nIntentando retirar cantidad negativa...")
        try:
            mi_cuenta.retirar(-20)
        except ValueError as e:
            print(f"Capturado Error al retirar (cantidad negativa): {e}")
        print(f"Saldo actual: ${mi_cuenta.obtener_saldo():.2f}")

        # 3d. Intentar retirar más dinero del disponible
        print("\nIntentando retirar más dinero del disponible...")
        try:
            monto_retiro_excesivo = mi_cuenta.obtener_saldo() + 100
            print(f"(Intentando retirar ${monto_retiro_excesivo:.2f})")
            mi_cuenta.retirar(monto_retiro_excesivo)
        except SaldoInsuficienteError as e:
            print(f"Capturado Error de Saldo Insuficiente: {e}")
        except ValueError as e:  # Por si la cantidad fuera negativa por error
            print(f"Capturado ValueError en retiro excesivo: {e}")
        print(f"Saldo actual: ${mi_cuenta.obtener_saldo():.2f}")

        # 3e. Realizar una operación válida de retiro
        print("\nRealizando un retiro válido...")
        try:
            mi_cuenta.retirar(50)
        except (ValueError, SaldoInsuficienteError) as e:  # Capturar ambos por si acaso
            print(f"Error inesperado en retiro válido: {e}")
        print(f"Saldo final de {mi_cuenta.obtener_titular()}: ${mi_cuenta.obtener_saldo():.2f}")

    print("\n--- Fin de las pruebas ---")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el propósito de la sentencia `raise`? ¿Cuándo la usarías?
2.  ¿Por qué podría ser útil crear excepciones personalizadas (como
    `SaldoInsuficienteError`) en lugar de usar siempre las excepciones
    incorporadas de Python (como `ValueError` o `Exception`)?
3.  Cuando defines una excepción personalizada, ¿por qué es una buena práctica
    hacerla heredar de `Exception` (o de otra excepción más específica)?
4.  En los bloques `except`, ¿cómo puedes acceder al mensaje o a los argumentos
    con los que se lanzó la excepción (ej: `except ValueError as e:`)?
5.  Si una función puede lanzar varios tipos de excepciones personalizadas o
    incorporadas, ¿cómo puedes manejar cada una de forma diferente en el
    código que llama a esa función?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

def alternativa_1():
    """Excepción personalizada que guarda DATOS, no solo un mensaje.

    El código que captura el error puede usar `error.saldo` y `error.monto`
    (por ejemplo, para mostrar «te faltan $X») sin tener que leer el texto.
    Cuándo conviene: cuando quien captura necesita los valores para decidir.
    """
    class SaldoInsuficienteError(Exception):
        def __init__(self, saldo, monto):
            self.saldo = saldo
            self.monto = monto
            super().__init__(f"Saldo ${saldo:.2f}, se intentó retirar ${monto:.2f}")

    def retirar(saldo, monto):
        if monto > saldo:
            raise SaldoInsuficienteError(saldo, monto)
        return saldo - monto

    try:
        retirar(100, 250)
    except SaldoInsuficienteError as error:
        print(f"Te faltan ${error.monto - error.saldo:.2f}")


def alternativa_2():
    """Una excepción «raíz» de la que cuelgan todas las de la aplicación.

    Con `CuentaError` como base, se puede capturar cualquier error de la
    cuenta con un solo `except`, o ser específico si hace falta.
    Cuándo conviene: cuando hay varias excepciones propias relacionadas.
    """
    class CuentaError(Exception):
        """Base de todos los errores de la cuenta."""

    class MontoInvalidoError(CuentaError):
        pass

    class SaldoInsuficienteError(CuentaError):
        pass

    for error_a_lanzar in (MontoInvalidoError("monto negativo"), SaldoInsuficienteError("no alcanza")):
        try:
            raise error_a_lanzar
        except CuentaError as error:           # atrapa las dos
            print(f"{type(error).__name__}: {error}")


def alternativa_3():
    """Devolver un resultado (True/False) en vez de lanzar una excepción.

    Es simple, pero quien llama puede olvidar revisar el resultado y el error
    pasa desapercibido; una excepción, en cambio, obliga a tratarlo o detiene
    el programa. Además, con un booleano no se sabe POR QUÉ falló.
    Cuándo conviene: cuando «no se pudo» es un resultado normal y esperado,
    no una situación excepcional (por ejemplo, buscar algo que puede no estar).
    """
    def retirar(saldo, monto):
        if monto <= 0 or monto > saldo:
            return saldo, False
        return saldo - monto, True

    saldo, exito = retirar(200, 300)
    print(f"¿Retiro exitoso? {exito}. Saldo: {saldo}")


# alternativa_1()
# alternativa_2()
# alternativa_3()
