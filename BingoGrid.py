from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class BingoGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        for i in range(9):
            btn = Button(text=f"Cell {i+1}")
            btn.bind(on_press=self.mark_square)
            self.add_widget(btn)

    def mark_square(self, instance):
        # toggle marked state
        if instance.background_color == [0, 1, 0, 1]:
            instance.background_color = [1, 1, 1, 1] #turn it green
        else:
            instance.background_color = [0, 1, 0, 1] # Green when clicked