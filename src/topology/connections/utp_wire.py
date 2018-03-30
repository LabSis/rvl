# coding: utf-8

import topology.connection as con
import topology.devices.uml_server as uml_server
import constants


class UTPWire(con.Connection):

    def __init__(self):
        self.icon_path = "recursos/img/server.png"

    def get_device1(self):
        return self._device1

    def get_device2(self):
        return self._device2

    def get_interface1(self):
        return self._interface1

    def get_interface2(self):
        return self._interface2

    def set_device1(self, device1, interface1):
        self._device1 = device1
        self._interface1 = interface1

    def set_device2(self, device2, interface2):
        self._device2 = device2
        self._interface2 = interface2

    def set_interface1(self, interface1):
        self._interface1 = interface1

    def set_interface2(self, interface2):
        self._interface2 = interface2

    def get_url_icon(self):
        return "recursos/img/router.png"

    def __repr__(self):
        return str(self._device1) + ' (' +  str(self._interface1) + ') <-> ' + str(self._device2) + ' (' +  str(self._interface1) + ')'
