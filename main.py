import pygame
from r_window import Window


def main():
    "Main game loop"
    window = Window()
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        events = pygame.event.get()
        window.draw()
        run = input(events, window)
    

def input(events, window):
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
            
    return run


if __name__ == '__main__':
    main()