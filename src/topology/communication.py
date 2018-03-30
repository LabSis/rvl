#coding:utf-8
"""
Módulo de comunicacion el cual contiene la clase Comunicacion junto a todos
los elementos de Comunicacion: UMLSwitch, etc.

Version:
    1.01

Unit Tests:
    Approved 100 % -- El archivo para probar es test_comunicacion.py

Author:
    Parisi Germán
"""
import copy

class Comunication():
    """
    Description:
        Esta clase representa una comunicacion a un dispositivo o bien a otro
        elemento de comunicación. Esto último podría ser switch con switch.

    Constructor:
        Inicializa la comunicación con un nombre lógico, un nombre, una
        configuración y un tipo de comunicación.

    Public Methods:
        get_nombre_logico
        get_nombre
        get_configuracion
        get_tipo
        get_cantidad_conexiones
        get_conexiones
        set_nombre
        set_configuracion
        agregar_conexion
        eliminar_conexion

    Private Methods:
    _configurar -- Realiza la configuración de la comunicación.

    Special Methods:
        __cmp__
        __hash__
        __str__

    """
    def __init__(self, nombre_logico, nombre, configuracion, oculto=False,
                                            tipo=Const.ETQ_CANVAS_UML_SWITCH):
        """
        Arguments:
            nombre_logico -- Es el nombre lógico de la comunicación. Este nombre
            no acepta espacios. Si llegara a tener algún espacio lo reemplaza
            por "_".
            nombre -- Es el nombre de la comunicación.
            configuracion -- Es la configuración de la comunicación. Esta
            configuración debe ser un objeto de la clase Configuracion.
            tipo -- Es el tipo de comunicación. Por defecto, el tipo de
            dispositivo es un switch. Los diferentes tipos se declaran como
            constantes de este módulo.

        Exceptions:
            AttributeError -- El nombre lógico no puede ser nulo
            AttributeError -- La configuracion no puede ser nula
            AttributeError -- El tipo no puede ser nulo
        """
        if nombre_logico is None:
            raise AttributeError("El nombre lógico no puede ser nulo")
        if tipo is None:
            raise AttributeError("El tipo no puede ser nulo")
        self.nombre_logico = nombre_logico.replace(" ", "_")
        self.nombre = nombre
        self.configuracion = configuracion
        self.tipo = tipo
        self.oculto = oculto
        self.conexiones = []
        self._configurar()

    def agregar_conexion(self, otro):
        """
        Description:
            Agrega una conexión a la comunicación.

        Arguments:
            otro -- Es el otro elemento de conexión, el cual puede ser un
            dispositivo o una comunicación.

        Exceptions:
            AttributeError -- El otro elemento no puede ser nulo.
        """
        if otro is None:
            raise AttributeError("El otro elemento no puede ser nulo")
        self.conexiones.append(otro)

    def eliminar_conexion(self, otro):
        """
        Description:
            Elimina una conexion a la comunicación.

        Arguments:
            otro -- Es el otro elemento de conexión.

        Preconditions:
            El otro elemento no puede ser nulo.
        """
        assert otro is not None
        self.conexiones.remove(otro)

    def get_cantidad_conexiones(self):
        """
        Description:
            Retorna la cantidad de conexiones.
        """
        return len(self.conexiones)

    def get_conexiones(self):
        """
        Description:
            Retorna las conexiones a las cuales está conectado.

        """
        return self.conexiones

    def get_configuracion(self):
        """
        Description:
            Devuelve la configuración del dispositivo.
        """
        return self.configuracion

    def get_tipo(self):
        """
        Description:
            Retorna el nombre del tipo de la comunicación.
        """
        return self.tipo

    def get_nombre_logico(self):
        """
        Description:
            Devuelve el nombre lógico de la comunicación.
        """
        return self.nombre_logico

    def get_nombre(self):
        """
        Description:
            Devuelve el nombre de la comunicación.
        """
        return self.nombre

    def is_oculto(self):
        return self.oculto

    def set_nombre(self, nombre):
        """
        Description:
            Establece el nombre de la comunicación. Acepta cualquier caracter.
        """
        self.nombre = nombre

    def set_configuracion(self, configuracion):
        """
        Description:
            Cambia la configuración de la comunicación.
        """
        self.configuracion = configuracion
        self._configurar()

    def __cmp__(self, otro):
        if self.nombre_logico == otro.nombre_logico:
            return 0
        elif self.nombre_logico < otro.nombre_logico:
            return -1
        else:
            return 1

    def __hash__(self):
        return hash(self.nombre_logico)

    def __str__(self):
        return self.nombre_logico

    def _configurar(self):
        """
        Description:
            Configura la comunicación.
        """
        pass


class UMLSwitch(Comunicacion):
    def __init__(self, nombre_logico, nombre, configuracion=None, oculto=False):
        if configuracion is None:
            configuracion = conf.Configuracion()
            configuracion.set_atributo("hidden", "no")
        Comunicacion.__init__(self, nombre_logico, nombre, configuracion,
                                            oculto, Const.ETQ_CANVAS_UML_SWITCH)
        # Propiedades de TAP por el momento están acá. Ver bien.
        self.tiene_tap = False
        self.nombre_tap = None

    def get_nombre_tap(self):
        return self.nombre_tap

    def get_tiene_tap(self):
        return self.tiene_tap

    def set_nombre_tap(self, nombre_tap):
        self.nombre_tap = nombre_tap

    def set_tiene_tap(self, tiene_tap):
        self.tiene_tap = tiene_tap

    def __copy__(self):
        uml_switch = UMLSwitch(self.nombre_logico, self.nombre,
                                                            self.configuracion)
        return uml_switch


class UMLInternet(Comunicacion):

    def __init__(self, nombre_logico, nombre, configuracion=None):
        if configuracion is None:
            configuracion = conf.Configuracion()
            configuracion.set_atributo("hidden", "no")
        Comunicacion.__init__(self, nombre_logico, nombre, configuracion,
                                        False, Const.ETQ_CANVAS_UML_INTERNET)

    def __copy__(self):
        uml_internet = UMLInternet(self.nombre_logico, self.nombre,
                                                            self.configuracion)
        return uml_internet
