


from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class Demo(MDApp):
    def build(self):
        label = MDLabel(text="Hello world", halign="center", theme_text_color="Custom",
        text_color=(0, 0, 1, 1))

        icon_label = MDIcon(icon="Library-video", halign="center")
        return icon_label
Demo().run()