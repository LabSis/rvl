# coding: utf-8
"""Módulo uml_server

Contiene a la clase UML Server.

Extiende a la clase Device que incorpora mucha funcionalidad por defecto.

"""

import topology.device as dev
from lib.canvas import ImageCanvas


class UMLCloud(dev.Device):

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
        return "Nube"

    def is_tool(self):
        return True

    def get_url_icon(self):
        return "resources/img/cloud-icon.png"

    def get_url_canvas_icon(self):
        return "resources/img/cloud-canvas.png"

    def get_object_canvas(self):
        return ImageCanvas(self.get_url_canvas_icon())

    def get_subtype(self):
        return "Nube"

    def __repr__(self):
        return "Nube"

    def __copy__(self):
        uml_cloud = UMLCloud(self.name, self.configuration)
        return uml_cloud

