from kivy.app import App
from kivy.lang import Builder


class MilesToKilometres(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            current_number = int(self.root.ids.input_miles.text)
        except ValueError:
            current_number = 0

        current_number += increment
        self.root.ids.input_miles.text = str(current_number)

    def convert_miles_to_km(self):
        try:
            miles = int(self.root.ids.input_miles.text)
        except ValueError:
            self.root.ids.display_label.text = str(0.0)
            return

        self.root.ids.display_label.text = str(miles * 1.6)

MilesToKilometres().run()