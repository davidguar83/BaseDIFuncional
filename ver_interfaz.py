import gi
from conexionBD import ConexionBD
gi.require_version("Gtk","3.0")

from gi.repository import Gtk

class Ventana():

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("INTERFAZDI.glade")
        VentanaDatos = builder.get_object("VentanaDatos")
        VentanaDatos.show_all()




if __name__ == "__main__":
    Ventana()
    Gtk.main()