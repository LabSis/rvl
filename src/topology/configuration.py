#coding:utf-8
"""
Este módulo provee una clase que permite mantener un diccionario clave-valor.
"""
class Configuration():
    """
    Description:
        Esta clase representa una configuración genérica. Puede ser una
        configuración para cualquier objeto.

        Básicamente es un diccionario que mantiene una clave y un valor.

    Constructor:
        Inicializa una configuración vacía.

    Public Methods:
        del_atributo
        existe_atributo
        get_atributo
        set_atributo

    Special Methods:
        __str__
        __call__
    """
    def __init__(self):
        """
        Description:
            Inicia la configuración vacía.
        """
        self.dicc = {}

    def set_attribute(self, attribute, value):
        """
        Description:
            Establece un atributo a la configuración con su respectivo valor.

        Arguments:
            attribute -- Es el nombre del atributo.
            value -- Es el valor del atributo.
        """
        self.dicc[attribute] = value

    def get_attribute(self, attribute):
        """
        Description:
            Devuelve el valor del atributo pasado como parámetro.

        Arguments:
            atributo -- Es el nombre del atributo que se quiere obtener.

        Returns:
            El valor del atributo.

        Exceptions:
            KeyError -- La clave no existe en la configuración.
        """
        return self.dicc[attribute]

    def exists_attribute(self, attribute):
        """
        Description:
            Devuelve si el atributo existe.

        Arguments:
            attribute -- Es el nombre del atributo que se desea saber si existe.

        Returns:
            True -- Si el atributo existe.
            False -- Si el atributo no existe.

        """
        existe = True
        try:
            self.dicc[attribute]
        except KeyError:
            existe = False
        return existe

    def del_attribute(self, attribute):
        """
        Description:
            Borra un atributo de este objeto.

        Arguments:
            atributo -- Es el nombre del atributo a borrar.

        Returns:
            True -- Siempre que la clave que se pasa como parámetro existe en la
            configuración.

        Exceptions:
            KeyError -- Lanza esta excepción si la clave no existe en la
            configuración
        """
        self.dicc[attribute] = None
        return True

    def __str__(self):
        return str(self.dicc)

    def __call__(self, clave):
        """
        Exceptions:
            KeyError -- Lanza esta excepción si la clave no existe en la
            configuración
        """
        return self.dicc[clave]
