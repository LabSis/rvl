# -*- coding: utf-8 -*-
"""
Módulo que crea la barra de herramientas.

"""
import gi.repository.Gtk as Gtk


class ActionController():

    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.toolbar = Toolbar(parent, self)
        self.parent.add(self.toolbar)

    def new_topology(self, w):
        self.controller.new_topology()
        self.toolbar.progress_bar.set_no_show_all(False)
        self.toolbar.show_all()

    def open_topology(self, w):
        self.controller.open_topology()

    def save_topology(self, w):
        self.controller.save_topology()

    def execute_topology(self, w):
        self.toolbar.btn_stop.set_sensitive(True)
        w.set_sensitive(False)
        self.controller.execute()

    def stop_topology(self, w):
        self.toolbar.btn_execute.set_sensitive(True)
        w.set_sensitive(False)
        self.controller.stop()


class Toolbar(Gtk.Box):

    def __init__(self, parent, action_controller):
        Gtk.HBox.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.PADDING = 2

        img_new_topology = Gtk.Image()
        img_new_topology.set_from_stock(Gtk.STOCK_NEW, Gtk.IconSize.BUTTON)
        btn_new_topology = Gtk.Button()
        btn_new_topology.add(img_new_topology)
        btn_new_topology.connect("clicked", action_controller.new_topology)
        self.pack_start(btn_new_topology, False, False, self.PADDING)

        img_open_topology = Gtk.Image()
        img_open_topology.set_from_stock(Gtk.STOCK_OPEN, Gtk.IconSize.BUTTON)
        btn_open_topology = Gtk.Button()
        btn_open_topology.add(img_open_topology)
        btn_open_topology.connect("clicked", action_controller.open_topology)
        self.pack_start(btn_open_topology, False, False, self.PADDING)

        img_save_topology = Gtk.Image()
        img_save_topology.set_from_stock(Gtk.STOCK_SAVE, Gtk.IconSize.BUTTON)
        btn_save_topology = Gtk.Button()
        btn_save_topology.add(img_save_topology)
        btn_save_topology.connect("clicked", action_controller.save_topology)
        self.pack_start(btn_save_topology, False, False, self.PADDING)

        separator_1 = Gtk.Box()
        self.pack_start(separator_1, False, False, 10)

        img_copy = Gtk.Image()
        img_copy.set_from_stock(Gtk.STOCK_COPY, Gtk.IconSize.BUTTON)
        btn_copy = Gtk.Button()
        btn_copy.add(img_copy)
        btn_copy.set_sensitive(False)
        self.pack_start(btn_copy, False, False, self.PADDING)

        img_cut = Gtk.Image()
        img_cut.set_from_stock(Gtk.STOCK_CUT, Gtk.IconSize.BUTTON)
        btn_cut = Gtk.Button()
        btn_cut.add(img_cut)
        btn_cut.set_sensitive(False)
        self.pack_start(btn_cut, False, False, self.PADDING)

        img_paste = Gtk.Image()
        img_paste.set_from_stock(Gtk.STOCK_PASTE, Gtk.IconSize.BUTTON)
        btn_paste = Gtk.Button()
        btn_paste.add(img_paste)
        btn_paste.set_sensitive(False)
        self.pack_start(btn_paste, False, False, self.PADDING)

        separator_2 = Gtk.Box()
        self.pack_start(separator_2, False, False, 10)

        img_undo = Gtk.Image()
        img_undo.set_from_stock(Gtk.STOCK_UNDO, Gtk.IconSize.BUTTON)
        btn_undo = Gtk.Button()
        btn_undo.add(img_undo)
        btn_undo.set_sensitive(False)
        self.pack_start(btn_undo, False, False, self.PADDING)

        img_redo = Gtk.Image()
        img_redo.set_from_stock(Gtk.STOCK_REDO, Gtk.IconSize.BUTTON)
        btn_redo = Gtk.Button()
        btn_redo.add(img_redo)
        btn_redo.set_sensitive(False)
        self.pack_start(btn_redo, False, False, self.PADDING)

        separator_3 = Gtk.Box()
        self.pack_start(separator_3, False, False, 10)

        img_execute = Gtk.Image()
        img_execute.set_from_stock(Gtk.STOCK_MEDIA_PLAY, Gtk.IconSize.BUTTON)
        self.btn_execute = Gtk.Button()
        self.btn_execute.add(img_execute)
        self.btn_execute.connect("clicked", action_controller.execute_topology)
        self.pack_start(self.btn_execute, False, False, self.PADDING)

        img_stop = Gtk.Image()
        img_stop.set_from_stock(Gtk.STOCK_MEDIA_STOP, Gtk.IconSize.BUTTON)
        self.btn_stop = Gtk.Button()
        self.btn_stop.add(img_stop)
        self.btn_stop.set_sensitive(False)
        self.btn_stop.connect("clicked", action_controller.stop_topology)
        self.pack_start(self.btn_stop, False, False, self.PADDING)

        self.progress_bar = Gtk.ProgressBar()
        self.pack_start(self.progress_bar, False, False, 0)
        self.progress_bar.set_no_show_all(True)

        self.set_name("toolbar")


if __name__ == "__main__":
    import sys
    sys.path.append(".")
    import gui.toolbar as toolbar

    window = Gtk.Window()
    window.connect('delete-event', Gtk.main_quit)

    action_controller = toolbar.ActionController(window, None)
    window.show_all()
    Gtk.main()
