# ONE LINE A DAY PROGRAM

# rules:
# write 1 line of python code a day or change one line a day
# one statement per line

import time, math, pygame

pygame.init()

points = 0
ppc = 1

width, height = 500, 500

screen = pygame.display.set_mode((width, height))
FONT = pygame.font.SysFont("Consolas", 20)
pygame.display.set_caption("One Line A Day Incremental Game")

FPS = 60
CLOCK = pygame.time.Clock()

BGCOLOR = (0, 0, 0) # black

class Button: 
    def __init__ (self, x, y, width, height, color, txt_col, text="", font_size=32): pass

def draw(): 
    pygame.draw.rect(
        screen, 
        (255, 125, 0), 
        pygame.Rect(100, 100, 100, 50)
    )

running = True
while running: 
    running = running and not any(event.type == pygame.QUIT for event in pygame.event.get())
    screen.fill(BGCOLOR)
    draw()