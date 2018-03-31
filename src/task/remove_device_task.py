#coding:utf-8

from task.task import Task


class RemoveDeviceTask(Task):

    def __init__(self):
        super().__init__()

    def run(self, main_controller):
        print("Eliminando")

    def rollback(self, main_controller):
        print("Rollback")