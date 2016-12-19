import gi
import os
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject, Gdk
from engine import Engine

gtk_builder_file = os.path.splitext(__file__)[0] + '.ui'

class EnigmaX():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gtk_builder_file)
        self.engine = Engine()
        self.window = self.builder.get_object('windowMain')
        self.textBox = self.builder.get_object('entry')
        self.label = self.builder.get_object('label')
        self.label2 = self.builder.get_object('enigma')
        self.engineToString()

        self.textBox.connect('activate', self.signal_text_activate)
        self.textBox.connect('changed', self.signal_text_changed)
        self.window.connect('destroy', self.signal_window_destroy)

        self.ciphertext = ''

        self.window.show_all()
    
    def signal_window_destroy(self, _):
        self.window.destroy()
        Gtk.main_quit()

    def signal_text_activate(self, *args):
        self.label.set_text(self.engine.run(self.textBox.get_text()))
        self.engineToString()
    
    def signal_text_changed(self, *args):
        newChar = self.textBox.get_text()[-1] if len(self.textBox.get_text()) else ''
        self.ciphertext += self.engine.translate(newChar.upper())
        self.label.set_text(self.ciphertext)
        self.engineToString()
    
    def engineToString(self):
        self.label2.set_text(self.engine.toString())

e = EnigmaX()
Gtk.main()
