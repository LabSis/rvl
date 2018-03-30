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
        # palette = Gtk.Widget.get_ancestor(Gtk.drag_get_source_widget(drag_context), Gtk.ToolPalette)
        #if palette is not None:
        #    item = Gtk.ToolPalette.get_drag_item(palette, data);
        #    etq = item.get_icon_name();
        #    if item is not None:
        #        if not self.agregar_objeto(widget, etq, x, y):
        #            self.log.warning("Warning 100: El dispositivo no se puede"
        #                             " agregar. El nombre del dispositivo ya existe.")