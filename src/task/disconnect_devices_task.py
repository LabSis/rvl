#coding:utf-8

from task.task import Task
from lib.canvas import Linking


class DisconnectDevicesTask(Task):

    def __init__(self):
        super().__init__()
        self.initial_device = None
        self.interface = None
        self.linking_object = None
        self.object_canvas = None

    def run(self, main_controller):
        pass

    def rollback(self, main_controller):
        pass