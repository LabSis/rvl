# conding: utf-8
"""
Description:
    Módulo que permite manejar los errores indicando por donde los va a mostrar.


# Modos para mostrar los errores #

    Se puede usar cualquiera de las siguientes 3 constantes o bien una
    combinación de ellas para lograr el efecto combinado:

            GUI_MODE
            CONSOLE_MODE
            FILE_MODE

    Por ejemplo, si se desea mostrar los errores por GUI y por Consola entonces
    el valor a pasar como parámetro en la clase sería de 3.

"""

from gi.repository import Gtk

GUI_MODE = 1
CONSOLE_MODE = 2
FILE_MODE = 4

DEFAULT_MODE = 1


class Logger():
    """
    Description:
        Esta clase permite manejar los errores y el llamador le puede indicar
    por donde quiere que se muestren.
   """

    def __init__(self, mode, window=None):
        """

        Arguments:
           mode -- Es por donde va a mostrar los errores. Puede ser cualquier
           valor entre 1 y 7. Existen 3 valores prefijados, estos son: 1, 2 y
           4. Los restantes: 3, 5 y 6 se obtienen a partir de la combinacion
           (sumas) de los anteriores. Por ejemplo, un valor de 5=1+4 estaria
           combinando GUI y archivo.
        """
        self.mode = mode
        self.window = window

    def error(self, mensaje):
        if(self.mode & GUI_MODE == GUI_MODE):
            # Encendido el mode por GUI.
            self._mostrar_error_por_gui(mensaje)
        if(self.mode & CONSOLE_MODE == CONSOLE_MODE):
            # Encendido el mode por consola.
            print (mensaje)
        if(self.mode & FILE_MODE == FILE_MODE):
            # Encendido el mode por archivo.
            print (("POR ARCHIVO: " + mensaje))

    def warning(self, mensaje):
        if(self.mode & GUI_MODE == GUI_MODE):
            # Encendido el mode por GUI.
            self._mostrar_warning_por_gui(mensaje)
        if(self.mode & CONSOLE_MODE == CONSOLE_MODE):
            # Encendido el mode por consola.
            print (mensaje)
        if(self.mode & FILE_MODE == FILE_MODE):
            # Encendido el mode por archivo.
            print (("POR ARCHIVO: " + mensaje))

    def info(self, mensaje):
        if(self.mode & GUI_MODE == GUI_MODE):
            # Encendido el mode por GUI.
            self._mostrar_info_por_gui(mensaje)
        if(self.mode & CONSOLE_MODE == CONSOLE_MODE):
            # Encendido el mode por consola.
            print (mensaje)
        if(self.mode & FILE_MODE == FILE_MODE):
            # Encendido el mode por archivo.
            print (("POR ARCHIVO: " + mensaje))

    def _mostrar_error_por_gui(self, mensaje):
        dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.ERROR,
                                                Gtk.ButtonsType.OK, mensaje)
        dialog.run()
        dialog.destroy()

    def _mostrar_warning_por_gui(self, mensaje):
        dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.WARNING,
                                                Gtk.ButtonsType.OK, mensaje)
        dialog.run()
        dialog.destroy()

    def _mostrar_info_por_gui(self, mensaje):
        dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
                                                Gtk.ButtonsType.OK, mensaje)
        dialog.run()
        dialog.destroy()
