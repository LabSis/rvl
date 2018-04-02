# coding: utf-8

import topology.connection as con
import topology.devices.uml_server as uml_server
import constants
import lib.canvas as canvas


class OpticalFiber(con.Connection):

    def __init__(self):
        self.devices = [None, None]
        self.interfaces = [None, None]

    def get_tool_name(self):
        return "Fibra óptica"

    def is_tool(self):
        return True

    def get_url_icon(self):
        return "resources/img/optical-fiber-icon.png"

    def get_object_canvas(self):
        line_canvas = canvas.LineCanvas()
        line_canvas.set_x(0)
        line_canvas.set_y(0)
        line_canvas.set_width(50)
        line_canvas.set_height(50)
        return line_canvas

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

    def set_device2(self, device2, interface2):
        self.devices[1] = device2
        self.interfaces[1] = interface2

    def set_interface1(self, interface1):
        self.interfaces[0] = interface1

    def set_interface2(self, interface2):
        self.interfaces[1] = interface2

    def __repr__(self):
        return str(self._device1) + ' (' +  str(self._interface1) + ') <-> ' + str(self._device2) + ' (' +  str(self._interface1) + ')'
