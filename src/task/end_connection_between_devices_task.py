#coding:utf-8

from task.task import Task
from lib.canvas import LineCanvas


class EndConnectionBetweenDevicesTask(Task):
    """
    Es una tarea que permite la conexión entre 2 o más devices dependiendo de la conexión.

    Tiene el dispositivo inicial y final.
    Tiene la interfaz inicial y final.
    Tiene la conexión (UTP-C5, fibra óptica, etc.).

    """

    def __init__(self):
        super().__init__()
        self.initial_device = None
        self.initial_interface = None
        self.final_device = None
        self.final_interface = None
        self.conection = None
        self.connect_devices_task = None

    def run(self, main_controller):
        linking_object = self.connect_devices_task.linking_object
        if self.initial_device is not None:
            initial_object_canvas = self.initial_device.get_object_canvas()
            xi = initial_object_canvas.get_xc()
            yi = initial_object_canvas.get_yc()
        else:
            raise Exception('No se detectó dispositivo inicial para realizar el enlace')

        if self.final_device is not None:
            final_object_canvas = self.final_device.get_object_canvas()
            xf = final_object_canvas.get_xc()
            yf = final_object_canvas.get_yc()
        else:
            raise Exception('No se detectó dispositivo final para realizar el enlace')

        if self.initial_interface is None:
            raise Exception('No se detectó interfaz inicial para realizar el enlace')

        if self.final_interface is None:
            raise Exception('No se detectó interfaz final para realizar el enlace')

        if self.conection is None:
            raise Exception('No se detectó conexión para realizar el enlace')

        width = xf - xi
        height = yf - yi

        connection_canvas = self.conection.get_object_canvas()
        if connection_canvas is not None:
            connection_canvas.set_x(xi)
            connection_canvas.set_y(yi)
            connection_canvas.set_width(width)
            connection_canvas.set_height(height)
            main_controller.window.canvas_panel.add_last_canvas_object(connection_canvas, xi, yi)
            # self.initial_interface.interface_canvas = connection_canvas
            # self.final_interface.interface_canvas = connection_canvas

    def rollback(self, main_controller):
        pass