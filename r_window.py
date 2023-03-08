import os
import pygame

class Window:
    def __init__(self):
        self.width = 640
        self.height = 320
        pygame.display.set_caption('Roguelike Engine')
        self.display = pygame.display.set_mode((self.width, self.height))
        self.tile_size()
        self.fullscreen = False
        
    def tile_size(self):
        "Set the factor and tile size based on display resolution"
        display_info = pygame.display.Info()
        self.factor = (display_info.current_w / self.width) * 2
        self.tilesize = 16 * self.factor
        
    def draw(self, objects=[]):
        """Draws everything to the display

        Args:
            objects (list, optional): Object with image, position and
                collision data. Must have a draw method. Defaults to [].
        """
        self.display.fill(pygame.Color(79,164,184))
        for object in objects:
            object.draw(self)
        pygame.display.update()

        
    def get_image(self, image_path, degrees=0):
        """_summary_

        Args:
            image_path (string): Path to image from the assets folder
            degrees (integer, optional): Degrees to rotate the image by. Defaults to 0.

        Returns:
            pygame.Surface: Pygame image asset
        """
        image_path = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                                  'assets',
                                  image_path+'.png')
        loaded_image = pygame.image.load(image_path)
        loaded_image = pygame.transform.scale(loaded_image, (self.tilesize, self.tilesize))
        if degrees:
            loaded_image = pygame.transform.rotate(loaded_image, degrees)
        return loaded_image
        
    def toggle_fullscreen(self):
        "Toggles between fullscreen mode and small window"
        if self.fullscreen:
            self.display = pygame.display.set_mode((self.width, self.height))
            self.fullscreen = False
        else:
            self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.fullscreen = True
            
        self.draw()
        self.tile_size()
        