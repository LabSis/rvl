# coding: utf-8
"""Módulo topology

Este módulo contiene la clase Topology y la clase IdGenerator
"""


class Topology:
    def __init__(self):
        pass

    def add_object(self, obj):
        """
        Description:
            Agrega un objeto a la topología. También genera un id para representar a este objeto.

            No acepta objetos repetidos. Un objeto es igual a otro si la instancia es la misma.

            Además, llama al callback_added del objeto una vez agregado el mismo.

        Args:
            obj: es el objeto a agregar. Debe ser una instancia de la clase TopologyObject o de alguna subclase de ésta.

        Returns:
            True si se pudo agregar el objeto con éxito o False en caso contrario (el objeto ya existía o es None)

        """
        pass

    def get_objects(self):
        pass

    def len_objects(self):
        pass

    def remove_object(self, obj):
        pass

    def generate_unique_id(self):
        pass


class IdGenerator():
    def __init__(self):
        self._id = 0

    def next_id(self):
        self._id += 1
        return self._id