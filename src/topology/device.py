# coding: utf-8
"""Módulo device.

Este módulo contiene todos los dispositivos que se pueden insertar en la
topología.

Esta clase es la padre de todos los dispositivos que se van a crear.

"""
from topology.topology_object import TopologyObject


class Device(TopologyObject):
    """
    Description:
        Esta clase representa un dispositivo donde cada uno posee una cantidad
        limitada de interfaces. La cantidad de interfaces se puede cambiar,
        para ello existen algunas restricciones que se detallan en el método
        set_count_nics.
    """

    def __init__(self):
        self.interfaces = []

    def add_interface(self, interface):
        pass
