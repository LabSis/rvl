# coding: utf-8

import topology.connection as con
import topology.devices.uml_server as uml_server
import constants
import lib.canvas as canvas


class OpticalFiber(con.WireConnectionCanvas):

    def __init__(self):
        self.devices = [None, None]
        self.interfaces = [None, None]
        self.line_canvas = con.WireConnectionCanvas()

    def get_tool_name(self):
        return "Fibra óptica"

    def is_tool(self):
        return True

    def get_url_icon(self):
        return "resources/img/optical-fiber-icon.png"

    def get_object_canvas(self):
        return self.line_canvas

    def get_device1(self):
        return self.devices[0]

    def get_device2(self):
        return self.devices[1]

    def get_interface1(self):
        return self.interfaces[0]

    def get_interface2(self):
        return self.interfaces[1]

    def set_device1(self, device1, interface1):
        self.devices[0] = device1
        self.interfaces[0] = interface1
        self.line_canvas.initial_device = device1

    def set_device2(self, device2, interface2):
        self.devices[1] = device2
        self.interfaces[1] = interface2
        self.line_canvas.final_device = device2

    def set_interface1(self, interface1):
        self.interfaces[0] = interface1

    def set_interface2(self, interface2):
        self.interfaces[1] = interface2

    def __repr__(self):
        return str(self._device1) + ' (' +  str(self._interface1) + ') <-> ' + str(self._device2) + ' (' +  str(self._interface1) + ')'
