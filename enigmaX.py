import gi
import os
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject, Gdk
from Scrambler import Scrambler
from reflector import Reflector

gtk_builder_file = os.path.splitext(__file__)[0] + '.ui'

class Engine():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gtk_builder_file)
        start1 = 1
        start2 = 2
        start3 = 3
        self.scrambler1 = Scrambler(start1)
        self.scrambler2 = Scrambler(start2)
        self.scrambler3 = Scrambler(start3)
        self.reflector = Reflector()
        self.toString()

    def toString(self):
        for i in range(0, 26):
            print ' '.join([self.scrambler1[i], self.scrambler2[i], self.scrambler3[i], 
                            self.reflector._dict.keys()[i],
                            self.reflector._dict[self.reflector._dict.keys()[i]],
                            self.reflector._rev_dict.keys()[i],
                            self.reflector._rev_dict[self.reflector._rev_dict.keys()[i]]])
            
e = Engine()
