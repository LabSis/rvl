# coding: utf-8
"""Módulo topology_object.

Representa la máxima abstracción de un objeto en una topología.

Cualquier clase que extienda de esta podrá ser parte de una topología.





"""

import input_output.config_file as CF
import re
from lib import canvas

class TopologyObject(canvas.ObjectCanvas):
    """
    """
    def __init__(self):
        # Privados
        self._cf = CF.ConfigFile()
        self._name = "RVL"

        # Públicos
        self.icon_name = "default_icon_name"
        self.icon_path = "recursos/img/server.png"  # Si quiere agregar un ícono que dependa de la instancia cambie este atributo.

    def get_icon(self):
        """
        Description:
            Retorna el ícono para este objeto.

        Returns:
            Un string con el path del ícono para este objeto.
        """
        if self.icon_path is None:
            if self.icon_name is not None:
                return self._cf.get_value(self.icon_name)
            return None
        return self.icon_path

    def get_hostname(self):
        """
        Description:
            Retorna el nombre del objeto dejando solo los caracteres desde la 'a' a la 'z' en el alfabeto inglés, el '-',
             el '_' y los números desde el 0 al 9.

            A todos los demás caracteres los elimina.

        Returns:
            El hostname de este objeto.
        """
        return re.sub(r'[^a-zA-Z\-\_0-9]', '', self._name)

    def get_name(self):
        """
        Description:
            Retorna el nombre de este objeto. Tener en cuenta que este nombre puede variar por cada instancia y
            probablemente sea ingresado por el usuario.

        Returns:
            El nombre de este objeto.
        """
        return self._name

    def get_tool_name(self):
        """
        Description:
            Retorna la etiqueta que se mostrará en la barra de herramientas.
        
        Returns:
            Un string con la etiqueta.
        """
        return "Topology Object"

    def set_name(self, name):
        """
        Description:
            Establece el nombre del objeto.

        Args:
            name: el nombre del objeto.
        """
        self._name = name

    def set_id(self, id):
        self.id = id

    def is_visible(self):
        """
        Description:
            Este método es llamado cuando el canvas va a redibujarse. Si necesita que algún objeto no sea visible en la
            topología entonces redefina este método y retorne False.

        Returns:
            True si este objeto es visible en la topología o False en caso contrario.
        """
        return True

    def is_tool(self):
        """
        Description:
            Este método sirve para indicar que este objeto va o no va a aparecer en la barra de objetos.

        Returns:
            True si este objeto aparecerá en la barra de objetos o False en caso contrario.
        """
        return True

    def callback_added(self, event, topology):
        """
        Description:
            Es un callback que se llama cuando este objeto es agregado a la topología.
            Generalmente este callback es llamado cuando se agrega el objeto al canvas pero esto no siempre es así. Hay
            que tener en cuenta que puede llamarse en otro momento por ejemplo en aquellos casos en que otros objetos
            agreguen objetos a la topología indirectamente.

        Args:
            event: es un objeto que tiene información asociada al evento AddedEvent.
            topology: es la topologia en la cual se agrego a este objeto.
        """
        pass

    def callback_removed(self, event, topology):
        """
        Description:
            Es un callback que se llama cuando este objeto es borrado de la topología.

        Args:
            event: es un objeto que tiene información asociada al evento RemovedEvent
            topology: es la topología desde la cual se borró este objeto.

        """
        pass

    
    def get_subtype(self):
        return ""

