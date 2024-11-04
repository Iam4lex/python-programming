from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. — Albert Schweitzer",
    "Your time is limited, don’t waste it living someone else’s life. — Steve Jobs",
    "The best way to predict the future is to create it. — Peter Drucker",
    "It does not matter how slowly you go as long as you do not stop. — Confucius",
    "You miss 100% of the shots you don’t take. — Wayne Gretzky",
    "Believe you can and you’re halfway there. — Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. — Franklin D. Roosevelt",
    "Act as if what you do makes a difference. It does. — William James",
    "Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau"
]

class QuoteGeneratorApp(App):
    def build(self):
        self.title = 'Random Quote Generator'
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Set a background color for the layout
        with layout.canvas.before:
            Color(1, 0.9, 0.5, 1)  # Light yellow background
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self.update_rect, pos=self.update_rect)

        # Label to display the quote
        self.quote_label = Label(text="", size_hint=(1, 0.8), text_size=(400, None),
                                 halign='center', valign='middle', color=(10, 0.5, 0, 1))  # Green text
        self.quote_label.bind(size=self.update_text_size)  # Bind size to update text size
        layout.add_widget(self.quote_label)

        # Button to get a new quote
        quote_button = Button(text='Get Random Quote', size_hint=(1, 0.2))
        quote_button.bind(on_press=self.get_random_quote)
        
        # Set button background color
        with quote_button.canvas.before:
            Color(1, 0.65, 0, 1)  # Orange background
            self.btn_rect = Rectangle(size=quote_button.size, pos=quote_button.pos)

        quote_button.bind(size=self.update_button_rect, pos=self.update_button_rect)
        layout.add_widget(quote_button)

        return layout

    def update_text_size(self, *args):
        # Update the text size to allow for wrapping
        self.quote_label.text_size = (self.quote_label.width, None)

    def get_random_quote(self, instance):
        random_quote = random.choice(quotes)
        self.quote_label.text = random_quote

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def update_button_rect(self, instance, value):
        self.btn_rect.size = instance.size
        self.btn_rect.pos = instance.pos

if __name__ == '__main__':
    QuoteGeneratorApp().run()
