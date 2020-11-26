from .constants import BLUE, WHITE, BLACK, ROWS, COLS, SQUARE_SIZE
import pygame, time

class Unit:
    def __init__(self, row, col, living):
        self.neighbors = 0
        self.row = row
        self.col = col
        self.living = living
        self.iterations = 0
        self.color = self.getColor()
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row
    
    def make_living(self):
        self.living = True
        self.color = BLUE

    def make_dead(self):
        self.living = False
        self.color = WHITE
        self.iterations = 0
    
    def check_living(self):
        return self.living
    
    def getColor(self):
        if self.living:
            return BLUE
        else:
            return WHITE

    def check_neighbors(self):
        return int(self.neighbors)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

    def __repr__(self):
        return f'Living: {self.living} Color: {self.color} (Row, Col) : ({self.row},{self.col}) (X,Y): ({self.x}, {self.y})'


    

