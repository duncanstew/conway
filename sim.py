import pygame, time
from conway.constants import WIDTH, HEIGHT, BLUE, ROWS, COLS
from conway.board import Board
import random

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
GENERATION = 0
pygame.display.set_caption('conway sim')
pygame.font.init()
font = pygame.font.SysFont(None, 24)

def main():
    global GENERATION
    run = True
    clock = pygame.time.Clock()
    board = Board()




    while run:
        clock.tick(FPS)
        if GENERATION == 0:
            board.glider1(97,97)
            board.glider2(20,20)
            board.stable(60,60)
            board.lightweight_space_ship(50,50)
            board.lightweight_space_ship(80,80)

        board.update_all_neighbors()
        board.propogate()
        GENERATION += 1

        if GENERATION % 15 == 0:
            board.glider1(97,97)
            x = random.randint(0,ROWS)
            y = random.randint(0,COLS)
            board.glider1(x//2,y//2)
            board.lightweight_space_ship(x,y)
            board.lightweight_space_ship(80,80)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
        board.draw(WIN)
        img = font.render(str(GENERATION), True, BLUE)
        WIN.blit(img, (20, 20))
        pygame.display.update()
    
    pygame.quit()

main()