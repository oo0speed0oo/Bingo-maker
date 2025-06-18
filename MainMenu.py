from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        # Create buttons and store references
        self.solo_btn = Button(text="Solo Game")
        self.solo_btn.bind(on_press=self.on_button_press)

        self.group_btn = Button(text="Local Group Game (Coming Soon)")
        # no binding for now

        self.create_btn = Button(text="Create Bingo Grid (Coming Soon)")
        self.create_btn.bind(on_press=self.on_button_press)

        layout.add_widget(self.solo_btn)
        layout.add_widget(self.group_btn)
        layout.add_widget(self.create_btn)

        self.add_widget(layout)

        self.buttons = [self.solo_btn, self.group_btn, self.create_btn]

        self.selected_button = None  # Track selected button

    def on_button_press(self, instance):
        # Reset all buttons background color
        for btn in self.buttons:
            btn.background_color = (1, 1, 1, 1)  # white (default)

        # Change the pressed button color
        instance.background_color = (0.2, 0.6, 0.9, 1)  # light blue highlight

        self.selected_button = instance

        # Now navigate or perform action based on which button
        if instance == self.solo_btn:
            self.manager.current = "solo_menu"
        elif instance == self.create_btn:
            self.manager.current = "create_menu"

