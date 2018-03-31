# coding: utf-8


class ObjectButton():
    """
    Clase que representa un objeto en forma de botón. El objeto es cualquier cosa
     que puede ser añadido a la topología.
    """

    def __init__(self, label, icon_path, position, topology_object):
        """
        :param label: string
        :param icon_path: path del icono
        :param position: posición en la cuál se va a mostrar en el grupo que lo contiene
        :param canvas_object:
        """
        assert label is not None and label != ""
        self.label = label
        self.icon_path = icon_path
        self.position = position
        self.topology_object = topology_object
