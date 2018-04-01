#coding:utf-8
"""Módulo main_window

Módulo de interfaz gráfica principal.

"""
# import gui.button_object as button_object
# import gui.group_object as group_object
import gui.menu as menu
import gui.toolbar as toolbar
# import gui.barra_herramientas as barra_herramientas
# import gui.panel_central as panel_central
import gui.properties_panel as pp
#import gui.groups_panel as Gp
import gui.canvas_panel as Cp
import input_output.config_file as CF
import gi.repository.Gtk as Gtk
import gi.repository.Gdk as Gdk
from gui.left_panel import LeftPanel
from gui.drag_and_drop import DragAndDrop

#import constantes as Const


class MainWindow(Gtk.Window):
    """
    Esta clase representa la ventana principal de la aplicación.

    Está formada por:
    --> Gtk.Box orientation=VERTICAL (main box)
        --> Gtk.Box orientation=HORIZONTAL (menú)
        --> Gtk.Box orientation=HORIZONTAL (barra de herramientas)
        --> Gtk.Box orientation=HORIZONTAL (central box)
        --> Gtk.Box orientation=HORIZONTAL (footer box)
    """
    def __init__(self, controller):
        Gtk.Window.__init__(self)
        self.controller = controller
        self.canvas_panel = None

    def open_window(self, width, height, maximize):
        self.set_default_size(width, height)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.menu_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.toolbar_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.central_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.footer_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self._add_menu_box()
        self._add_toolbar_box()
        self._add_central_box()
        self._add_footer_box()

        self.main_event_box = Gtk.EventBox()
        self.main_event_box.add(self.main_box)
        self.main_event_box.set_name("main_event_box")

        #self.main_event_box.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65500,0,0))

        #self._agregar_barra_menus()
        #self._agregar_barra_herramientas()
        #self._agregar_panel_central()
        #self._agregar_panel_dispositivos()
        #self._agregar_panel_propiedades()

        #panel_desplazable_horizontal = Gtk.HPaned()
        #panel_desplazable_horizontal.pack1(self.panel_dispositivos)
        #panel_desplazable_horizontal.pack2(self.panel_central)
        #self.box_central.pack_start(panel_desplazable_horizontal, True, True, 0)

        #panel_desplazable_vertical = Gtk.VPaned()
        #panel_desplazable_vertical.pack1(self.box_central)
        #panel_desplazable_vertical.pack2(self.panel_propiedades)
        #panel_desplazable_vertical.set_position(650)
        #self.box_principal.pack_start(panel_desplazable_vertical, True, True, 0)

        self.connect("delete-event", self._cerrar_ventana)

        self.add(self.main_event_box)
        if maximize:
            self.maximize()
        self._set_title()
        self.set_icon_from_file("resources/img/icono.png")

        self._load_style()
        self.show_all()
        #self.panel_propiedades.ocultar_pestania_propiedades()
        Gtk.main()

    def get_canvas_panel(self):
        """
        Description:
            Retorna el contenedor del canvas.
        """
        return self.canvas_panel

    def _add_menu_box(self):
        """
        Description:
            Agrega el menú de la aplicación.
        """
        m = menu.Menu(self, self.controller)
        self.menu_box.pack_start(m, False, False, 0)
        self.main_box.pack_start(self.menu_box, False, False, 0)

    def _add_central_box(self):
        """
        Description:
            Agrega el panel de objetos y el canvas al contenedor.
        """
        # Agrego el Canvas
        pr = CF.ConfigFile()
        try:
            width_canvas = int(pr.get_value("ancho_canvas"))
        except Exception:
            width_canvas = self.get_screen().width()

        try:
            height_canvas = int(pr.get_value("alto_canvas"))
        except Exception:
            height_canvas = self.get_screen().width()

        if width_canvas <= 0 or height_canvas <= 0:
            raise Exception("Error en el formato del tamaño del canvas")

        # Agrego el scrollbar
        scrollbar = Gtk.ScrolledWindow()
        scrollbar.set_border_width(10)
        scrollbar.set_policy(Gtk.PolicyType.AUTOMATIC,
            Gtk.PolicyType.AUTOMATIC)

        self.canvas_panel = Cp.CanvasPanel(self, self.controller, width_canvas, height_canvas)

        scrollbar.add_with_viewport(self.canvas_panel)

        # Agrego el panel de objetos
        #objects_panel = Gp.GroupsPanel(self, self.controller)

        objects_panel_event_box = Gtk.EventBox()
        #objects_panel_event_box.add(objects_panel)
        objects_panel_event_box.set_name("objects_panel_event_box")

        left_panel = LeftPanel()

        drag_and_drop = DragAndDrop()
        drag_and_drop.connect(left_panel.object_palette, self.canvas_panel.canvas)

        paned = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        paned.pack1(left_panel)
        paned.pack2(scrollbar)
        paned.set_position(self.get_default_size()[0] * 0.3)
        paned.set_name("paned_central")

        event_paned_box = Gtk.EventBox()
        event_paned_box.add(paned)
        event_paned_box.set_name("paned_central_event_box")

        self.central_box.pack_start(event_paned_box, True, True, 0)

    def _add_toolbar_box(self):
        """
        Description:
            Agrega el menú de barra de herramientas.
        """
        self.toolbar = toolbar.Toolbar(self, self.controller)
        self.toolbar_box.pack_start(self.toolbar, True, True, 10)

        toolbar_event_box = Gtk.EventBox()
        toolbar_event_box.add(self.toolbar_box)
        toolbar_event_box.set_name("toolbar_event_box")

        self.main_box.pack_start(toolbar_event_box, False, False, 0)

    def _add_footer_box(self):
        """
        Description:
            Agrega el panel de propiedades.
        """
        notebook = Gtk.Notebook()
        properties_panel = pp.PropertiesPanel(self, self.controller)
        notebook.append_page(properties_panel, Gtk.Label("Propiedades"))
        notebook.set_tab_detachable(properties_panel, True)
        notebook.set_group_name("principal")
        notebook.set_show_border(True)
        notebook.set_scrollable(True)

        self.footer_box.pack_start(notebook, True, True, 0)
        paned = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        paned.add1(self.central_box)
        paned.add2(self.footer_box)
        paned.set_position(self.get_default_size()[1] * 0.9)
        self.main_box.pack_start(paned, True, True, 0)

    def _set_title(self):
        """
        Description:
            Cambia el título de la ventana de acuerdo al nombre del trabajo y 
            a si está guardado o no.
        """
        self.titulo = "Simulador de Redes LabSis"
        self.set_title("%s (Sin guardar)" % (self.titulo))

    def _cerrar_ventana(self, w, e):
        """
        Description:
            Cierra la aplicación.
        """
        ok = False
        if self.controller.has_changed():
            dialogo_pregunta = Gtk.Dialog(
                 "Pregunta",
                 self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                 Gtk.STOCK_OK, Gtk.ResponseType.OK))
            dialogo_pregunta.set_default_size(300, 50)

            lbl_texto = Gtk.Label("No guardó su trabajo, por lo tanto se "
            "perderán los cambios no guardados. ¿Está seguro que desea salir?")
            lbl_texto.set_line_wrap(True)

            box = dialogo_pregunta.get_content_area()
            box.add(lbl_texto)
            dialogo_pregunta.show_all()
            resp_pregunta = dialogo_pregunta.run()
            if resp_pregunta == Gtk.ResponseType.OK:
                ok = True
            dialogo_pregunta.destroy()
        else:
            ok = True
        if ok:
            Gtk.main_quit()
        else:
            return True

    def _load_style(self):
        """
        Description:
            Carga el estilo CSS de la aplicación.
        """
        style_provider = Gtk.CssProvider()
        css = None
        with open("gui/estilos.css", "r") as f:
            css = f.read()

        # Si el css no es válido lanzará una excepción.
        style_provider.load_from_data(bytearray(css, "UTF-8"))

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
