#coding:utf-8

from task.task import Task


class AddObjectTask(Task):

    def __init__(self, topology_object, x, y):
        super().__init__()
        self.topology_object = topology_object
        self.x = x
        self.y = y

    def run(self, main_controller):
        object_canvas = self.topology_object.get_object_canvas()
        main_controller.window.canvas_panel.add_ahead_canvas_object(object_canvas, self.x, self.y)

    def rollback(self, main_controller):
        print("Rollback")