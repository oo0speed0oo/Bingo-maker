from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from ImageLoader import ImageLoader
from BingoScreen import BingoGameScreen
from MainMenu import MainMenuScreen
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
