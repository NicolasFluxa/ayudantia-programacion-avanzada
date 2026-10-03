"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
          Clase de Configuración de Aplicación (Integrando Conceptos)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea una clase `ConfiguracionApp` que gestione la configuración de una aplicación
hipotética. Esta clase integrará propiedades, métodos de clase y estáticos.

1.  **Atributos de Instancia (manejados con propiedades):**
    a.  `_nombre_app` (string): Nombre de la aplicación.
    b.  `_version` (string): Versión actual, ej: "1.0.0".
    c.  `_modo_tema` (string): Puede ser "claro" u "oscuro". Con valor por defecto "claro".
        - Usa `@property` para un getter `modo_tema`.
        - Usa `@modo_tema.setter` para un setter que valide que el valor sea
          solo "claro" u "oscuro"; si no, lanza `ValueError`.

2.  **Atributo de Clase:**
    a.  `formatos_exportacion_soportados = ["JSON", "XML", "CSV"]` (lista de strings).

3.  **Constructor `__init__`:**
    a.  Debe aceptar `nombre_app` y `version_inicial`.
    b.  Debe inicializar `self._nombre_app`, `self._version` y `self.modo_tema`
        (usando el setter para `modo_tema` para aplicar la validación y el valor por defecto
        si no se proporciona uno explícitamente, aunque aquí lo forzaremos a "claro" inicialmente).

4.  **Método de Instancia:**
    a.  `mostrar_configuracion(self)`: Imprime todos los detalles de la configuración
        actual (nombre, versión, modo tema).

5.  **Método de Clase (`@classmethod`):**
    a.  `desde_diccionario(cls, datos_config)`:
        i.  Recibe un diccionario `datos_config` (ej: `{"app_nombre": "MiEditor",
        "app_version": "2.1.0", "modo_tema": "oscuro"}`; las claves que falten usan valores por defecto).
        ii. Crea y retorna una instancia de `ConfiguracionApp` usando los valores
            del diccionario. Si falta alguna clave, usa valores por defecto razonables.
    b.  `listar_formatos_soportados(cls)`: Imprime los formatos de exportación soportados
        accediendo al atributo de clase.

6.  **Método Estático (`@staticmethod`):**
    a.  `validar_nombre_version(version_str)`:
        i.  Recibe un string de versión.
        ii. Retorna `True` si el formato parece válido (ej: "X.Y.Z" donde X, Y, Z
            son números), `False` en caso contrario. (Implementa una validación simple).

7.  **Demostración:**
    a.  Crea una instancia de `ConfiguracionApp` usando el constructor.
    b.  Muestra su configuración. Cambia el modo tema (prueba uno válido y uno inválido).
    c.  Llama al método de clase `listar_formatos_soportados()`.
    d.  Crea otra instancia usando el método de clase `desde_diccionario()`. Muestra su config.
    e.  Usa el método estático `validar_nombre_version()` con algunos ejemplos.

## OBJETIVO Y RESULTADO ESPERADO:
## --------------------------------
Objetivo: juntar en una sola clase lo visto en la semana: propiedades con
validación, un atributo de clase compartido, un constructor alternativo
(`@classmethod`) y una utilidad que no depende del objeto (`@staticmethod`).

Al ejecutar verás:
  - la configuración de «Mi Super App» v1.0.0 en modo «claro»; luego en modo
    «oscuro»; un `ValueError` al intentar el modo «azul»;
  - la versión actualizada a 2.0.0 y un `ValueError` al intentar «beta»;
  - la lista de formatos soportados (JSON, XML, CSV);
  - dos aplicaciones creadas desde un diccionario: «Editor Pro» 3.5.2 en modo
    oscuro, y «Utilidad Simple» con la versión por defecto 0.1.0;
  - una tabla con seis versiones y si son válidas (solo las del tipo «X.Y.Z»).

-------------------------------------------------------------------------------
"""
import re  # Para validación de versión un poco más robusta (opcional)


class ConfiguracionApp:
    """Gestiona la configuración de una aplicación."""

    # 2a. Atributo de Clase
    formatos_exportacion_soportados = ["JSON", "XML", "CSV"]
    MODOS_TEMA_VALIDOS = ["claro", "oscuro"]

    def __init__(self, nombre_app, version_inicial):
        # 3. Constructor
        self._nombre_app = nombre_app

        if ConfiguracionApp.validar_nombre_version(version_inicial):
            self._version = version_inicial
        else:
            print(f"Advertencia: Formato de versión '{version_inicial}' inválido. Usando '1.0.0'.")
            self._version = "1.0.0"

        self.modo_tema = "claro"  # Llama al setter para modo_tema
        print(f"Configuración para '{self._nombre_app}' v{self._version} inicializada.")

    @property
    def nombre_app(self):
        return self._nombre_app

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, nueva_version):
        if ConfiguracionApp.validar_nombre_version(nueva_version):
            self._version = nueva_version
            print(f"Versión de la app actualizada a: {self._version}")
        else:
            raise ValueError(f"Formato de versión '{nueva_version}' inválido. Use 'X.Y.Z'.")

    @property
    def modo_tema(self):
        """Getter para el modo_tema."""
        return self._modo_tema

    @modo_tema.setter
    def modo_tema(self, nuevo_modo):
        """Setter para modo_tema con validación."""
        if nuevo_modo.lower() in self.MODOS_TEMA_VALIDOS:
            self._modo_tema = nuevo_modo.lower()
            print(f"Modo tema establecido a: '{self._modo_tema}'")
        else:
            raise ValueError(f"Modo tema '{nuevo_modo}' inválido. Permitidos: {self.MODOS_TEMA_VALIDOS}")

    # 4a. Método de Instancia
    def mostrar_configuracion(self):
        """Imprime la configuración actual de la aplicación."""
        print("\n--- Configuración Actual de la Aplicación ---")
        print(f"  Nombre App: {self.nombre_app}")  # Usa el getter
        print(f"  Versión   : {self.version}")  # Usa el getter
        print(f"  Modo Tema : {self.modo_tema}")  # Usa el getter
        print("-------------------------------------------")

    # 5a. Método de Clase (constructor alternativo)
    @classmethod
    def desde_diccionario(cls, datos_config):
        """Crea una instancia de ConfiguracionApp desde un diccionario."""
        nombre = datos_config.get("app_nombre", "AppDesconocida")  # Valor por defecto si no está
        ver = datos_config.get("app_version", "0.1.0")  # Valor por defecto si no está
        print(f"\nCreando instancia desde diccionario: Nombre='{nombre}', Versión='{ver}'")
        instancia = cls(nombre, ver)  # Llama al __init__ de la clase (ConfiguracionApp)

        # Opcional: configurar otros atributos si están en el diccionario
        if "modo_tema" in datos_config:
            try:
                instancia.modo_tema = datos_config["modo_tema"]  # Usa el setter
            except ValueError as e:
                print(f"Advertencia al cargar desde dict: {e}. Se mantiene el modo por defecto.")
        return instancia

    # 5b. Método de Clase para acceder a atributos de clase
    @classmethod
    def listar_formatos_soportados(cls):
        """Imprime los formatos de exportación soportados."""
        print("\n--- Formatos de Exportación Soportados ---")
        for formato in cls.formatos_exportacion_soportados:
            print(f"  - {formato}")
        print("------------------------------------------")

    # 6a. Método Estático
    @staticmethod
    def validar_nombre_version(version_str):
        """
        Valida si un string de versión tiene un formato simple como "X.Y.Z".
        (Validación simple, puede ser mejorada con regex más complejos).
        """
        if not isinstance(version_str, str):
            return False
        partes = version_str.split('.')
        if len(partes) != 3:
            return False
        for parte in partes:
            if not parte.isdigit():
                return False
        return True
        # Alternativa con regex más robusto:
        # pattern = r"^\d+\.\d+\.\d+$" # Ej: 1.0.0, 10.23.4
        # return bool(re.match(pattern, version_str))


# --- 7. Demostración ---
print("--- Demo de ConfiguracionApp ---")

# 7a. Crear instancia con constructor
config1 = ConfiguracionApp("Mi Super App", "1.0.0")

# 7b. Mostrar y cambiar configuración
config1.mostrar_configuracion()
try:
    config1.modo_tema = "oscuro"
    config1.mostrar_configuracion()
    print("\nIntentando modo tema inválido 'azul':")
    config1.modo_tema = "azul"  # Esto lanzará ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    print("\nIntentando actualizar versión a '2.0.0':")
    config1.version = "2.0.0"
    config1.mostrar_configuracion()
    print("\nIntentando actualizar versión a 'beta':")
    config1.version = "beta"  # Esto lanzará ValueError
except ValueError as e:
    print(f"Error: {e}")

# 7c. Listar formatos soportados (método de clase)
ConfiguracionApp.listar_formatos_soportados()

# 7d. Crear instancia desde diccionario (método de clase)
datos = {"app_nombre": "Editor Pro", "app_version": "3.5.2", "modo_tema": "oscuro"}
config2 = ConfiguracionApp.desde_diccionario(datos)
config2.mostrar_configuracion()

datos_incompletos = {"app_nombre": "Utilidad Simple"}
config3 = ConfiguracionApp.desde_diccionario(datos_incompletos)
config3.mostrar_configuracion()

# 7e. Usar método estático
print("\n--- Validación de Versiones (Método Estático) ---")
versiones_a_probar = ["1.0.0", "2.10.3", "1.2", "alpha", "1.b.3", "10.20.30"]
for v_str in versiones_a_probar:
    es_valida = ConfiguracionApp.validar_nombre_version(v_str)
    print(f"Versión '{v_str}' es válida? {es_valida}")
print("-----------------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En la clase `ConfiguracionApp`, `formatos_exportacion_soportados` es un atributo
    de clase. ¿Cómo se accede a él desde un método de clase (`listar_formatos_soportados`)
    y cómo se accedería desde un método de instancia?
2.  El método `desde_diccionario` es un `@classmethod`. ¿Por qué es útil que reciba
    `cls` como primer argumento en lugar de `self`? ¿Qué le permite hacer `cls`?
3.  El método `validar_nombre_version` es un `@staticmethod`. ¿Por qué no necesita
    acceso a `self` (la instancia) ni a `cls` (la clase)? ¿Podría esta función
    existir fuera de la clase y cumplir el mismo propósito? ¿Cuál es la ventaja
    de agruparla dentro de la clase como un método estático?
4.  Explica cómo la propiedad `modo_tema` (con su getter y setter) permite
    controlar los valores que se pueden asignar a `self._modo_tema`.
5.  Si quisieras añadir una nueva configuración, por ejemplo, `idioma_app` con
    valores permitidos "es" (español) e "en" (inglés) y un valor por defecto "es",
    ¿cómo modificarías la clase (constructor, propiedades) para incluirla?
-------------------------------------------------------------------------------
"""


# =============================================================================
# OTRAS FORMAS DE HACERLO
# =============================================================================
# Las funciones de abajo logran lo mismo que la solución de arriba, pero con
# otra técnica. NO se ejecutan solas: al final hay llamadas comentadas; quita
# el «#» de la que quieras probar. Cada una indica cuándo conviene usarla.

import re
from dataclasses import dataclass
from enum import Enum


def alternativa_1():
    """`Enum` para el modo de tema, en vez de una lista de textos.

    Con una lista, «claro» y «claroo» son ambos textos: el error aparece al
    validar. Con un `Enum`, los valores válidos son un conjunto cerrado y el
    editor ayuda a escribirlos (`Tema.OSCURO`).
    Cuándo conviene: cuando hay un conjunto fijo de opciones que se usa en
    varios lugares del programa.
    """
    class Tema(Enum):
        CLARO = "claro"
        OSCURO = "oscuro"

    tema = Tema("oscuro")                                   # convierte desde el texto
    print(tema, tema.value)
    try:
        Tema("azul")
    except ValueError as error:
        print(f"Error: {error}")


def alternativa_2():
    """Validar la versión con una expresión regular.

    La solución usa `split` + `isdigit`. Con `re.fullmatch` queda en una línea
    y el patrón dice exactamente qué se acepta. Se usa [0-9] porque `isdigit`
    y el atajo de dígitos de las regex también aceptan dígitos de otros alfabetos.
    Cuándo conviene: formatos con reglas más complejas (versiones tipo
    «1.2.3-beta»); para algo tan simple las dos formas sirven.
    """
    def version_valida(texto):
        return isinstance(texto, str) and re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", texto) is not None

    for v in ("1.0.0", "2.10.3", "1.2", "alpha", "1.b.3"):
        print(f"{v!r}: {version_valida(v)}")


def alternativa_3():
    """@dataclass para guardar la configuración y `**` para crearla desde un dict.

    Si los campos del dataclass coinciden con las claves del diccionario,
    `Configuracion(**datos)` reemplaza al método `desde_diccionario`. Los valores
    por defecto salen de los campos con `=`.
    Cuándo conviene: configuración sencilla y con claves conocidas. Si las
    claves del diccionario no coinciden con los campos, o necesitas
    transformar datos, el `@classmethod` da más control.
    """
    @dataclass
    class Configuracion:
        app_nombre: str = "AppDesconocida"
        app_version: str = "0.1.0"
        modo_tema: str = "claro"

    datos = {"app_nombre": "Editor Pro", "app_version": "3.5.2"}
    print(Configuracion(**datos))
    print(Configuracion())                                  # todo por defecto


# alternativa_1()
# alternativa_2()
# alternativa_3()
