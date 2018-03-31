# coding: utf-8
"""Módulo circle

Contiene a la clase Rectangle.

"""

import topology.shape as shape
import lib.canvas as canvas


class Rectangle(shape.Shape):

    def __init__(self):
        pass

    def get_tool_name(self):
        return "Rectángulo"

    def is_tool(self):
        return True

    def get_url_icon(self):
        return "resources/img/rectangle-icon.png"

    def get_object_canvas(self):
        rectangle_canvas = canvas.RectangleCanvas()
        rectangle_canvas.set_width(100)
        rectangle_canvas.set_height(100)
        return rectangle_canvas

    def get_subtype(self):
        return "Rectángulo"

    def __repr__(self):
        return "Rectángulo"

    def __copy__(self):
        rectangulo = Rectangle()
        return rectangulo
