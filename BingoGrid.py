from kivy.uix.gridlayout import GridLayout
from ImageButton import ImageButton
import random

class BingoGrid(GridLayout):
    def __init__(self, size, images, on_cell_press=None, **kwargs):
        super().__init__(**kwargs)
        self.grid_size = size
        self.cols = size
        self.on_cell_press = on_cell_press
        self.populate_grid(images)

    def populate_grid(self, images):
        count = 0
        image_items = list(images.items())
        random.shuffle(image_items)

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if count >= self.grid_size * self.grid_size:
                    break

                label, path = image_items[count]

                # Pass label to the ImageButton
                btn = ImageButton(image_path=path, label=label)

                btn.row = row
                btn.col = col

                btn.bind(on_press=self.handle_button_press)

                self.add_widget(btn)
                count += 1

    def handle_button_press(self, button):
        print("In handle button_press in BINGOGRID")
        if self.on_cell_press:
            self.on_cell_press(button.row, button.col, button.label)
