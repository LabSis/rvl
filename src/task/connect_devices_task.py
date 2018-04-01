#coding:utf-8

from task.task import Task
from lib.canvas import Linking


class ConnectDevicesTask(Task):

    def __init__(self):
        super().__init__()
        self.initial_device = None
        self.linking_object = None
        self.object_canvas = None

    def run(self, main_controller):
        main_controller.window.canvas_panel.canvas.linking = True
        main_controller.window.canvas_panel.canvas.connect_devices_task = self
        object_canvas = self.initial_device.get_object_canvas()
        x = object_canvas.get_x() + object_canvas.get_width() / 2
        y = object_canvas.get_y() + object_canvas.get_height() / 2
        linking_object = Linking(x, y)
        main_controller.window.canvas_panel.add_last_canvas_object(linking_object, x, y)
        self.object_canvas = object_canvas
        self.linking_object = linking_object

    def rollback(self, main_controller):
        main_controller.window.canvas_panel.canvas.linking = False
        main_controller.window.canvas_panel.canvas.connect_devices_task = None
        main_controller.window.canvas_panel.canvas.remove_object(self.linking_object)