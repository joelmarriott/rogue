import csv
import os
import pygame

class WorldMap:
    def __init__(self, map_name, window):
        self.world_map = self.construct_map(map_name, window)
        self.pos_x = 0
        self.pos_y = window.height / 2
        
    def construct_map(self, map_name, window):
        """Render the map contained in the .map file

        Args:
            map_name (str): Name of the .map file contained in assets/world
            window (r_window.Window): Game window configuration

        Returns:
            Nested List (r_world.Tile): Each list contains a list (row) of tiles
        """
        map_matrix = self.read_in_csv(map_name)
        world_map = []
        images = [
                     0,
                     window.get_image('world/floor/grass'),               # 1
                     window.get_image('world/floor/mud'),                 # 2
                     window.get_image('world/floor/mud_stone'),           # 3
                     window.get_image('world/floor/stone'),               # 4
                     window.get_image('world/floor/grass_top'),           # 5
        ]
        for i, row in enumerate(map_matrix):
            world_map.append([])
            for tile in row:
                solid = True
                if tile <= 0:
                    image = 0
                image = images[tile]
                if tile == 5:
                    solid = False
                world_map[i].append(Tile(image, solid))
        return world_map
    
    def read_in_csv(self, map_name):
        """Read in the CSV map of tile types to a nested list

        Args:
            map_name (str): Name of the .map file contained in assets/world

        Returns:
            Nested List (int): Each list contains a list (row) of integers
                corresponding to types of tile
        """
        map_matrix = []
        directory = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                              'assets',
                              'world')
        with open(os.path.join(directory, map_name+'.map')) as map_file:
            csv_reader = csv.reader(map_file, delimiter=',')
            for row in csv_reader:
                map_row = [ int(value) for value in row]
                map_matrix.append(map_row)
        return map_matrix
    
    def draw(self, window):
        """Draw the world map on the display

        Args:
            window (r_window.Window): Game window configuration
        """
        tile_x = self.pos_x
        start_tile_x = tile_x
        tile_y = self.pos_y
        for row in self.world_map:
            for tile in row:
                if tile:
                    tile.pos_x = tile_x
                    tile.pos_y = tile_y
                    tile.draw(window)
                tile_x += window.tilesize
            tile_x = start_tile_x
            tile_y += window.tilesize
            
            
class Tile:
    def __init__(self, image, solid=False):
        self.pos_x = 0
        self.pos_y = 0
        self.image = image
        self.solid = solid
        
    def draw(self, window):
        """Draw the tile on the display

        Args:
            window (r_window.Window): Game window configuration
        """
        if self.image:
            window.display.blit(self.image, (self.pos_x, self.pos_y))