# coding:utf-8

import copy
import gi.repository.Gtk as Gtk
import gi.repository.Gdk as Gdk
import gi.repository.Pango as Pango
try:
    import lib.canvas as Canvas
except Exception as ex:
    print(ex)
from gui.drag_and_drop import IDragAndDropReceiverData
from task.end_connection_between_devices_task import EndConnectionBetweenDevicesTask
from task.add_object_task import AddObjectTask
from task.task import execute_task
from topology.connections.utp_c5 import UTPC5


class CanvasPanel(Gtk.Box):

    def __init__(self, parent, controller, width_canvas, height_canvas):
        """
        Description:
            El tamaño del canvas está dado por width_canvas y height_canvas.
            Si el tamaño dado por width_canvas_visible y height_canvas_visible
            es mayor al del width_canvas y height_canvas entonces se ignoran.

            Los 4 valores deben ser positivos.

        Arguments:
            parent -- es el padre.
            controller -- es el controlador de la aplicación.
            width_canvas -- es el ancho del canvas.
            height_canvas -- es el alto del canvas.
            width_canvas_visible -- es el ancho de lo que se ve del canvas.
                Debe ser menor o igual que width_canvas.
            height_canvas_visible -- es el alto de lo que se ve del canvas.
                Debe ser menor o igual que height_canvas.
        """
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.main_controller = controller
        canvas = WrapperCanvas(controller)
        canvas.add_events(Gdk.EventMask.ALL_EVENTS_MASK)
        canvas.set_size_request(width_canvas, height_canvas)

        canvas.set_verbose(False)

        container_fixed = Gtk.Fixed()
        container_fixed.put(canvas, 0, 0)

        self.canvas = canvas

        self.canvas.set_name("canvas")
        self.set_name("canvas_panel")

        self.pack_start(container_fixed, True, True, 0)

    def add_ahead_canvas_object(self, canvas_object, x, y):
        self.canvas.add_ahead_canvas_object(canvas_object, x, y)

    def add_last_canvas_object(self, canvas_object, x, y):
        self.canvas.add_last_canvas_object(canvas_object, x, y)


class WrapperCanvas(Canvas.Canvas, IDragAndDropReceiverData):

    def __init__(self, main_controller):
        super().__init__()
        self.linking = False
        self.connect_devices_task = None
        self.main_controller = main_controller

    def drag_data_received(self, widget, drag_context, x, y, data, info, time):
        palette = Gtk.Widget.get_ancestor(Gtk.drag_get_source_widget(drag_context), Gtk.ToolPalette)
        if palette is not None:
            item = Gtk.ToolPalette.get_drag_item(palette, data)
            if item is not None:
                topology_object = copy.copy(item.object_button.topology_object)
                add_object_task = AddObjectTask(topology_object, x, y)
                execute_task(None, add_object_task)
                #object_canvas = topology_object.get_object_canvas()
                #if not self.add_ahead_canvas_object(object_canvas, x, y):
                    #print("No se pudo agregar el dispositivo")
                    #self.log.warning("No se pudo agregar el dispositivo")

    def add_ahead_canvas_object(self, canvas_object, x, y):
        canvas_object.set_x(x)
        canvas_object.set_y(y)
        self.add_ahead(canvas_object)
        return False

    def add_last_canvas_object(self, canvas_object, x, y):
        canvas_object.set_x(x)
        canvas_object.set_y(y)
        self.add_last(canvas_object)
        return True

    def ev_left_click_in_empty_point(self, w, x, y):
        if self.linking:
            self.connect_devices_task.rollback(self.main_controller)

    def ev_left_click_in_object(self, obj, x, y):
        if self.linking:
            final_device = self.main_controller.topology.get_object(obj.device.get_id())
            end_connection = EndConnectionBetweenDevicesTask()
            end_connection.connect_devices_task = self.connect_devices_task
            end_connection.initial_device = self.connect_devices_task.initial_device
            end_connection.initial_interface = self.connect_devices_task.initial_interface
            end_connection.final_device = final_device
            end_connection.final_interface = final_device.get_interface(0)
            upt_c5_connection = UTPC5()
            end_connection.connection = upt_c5_connection
            self.connect_devices_task.rollback(self.main_controller)
            end_connection.run(self.main_controller)


if __name__ == "__main__":
    import sys
    sys.path.append(".")
    import lib.canvas as Canvas

    window = Gtk.Window()
    window.connect('delete-event', Gtk.main_quit)

    canvas = CanvasPanel(window, None, 400, 400, 300, 300)
    obj1 = Canvas.CircleCanvas(300, 200, 50)
    canvas.add_last_canvas_object(obj1)

    window.add(canvas)
    window.set_default_size(800, 600)

    window.show_all()
    Gtk.main()
