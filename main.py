import pygame, constants
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
            
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
       
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds



if __name__ == "__main__":
    main()
