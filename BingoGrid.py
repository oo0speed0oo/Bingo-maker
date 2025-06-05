from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class BingoGrid(GridLayout):
    def __init__(self, images, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3  # or 4 if it's a 4x4 grid
        self.populate_grid(images)

    def populate_grid(self, images):
        count = 0
        for filename, path in images.items():
            if count >= self.cols * self.cols:
                break
            img = Image(source=path)
            self.add_widget(img)
            count += 1


'''
#old code

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from image_loader import ImageLoader


class BingoGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        for i in range(9):
            btn = Button(background_normal = f'photos/00{i+1}.jpg')
            btn.bind(on_press=self.mark_square)
            self.add_widget(btn)

    def mark_square(self, instance):
        # toggle marked state
        if instance.background_color == [0, 1, 0, 1]:
            instance.background_color = [1, 1, 1, 1] #turn it green
        else:
            instance.background_color = [0, 1, 0, 1] # Green when clicked
'''