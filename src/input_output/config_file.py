# coding: utf-8
"""
Módulo conteniendo la clase ConfigFile la cual es responsable para leer
la configuración del archivo general del simulador.

"""

import os
import configparser

separador = os.sep

RUTA_ARCHIVO_PROP_INI = "configuracion%sprop.ini" % (separador)


class ConfigFile(object):
    """
    Description:
        Esta clase permite leer el archivo de configuración general del
        simulador, el cual define las propiedades de la interfaz gráfica
        con el usuario, entre otras.

        Esta clase no realiza una validación sobre si el archivo está bien o
        mal formado. Simplemente devuelve propiedades dejando al llamador la
        responsabilidad de actuar cuando el archivo está mal formado.

        Clase que implementa el patrón Singleton.
    """
    instance = None

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, path=None):
        if path is None:
            self.path = 'configuracion/prop.ini'
        else:
            self.path = path
        try:
            self.parser = configparser.ConfigParser()
            self.parser.read(self.path)
        except Exception:
            raise

    def get_value(self, key, section='DEFAULT'):
        """
        Description:
            Retorna el valor de la clave y sección requerida.

        Arguments:
            key -- el nombre de la clave
            section -- el nombre de la sección (opcional)

        Returns:
            Valor de la clave

        Exceptions:
            NoOptionError -- la clave no existe en la sección
            NoSectionError -- la sección no existe
        """
        if section in self.parser:
            if key in self.parser[section]:
                return self.parser[section][key]
            else:
                raise configparser.NoOptionError(key, section)
        else:
            raise configparser.NoSectionError(section)

    def set_value(self, value, key, section='DEFAULT'):
        """
        Description:
            Establece el valor a una clave. La clave debe existir.

        Arguments:
            value -- nuevo valor de la clave
            key -- el nombre de la clave
            section -- el nombre de la sección (opcional)

        Exceptions:
            NoOptionError -- la clave no existe
            NoSectionError -- la sección no existe
        """
        if section in self.parser:
            if key in self.parser[section]:
                self.parser[section][key] = value
            else:
                raise configparser.NoOptionError(key, section)
        else:
            raise configparser.NoSectionError(section)
        with open(self.path, 'w') as configfile:
            self.parser.write(configfile)

    def add_key(self, value, key, section='DEFAULT'):
        """
        Description:
            Agrega un nuevo par (clave:valor) al archivo de configuración.

        Arguments:
            value -- el valor de la nueva clave
            key -- el nombre de la clave
            section -- el nombre de la sección (opcional)

        Exceptions:
            NoSectionError -- la sección no existe
        """
        if section in self.parser:
            self.parser[section][key] = value
        else:
            raise configparser.NoSectionError(section)
        with open(self.path, 'w') as configfile:
            self.parser.write(configfile)
