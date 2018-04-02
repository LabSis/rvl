# coding: utf-8
"""Módulo topology

Este módulo contiene la clase Topology y la clase IdGenerator
"""

#import constants
#import controller.statistics as st
#from events import added_event, removed_event


class Topology():
    def __init__(self):
        self._id_generator = IdGenerator()  # Un generador de ids usados para agregar un id a un objeto.
        self._objects = []  # Lista de los objetos que están actualmente agregados.
        self._ids = []  # Cada elemento de esta lista corresponde con cada elemento de la lista objects.

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
        if obj is not None:
            exists = False
            for o in self._objects:
                if o == obj:
                    exists = True
                    break
            if not exists:
                self._objects.append(obj)
                new_id = "object-%d" % self._id_generator.next_id()
                self._ids.append(new_id)
                obj.set_id(new_id)

                # Run event
                # TODO
                # event = added_event.AddedEvent()
                # obj.callback_added(event, self)
                return True
            else:
                return False
        return False

    def clear(self):
        """
        
        """
        ok = True
        for obj in self._objects:
            if not self.remove_object(obj):
                ok = False
        if ok:
            self._id_generator = IdGenerator()
        else:
            raise ValueError("Error al limpiar la topología")

    def get_ids(self):
        return self._ids

    def get_object(self, id_a_buscar):
        i = 0
        for id in self._ids:
            if id == id_a_buscar:
                return self._objects[i]
            i += 1
        return None

    def get_objects(self):
        return self._objects

    def len_objects(self):
        return len(self._objects)

    def remove_object(self, obj):
        ok = True
        try:
            index = self._objects.index(obj)
            self._ids.pop(index)
            self._objects.remove(obj)
            # event = removed_event.RemovedEvent()
            # obj.callback_removed(event, self)
        except:
            ok = False
        return ok

    def __str__(self):
        string = "Objetos: "
        string += str(self.get_objects())
        return string

"""
    def add_communication(self, com):
        self.communications.append(com)

    def add_connection(self, connection):
        ok = connection.validate_connection(self)
        if ok:
            self.connections.append(connection)
        else:
            raise Exception("La conexión no está permitida")
    
    #@st.statistics
    def add_device(self, device):
        self.devices.append(device)

    def change_configuration_to_device(self, device, config):
        pass

    def delete_communication(self, com_id):
        pass

    def delete_device(self, device_id):
        pass

    def get_count_devices(self):
        return len(self.devices)

    def get_count_communications(self):
        return len(self.communications)

    def get_count_connections(self):
        return len(self.connections)

    def set_count_interfaces(self, device, count):
        pass

    def __str__(self):
        r = str(self.devices)
        r += str(self.connections)
        return r

    def __repr__(self):
        r = str(self.devices)
        r += str(self.connections)
        return r
"""


class IdGenerator():
    def __init__(self):
        self._id = 0

    def next_id(self):
        self._id += 1
        return self._id
