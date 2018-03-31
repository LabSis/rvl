#coding:utf-8

from controller.main_controller import MainController


def execute_task(widget, task):
    task_runner = TaskRunner()
    task_runner.run_task(task)


class TaskRunner:
    __instance = None
    def __new__(cls):
        if TaskRunner.__instance is None:
            TaskRunner.__instance = object.__new__(cls)
        return TaskRunner.__instance

    def __init__(self):
        self.main_controller = MainController()
        self.tasks_queue = []

    def run_task(self, task):
        memento = task.run(self.main_controller)
        if memento is not None:
            task.memento = memento
            self.tasks_queue.append(task)


class Task:

    def __init__(self, data):
        self.data = data
        self.memento = None

    def run(self, main_controller):
        pass

    def rollback(self, main_controller):
        pass


class Memento:

    def __init__(self, state):
        self.state = state