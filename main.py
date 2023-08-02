import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    pygame.display.set_caption("Pacman Remastered - Aarush, Evan and Harshith")

    done = False

    clock = pygame.time.Clock()

    game = Game()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        # --- Limits to 30 frames for easier computation power allocation
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
