from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SoloGameMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.selected_grid_size = 3
        self.selected_source = "internal"

        layout = BoxLayout(orientation="vertical", spacing=10, padding=40)

        # Grid Size Selection
        layout.add_widget(Label(text="Select Grid Size:", font_size=20))
        self.size_buttons = BoxLayout(spacing=10)
        self.btn_3x3 = Button(text="3x3")
        self.btn_4x4 = Button(text="4x4")
        self.btn_3x3.bind(on_press=lambda x: self.set_grid_size(3))
        self.btn_4x4.bind(on_press=lambda x: self.set_grid_size(4))
        self.size_buttons.add_widget(self.btn_3x3)
        self.size_buttons.add_widget(self.btn_4x4)
        layout.add_widget(self.size_buttons)

        # Image Source Selection
        layout.add_widget(Label(text="Choose Image Source:", font_size=20))
        self.source_buttons = BoxLayout(spacing=10)
        self.internal_btn = Button(text="Internal Storage")
        self.preloaded_btn = Button(text="Preloaded Grid")
        self.internal_btn.bind(on_press=lambda x: self.set_source("internal"))
        self.preloaded_btn.bind(on_press=lambda x: self.set_source("preloaded"))
        self.source_buttons.add_widget(self.internal_btn)
        self.source_buttons.add_widget(self.preloaded_btn)
        layout.add_widget(self.source_buttons)

        # Navigation Buttons
        nav_buttons = BoxLayout(spacing=10, size_hint=(1, 0.2))
        start_btn = Button(text="Start Game")
        back_btn = Button(text="Back")
        start_btn.bind(on_press=self.start_game)
        back_btn.bind(on_press=self.go_back)
        nav_buttons.add_widget(start_btn)
        nav_buttons.add_widget(back_btn)
        layout.add_widget(nav_buttons)

        self.add_widget(layout)

        # Initialize button colors to reflect default selections
        self.update_grid_button_colors()
        self.update_source_button_colors()

    def set_grid_size(self, size):
        self.selected_grid_size = size
        self.update_grid_button_colors()
        print(f"Grid size selected: {size}x{size}")

    def set_source(self, source_type):
        self.selected_source = source_type
        self.update_source_button_colors()
        print(f"Image source selected: {source_type}")

    def update_grid_button_colors(self):
        # Reset both buttons to default color
        default_color = (1, 1, 1, 1)  # white
        selected_color = (0.2, 0.6, 0.9, 1)  # light blue

        self.btn_3x3.background_color = selected_color if self.selected_grid_size == 3 else default_color
        self.btn_4x4.background_color = selected_color if self.selected_grid_size == 4 else default_color

    def update_source_button_colors(self):
        default_color = (1, 1, 1, 1)
        selected_color = (0.2, 0.6, 0.9, 1)

        self.internal_btn.background_color = selected_color if self.selected_source == "internal" else default_color
        self.preloaded_btn.background_color = selected_color if self.selected_source == "preloaded" else default_color

    def start_game(self, instance):
        print(f"Starting game with {self.selected_grid_size}x{self.selected_grid_size} grid, source: {self.selected_source}")

        # Get the wrapper Screen from the manager
        game_screen_wrapper = self.manager.get_screen("game")

        # Access the inner BingoGameScreen widget (assumes it is the first child)
        bingo_widget = game_screen_wrapper.children[0]

        # Call setup_game on the bingo widget with the user's selected options
        bingo_widget.setup_game(grid_size=self.selected_grid_size, source=self.selected_source)

        # Switch to the game screen
        self.manager.current = "game"

    def go_back(self, instance):
        self.manager.current = "main"