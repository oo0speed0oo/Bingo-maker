from kivy.app import App
from bingoGrid import BingoGrid
from image_loader import ImageLoader  # assuming it's in a separate file

#understand what happened. You got it working but just copied and pasted the code
#understand what you did. the try to ramdonize the photos it picks.
class BingoApp(App):
    def build(self):
        loader = ImageLoader("photos") #file path
        loader.load_images()
        images = loader.get_images()
        return BingoGrid(4,images)

if __name__ == "__main__":
    BingoApp().run()