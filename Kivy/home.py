
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IconRightWidget, ThreeLineIconListItem, IconLeftWidget, ImageLeftWidget


class DemoApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Green"

        screen = Screen()
 
        # box_layout = MDBoxLayout(
        #     orientation = "vertical",
        #     spacing = 10,
        #     pos_hint = {"center_x":0.5, "center_y":0.5},
        #     size_hint = (None, None)
        # )

        # box_layout.width = 400

        list_view = MDList()


        for lst in range(1, 6):
            image = ImageLeftWidget(source='kui.png', on_release=self.kui)
            list_items = ThreeLineIconListItem(text=f"List {str(lst)}", on_release=self.kui)
            list_items.add_widget(image)
            list_view.add_widget(list_items)

        # box_layout.add_widget(list_view)

        screen.add_widget(list_view)


        return screen
    def list_one(self, obj):
        print("Hello world")

    def kui(self, obj):
        print("Hello kui")

if __name__ == "__main__":
    DemoApp().run()