# coding: utf-8
"""
"""

import topology.topology_object as TO


class Connection(TO.TopologyObject):

    def __init__(self):
        self.devices = []
        self.interfaces = []

    def get_object_canvas(self):
        return None
