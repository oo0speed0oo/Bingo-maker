from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty

class ImageButton(Button):
    image_path = StringProperty()
    is_pressed = BooleanProperty(False)

    def __init__(self, image_path, **kwargs):
        super().__init__(**kwargs)
        self.image_path = image_path
        self.background_normal = image_path
        self.background_down = image_path
        self.bind(on_press=self.on_button_press)

    def on_button_press(self, instance):
        self.is_pressed = True
        self.opacity = 0.5  # Darken the button to show it's been pressed