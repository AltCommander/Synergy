class Kassa(object):
    def __init__(self):
        self.money = 0

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, x):
        if self.money >= x:
            self.money -= x
        else:
            print("Недостаточно средств")