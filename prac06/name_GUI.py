from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

class NameAndAge(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        file = open("names.txt", "r")
        names = file.readlines()
        self.newNames = []
        for line in names:
            self.newNames.append(line.strip().split(","))

    def build(self):
        Window.size = (500,200)
        self.title = "Age Displayer"
        self.root = Builder.load_file("name_GUI.kv")
        self.createWidgets()
        return self.root

    def createWidgets(self):
        for name in self.newNames:
            temp_button = Button(text = name[0])
            temp_button.bind(on_release = self.pressName)
            self.root.ids.names.add_widget(temp_button)

    def pressName(self, instance):
        name = instance.text
        for i in self.newNames:
            if i[0] == name:
                self.root.ids.age.text = str(i[1])


NameAndAge().run()