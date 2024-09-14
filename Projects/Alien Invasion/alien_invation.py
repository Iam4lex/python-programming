
# Import the necessary modules

import sys
import pygame
from settinngs import Settings
from ship import Ship

class AlienInvasion:
 """Overall class to manage game assets and behavior."""
 def __init__(self):
   """Initialize the game, and create game resources."""
   pygame.init()
   self.screen = pygame.display.set_mode((1000, 600))
   self.settings = Settings()

   self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height)
   )
   pygame.display.set_caption("Alien Invasion")
   self.ship = Ship(self)

   # Set the background color of the screen
   self.bg_color = (220, 210, 230)

 def run_game(self):
    """Start the main loop for the game."""

    while True:
       # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
   
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game() 