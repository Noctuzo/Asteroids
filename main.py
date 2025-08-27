import pygame, constants


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_over = False
    while game_over is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill((0,0,0))
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
