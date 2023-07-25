import pygame
from random import randint
from copy import deepcopy
import sys

FPS = 60
RES = WIDTH, HEIGHT = (1700, 900)
TILE = 5
W = WIDTH // TILE
H = HEIGHT // TILE
SELECTED_BOX_COLOR = '#222222'
BOX_COLOR = '#448844'

class Game:
    def __init__(self):
        pygame.init()
        self.menu_init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.pause = False
        self.starting_arrangement(0)
        
    def starting_arrangement(self, num):
        if num == 0:
            self.next_field = [[0 for i in range(W)] for j in range(H)]
            self.current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]
        if num == 1:
            self.next_field = [[0 for i in range(W)] for j in range(H)]
            self.current_field = [[1 if i % 2 == 0 else 0 for i in range(W)] for j in range(H)]

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption("Game of life")

    def draw(self):
        self.screen.fill('black')

        # draw grid
        [pygame.draw.line(self.screen, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
        [pygame.draw.line(self.screen, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

        # draw life
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if self.current_field[y][x]:
                    pygame.draw.rect(self.screen, pygame.Color('forestgreen'), (x * TILE + 2, y * TILE - 2, TILE - 2, TILE - 2))
                self.next_field[y][x] = self.check_cell(self.current_field, x, y)

        self.current_field = deepcopy(self.next_field)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause = not self.pause
                elif event.key == pygame.K_1:
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
        self.boxes.append(Box(WIDTH//4, 40, WIDTH//2, 200, 'MENU'))
        self.boxes.append(Box(WIDTH//4, 280, WIDTH//2, 200, 'Start'))
        self.boxes.append(Box(WIDTH//4, 520, WIDTH//2, 200, 'Exit'))

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
                pass
            else:
                self.draw()            
    
class Box:
    def __init__(self, top, left, width, height, text):
        self.rect = pygame.Rect(left, top, width, height)
        self.text = text
        self.font = pygame.font.Font()

    def get_selection(self):

        return False

    def draw(self):
        self.selected = self.get_selection()
        color = SELECTED_COLOR if self.selected else BOX_COLOR

if __name__ == '__main__':
    game = Game()
    game.run()