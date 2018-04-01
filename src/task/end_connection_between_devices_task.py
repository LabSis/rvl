#coding:utf-8

from task.task import Task
from lib.canvas import LineCanvas


class EndConnectionBetweenDevicesTask(Task):

    def __init__(self):
        super().__init__()
        self.initial_device = None
        self.final_device = None
        self.connect_devices_task = None

    def run(self, main_controller):
        linking_object = self.connect_devices_task.linking_object
        xi = linking_object.pfx
        yi = linking_object.pfy
        width = linking_object.get_x() - linking_object.pfx
        height = linking_object.get_y() - linking_object.pfy
        obj = LineCanvas()
        obj.set_x(xi)
        obj.set_y(yi)
        obj.set_width(width)
        obj.set_height(height)
        main_controller.window.canvas_panel.add_last_canvas_object(obj, xi, yi)

    def rollback(self, main_controller):
        pass