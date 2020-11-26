from .constants import ROWS, COLS, SQUARE_SIZE, BLACK, WHITE, HEIGHT, WIDTH, GREY
import pygame
from .unit import Unit 


class Board:
    def __init__(self):
        self.display = []
        self.create_board()


    def create_board(self):
        for row in range(ROWS):
            self.display.append([])
            for col in range(COLS):
                self.display[row].append(Unit(row, col, living=False))

    def print_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                print(self.display[row][col])

    def update_cell(self, row, col):
        unit = self.getUnit(row, col)
        unit.make_living()
        self.display[row][col] = unit

    def check_neighbors(self, row, col):
        current = self.getUnit(row, col)
        current.neighbors = 0
        for x in range(-1,2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    # print(f'XY: {x} {y}')
                    xx = row + x
                    yy = col + y
                    # print(f'Pre Ifs: {xx} {yy}')
                    if xx > -1 and xx < ROWS:
                        if yy > -1 and yy < COLS:
                            neighbor = self.getUnit(xx,yy)
                            if neighbor.check_living():
                                current.neighbors += 1
        
        # print(f'{current} Neighbors Living: {current.neighbors}')

    def update_all_neighbors(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.check_neighbors(row,col)
                    
    def propogate(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.conway_rules(row,col)

    def glider1(self, row, col):
        coordinates = [(-1,-1),(-1,0),(-1,1),(0,-1),(1,0)]
        self.pattern(row, col, coordinates)

    def glider2(self, row, col):
        coordinates = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,1)]
        self.pattern(row, col, coordinates)

    def stable(self, row, col):
        coordinates = [(1,0),(0,0),(0,-1),(0,1)]
        self.pattern(row, col, coordinates)

    def lightweight_space_ship(self,row,col):
        coordinates = [(-1,-1),(0,-2),(1,-2),(2,-2),(2,-1),(2,0),(2,1),(-1,2),(1,2)]
        self.pattern(row,col,coordinates)
    
    def glider_gun(self,row,col):
        coordinates= [()]
        self.pattern(row,col,coordinates)

    def pattern(self,row, col, coordinates):
        try:
            for tup in coordinates:
                i,j = tup
                xx = row + i
                yy = col + j
                self.update_cell(xx,yy)
        except:
            print('Index Error')

    def conway_rules(self, row, col):
        unit = self.getUnit(row, col)
        living = unit.check_living()
        neighbors = unit.check_neighbors()

        if living:
            if neighbors < 2 or neighbors > 3:
                unit.make_dead()
                self.display[row][col] = unit

        else:
            if neighbors == 3:
                unit.make_living()
                self.display[row][col] = unit



    def getUnit(self, row, col):
        return self.display[row][col]

    def draw(self, win):
        win.fill(WHITE)

        for row in range(ROWS):
            for col in range(COLS):
                cell = self.display[row][col]
                cell.draw(win)
        for c in range(ROWS):
            pygame.draw.line(win, GREY, (c*SQUARE_SIZE, 0),(c * SQUARE_SIZE, HEIGHT))
            pygame.draw.line(win, GREY, (0, c*SQUARE_SIZE),(WIDTH, c * SQUARE_SIZE))

    def __repr__(self):
        return '{} {}'.format(ROWS, COLS)