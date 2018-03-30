# coding: utf-8
"""Módulo interface

Este módulo contiene la clase Shape.
La clase Shape representa una figura como el círculo, cuadrado, etc.

No debería instanciar un objeto de esta clase sino más bien de alguna
clase hija de ésta.

"""

import constants
import topology.topology_object as TO

class Shape(TO.TopologyObject):
    """
    Description:
        Representa una figura.
    """
    def __init__(self):
        pass

    def is_visible(self):
        return False

    def __repr(self):
        return "%s" % (self._name)
