# coding:utf-8

import gi.repository.Gtk as Gtk
import gi.repository.Gdk as Gdk


class DragAndDrop:

    def __init__(self):
        pass

    def connect(self, source, receiver):
        receiver.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.COPY)
        receiver.connect("drag-data-received", receiver.drag_data_received)

        source.add_drag_dest(receiver, Gtk.DestDefaults.ALL, Gtk.ToolPaletteDragTargets.ITEMS,
                             Gdk.DragAction.COPY)


class IDragAndDropDataSource:
    def __init__(self):
        pass


class IDragAndDropReceiverData:
    def __init__(self):
        pass

    def drag_data_received(self, widget, drag_context, x, y, data, info, time):
        pass