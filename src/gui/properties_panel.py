# coding:utf-8
"""
Description:
    Este módulo maneja la interfaz de las propiedades. Esto es, muestra
las propiedades adecuadas para cada objeto seleccionado.

Author:
    Parisi Germán
"""
import gi.repository.Gtk as Gtk


class PropertiesPanel(Gtk.Box):
    """
    Description:
        Este panel muestra las propiedades de un dispostivo seleccionado
        o bien no muestra nada.
    """
    def __init__(self, parent, controller):
        Gtk.Box.__init__(self)
        boton = Gtk.Button("Panel de propiedades")
        self.pack_start(boton, True, True, 0)
        
