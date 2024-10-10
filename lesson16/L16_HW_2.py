class Turtle(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.s = 1

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            print("Черепшка больше не может деградировать.")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
            
        total_distance = dx + dy
            
        moves = total_distance // self.s

        if total_distance % self.s != 0:
            moves += 1

        return moves