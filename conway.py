import pygame
from random import randint
from copy import deepcopy
import sys

pygame.init()
FPS = 60
RES = WIDTH, HEIGHT = (1700, 900)
TILE = 7
W = WIDTH // TILE
H = HEIGHT // TILE
SELECTED_BOX_COLOR = '#222222'
BOX_COLOR = '#222222'
BOX_HEIGHT = 100
BOX_WIDTH = WIDTH // 2
FONT = pygame.font.Font(None, 40)
FONT_SIZE = 30

class Game:
    def __init__(self):
        self.create_buttons()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.pause = True
        self.grid = True
        self.starting_arrangement(0)
        
    def starting_arrangement(self, num):
        self.next_field = [[0 for i in range(W)] for j in range(H)]
        
        if num == 0:
            self.current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]
        elif num == 1:
            self.current_field = [[1 if i % 2 == 0 else 0 for i in range(W)] for j in range(H)]
        elif num == 2:
            self.current_field = [[1 if not (i * j) % 20 else 0 for i in range(W)] for j in range(H)]
        elif num == 3:
            self.current_field = [[0 for i in range(W)] for j in range(H)]
            for i in range(H):
                self.current_field[i][i + (W - H) // 2] = 1
                self.current_field[H - i - 1][i + (W - H) // 2] = 1
        elif num == 4:
            self.current_field = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]
        elif num == 5:
            self.current_field = [[1 if i % 5 and j % 3 else 0 for i in range(W)] for j in range(H)]
            

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption("Game of life")

    def draw(self):
        self.screen.fill('black')

        # draw grid
        if self.grid:
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
                elif event.key == pygame.K_SPACE:
                    self.grid = not self.grid
                elif event.key == pygame.K_1:
                    self.starting_arrangement(1)
                elif event.key == pygame.K_0:
                    self.starting_arrangement(0)
                elif event.key == pygame.K_2:
                    self.starting_arrangement(2)
                elif event.key == pygame.K_3:
                    self.starting_arrangement(3)
                elif event.key == pygame.K_4:
                    self.starting_arrangement(4)
                elif event.key == pygame.K_5:
                    self.starting_arrangement(5)
                    
        if self.exit_button.active:
            pygame.quit()
            sys.exit()
        if self.start_button.active:
            self.pause = False

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

    def create_buttons(self):
        margin_height = (HEIGHT - (BOX_HEIGHT * 3 + 2 * 40)) // 2
        self.start_button = Button('START', BOX_WIDTH, BOX_HEIGHT, (WIDTH//4, margin_height + BOX_HEIGHT))
        self.exit_button = Button('EXIT', BOX_WIDTH, BOX_HEIGHT, (WIDTH//4, margin_height + 2 * BOX_HEIGHT + 40))
        self.buttons = [self.start_button, self.exit_button]

    def menu(self):
        self.screen.fill('darkgrey')
        self.font = pygame.font.Font(None, 100)
        text_surf = self.font.render("GAME OF LIFE", True, "#ffffff")
        text_rect = text_surf.get_rect(midtop = pygame.math.Vector2(WIDTH//2, 40))
        self.screen.blit(text_surf, text_rect)
        surface = pygame.display.get_surface()
        for button in self.buttons:
            button.draw(surface)
        
    def run(self):
        while True:
            self.check_events()
            self.update()
            if self.pause:
                self.menu()
                pass
            else:
                self.draw()            

class Button:
    def __init__(self, text, width, height, pos):
        self.active = False
        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.passive_color = '#475F77'
        self.active_color = '#475F99'
        self.curr_color = self.passive_color
        
        # text
        self.text_surf = FONT.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self, screen):
        self.check_click()
        pygame.draw.rect(screen, self.curr_color, self.top_rect, border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.curr_color = self.active_color
            if pygame.mouse.get_pressed()[0]:
                self.active = True
            else:
                self.active = False
        else:
            self.curr_color = self.passive_color

if __name__ == '__main__':
    game = Game()
    game.run()