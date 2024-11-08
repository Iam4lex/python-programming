
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IconRightWidget


class DemoApp(MDApp):

    def build(self):

        screen = Screen()

        box_layout = MDBoxLayout(
            orientation = "vertical",
            spacing = 10,
            pos_hint = {"center_x":0.5, "center_y":0.5},
            size_hint = (None, None)
        )

        box_layout.width = 400

        list_view = MDList()

        icon = IconRightWidget(icon="android")

        for lst in range(1, 6):
            list_items = OneLineListItem(text=f"List {str(lst)}")
            list_view.add_widget(list_items)

            list_items.add_widget(icon)

        box_layout.add_widget(list_view)

        screen.add_widget(box_layout)


        return screen
    def list_one(self, obj):
        print("Hello world")

if __name__ == "__main__":
    DemoApp().run()