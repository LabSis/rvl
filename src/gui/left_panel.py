# coding:utf-8

import gi.repository.Gtk as Gtk
try:
    from gui.object_palette import ObjectPalette
    from gui.job_panel import JobPanel
except Exception as exc:
    pass


class LeftPanel(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self)
        self.notebook = Gtk.Notebook()
        self.pack_start(self.notebook, True, True, 0)
        self._create_pages()
        self.set_name("left_panel")

    def _create_pages(self):
        # Page object pallete
        self.object_palette = ObjectPalette()
        name_page_palette = "Objetos"
        self.notebook.append_page(self.object_palette, Gtk.Label(name_page_palette))

        # Page job panel
        self.job_panel = JobPanel()
        name_page_job = "Guías de trabajos"
        self.notebook.append_page(self.job_panel, Gtk.Label(name_page_job))


if __name__ == "__main__":
    import sys
    sys.path.append(".")
    from gui.object_palette import ObjectPalette
    from gui.job_panel import JobPanel
    leftpanel = LeftPanel()
    window = Gtk.Window()
    window.connect('delete-event', Gtk.main_quit)
    window.add(leftpanel)
    window.show_all()
    Gtk.main()
