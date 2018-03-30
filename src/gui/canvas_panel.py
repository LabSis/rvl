# coding:utf-8

import gi.repository.Gtk as Gtk
import gi.repository.Gdk as Gdk
import gi.repository.Pango as Pango
try:
    import lib.canvas as Canvas
except Exception as ex:
    print(ex)


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
        canvas = Canvas.Canvas()
        canvas.add_events(Gdk.EventMask.ALL_EVENTS_MASK)
        canvas.set_size_request(width_canvas, height_canvas)

        canvas.set_verbose(False)

        container_fixed = Gtk.Fixed()
        container_fixed.put(canvas, 0, 0)

        self.canvas = canvas

        self.canvas.set_name("canvas")
        self.set_name("canvas_panel")

        self.pack_start(container_fixed, True, True, 0)


    def add_last_canvas_object(self, canvas_object):
        self.canvas.add_last(canvas_object)


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
