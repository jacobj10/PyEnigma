import gi
import os
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject, Gdk
from scrambler import Scrambler
from reflector import Reflector

gtk_builder_file = os.path.splitext(__file__)[0] + '.ui'

class Engine():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gtk_builder_file)
        start1 = 0
        start2 = 0
        start3 = 0
        self.scrambler1 = Scrambler(start1)
        self.scrambler2 = Scrambler(start2)
        self.scrambler3 = Scrambler(start3)
        self.reflector = Reflector()
        self.counter = 1
        print self.run("hello this is a message from earth I really like the way that we have fun")
        print self.run("ZCZJU NVTH KL Z GGCKQDM ZQNN QUHWG H YDKRJQ SGSG LPH KGA HAIJ ZG ZCDD EGU")

    def translate(self, char):
        x = self.scrambler1._rev_dict[self.scrambler2._rev_dict[self.scrambler3._rev_dict[self.reflector._dict[self.scrambler3._dict[self.scrambler2._dict[self.scrambler1._dict[char]]]]]]]
        self.scrambler1.increment()
        if self.counter % 26 == 0:
            self.scrambler2.increment()
            if self.counter % 52 == 0:
                self.scrambler3.increment()
        return x

    def run(self, plaintext):
        ciphertext = ''
        for i in range(0, len(plaintext)):
            if plaintext[i] != ' ':
                ciphertext += self.translate(plaintext[i].upper())
                self.counter += 1
            else:
                ciphertext +=  ' '
        self.counter = 1
        self.scrambler1.reset()
        self.scrambler2.reset()
        self.scrambler3.reset()
        return ciphertext
e = Engine()
