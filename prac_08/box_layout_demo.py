from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        # Find the label by id and update the text
        name_input = self.root.ids.name_input.text
        greeting_label = self.root.ids.greeting_label
        if name_input:
            greeting_label.text = f"Hello, {name_input}!"
        else:
            greeting_label.text = "Please enter your name."

BoxLayoutDemo().run()
