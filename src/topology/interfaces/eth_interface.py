# coding: utf-8

import topology.interface as interface


class ETHInterface(interface.Interface):

    def __init__(self):
        interface.Interface.__init__(self)

    def is_tool(self):
        return False

    def get_url_icon(self):
        return "recursos/img/router.png"

    def get_tool_name(self):
        return "eth"
