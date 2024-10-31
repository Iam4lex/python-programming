from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.icon = "icon.png"

        # Main layout
        layout = BoxLayout(orientation='vertical')

        # Display
        self.input_box = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=55,
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1)
        )
        layout.add_widget(self.input_box)

        # Button layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size=32)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current = self.input_box.text
        button_text = instance.text

        if button_text == 'C':
            self.input_box.text = ''
        elif button_text == '=':
            try:
                self.input_box.text = str(eval(current))
            except Exception:
                self.input_box.text = 'Error'
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            
            new_text = current + button_text
            self.input_box.text = new_text
            self.last_was_operator = button_text in self.operators

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
