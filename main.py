from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from image_loader import ImageLoader
from bingoScreen import BingoGameScreen
from mainMenu import MainMenuScreen
from soloMenu import SoloGameMenuScreen

class BingoApp(App):
    def build(self):
        sm = ScreenManager()

        # Load images
        loader = ImageLoader("photos")
        loader.load_images()
        images = loader.get_images()

        # Create screens
        main_menu = MainMenuScreen(name="main")
        solo_menu = SoloGameMenuScreen(name="solo_menu")

        # Wrap BingoGameScreen inside a Screen
        game_screen_wrapper = Screen(name="game")
        bingo_widget = BingoGameScreen(images, grid_size=3)
        game_screen_wrapper.add_widget(bingo_widget)

        # Add screens to manager
        sm.add_widget(main_menu)
        sm.add_widget(solo_menu)
        sm.add_widget(game_screen_wrapper)

        # Start at the main menu
        sm.current = "main"

        return sm

if __name__ == "__main__":
    BingoApp().run()



'''
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
'''
