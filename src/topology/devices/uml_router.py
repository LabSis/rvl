# coding: utf-8
"""Módulo uml_router

Contiene a la clase UML Router.

"""

import topology.device as dev

import topology.interface as interface
from topology.interfaces import eth_interface
from topology.device import DeviceCanvas


class UMLRouter(dev.Device):

    def __init__(self, name=""):
        # if configuration is None:
        #    configuration = conf.Configuration()
        #    configuration.set_attribute("quantity_nics", 1)
        #    configuration.set_attribute("ram", 64)
        #    configuration.set_attribute("diff_imagen", "full_router.dimg")
        self.name = name
        interfaces_amount = 3
        dev.Device.__init__(self, interfaces_amount)

        eth0 = eth_interface.ETHInterface()
        eth0.set_name("eth0")

        eth1 = eth_interface.ETHInterface()
        eth1.set_name("eth1")

        eth2 = eth_interface.ETHInterface()
        eth2.set_name("eth2")

        self.add_interface(eth0)
        self.add_interface(eth1)
        self.add_interface(eth2)

        self.canvas_device = DeviceCanvas(self.get_url_canvas_icon(), "Router", self)

    def get_tool_name(self):
        return "Router"

    def is_tool(self):
        return True

    def get_url_icon(self):
        return "resources/img/router-icon.png"

    def get_url_canvas_icon(self):
        return "resources/img/router-canvas.png"

    def get_object_canvas(self):
        return self.canvas_device

    def get_position(self):
        return 0

    def get_subtype(self):
        return "Router"

    def __repr__(self):
        return "Router"

    def __copy__(self):
        uml_router = UMLRouter(self.name)
        return uml_router
