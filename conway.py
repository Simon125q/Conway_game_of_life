import pygame
from random import randint
from copy import deepcopy
import sys

FPS = 60
RES = WIDTH, HEIGHT = (1600, 900)
TILE = 50
W = WIDTH // TILE
H = HEIGHT // TILE

class Game:
    def __init__(self):
        pygame.init()
        self.menu_init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.pause = True
        
    def starting_arrangement(self, num):
        if num == 0:
            self.next_field = [[o for i in range(W)] for j in range(H)]
            self.current_field = [[randint(0, 1) for i in range(W)] for i in range(H)]

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
                    self.pause = not self.pause
                elif event.key == pygame.K1:
                    self.starting_arrangement(1)

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

    def menu_init(self):
        self.boxes.append(Box(x, y, width, height, 'MENU'))
        self.boxes.append(Box(x, y, width, height, 'Start'))
        self.boxes.append(Box(x, y, width, height, 'Exit'))

    def menu(self):
        self.screen.fill('yellow')
        for box in boxes:
            box.draw()

    def run(self):
        while True:
            self.check_events()
            self.update()
            if self.pause:
                self.menu()
            else:
                self.draw()            
    
class Box:
    def __init__(self, top, left, width, height, text):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        pass

if __name__ == 'main':
    game = Game()
    game.run()