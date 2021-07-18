import random


class Player:
    def __init__(self, name, ht, wt, sh2_per, sh2_tot, sh3_per, sh3_tot, reb, st, bl):
        self.name = name
        self.ht = ht
        self.wt = wt
        self.sh2_per = sh2_per
        self.sh2_tot = sh2_tot
        self.sh3_tot = sh3_tot
        self.sh3_per = sh3_per
        self.reb = reb
        self.st = st
        self.bl = bl

    def __str__(self):
        return self.name

    def shoot(self):
        index = random.random()
        if index < float(self.sh2_tot):
            if index < float(self.sh2_per):
                return 2
            else:
                return -2
        else:
            if index < float(self.sh3_tot):
                if index < float(self.sh3_per):
                    return 3
            else:
                return -3
random.seed(0)

Kobe = Player('Kobe Bryant', 78, 212, .479, 15.3, .329, 4.1, 5.2, 1.4, .5)
Shaq = Player('Shaquille O\'neal', 85, 325, .582, 16.1, 0, 0, 10.9, .6, 2.3)

print(Kobe.shoot())

