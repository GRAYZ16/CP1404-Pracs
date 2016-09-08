from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from random import randint


class LoopedLabels(App):

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        # TODO: After running it, add another entry to the dictionary and see how the layout changes
        self.labels = ["Hello", "Kivy", "Prac06", "Memes"]
        self.increment = 0

    def build(self):
        self.title = "Add Labels through a loop"
        self.root = Builder.load_file('string_labels.kv')
        return self.root

    def add_label(self):
        temp_label = Label(text=self.labels[self.increment % len(self.labels)])
        self.increment += 1
        self.root.ids.label_box.add_widget(temp_label)

LoopedLabels().run()
