from kivy.app import App
from BingoGrid import BingoGrid
class BingoApp(App):
    def build(self):
        return BingoGrid()

if __name__=="__main__":
    BingoApp().run()