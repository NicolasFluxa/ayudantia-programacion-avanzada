"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                       Herencia con Jerarquía de Vehículos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea una jerarquía de clases para representar diferentes tipos de vehículos,
practicando la herencia y la especialización de métodos y atributos.

1.  Define una clase base `Vehiculo`:
    a.  Constructor `__init__(self, marca, modelo, anio_fabricacion)`:
        Inicializa `self.marca`, `self.modelo`, `self.anio_fabricacion`.
        También un atributo `self.encendido = False`.
    b.  Método `arrancar(self)`: Si no está encendido, lo enciende y muestra
        "[Marca Modelo] ha arrancado." Si ya está encendido, muestra que ya lo está.
    c.  Método `apagar(self)`: Si está encendido, lo apaga y muestra
        "[Marca Modelo] se ha apagado." Si ya está apagado, muestra que ya lo está.
    d.  Método `descripcion_general(self)`: Retorna un string con la marca,
        modelo y año del vehículo.

2.  Define una clase `Coche` que herede de `Vehiculo`:
    a.  Constructor `__init__(self, marca, modelo, anio_fabricacion, numero_puertas)`:
        Debe usar `super()` para inicializar los atributos de `Vehiculo` y
        luego inicializar `self.numero_puertas`.
    b.  Sobrescribe `descripcion_general(self)` para añadir el número de puertas
        a la descripción retornada por la superclase.
    c.  Añade un método `tocar_bocina(self)` que imprima "[Marca Modelo] dice: ¡Pip Pip!".

3.  Define una clase `Motocicleta` que herede de `Vehiculo`:
    a.  Constructor `__init__(self, marca, modelo, anio_fabricacion, tipo_cadena)`:
        Debe usar `super()` e inicializar `self.tipo_cadena` (ej: "Estándar", "Reforzada").
    b.  Sobrescribe `descripcion_general(self)` para añadir el tipo de cadena.
    c.  Añade un método `hacer_caballito(self)` que imprima
        "¡[Marca Modelo] está haciendo un caballito! (¡Con cuidado!)", pero
        solo si la moto está encendida (si no, avisa que no puede hacerlo).

4.  Crea instancias de `Coche` y `Motocicleta`. Prueba todos sus métodos:
    `arrancar`, `apagar`, `descripcion_general`, y los métodos específicos.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: armar una jerarquía de dos niveles (`Vehiculo` -> `Coche` y
`Motocicleta`) donde las subclases reutilizan el constructor y los métodos de
la base, y amplían la descripción con `super()`.

Al ejecutar verás para el coche y para la moto: la descripción general
(marca, modelo, año y el dato propio: puertas o tipo de cadena), cómo arrancar
y apagar cambian el estado (y avisan si ya estaba en ese estado), la bocina del
coche, y el caballito de la moto, que solo funciona con la moto encendida.

-------------------------------------------------------------------------------
"""

class Vehiculo:
    """Clase base para representar un vehículo."""
    def __init__(self, marca, modelo, anio_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
        self.encendido = False
        print(f"Vehículo creado: {self.marca} {self.modelo} ({self.anio_fabricacion})")

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"{self.marca} {self.modelo} ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya estaba apagado.")

    def descripcion_general(self):
        return f"{self.marca} {self.modelo}, Año: {self.anio_fabricacion}"


class Coche(Vehiculo):
    """Representa un coche, que es un tipo de Vehículo."""
    def __init__(self, marca, modelo, anio_fabricacion, numero_puertas):
        super().__init__(marca, modelo, anio_fabricacion)
        self.numero_puertas = numero_puertas
        print(f"  -> Es un Coche con {self.numero_puertas} puertas.")

    def descripcion_general(self):
        # Llama al método de la superclase y añade información específica
        desc_base = super().descripcion_general()
        return f"{desc_base}, Puertas: {self.numero_puertas}"

    def tocar_bocina(self):
        print(f"{self.marca} {self.modelo} dice: ¡Pip Pip!")


class Motocicleta(Vehiculo):
    """Representa una motocicleta, que es un tipo de Vehículo."""
    def __init__(self, marca, modelo, anio_fabricacion, tipo_cadena):
        super().__init__(marca, modelo, anio_fabricacion)
        self.tipo_cadena = tipo_cadena
        print(f"  -> Es una Motocicleta con cadena tipo '{self.tipo_cadena}'.")

    def descripcion_general(self):
        desc_base = super().descripcion_general()
        return f"{desc_base}, Cadena: {self.tipo_cadena}"

    def hacer_caballito(self):
        if self.encendido:
            print(f"¡{self.marca} {self.modelo} está haciendo un caballito! (¡Con cuidado!)")
        else:
            print(f"{self.marca} {self.modelo} no puede hacer un caballito si está apagada.")


print("\n--- Probando la Jerarquía de Vehículos ---")
# 4. Crear instancias y probar métodos
mi_coche = Coche("Toyota", "Corolla", 2022, 4)
mi_moto = Motocicleta("Honda", "CBR500R", 2021, "Reforzada")

print("\n--- Acciones del Coche ---")
print(mi_coche.descripcion_general())
mi_coche.arrancar()
mi_coche.tocar_bocina()
mi_coche.arrancar() # Intentar arrancar de nuevo
mi_coche.apagar()
mi_coche.apagar()   # Intentar apagar de nuevo

print("\n--- Acciones de la Motocicleta ---")
print(mi_moto.descripcion_general())
mi_moto.arrancar()
mi_moto.hacer_caballito()
mi_moto.apagar()
mi_moto.hacer_caballito() # Intentar sin estar encendida

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En las clases `Coche` y `Motocicleta`, ¿cómo se reutiliza la lógica del
    constructor de `Vehiculo` para inicializar `marca`, `modelo` y `anio_fabricacion`?
2.  Al sobrescribir `descripcion_general` en `Coche` y `Motocicleta`, ¿cómo se
    accede a la implementación original de `descripcion_general` de la clase `Vehiculo`
    para no repetir código?
3.  ¿Podrías crear una clase `Camion` que herede de `Vehiculo` y añada atributos
    como `capacidad_carga` y un método como `cargar_mercancia()`? Esboza cómo sería.
4.  ¿Qué es la "relación ES-UN" (is-a relationship) en el contexto de la herencia?
    ¿Cómo se aplica a `Coche` y `Vehiculo`?
5.  Si un método no se sobrescribe en la subclase, ¿qué versión del método se
    ejecuta cuando se llama desde un objeto de la subclase?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

from dataclasses import dataclass, field


def alternativa_1():
    """Composición: el coche TIENE un motor, en vez de heredar el encendido.

    El estado «encendido» y sus métodos viven en una clase `Motor`; `Coche` y
    `Motocicleta` la usan sin repetirla ni heredar de un `Vehiculo` común.
    Cuándo conviene: cuando una pieza se comparte entre cosas que no son del
    mismo tipo (una lancha y un generador también tienen motor).
    """
    class Motor:
        def __init__(self):
            self.encendido = False

        def arrancar(self):
            self.encendido = True
            print("Motor en marcha.")

        def apagar(self):
            self.encendido = False
            print("Motor apagado.")

    class Coche:
        def __init__(self, marca, modelo, puertas):
            self.marca = marca
            self.modelo = modelo
            self.puertas = puertas
            self.motor = Motor()                   # composición

    coche = Coche("Toyota", "Corolla", 4)
    coche.motor.arrancar()
    coche.motor.apagar()


def alternativa_2():
    """Herencia con @dataclass: menos código de constructor.

    `field(init=False)` deja `encendido` fuera del constructor (siempre parte
    en False). Cada subclase solo declara sus campos nuevos.
    Cuándo conviene: jerarquías que son sobre todo datos.
    """
    @dataclass
    class Vehiculo:
        marca: str
        modelo: str
        anio_fabricacion: int
        encendido: bool = field(default=False, init=False)

        def descripcion_general(self):
            return f"{self.marca} {self.modelo}, Año: {self.anio_fabricacion}"

    @dataclass
    class Coche(Vehiculo):
        numero_puertas: int = 4

        def descripcion_general(self):
            return f"{super().descripcion_general()}, Puertas: {self.numero_puertas}"

    print(Coche("Toyota", "Corolla", 2022, 4).descripcion_general())


def alternativa_3():
    """Mixin: una capacidad suelta que se «mezcla» en las clases que la necesitan.

    La bocina no es de todos los vehículos (la moto de la solución no la tiene),
    así que se separa en una clase pequeña y se agrega por herencia múltiple.
    Cuándo conviene: una habilidad compartida por clases que no son hermanas.
    """
    class ConBocina:
        def tocar_bocina(self):
            print(f"{self.marca} {self.modelo} dice: ¡Pip Pip!")

    class Vehiculo:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

    class Coche(Vehiculo, ConBocina):
        pass

    Coche("Toyota", "Corolla").tocar_bocina()


# alternativa_1()
# alternativa_2()
# alternativa_3()
