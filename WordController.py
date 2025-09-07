import random
import pyttsx3
from GameLogic import BingoLogic
from BingoGrid import BingoGrid

class WordController:
    def __init__(self, all_images, label_display, image_display):

        self.all_images = all_images
        self.label_display = label_display
        self.image_display = image_display

        self.image_list = []
        self.current_index = 0
        self.current_called_word = ''

        self.logic = None
        self.grid = None

    def setup_game(self, grid_size, source="internal"):
        self.grid_size = grid_size

        if source == "internal":
            images = self.all_images
        else:
            images = self.all_images  # Placeholder for other sources

        self.image_list = list(images.items())
        random.shuffle(self.image_list)
        self.current_index = 0

        self.logic = BingoLogic(grid_size)

        # Build grid UI
        self.grid = BingoGrid(grid_size, images, on_cell_press=self.on_cell_press)

        self.show_image(0)

    def show_image(self, index):
        if index < 0 or index >= len(self.image_list):
            self.label_display.text = "Done!"
            self.image_display.source = ''
            self.current_called_word = ''
            return

        label, path = self.image_list[index]
        self.image_display.source = path

        if label.lower().endswith((".jpg", ".png")):
            self.current_called_word = label.rsplit(".", 1)[0]
        else:
            self.current_called_word = label

        self.label_display.text = self.current_called_word
        self.speak(self.current_called_word)

    def next_image(self, *args):
        if self.current_index + 1 < len(self.image_list):
            self.current_index += 1
            self.show_image(self.current_index)
        else:
            self.label_display.text = "Done!"
            self.image_display.source = ''
            self.current_called_word = ''

    def previous_image(self, *args):
        if self.current_index - 1 >= 0:
            self.current_index -= 1
        self.show_image(self.current_index)

    def recall_image(self, *args):
        self.show_image(self.current_index)

    def speak(self, text):
        print("in speak method")
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            print(f"(Speak fallback) {text}")

    def on_cell_press(self, row, col, label):
        """Handle cell tap from grid."""
        stripped_label = label.rsplit(".", 1)[0]

        if stripped_label != self.current_called_word:
            self.speak(f"'{stripped_label}' is not the current word!")
            print(f"⛔ '{stripped_label}' is not the label!")
            #return
        else:
            self.logic.mark_pressed(row, col)
            self.speak(f"you have {stripped_label}")

        if self.logic.check_win():
            print("🎉 BINGO! You win!")  # Replace with a popup or Kivy event
