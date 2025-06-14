from kivy.app import App
from image_loader import ImageLoader
from bingoScreen import BingoGameScreen

class BingoApp(App):
    def build(self):
        loader = ImageLoader("photos")
        loader.load_images()
        images = loader.get_images()

        grid_size = 3  # or 4, etc.
        game_screen = BingoGameScreen(images, grid_size=grid_size)

        return game_screen

if __name__ == "__main__":
    BingoApp().run()
