
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.button import MDButton
from kivymd.uix.button import MDButtonIcon

username_input = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

class TodoApp(MDApp):

    def build(self):
        screen = Screen()

        # user_name = MDTextField(text="Enter username", pos_hint={"center_x":0.5, "center_y":0.5},
        #                         size_hint_x=None, width=400)

        username = Builder.load_string(username_input)
        button = MDButtonIcon(text="Click Me", pos_hint={"center_x":0.5, "center_y":0.5})


        
        # screen.add_widget(username)
        screen.add_widget(button)

        
        return screen

TodoApp().run()