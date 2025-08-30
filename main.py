import pygame, constants, sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    pygame.freetype.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    font = pygame.freetype.SysFont("Arial", 24)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collide(player):
                if player.lives > 0:
                    player.lives -= 1
                    asteroid.kill()
                    print(f"Lives remaining: {player.lives}")
                else:
                    print("Game over!")
                    sys.exit()

        for shot in shots:
            for asteroid in asteroids:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
                    

        screen.fill((0,0,0))
        
        font.render_to(screen, (10, 10), f"Lives remaining: {player.lives}", (255, 255, 255))

        for obj in drawable:
            obj.draw(screen)
       
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds



if __name__ == "__main__":
    main()
