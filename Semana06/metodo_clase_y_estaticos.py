"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                      Métodos de Clase y Métodos Estáticos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Además de los métodos de instancia (que operan sobre un objeto específico y
reciben `self`), las clases pueden tener métodos de clase (que operan sobre la
clase misma y reciben `cls`) y métodos estáticos (que no operan ni sobre la
instancia ni sobre la clase, son como funciones normales agrupadas en la clase).

1.  **Métodos Estáticos (`@staticmethod`):**
    a.  Define una clase `GeometriaUtils`.
    b.  Dentro de ella, define un método estático `es_triangulo_valido(lado1, lado2, lado3)`
        que reciba las longitudes de tres lados y retorne `True` si pueden formar
        un triángulo (la suma de dos lados cualesquiera debe ser mayor que el tercero),
        y `False` en caso contrario. Este método no necesita `self` ni `cls`.
    c.  Llama a este método directamente desde la clase:
        `GeometriaUtils.es_triangulo_valido(3, 4, 5)` y con otros ejemplos.

2.  **Métodos de Clase (`@classmethod`):**
    a.  Define una clase `Producto`.
    b.  Añade un atributo de CLASE `contador_productos_creados = 0`.
    c.  En el `__init__(self, nombre, precio)`:
        i.  Inicializa `self.nombre` y `self.precio`.
        ii. Incrementa `Producto.contador_productos_creados` (o `cls.contador_productos_creados`
            si se accediera desde un método de clase, pero aquí en `__init__` es más directo
            con el nombre de la clase).
    d.  Define un método de clase `obtener_total_productos(cls)`:
        i.  Debe usar el decorador `@classmethod`.
        ii. Debe recibir `cls` como primer parámetro.
        iii.Debe retornar el valor de `cls.contador_productos_creados`.
    e.  Define otro método de clase `crear_producto_oferta(cls, nombre, precio_original, descuento_porc)`:
        i.  Calcule el precio con descuento.
        ii. Retorne una NUEVA instancia de la clase `Producto` (usando `cls(...)`)
            con el nombre y el precio con descuento.
    f.  Crea varias instancias de `Producto`.
    g.  Llama a `Producto.obtener_total_productos()` para ver el contador.
    h.  Crea un producto usando `Producto.crear_producto_oferta()` y verifica sus datos.
        Verifica nuevamente el total de productos.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: distinguir los tres tipos de método según lo que necesitan:
  - de instancia (`self`): trabajan con los datos de UN objeto;
  - de clase (`cls`): trabajan con la clase (su contador, o crean objetos);
  - estáticos (nada): son funciones sueltas que se agrupan en la clase por orden.

Al ejecutar verás:
  - cuatro pruebas de `es_triangulo_valido` (3,4,5 -> True; 1,2,5 -> False;
    7,10,5 -> True; 1,1,-1 -> False);
  - la creación de tres productos y «Total de productos creados: 3»;
  - un producto en oferta (Monitor Curvo con 15 % de descuento = $255.00) y
    el total actualizado a 4.

-------------------------------------------------------------------------------
"""


# 1. Métodos Estáticos
class GeometriaUtils:
    """Clase con utilidades geométricas como métodos estáticos."""

    @staticmethod
    def es_triangulo_valido(lado1, lado2, lado3):
        """
        Verifica si tres longitudes pueden formar un triángulo.
        No necesita acceso a la instancia (self) ni a la clase (cls).
        """
        # Validar que los lados sean positivos
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            return False
        # Condición del triángulo: la suma de dos lados debe ser mayor que el tercero
        return (lado1 + lado2 > lado3) and \
            (lado1 + lado3 > lado2) and \
            (lado2 + lado3 > lado1)


print("--- Probando Métodos Estáticos (GeometriaUtils) ---")
print(f"¿Pueden 3, 4, 5 formar un triángulo? {GeometriaUtils.es_triangulo_valido(3, 4, 5)}")  # True
print(f"¿Pueden 1, 2, 5 formar un triángulo? {GeometriaUtils.es_triangulo_valido(1, 2, 5)}")  # False
print(f"¿Pueden 7, 10, 5 formar un triángulo? {GeometriaUtils.es_triangulo_valido(7, 10, 5)}")  # True
print(f"¿Pueden 1, 1, -1 formar un triángulo? {GeometriaUtils.es_triangulo_valido(1, 1, -1)}")  # False
print("-------------------------------------------------")


# 2. Métodos de Clase
class Producto:
    """Representa un producto y lleva un conteo de cuántos se han creado."""
    # b. Atributo de clase
    contador_productos_creados = 0

    def __init__(self, nombre, precio):
        # c.i. Inicializar atributos de instancia
        self.nombre = nombre
        self.precio = float(precio)
        # c.ii. Incrementar el contador de clase
        Producto.contador_productos_creados += 1
        # Alternativamente, si estuviéramos en un método de clase, usaríamos cls.contador_productos_creados
        print(f"Producto '{self.nombre}' creado. Precio: ${self.precio:.2f}")

    def __str__(self):  # Para una mejor representación al imprimir el objeto
        return f"Producto(Nombre: '{self.nombre}', Precio: ${self.precio:.2f})"

    # d. Método de clase para obtener el total
    @classmethod
    def obtener_total_productos(cls):
        """Retorna el número total de instancias de Producto creadas."""
        # 'cls' se refiere a la clase Producto misma
        return cls.contador_productos_creados

    # e. Método de clase como "constructor alternativo" o "fábrica"
    @classmethod
    def crear_producto_oferta(cls, nombre, precio_original, descuento_porc):
        """
        Crea una instancia de Producto con un precio de oferta.
        'cls' permite llamar al constructor de la clase (cls(...) es como Producto(...)).
        """
        if not (0 < descuento_porc < 100):
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100 (no inclusivos).")

        precio_con_descuento = precio_original * (1 - (descuento_porc / 100))
        print(f"Creando producto en oferta '{nombre}' con {descuento_porc}% de descuento...")
        return cls(nombre, precio_con_descuento)  # Llama a Producto(nombre, precio_con_descuento)


print("\n--- Probando Métodos de Clase (Producto) ---")
# f. Crear instancias de Producto
p1 = Producto("Laptop Pro", 1200.00)
p2 = Producto("Mouse Gamer", 45.50)
p3 = Producto("Teclado Ergonómico", 89.99)

# g. Obtener el total de productos creados
total = Producto.obtener_total_productos()
print(f"\nTotal de productos creados hasta ahora: {total}")  # Debería ser 3

# h. Crear un producto usando el método de clase "fábrica"
try:
    producto_oferta = Producto.crear_producto_oferta("Monitor Curvo", 300.00, 15)  # 15% de descuento
    print(f"Producto en oferta creado: {producto_oferta}")
except ValueError as e:
    print(f"Error creando producto en oferta: {e}")

# Verificar el contador de nuevo
total_actualizado = Producto.obtener_total_productos()
print(f"Total de productos creados después de la oferta: {total_actualizado}")  # Debería ser 4

# También se puede llamar al método de clase desde una instancia,
# aunque es más común llamarlo desde la clase.
# 'cls' seguirá siendo la clase Producto.
# print(f"Total llamado desde instancia p1: {p1.obtener_total_productos()}")

print("------------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la diferencia principal entre un método de instancia, un método de
    clase y un método estático en términos de lo que reciben como primer
    argumento implícito (`self`, `cls`, o ninguno)?
2.  ¿Cuándo usarías un `@staticmethod`? Da un ejemplo de una utilidad que
    podría ser un método estático en una clase.
3.  ¿Cuándo usarías un `@classmethod`? El ejemplo de `crear_producto_oferta`
    es un "constructor alternativo" o "método de fábrica". ¿Qué ventajas ofrece esto?
4.  En `Producto`, el atributo `contador_productos_creados` es un atributo de clase.
    ¿Qué significa esto? ¿Comparten todas las instancias de `Producto` este mismo
    contador, o cada una tiene el suyo?
5.  ¿Se puede llamar a un método estático desde una instancia de la clase
    (ej: `mi_objeto.metodo_estatico()`)? ¿Y a un método de clase?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

from dataclasses import dataclass
from itertools import count


def alternativa_1():
    """Función suelta en el módulo, en lugar de un @staticmethod.

    El método estático no usa `self` ni `cls`, así que es una función normal
    metida en una clase. En Python se puede dejar suelta, sin la clase.
    Cuándo conviene: la mayoría de las veces (es más simple de importar y
    usar). El método estático conviene cuando la utilidad pertenece
    claramente a una clase y quieres encontrarla ahí (`GeometriaUtils.xxx`).
    """
    def es_triangulo_valido(a, b, c):
        return min(a, b, c) > 0 and a + b > c and a + c > b and b + c > a

    print(es_triangulo_valido(3, 4, 5))                     # True
    print(es_triangulo_valido(1, 2, 5))                     # False


def alternativa_2():
    """Función fábrica externa en lugar de @classmethod (y por qué pierde).

    Funciona, pero `crear_oferta` está atada a `Producto`. Con una subclase
    devuelve el tipo equivocado; el `@classmethod` usa `cls` y siempre
    devuelve la clase desde la que se llamó.
    Cuándo conviene: la función externa solo si nunca habrá subclases;
    el `@classmethod` es mejor cuando la clase puede heredarse.
    """
    class Producto:
        def __init__(self, nombre, precio):
            self.nombre, self.precio = nombre, precio

        @classmethod
        def oferta_con_classmethod(cls, nombre, precio, descuento):
            return cls(nombre, precio * (1 - descuento / 100))

    class ProductoPerecible(Producto):
        pass

    def crear_oferta(nombre, precio, descuento):
        return Producto(nombre, precio * (1 - descuento / 100))

    print(type(ProductoPerecible.oferta_con_classmethod("Leche", 1000, 10)).__name__)  # ProductoPerecible
    print(type(crear_oferta("Leche", 1000, 10)).__name__)                               # Producto (¡no es el que querías!)


def alternativa_3():
    """Contador con `itertools.count` y `@dataclass`.

    En vez de un entero que se incrementa a mano, `count()` entrega 1, 2, 3...
    cada vez que se le pide el siguiente valor; así cada producto recibe además
    un identificador único.
    Cuándo conviene: cuando necesitas ids únicos, no solo contar cuántos hay.
    """
    @dataclass
    class Producto:
        nombre: str
        precio: float
        _ids = count(1)                                     # sin anotación: es atributo de CLASE

        def __post_init__(self):
            self.id = next(Producto._ids)

    p1, p2 = Producto("Laptop Pro", 1200), Producto("Mouse Gamer", 45.5)
    print(p1.id, p2.id)                                     # 1 2


# alternativa_1()
# alternativa_2()
# alternativa_3()
