from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        solo_btn = Button(text="Solo Game")
        solo_btn.bind(on_press=self.go_to_solo_menu)

        group_btn = Button(text="Local Group Game (Coming Soon)")
        # group_btn.bind(on_press=...)  # do nothing for now

        create_btn = Button(text="Create Bingo Grid")
        create_btn.bind(on_press=self.go_to_create_menu)

        layout.add_widget(solo_btn)
        layout.add_widget(group_btn)
        layout.add_widget(create_btn)

        self.add_widget(layout)

    def go_to_solo_menu(self, instance):
        self.manager.current = "solo_menu"

    def go_to_create_menu(self, instance):
        self.manager.current = "create_menu"