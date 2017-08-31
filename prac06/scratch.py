"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesToKm(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('scratch.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.validate_number()
        result = value * 1.60934
        self.root.ids.output_label.text = "{:.3f}".format(result)

    def handle_increment(self, increment):
        value = self.validate_number() + increment
        self.root.ids.input_number.text = str(value)

    def validate_number(self):
        try:
            number = float(self.root.ids.input_number.text)
            return number
        except ValueError:
            return 0


MilesToKm().run()
