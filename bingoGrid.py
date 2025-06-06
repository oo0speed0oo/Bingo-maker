from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from imageButton import ImageButton
import random

class BingoGrid(GridLayout):
    def __init__(self, columns, images, **kwargs):
        super().__init__(**kwargs)
        self.cols = columns  # or 4 if it's a 4x4 grid
        self.populate_grid(images)

    def populate_grid(self, images):
        count = 0
        image_items = list(images.items())
        random.shuffle(image_items)

        for filename, path in images.items():
            if count >= self.cols * self.cols:
                break
            btn = ImageButton(image_path=path)
            self.add_widget(btn)
            count += 1