"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                 Encapsulamiento Básico con Cuenta Bancaria
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio introduce el concepto de encapsulamiento, utilizando una clase
`CuentaBancaria` para gestionar un saldo de forma controlada.

1.  Define una clase llamada `CuentaBancaria`.
2.  En el constructor `__init__(self, titular, saldo_inicial=0)`:
    a.  Inicializa un atributo de instancia "privado" para el titular (ej: `self.__titular`).
    b.  Inicializa un atributo de instancia "privado" para el saldo (ej: `self.__saldo`).
        Valida que el saldo inicial no sea negativo; si lo es, asígnalo a 0 e
        imprime una advertencia.
3.  Define un método público `depositar(self, cantidad)`:
    a.  Debe aceptar una `cantidad` positiva a depositar.
    b.  Si la cantidad es positiva, la añade al saldo. Imprime un mensaje de éxito.
    c.  Si la cantidad no es positiva, imprime un mensaje de error.
4.  Define un método público `retirar(self, cantidad)`:
    a.  Debe aceptar una `cantidad` positiva a retirar.
    b.  Si la cantidad es positiva Y hay saldo suficiente, la resta del saldo.
        Imprime un mensaje de éxito.
    c.  Si la cantidad no es positiva, imprime un mensaje de error.
    d.  Si no hay saldo suficiente, imprime un mensaje de fondos insuficientes.
5.  Define un método público `obtener_saldo(self)`:
    a.  Debe retornar el valor del saldo "privado".
6.  Define un método público `obtener_titular(self)`:
    a. Debe retornar el valor del titular "privado".
7.  Crea un objeto de `CuentaBancaria`. Intenta acceder directamente al atributo
    `__saldo` desde fuera de la clase (ej: `mi_cuenta.__saldo`). ¿Qué sucede?
8.  Realiza depósitos y retiros utilizando los métodos. Imprime el saldo
    usando `obtener_saldo()` después de cada operación.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: proteger el saldo para que solo cambie a través de `depositar` y
`retirar`, que validan cada operación.

Al ejecutar verás:
  - la cuenta de Ana (saldo 500.00) y la de Luis (se avisa que el saldo inicial
    negativo se corrigió a 0.00);
  - un `AttributeError` al intentar leer `cuenta_ana.__saldo` desde fuera (es
    lo esperado: Python renombra el atributo internamente, «name mangling»);
  - las operaciones de Ana: depósito de 200 (saldo 700), un depósito inválido,
    retiro de 100 (saldo 600), un retiro mayor al saldo (rechazado) y un retiro
    inválido; saldo final 600.00;
  - un depósito de 150 en la cuenta de Luis, que termina con 150.00.

-------------------------------------------------------------------------------
"""

class CuentaBancaria:
    """Representa una cuenta bancaria con operaciones básicas y encapsulamiento."""

    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            titular (str): El nombre del titular de la cuenta.
            saldo_inicial (float or int): El saldo inicial de la cuenta.
        """
        self.__titular = titular # Atributo "privado" para el titular

        if saldo_inicial >= 0:
            self.__saldo = float(saldo_inicial) # Atributo "privado" para el saldo
        else:
            self.__saldo = 0.0
            print(f"Advertencia para {self.__titular}: El saldo inicial no puede ser negativo. Se ha establecido en 0.")
        print(f"Cuenta creada para {self.__titular} con saldo inicial de ${self.__saldo:.2f}")

    def depositar(self, cantidad):
        """Deposita una cantidad en la cuenta."""
        if cantidad > 0:
            self.__saldo += float(cantidad)
            print(f"Depósito de ${float(cantidad):.2f} realizado. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("Error: La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta si hay fondos suficientes."""
        cantidad_float = float(cantidad)
        if cantidad_float <= 0:
            print("Error: La cantidad a retirar debe ser positiva.")
        elif cantidad_float > self.__saldo:
            print(f"Error: Fondos insuficientes. Saldo actual: ${self.__saldo:.2f}, intento de retiro: ${cantidad_float:.2f}")
        else:
            self.__saldo -= cantidad_float
            print(f"Retiro de ${cantidad_float:.2f} realizado. Nuevo saldo: ${self.__saldo:.2f}")

    def obtener_saldo(self):
        """Retorna el saldo actual de la cuenta."""
        return self.__saldo

    def obtener_titular(self):
        """Retorna el titular de la cuenta."""
        return self.__titular

print("--- Creando y Operando con CuentaBancaria ---")
# 7. Crear objeto e intentar acceder a atributos "privados"
cuenta_ana = CuentaBancaria("Ana Contreras", 500)
cuenta_luis = CuentaBancaria("Luis Soto", -100) # Probará la validación del saldo inicial

print(f"\nTitular de la cuenta de Ana: {cuenta_ana.obtener_titular()}")
print(f"Saldo inicial de Ana: ${cuenta_ana.obtener_saldo():.2f}")

print("\nIntentando acceder directamente a __saldo (esto generará un AttributeError):")
try:
    print(cuenta_ana.__saldo)
except AttributeError as e:
    print(f"Error al intentar acceder a __saldo: {e}")
    print("Esto demuestra el 'name mangling' de Python para atributos con doble guion bajo.")

print("\n--- Operaciones para la cuenta de Ana ---")
# 8. Realizar depósitos y retiros
cuenta_ana.depositar(200)
cuenta_ana.depositar(-50) # Intento de depósito inválido
cuenta_ana.retirar(100)
cuenta_ana.retirar(700) # Intento de retiro con fondos insuficientes
cuenta_ana.retirar(-30) # Intento de retiro inválido
print(f"Saldo final de Ana: ${cuenta_ana.obtener_saldo():.2f}")

print("\n--- Operaciones para la cuenta de Luis ---")
print(f"Saldo actual de Luis: ${cuenta_luis.obtener_saldo():.2f}")
cuenta_luis.depositar(150)
print(f"Saldo final de Luis: ${cuenta_luis.obtener_saldo():.2f}")


"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué significa "encapsulamiento" en POO? ¿Por qué es útil?
2.  En Python, ¿qué indica el uso de un doble guion bajo (`__`) al inicio del
    nombre de un atributo (ej: `__saldo`)? ¿Lo hace verdaderamente privado?
    (Investiga "name mangling" o "decoración de nombres").
3.  ¿Qué son los métodos "getter" (como `obtener_saldo`) y "setter"?
    ¿Por qué se utilizan en lugar de acceder directamente a los atributos?
    (Este ejemplo no tiene un setter explícito para el saldo, ¿por qué podría ser una decisión de diseño?)
4.  Si quisieras permitir cambiar el titular de la cuenta después de su creación,
    ¿cómo implementarías un método `set_titular(self, nuevo_titular)`?
5.  ¿Por qué es importante validar las entradas (como `cantidad`) en los métodos
    `depositar` y `retirar`?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

def alternativa_1():
    """@property de solo lectura con un atributo «protegido» (un guion bajo).

    En Python la privacidad es una convención: `_saldo` significa «no lo toques
    desde fuera». Con `@property` el saldo se LEE como un atributo normal
    (`cuenta.saldo`) pero no se puede asignar (`cuenta.saldo = 5` da error).
    Cuándo conviene: es la forma más habitual en Python; reemplaza a los
    getters `obtener_*`. Se ve en profundidad en la Semana 6.
    """
    class CuentaBancaria:
        def __init__(self, titular, saldo_inicial=0):
            self._titular = titular
            self._saldo = max(float(saldo_inicial), 0.0)

        @property
        def saldo(self):
            return self._saldo

        @property
        def titular(self):
            return self._titular

        def depositar(self, cantidad):
            if cantidad > 0:
                self._saldo += cantidad

    cuenta = CuentaBancaria("Ana Contreras", 500)
    cuenta.depositar(200)
    print(cuenta.titular, cuenta.saldo)      # sin paréntesis
    try:
        cuenta.saldo = 1_000_000             # no hay setter: no se puede
    except AttributeError as error:
        print(f"Error esperado: {error}")


def alternativa_2():
    """Errores con excepciones en vez de mensajes impresos.

    La solución principal imprime «Error: ...» y sigue. Quien llama no se
    entera de que falló. Con excepciones propias el fallo no puede ignorarse
    por accidente (adelanto de la Semana 4).
    Cuándo conviene: cuando la cuenta se usa desde otro código (una ventana,
    una API) que debe reaccionar al error y no solo mostrarlo por consola.
    """
    class FondosInsuficientes(Exception):
        pass

    class CuentaBancaria:
        def __init__(self, titular, saldo_inicial=0):
            self.__titular = titular
            self.__saldo = float(saldo_inicial)

        def retirar(self, cantidad):
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if cantidad > self.__saldo:
                raise FondosInsuficientes(f"Saldo {self.__saldo:.2f}, pedido {cantidad:.2f}")
            self.__saldo -= cantidad

        def obtener_saldo(self):
            return self.__saldo

    cuenta = CuentaBancaria("Luis Soto", 100)
    for monto in (30, 500, -5):
        try:
            cuenta.retirar(monto)
            print(f"Retiro de {monto} exitoso. Saldo: {cuenta.obtener_saldo():.2f}")
        except (ValueError, FondosInsuficientes) as error:
            print(f"No se pudo retirar {monto}: {error}")


# alternativa_1()
# alternativa_2()
