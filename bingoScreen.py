from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import pyttsx3
import random

from bingoGrid import BingoGrid
from game_logic import BingoLogic

class BingoGameScreen(BoxLayout):
    def __init__(self, images, grid_size=3, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        self.all_images = images  # dict {label: path}
        self.grid_size = grid_size

        self.current_index = 0

        # LEFT: Caller view
        self.left_panel = BoxLayout(orientation='vertical', size_hint=(0.4, 1))

        self.image_display = Image()
        self.label_display = Label(font_size='24sp', size_hint=(1, 0.2))
        self.next_button = Button(text="Next", size_hint=(1, 0.2))
        self.next_button.bind(on_press=self.next_image)

        self.back_button = Button(text="Back", size_hint=(1, 0.2))
        self.back_button.bind(on_press=self.previous_image)

        self.repeat_button = Button(text="Repeat", size_hint=(1, 0.2))
        self.repeat_button.bind(on_press=self.recall_image)

        self.left_panel.add_widget(self.image_display)
        self.left_panel.add_widget(self.label_display)
        self.left_panel.add_widget(self.repeat_button)
        self.left_panel.add_widget(self.next_button)
        self.left_panel.add_widget(self.back_button)

        # RIGHT: Bingo grid (initialized later)
        self.grid = None

        # Add left panel only for now; grid added in setup_game
        self.add_widget(self.left_panel)

        # Setup initial game
        self.setup_game(grid_size, source="internal")

    def setup_game(self, grid_size, source="internal"):
        """Reset or initialize game with given grid size and image source."""
        self.grid_size = grid_size

        # Choose images based on source
        if source == "internal":
            images = self.all_images
        elif source == "preloaded":
            # TODO: load your preloaded saved game images here
            images = self.all_images  # Placeholder, change as needed
        else:
            images = self.all_images

        self.image_list = list(images.items())
        random.shuffle(self.image_list)

        self.current_index = 0

        self.logic = BingoLogic(grid_size)

        # Remove old grid if exists
        if self.grid:
            self.remove_widget(self.grid)

        # Create new grid with new size and images
        self.grid = BingoGrid(grid_size, images, on_cell_press=self.on_cell_press)
        self.add_widget(self.grid)

        # Show first image
        self.show_image(0)

    def show_image(self, index):
        if index < 0 or index >= len(self.image_list):
            self.label_display.text = "Done!"
            self.image_display.source = ''
            return

        label, path = self.image_list[index]
        self.image_display.source = path

        # Remove file extension like ".jpg"
        cleaned_label = label
        if label.lower().endswith(".jpg"):
            cleaned_label = label[:-4]
        self.label_display.text = cleaned_label

        self.speak(cleaned_label)

    def next_image(self, *args):
        if self.current_index + 1 < len(self.image_list):
            self.current_index += 1
            self.show_image(self.current_index)
        else:
            self.label_display.text = "Done!"
            self.image_display.source = ''

    def previous_image(self, *args):
        if self.current_index - 1 >= 0:
            self.current_index -= 1
            self.show_image(self.current_index)
        else:
            # Already at start
            self.show_image(self.current_index)

    def recall_image(self, *args):
        self.show_image(self.current_index)

    def speak(self, text):
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            print(f"(Speak) {text}")

    def on_cell_press(self, row, col):
        self.logic.mark_pressed(row, col)
        if self.logic.check_win():
            print("🎉 You win!")  # Replace with popup or UI update as needed
