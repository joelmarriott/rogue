import pygame
from r_window import Window


def main():
    window = Window()
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        events = pygame.event.get()
        window.draw()
        run = input(events, window)
    

def input(events, window):
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