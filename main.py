import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    


    print(
    "Starting asteroids!\n"
    f"Screen width: {SCREEN_WIDTH}\n"
    f"Screen height: {SCREEN_HEIGHT}"
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) 

        screen.fill("black")    

        for x in drawable:
            x.draw(screen)
            
        pygame.display.flip()
        
        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()