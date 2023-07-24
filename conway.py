import pygame
import sys

FPS = 60
RES = (1200, 700)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()

    def new_game(self):
        pass

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption("Game of life")

    def draw(self):
        self.screen.fill('black')

    def check_events(self)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()            
    
if __name__ == 'main':
    game = Game()
    game.run()