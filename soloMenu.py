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

        # --- Grid Size Section ---
        layout.add_widget(Label(text="Select Grid Size:", font_size=20))

        size_buttons = BoxLayout(spacing=10)
        btn_3x3 = Button(text="3x3")
        btn_4x4 = Button(text="4x4")

        btn_3x3.bind(on_press=lambda x: self.set_grid_size(3))
        btn_4x4.bind(on_press=lambda x: self.set_grid_size(4))

        size_buttons.add_widget(btn_3x3)
        size_buttons.add_widget(btn_4x4)
        layout.add_widget(size_buttons)

        # --- Image Source Section ---
        layout.add_widget(Label(text="Choose Image Source:", font_size=20))

        source_buttons = BoxLayout(spacing=10)
        internal_btn = Button(text="Internal Storage")
        preloaded_btn = Button(text="Preloaded Grid")

        internal_btn.bind(on_press=lambda x: self.set_source("internal"))
        preloaded_btn.bind(on_press=lambda x: self.set_source("preloaded"))

        source_buttons.add_widget(internal_btn)
        source_buttons.add_widget(preloaded_btn)
        layout.add_widget(source_buttons)

        # --- Start / Back Buttons ---
        nav_buttons = BoxLayout(spacing=10, size_hint=(1, 0.2))

        start_btn = Button(text="Start Game")
        start_btn.bind(on_press=self.start_game)

        back_btn = Button(text="Back")
        back_btn.bind(on_press=self.go_back)

        nav_buttons.add_widget(start_btn)
        nav_buttons.add_widget(back_btn)

        layout.add_widget(nav_buttons)

        self.add_widget(layout)

    def set_grid_size(self, size):
        print(f"Grid size selected: {size}x{size}")
        self.selected_grid_size = size

    def set_source(self, source_type):
        print(f"Image source selected: {source_type}")
        self.selected_source = source_type

    def start_game(self, instance):
        print(f"Starting game with {self.selected_grid_size}x{self.selected_grid_size}, source: {self.selected_source}")
        # You can pass these settings into your game screen here
        game_screen = self.manager.get_screen("game")
        game_screen.setup_game(grid_size=self.selected_grid_size, source=self.selected_source)
        self.manager.current = "game"

    def go_back(self, instance):
        self.manager.current = "main"
