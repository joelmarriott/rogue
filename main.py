import pygame
from r_window import Window
from r_world import WorldMap


def main():
    "Main game loop"
    window = Window()
    clock = pygame.time.Clock()
    
    this_world = WorldMap('overworld', window)
    
    run = True
    while run:
        clock.tick(30)
        events = pygame.event.get()
        window.draw([this_world])
        run = input(events, window, this_world)
    

def input(events, window, this_world):
    """Handles all game input

    Args:
        events (pygame.event): All events captured by pygame
        window (r_window.Window): The window instance of the rogue engine

    Returns:
        Boolean: Keep game running
    """
    run = True
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                window.toggle_fullscreen()
                display_info = pygame.display.Info()
                this_world.pos_y = display_info.current_h / 2
                this_world.world_map = this_world.construct_map('overworld', window)
            
    return run


if __name__ == '__main__':
    main()