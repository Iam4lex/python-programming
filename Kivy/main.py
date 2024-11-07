
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from helpers import username_helper, password_helper
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

class Demo(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_pelatte = "Green"

        box_layout = MDBoxLayout(
            orientation = "vertical",
            spacing = 20,
            pos_hint = {"center_x":0.5, "center_y":0.5},
            size_hint = (None, None)
        )


        # Widgets
        label = MDLabel(text="Login", halign="center")
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        button = MDRaisedButton(text="Login", pos_hint={"center_x":0.5, "center_y":0.5},
                                on_release=self.show_values)

        # Add widgets in the box layout
        box_layout.add_widget(label)
        box_layout.add_widget(self.username)
        box_layout.add_widget(self.password)
        box_layout.add_widget(button)

        box_layout.height = self.username.height + self.password.height + 40
        box_layout.width = 400

        # Add the box layout in the screen
        screen.add_widget(box_layout)

        return screen
    
    # Function for showing the dialog
    def show_values(self, obj):
        close_btn = MDRaisedButton(text="Close")
        more_btn = MDRaisedButton(text="More")
        dialog = MDDialog(title="Show details", 
                          text=f"Username: {self.username.text} \n\nPassword: {self.password.text}",
                          size_hint=(0.7, 1),
                          buttons=[close_btn, more_btn])
        dialog.open()
    
if __name__ == "__main__":
    Demo().run()
