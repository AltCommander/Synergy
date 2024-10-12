#0 - поле
#1 - дерево
#2 - река
#3 - госпиталь
#4 - магазин улучшений
#5 - огонь
from utils import randbool
from utils import randcell
from utils import randcell2
from clouds import Clouds

CELL_TYPES = "🟩🌲🌊🏥🏦🔥"
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 10000
BURNED_TREE = 10

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(3, 10)
        self.generate_river(10)
        self.generate_river(30)
        self.generate_upgrade_shop()
        self.generate_hospital()

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 
            or x >= self.h or y >= self.w):
            return False
        return True

    def print_map(self, heli, clouds):
        print("⬛" * (self.w + 2))
        for ri in range(self.h):
            print("⬛", end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print("⬜", end='')
                elif clouds.cells[ri][ci] == 2:
                    print("⚡", end='')
                elif (heli.x == ri and heli.y == ci):
                    print("🚁", end='')
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print("⬛")    
        print("⬛" * (self.w + 2))

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cy, cx = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        ry, rx = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cy, cx = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cy, cx = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()    

    def add_fire(self):
        c = randcell(self.w, self.h)
        cy, cx = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self, heli):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                    heli.score -= BURNED_TREE
        for i in range(10):
            self.add_fire()        


    def process_helicopter(self, heli, clouds):
        c = self.cells[heli.x][heli.y]
        d = clouds.cells[heli.x][heli.y]
        if (c == 2):
            heli.tank = heli.mxtank
        if (c == 5 and heli.tank > 0):
            heli.tank -= 1
            heli.score += TREE_BONUS
            self.cells[heli.x][heli.y] = 1
        if (c == 4 and heli.score >= UPGRADE_COST):
            heli.mxtank += 1
            heli.score -= UPGRADE_COST
        if (c == 3 and heli.score >= LIFE_COST):
            heli.lives += 10
            heli.score -= LIFE_COST
        if (d == 2):
            heli.lives -= 1
            if (heli.lives == 0):
                heli.game_over()

    def export_data(self):
        return {"cells": self.cells}
    
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]