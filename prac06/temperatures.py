"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class TemperatureConverter(App):
    def build(self):
        Window.size = (500,200)
        self.title = "Temperature Units Converter"
        self.root = Builder.load_file('temperature.kv')
        return self.root

    def handle_calculate(self, value):
        temp = float(self.root.ids.temperature.text)
        if value == 1:
            final = temp * 9.0 / 5 + 32
        else:
            final = 5 / 9 * (temp - 32)
        self.root.ids.output_label.text = str(final)

TemperatureConverter().run()

# MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     elif choice == "F":
#         # TODO: Write this section so the program converts F to C and displays the result
#         # Hint: celsius = 5 / 9 * (fahrenheit - 32)
#         fahrenheit = float(input("Fahrenheit: "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print("Result: {:.2f} C".format(celsius))
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")
