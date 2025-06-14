from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import pyttsx3
from kivy.core.audio import SoundLoader  # or use pyttsx3 for TTS
import random

from bingoGrid import BingoGrid
from game_logic import BingoLogic

class BingoGameScreen(BoxLayout):
    def __init__(self, images, grid_size=3, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        self.images = images  # Dict of {label: path}
        self.image_list = list(images.items())
        random.shuffle(self.image_list)

        self.logic = BingoLogic(grid_size)
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

        # RIGHT: Bingo grid
        self.grid = BingoGrid(grid_size, images, on_cell_press=self.on_cell_press)

        # Add both sides to screen
        self.add_widget(self.left_panel)
        self.add_widget(self.grid)

        # Show first image
        self.next_image()

    def next_image(self, *args):
        if self.current_index >= len(self.image_list):
            self.label_display.text = "Done!"
            self.image_display.source = ''
            return

        self.current_index += 1
        label, path = self.image_list[self.current_index]
        self.image_display.source = path
        cleaned_label = label.removesuffix(".jpg")
        self.label_display.text = cleaned_label
        self.speak(cleaned_label)
        #self.current_index += 1

    def previous_image(self, *args):
        if self.current_index >= len(self.image_list):
            self.label_display.text = "Done!"
            self.image_display.source = ''
            return

        self.current_index -= 1
        label, path = self.image_list[self.current_index]
        self.image_display.source = path
        cleaned_label = label.removesuffix(".jpg")
        self.label_display.text = cleaned_label
        self.speak(cleaned_label)
        #self.current_index -= 1

    def recall_image(self, *args):
        if self.current_index >= len(self.image_list):
            self.label_display.text = "Done!"
            self.image_display.source = ''
            return

        label, path = self.image_list[self.current_index]
        self.image_display.source = path
        cleaned_label = label.removesuffix(".jpg")
        self.label_display.text = cleaned_label
        self.speak(cleaned_label)


    def speak(self, text):
        # You can switch this to pyttsx3 if needed
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except:
            print(f"(Speak) {text}")

    def on_cell_press(self, row, col):
        self.logic.mark_pressed(row, col)
        if self.logic.check_win():
            print("🎉 You win!")  # You can replace with a popup
