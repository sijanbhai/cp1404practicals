from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        """Clear the input text field and reset the output label."""
        self.root.ids.input_name.text = ''  # Reset the TextInput field
        self.root.ids.output_label.text = ''  # Clear the output label

    def handle_greet(self):
        """Update the output label with a greeting based on the input name."""
        name = self.root.ids.input_name.text
        if name.strip():  # If the name is not empty or just whitespace
            self.root.ids.output_label.text = f'Hello, {name}!'
        else:
            self.root.ids.output_label.text = 'Hello, stranger!'


BoxLayoutDemo().run()
