from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        # Clear any name input or reset text
        self.root.ids.output_label.text = 'Enter your name'

    def handle_greet(self):
        # Change the label's text to greet the user
        name = self.root.ids.name_input.text  # Get the text from the name input field
        if name:  # If the name is not empty
            self.root.ids.output_label.text = f'Hello, {name}!'  # Greet the user
        else:
            self.root.ids.output_label.text = 'Hello, stranger!'  # Default greeting if name is empty

BoxLayoutDemo().run()
