import subprocess
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

username_helper = """
MDTextField:
    hint_text: "Enter your username"
    size_hint_x: None
    width: 400
    icon_right: "account"
"""

password_helper = """
MDTextField:
    hint_text: "Enter your password"
    helper_text: "or click on forgot password"
    helper_text_mode: "on_focus"
    size_hint_x: None
    width: 400
    icon_right: "key-variant"
    password: True
"""



class Demo(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"

        box_layout = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(None, None)
        )

        # Widgets
        label = MDLabel(text="Login", halign="center")
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        button = MDRaisedButton(
            text="Login", pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.show_values
        )

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
        if self.username.text == "":
            check_string = "Please enter username"
        else:
            check_string = "Username does not exist"
        
        close_btn = MDRaisedButton(text="Close", on_release=self.close_dialog)
        more_btn = MDRaisedButton(text="More", on_release=self.open_home)

        self.dialog = MDDialog(
            title="Show details", 
            text=f"Username: {check_string} \n\nPassword: {self.password.text}",
            buttons=[close_btn, more_btn]
        )
        self.dialog.open()

    def open_home(self, obj):
        # Use subprocess to run home.py
        subprocess.run(["python", "home.py"])

    def close_dialog(self, obj):
        self.dialog.dismiss()

if __name__ == "__main__":
    Demo().run()
