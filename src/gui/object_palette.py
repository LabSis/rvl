# coding:utf-8
import gi.repository.Gtk as Gtk
import gi.repository.Gdk as Gdk
from input_output.objects_loader import ObjectsLoader


class ObjectPalette(Gtk.ToolPalette):

    def __init__(self):
        Gtk.ToolPalette.__init__(self)
        self.set_style(Gtk.ToolbarStyle.BOTH_HORIZ)
        self.groups = []
        self._loader_objects()

    def add_drag_dest(self, widget):
        self.set_drag_source(widget, Gtk.DestDefaults.ALL, Gtk.ToolPaletteDragTargets.ITEMS,
                           Gdk.DragAction.COPY)

    def add_group(self, objects_group):
        """
        Agrega un grupo al toolpalette y a la lista de groups.
        :param group: ObjectsGroup
        :return:
        """
        assert len(objects_group.label) > 0
        assert len(objects_group.list) > 0
        new_group = Gtk.ToolItemGroup(label=objects_group.label)
        for object_button in objects_group.list:
            button = Gtk.ToolButton()
            button.set_tooltip_text(object_button.label)
            button.set_label(object_button.label)
            image = Gtk.Image.new_from_file(object_button.icon_path)
            button.set_icon_widget(image)
            new_group.insert(button, object_button.position)
        self.add(new_group)
        self.groups.append(new_group)

    def _loader_objects(self):
        loader = ObjectsLoader()
        list = loader.loader()
        for group in list:
            self.add_group(group)
