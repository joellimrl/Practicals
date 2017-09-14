from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class BoxLayoutDemo(App):
    def build(self):
        Window.size = (500,200)
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_grade(self):
        try:
            grade = int(self.root.ids.input_number.text)
        except ValueError:
            grade = -1
        if grade >= 0 and grade <= 100:
            if grade < 50:
                self.root.ids.output_label.text = "Fail"
            elif grade < 65:
                self.root.ids.output_label.text = "Pass"
            elif grade < 75:
                self.root.ids.output_label.text = "Credit"
            elif grade < 85:
                self.root.ids.output_label.text = "Distinction"
            else:
                self.root.ids.output_label.text = "High Distinction"
        else:
            self.root.ids.output_label.text = "What kind of score is that"

    def handle_clear(self):
        self.root.ids.output_label.text = ""
        self.root.ids.input_number.text = ""
BoxLayoutDemo().run()
