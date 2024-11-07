from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class Demo(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"

        # Create a box layout to center elements
        box_layout = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(None, None),
        )

        # Label
        label = MDLabel(text="Login", halign="center")

        # Load the text fields from the strings
        username = Builder.load_string(username_helper)
        password = Builder.load_string(password_helper)


        # Add widgets to the box layout
        box_layout.add_widget(label)
        box_layout.add_widget(username)
        box_layout.add_widget(password)

        # Set the size of the box layout according to the widgets
        box_layout.height = username.height + password.height + 40  # Adding spacing
        box_layout.width = 400  # Width matches the text fields

        # Add the box layout to the screen
        screen.add_widget(box_layout)

        return screen

Demo().run()
