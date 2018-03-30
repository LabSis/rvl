# coding: utf-8
"""Módulo circle

Contiene a la clase circle.

"""

import topology.shape as shape


class Circle(shape.Shape):

    def __init__(self):
        pass

    def get_url_icon(self):
        return "recursos/img/router.png"

    def get_subtype(self):
        return "Circle"

    def __repr__(self):
        return "Circle"

    def __copy__(self):
        circle = Circle()
        return circle
