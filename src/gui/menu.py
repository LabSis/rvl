# coding: utf-8
"""
Módulo que crea la barra de menús.

"""
import gi.repository.Gtk as Gtk

UI_MENU_INFO = """
<ui>
    <menubar name='Menubar'>
        <menu action='FileMenu'>
            <menuitem action='ItemNewTopology' />
            <menuitem action='ItemOpenTopology' />
            <menuitem action='ItemOpenTemplate' />
            <separator />
            <menuitem action='ItemSave' />
            <menuitem action='ItemSaveAs' />
            <separator />
            <menuitem action='ItemQuit' />
        </menu>
        <menu action="HelpMenu">
            <menuitem action="ItemAbout" />
        </menu>
    </menubar>
</ui>
"""


class Menu(Gtk.Box):
    """
    Esta clase representa la barra con todos los menús y submenús:
        Archivo
            Nuevo
            Abrir...
            Abrir plantilla
            Guardar
            Guardar como...
            Salir
        Edición
            Deshacer
            Rehacer
            Configuración
        Ayuda
            Manual
            Acerca de...
    """
    def __init__(self, parent, controller):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        general_action_group = Gtk.ActionGroup("general")

        uimanager = Gtk.UIManager()
        uimanager.add_ui_from_string(UI_MENU_INFO)

        # File menu
        action_file_menu = Gtk.Action("FileMenu", "Archivo", "Archivo", None)
        general_action_group.add_action(action_file_menu)

        action_new_topology = Gtk.Action("ItemNewTopology", "Nueva topología",
                                         "Nueva topología", None)
        general_action_group.add_action(action_new_topology)

        action_open_topology = Gtk.Action("ItemOpenTopology", "Abrir...",
                                          "Abrir topología", None)
        general_action_group.add_action(action_open_topology)

        action_open_template = Gtk.Action("ItemOpenTemplate",
                                          "Abrir plantilla", "Abrir plantilla",
                                          None)
        general_action_group.add_action(action_open_template)

        action_save = Gtk.Action("ItemSave", "Guardar", "Guardar", None)
        general_action_group.add_action(action_save)

        action_save_as = Gtk.Action("ItemSaveAs", "Guardar como...",
                                    "Guardar como...", None)
        general_action_group.add_action(action_save_as)

        action_save_as = Gtk.Action("ItemQuit", "Salir", "Salir", None)
        general_action_group.add_action(action_save_as)

        # Help menu
        action_help_menu = Gtk.Action("HelpMenu", "Ayuda", "Ayuda", None)
        general_action_group.add_action(action_help_menu)

        action_about = Gtk.Action("ItemAbout", "Acerca de", "Acerca de", None)
        general_action_group.add_action(action_about)

        uimanager.insert_action_group(general_action_group)
        menubar = uimanager.get_widget("/Menubar")

        self.pack_start(menubar, False, False, 0)
