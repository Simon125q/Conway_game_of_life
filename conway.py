import pygame
from random import randint
from copy import deepcopy
import sys

FPS = 60
RES = WIDTH, HEIGHT = (1600, 900)
TILE = 50
W = WIDTH // TILE
H = HEIGHT // TILE

next_field = [[o for i in range(W)] for j in range(H)]
current_field = [[randint(0, 1) for i in range(W)] for i in range(H)]

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

        # draw grid
        [pygame.draw.line(screen, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
        [pygame.draw.line(screen, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

        # draw life
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(screen, pygame.Color('forestgreen'), (x * TILE + 2, y * TILE - 2, TILE - 2, TILE - 2))
                next_field[y][x] = self.check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

    def check_events(self)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def check_cell(self, current_field, x, y):
        count = 0

        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j][i]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return True
            return False
        else:
            if count == 3:
                return True
            return False

    def menu(self):
            self.screen.fill('yellow')

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()            
    
if __name__ == 'main':
    game = Game()
    game.run()