# coding: utf-8
"""
"""

import topology.topology_object as TO
from lib.canvas import ObjectCanvas


class Connection(TO.TopologyObject):

    def __init__(self):
        self.devices = []
        self.interfaces = []

    def get_object_canvas(self):
        return None


class WireConnectionCanvas(ObjectCanvas):

    def __init__(self):
        super().__init__()
        self.initial_device = None
        self.final_device = None
        self.old_initial_x = self.x
        self.old_initial_y = self.y
        self.old_final_x = self.x
        self.old_final_y = self.y

    def move(self, s, device):
        initial_object_canvas = self.initial_device.get_object_canvas()
        final_object_canvas = self.final_device.get_object_canvas()
        self.old_initial_x = initial_object_canvas.get_xc()
        self.old_initial_y = initial_object_canvas.get_yc()
        self.old_final_x = final_object_canvas.get_xc()
        self.old_final_y = final_object_canvas.get_yc()

        if device.get_id() == self.initial_device.get_id():
            # Se mueve el dispositivo inicial, aplico movimiento al inicial.
            self.x = initial_object_canvas.get_xc()
            self.y = initial_object_canvas.get_yc()
            self.width = self.get_width() - s.get_x()
            self.height = self.get_height() - s.get_y()
        elif device.get_id() == self.final_device.get_id():
            print("Moviendo dispositivo final")
            # Se mueve el dispositivo final, aplico movimiento al final.
            self.width = self.get_width() + s.get_x()
            self.height = self.get_height() + s.get_y()

    def repaint(self):
        initial_object_canvas = self.initial_device.get_object_canvas()
        final_object_canvas = self.final_device.get_object_canvas()
        min_x = min(self.old_final_x, self.old_initial_x, initial_object_canvas.get_xc(), final_object_canvas.get_xc())
        min_y = min(self.old_final_y, self.old_initial_y, initial_object_canvas.get_yc(), final_object_canvas.get_yc())
        max_x = max(self.old_final_x, self.old_initial_x, initial_object_canvas.get_xc(), final_object_canvas.get_xc())
        max_y = max(self.old_final_y, self.old_initial_y, initial_object_canvas.get_yc(), final_object_canvas.get_yc())
        repaint_width = abs(max_x - min_x)
        repaint_height = abs(max_y - min_y)
        print(repaint_width, repaint_height)
        self.canvas.queue_draw_area(min_x - 3, min_y - 3, repaint_width + 6, repaint_height + 6)

    def draw(self, w, cr):
        cr.set_source_rgb(0, 0, 0)
        cr.move_to(self.x, self.y)
        cr.line_to(self.width + self.x, self.height + self.y)
        cr.stroke()

    def contains(self, x, y):
        return False
