import pygame

class Window:
    def __init__(self):
        self.width = 640
        self.height = 320
        pygame.display.set_caption('Roguelike Engine')
        self.display = pygame.display.set_mode((self.width, self.height))
        self.fullscreen = False
        
    def draw(self, objects=[]):
        """Draws everything to the display

        Args:
            objects (list, optional): Object with image, position and
                collision data. Must have a draw method. Defaults to [].
        """
        self.display.fill(pygame.Color(79,164,184))
        for object in objects:
            objects[object].draw()
        pygame.display.update()
        
    def toggle_fullscreen(self):
        "Toggles between fullscreen mode and small window"
        if self.fullscreen:
            self.display = pygame.display.set_mode((self.width, self.height))
            self.fullscreen = False
        else:
            self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.fullscreen = True

        