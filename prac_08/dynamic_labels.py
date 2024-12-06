from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically creates labels for a list of names."""

    def __init__(self, **kwargs):
        """Initialize the app and define the list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy app."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create labels from the list of names."""
        for name in self.names:
            label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
