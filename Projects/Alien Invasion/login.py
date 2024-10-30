from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

# Set window color
Window.clearcolor = (0.2, 0.6, 0.8, 1)  # Light blue background

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Main layout that centers items
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Username
        self.username = TextInput(hint_text="Username", size_hint=(None, None), size=(300, 40), 
                                  multiline=False, padding_y=[10, 10], background_color=[1, 1, 1, 1])
        
        # Password
        self.password = TextInput(hint_text="Password", size_hint=(None, None), size=(300, 40), 
                                  multiline=False, password=True, padding_y=[10, 10], background_color=[1, 1, 1, 1])
        
        # Login Button
        login_button = Button(text="Login", size_hint=(None, None), size=(150, 50), background_color=[0.1, 0.5, 0.1, 1], 
                              color=[1, 1, 1, 1], pos_hint={"center_x": 0.5})
        login_button.bind(on_press=self.validate_login)

        # Adding all widgets to layout
        layout.add_widget(Label(text="Login Form", font_size=24, color=[1, 1, 1, 1]))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_button)

        # Center layout within screen
        box_layout = BoxLayout(orientation='vertical', padding=[100, 150], spacing=10)
        box_layout.add_widget(layout)

        self.add_widget(box_layout)

    def validate_login(self, instance):
        username = self.username.text
        password = self.password.text
        # Add your login validation logic here
        print(f"Username: {username}, Password: {password}")

class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        return sm

if __name__ == '__main__':
    LoginApp().run()
