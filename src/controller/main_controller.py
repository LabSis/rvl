#coding:utf-8
"""Módulo del controlador general.

Contiene la clase MainController

"""

import input_output.config_file as CF
import input_output.reflective as Ref
import input_output.logger as Log

import gui.main_window as Window
import topology.topology as Top
import gi.repository.Gtk as Gtk
import constants as Constants


class MainController():
    """
    Esta clase representa el controlador general de la aplicación.
    """
    __instance = None
    def __new__(cls):
        if MainController.__instance is None:
            MainController.__instance = object.__new__(cls)
            MainController.__instance.window = Window.MainWindow(MainController.__instance)
            MainController.__instance.log = Log.Logger(Log.GUI_MODE | Log.CONSOLE_MODE, MainController.__instance.window)
            MainController.__instance.changed = False
            MainController.__instance.ejecution_mode = False
            propr = CF.ConfigFile()
            MainController.__instance.path = propr.get_value("ruta_trabajo")
        return MainController.__instance

    def __init__(self):
        pass

    def add_device(self, device):
        print ("Agregando dispositivo")
        self.topology.add_device(device)

    def add_connection(self, connection):
        print ("Agregando conexión")
        self.topology.add_connection(connection)

    def check_version_gtk(self):
        """
        Description:
            Verifica que la versión de Gtk se cumpla.
            La versión mínima es 3.10.8.
        """
        major_version = Gtk.get_major_version()
        minor_version = Gtk.get_minor_version()
        micro_version = Gtk.get_micro_version()
        if major_version < 3:
            return False
        if major_version == 3 and minor_version < 10:
            return False
        if major_version == 3 and minor_version == 10 and micro_version < 8:
            return False
        return True

    def check_version_pygobject(self):
        """
        Description:
            Verifica que la versión de PyGObject se cumpla.
            La versión mínima es 3.12.0.
        """
        version = Gtk.pygobject_version()
        major_version = version[0]
        minor_version = version[1]
        micro_version = version[2]
        if major_version < 3:
            return False
        if major_version == 3 and minor_version < 12:
            return False
        if major_version == 3 and minor_version == 12 and micro_version < 0:
            return False
        return True

    def get_objects(self):
        """
        Description:
            Retorna los objetos de la aplicación. Éstos se van a ubicar en el
            panel de objetos y son los que se tiran al canvas.
        """
        import gui.object_button as object_button
        import gui.objects_group as objects_group

        def _get_objects(path):
            ref = Ref.PackageReflective(path)
            objects = ref.get_objects()
            result = []
            pos = 1
            for obj in objects:
                o = object_button.ObjectButton(obj[0].get_subtype(),
                                        obj[0].get_icon(), pos, obj[0])
                result.append(o)
                pos += 1
            return result

        objects1 = _get_objects("topology/devices")
        objects2 = _get_objects("topology/connections")
        objects3 = _get_objects("topology/shapes")

        section1 = objects_group.ObjectsGroup("Dispositivos", objects1)
        section2 = objects_group.ObjectsGroup("Conexiones", objects2)
        section3 = objects_group.ObjectsGroup("Figuras", objects3)

        sections = []
        sections.append(section1)
        sections.append(section2)
        sections.append(section3)

        return sections

    def has_changed(self):
        return self.changed

    def new_topology(self):
        print ("Creando nueva topología")
        self.topology = Top.Topology()

    def open_topology(self):
        print ("Abriendo una topología")

    def save_topology(self):
        print ("Guardando la topología")

    def execute_topology(self):
        print ("Ejecutando topología")

    def stop_topology(self):
        print ("Deteniendo")

    def start(self):
        """
        Description:
            Este método inicia la aplicación.
        """
        if not self.check_version_gtk():
            self.log.error("Versión incorrecta de Gtk. Se necesita por lo menos la 3.10.8 y usted tiene %s.%s.%s" %
                (Gtk.get_major_version(), Gtk.get_minor_version(),
                    Gtk.get_micro_version()))
        try:
            propr = CF.ConfigFile()
            width = int(propr.get_value("ancho_ventana"))
            height = int(propr.get_value("alto_ventana"))
            maximize = propr.get_value("pantalla_completa") == Constants.YES
            self.new_topology()
            self.verbose = True
            self.window.open_window(width, height, maximize)
            # Luego de esto no se ejecuta más hasta cerrar la aplicación.
        except Exception as e:
            self.log.error(e)
