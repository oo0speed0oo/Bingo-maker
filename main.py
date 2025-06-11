from kivy.app import App
from bingoGrid import BingoGrid
from image_loader import ImageLoader
from game_logic import BingoLogic

class BingoApp(App):
    def build(self):
        loader = ImageLoader("photos")
        loader.load_images()
        images = loader.get_images()

        size = 3  # example grid size
        self.logic = BingoLogic(size)  # create the game logic

        self.grid = BingoGrid(size, images, on_cell_press=self.on_cell_press)
        # Pass a reference of logic to grid if needed, or let BingoApp handle events

        return self.grid

    def on_cell_press(self, row, col):
        self.logic.mark_pressed(row, col)
        if self.logic.check_win():
            print("🎉 You win!")

if __name__ == "__main__":
    BingoApp().run()
