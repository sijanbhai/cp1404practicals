from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Name Input and Greeting"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def greet_user(self):
        name = self.root.ids.name_input.text  # Get text from the TextInput widget
        greeting = f"Hello, {name}!" if name else "Please enter your name."
        self.root.ids.greeting_label.text = greeting  # Update the label with greeting

    def clear_name(self):
        self.root.ids.name_input.text = ""  # Clear the text in TextInput widget
        self.root.ids.greeting_label.text = "Please enter your name."  # Reset the label


BoxLayoutDemo().run()
