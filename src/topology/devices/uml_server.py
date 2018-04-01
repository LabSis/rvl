# coding: utf-8
"""Módulo uml_server

Contiene a la clase UML Server.

Extiende a la clase Device que incorpora mucha funcionalidad por defecto.

"""

import topology.device as dev
from topology.device import CanvasDevice


class UMLServer(dev.Device):

    def __init__(self, name="", configuration=None):
        # if configuration is None:
        #    configuration = conf.Configuration()
        #    configuration.set_attribute("quantity_nics", 1)
        #    configuration.set_attribute("ram", 64)
        #    configuration.set_attribute("diff_imagen", "full_servidor.dimg")
        self.name = name
        self.configuration = configuration
        interfaces_amount = 1
        dev.Device.__init__(self, interfaces_amount)

    def get_tool_name(self):
        return "Servidor"

    def is_tool(self):
        return True

    def get_url_icon(self):
        return "resources/img/server-icon.png"

    def get_url_canvas_icon(self):
        return "resources/img/server-canvas.png"

    def get_object_canvas(self):
        return CanvasDevice(self.get_url_canvas_icon(), "Servidor", self)

    def get_subtype(self):
        return "Server"

    def __repr__(self):
        return "Server"

    def __copy__(self):
        uml_server = UMLServer(self.name, self.configuration)
        return uml_server

