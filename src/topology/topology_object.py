# coding: utf-8
"""Módulo topology_object.

Representa la máxima abstracción de un objeto en una topología.

Cualquier clase que extienda de esta podrá ser parte de una topología.

"""
from lib import canvas


class TopologyObject(canvas.ObjectCanvas):
    """
    """

    def __init__(self, topology, main_window, main_controller):
        self.properties = {}

    def get_url_icon(self):
        """
        Description:
            Retorna el ícono para este objeto.

        Returns:
            Un string con el path del ícono para este objeto.
        """
        pass

    def is_tool(self):
        """
        Description:
            Este método sirve para indicar que este objeto va o no va a aparecer en la barra de objetos.

        Returns:
            True si este objeto aparecerá en la barra de objetos o False en caso contrario.
        """
        return True

    def is_resizable(self):
        pass

    def get_tool_name(self):
        """
        Description:
            Retorna la etiqueta que se mostrará en la barra de herramientas.

        Returns:
            Un string con la etiqueta.
        """
        return "Topology Object"

    def get_tool_position(self):
        pass

    def get_default_width(self):
        pass

    def get_default_height(self):
        pass

    def get_menu_contextual(self):
        pass

    def get_hostname(self):
        """
        Description:
            Retorna el nombre del objeto dejando solo los caracteres desde la 'a' a la 'z' en el alfabeto inglés, el '-',
             el '_' y los números desde el 0 al 9.

            A todos los demás caracteres los elimina.

        Returns:
            El hostname de este objeto.
        """
        pass

    def get_name(self):
        """
        Description:
            Retorna el nombre de este objeto. Tener en cuenta que este nombre puede variar por cada instancia y
            probablemente sea ingresado por el usuario.

        Returns:
            El nombre de este objeto.
        """
        pass

    def is_visible(self):
        """
        Description:
            Este método es llamado cuando el canvas va a redibujarse. Si necesita que algún objeto no sea visible en la
            topología entonces redefina este método y retorne False.

        Returns:
            True si este objeto es visible en la topología o False en caso contrario.
        """
        return True

    def get_neighbors(self):
        pass

    def get_id(self):
        pass

    def get_x(self):
        pass

    def get_y(self):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass

    def stop(self, topology, main_window, main_controller):
        pass

    def prepareForAdd(self, topology, main_window, main_controller):
        pass

    def prepareForRemove(self, topology, main_window, main_controller):
        pass
