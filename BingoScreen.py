from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from WordController import WordController


class BingoGameScreen(BoxLayout):
    def __init__(self, images, grid_size=3, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        self.all_images = images  # dict {label: path}
        self.grid_size = grid_size

        # LEFT: Caller view
        self.left_panel = BoxLayout(orientation='vertical', size_hint=(0.4, 1))

        self.image_display = Image()
        self.label_display = Label(font_size='24sp', size_hint=(1, 0.2))

        self.repeat_button = Button(text="Repeat", size_hint=(1, 0.2))
        self.next_button = Button(text="Next", size_hint=(1, 0.2))
        self.back_button = Button(text="Back", size_hint=(1, 0.2))

        self.left_panel.add_widget(self.image_display)
        self.left_panel.add_widget(self.label_display)
        self.left_panel.add_widget(self.repeat_button)
        self.left_panel.add_widget(self.next_button)
        self.left_panel.add_widget(self.back_button)

        self.add_widget(self.left_panel)

        # RIGHT: WordController will generate and return the grid
        self.controller = WordController(
            all_images=self.all_images,
            label_display=self.label_display,
            image_display=self.image_display
        )

        # Hook up buttons
        self.next_button.bind(on_press=self.controller.next_image)
        self.back_button.bind(on_press=self.controller.previous_image)
        self.repeat_button.bind(on_press=self.controller.recall_image)


    def setup_game(self, grid_size, source="internal"):
        self.grid_size = grid_size

        # Let WordController set up game logic and create grid
        self.controller.setup_game(grid_size, source)

        # Remove old grid if any
        if hasattr(self, 'grid') and self.grid:
            self.remove_widget(self.grid)

        # Add new grid from controller
        self.grid = self.controller.grid
        self.add_widget(self.grid)