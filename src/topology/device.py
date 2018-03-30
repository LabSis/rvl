# coding: utf-8
"""Módulo device.

Este módulo contiene todos los dispositivos que se pueden insertar en la
topología.

Esta clase es la padre de todos los dispositivos que se van a crear.

"""

import constants
import topology.topology_object as TO


class Device(TO.TopologyObject):
    """
    Description:
        Esta clase representa un dispositivo donde cada uno posee una cantidad
        limitada de interfaces. La cantidad de interfaces se puede cambiar,
        para ello existen algunas restricciones que se detallan en el método
        set_count_nics.
    """
    def __init__(self, interfaces_amount = 3):
        """
        """
        self._interfaces = []  # Network cards
        self._interfaces_amount = interfaces_amount  # Number of interfaces
        self.MAX_INTERFACES = 16  # Maximum number of interfaces

        # self._name = name
        # self._set_host_name(name)
        # self._configuration = configuration
        # self._type = constants.TYPE_DEVICE
        # self._conections = []  # List<Connection>
        # self._interfaces = []
        # self._configure()

    def add_interface(self, interface):
        if len(self._interfaces) >= self._interfaces_amount:
            raise ValueError("Se intentó insertar una interfaz y no hay lugar")
        self._interfaces.append(interface)

    def get_interface(self, i):
        """
        Description:
            Retorna la i-ésima interfaz.
        
        Returns:
            Retorna None en caso que el índice pasado no esté en el intervalo
            válido.
        """
        if i < 0 or i >= len(self._interfaces):
            return None
        return self._interfaces[i]

    def get_interfaces_amount(self):
        return self._interfaces_amount

    def set_interfaces_amount(self, number):
        """
        Description:
            Establece la cantidad de interfaces.
        """
        if number <= 0 or number > self._interfaces_amount:
            raise ValueError("Cantidad incorrecta de interfaces")
        self._interfaces_amount = number

    def __repr__(self):
        return self._name

    def get_configuration(self):
        return self._configuration

    def get_count_nics(self):
        return self._count_nics

    def get_host_name(self):
        return self._host_name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_position(self):
        return 0

    def get_subtype(self):
        return ""

    def get_type(self):
        return self._type

    def set_count_nics(self, cantidad_nics_nueva, forzar=False):
        pass

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name
        self._set_host_name(host_name)

