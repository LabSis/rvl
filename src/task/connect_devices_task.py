#coding:utf-8

from task.task import Task
from lib.canvas import Linking


class ConnectDevicesTask(Task):

    def __init__(self):
        super().__init__()
        self.initial_device = None

    def run(self, main_controller):
        object_canvas = self.initial_device.get_object_canvas()
        x = object_canvas.get_x()
        y = object_canvas.get_y()
        linking = Linking(x, y)
        print(main_controller.window)
        main_controller.window.canvas_panel.add_last_canvas_object(linking, x, y)

    def rollback(self, main_controller):
        print("Rollback")