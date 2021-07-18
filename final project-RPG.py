class Location:
    def __init__(self, name, description):
        # YOUR CODE HERE
        self.name = name
        self.description = description
        self.north = None
        self.south = None
        self.west = None
        self.east = None

    def possible_moves(self):
        # YOUR CODE HERE
        ret = []
        if self.north != None:
            ret.append(self.north)
        if self.south != None:
            ret.append(self.south)
        if self.east != None:
            ret.append(self.east)
        if self.west != None:
            ret.append(self.west)
        return ret

    def __str__(self):
        # YOUR CODE HERE
        lon = len(self.name)
        return '#' * (lon + 4) + '\n# ' + self.name + ' #\n' + '#' * (lon + 4) + '\n\n' + self.description + '\n'
water_pavilion = Location('Water Pavilion','Welcome to the hottest place in DKU!')
bridge_center = Location('Bridge: Center','Welcome to the bridge in front of the hottest place in DKU!')
bridge_north  = Location('Bridge: North','Welcome to the north of the bridge that in front of the hottest place in DKU!')
bridge_east = Location('Bridge: East','Welcome to the east of the bridge that in front of the hottest place in DKU!')
bridge_west = Location('Bridge: West','Welcome to the west of the bridge that in front of the hottest place in DKU!')
cc_east_ent = Location('Conference Center: East Entrance','You can run away from this prison toward west from here!')

cc_east_ent.east = bridge_west
bridge_west.west = cc_east_ent
bridge_west.east = bridge_center
bridge_center.west = bridge_west
bridge_center.east = bridge_east
bridge_east.west = bridge_center
bridge_center.north = bridge_north
bridge_north.south = bridge_center
bridge_center.south = water_pavilion
water_pavilion.north = bridge_center
import random


class Character:
    def __init__(self, name, location, sym):
        # YOUR CODE HERE

        self.name = name
        self.location = location
        self.sym = sym
        self.role = None
        self.hp = 50
        self.total_hp = 50
        self.speed = 5
        self.strength = 5

    def __str__(self):
        # YOUR CODE HERE
        return '################\n# {} #\n################\n\nHP: {} / {}\nSpeed: {}\nStrength: {}\nLocation: {}\n'.format(
            self.name, self.hp, self.total_hp, self.speed, self.strength, self.location)

    def __gt__(self, other):
        # YOUR CODE HERE
        p = self.speed / (self.speed + other.speed)
        return random.random() < p

    def attack(self, enemy):
        # YOUR CODE HERE
        if self > enemy:
            damage = int(random.random() * self.strength) + 1
            enemy.hp -= damage
            return '{} attacks {} for {} damage!'.format(self.name, enemy.name, damage)
        else:
            return '{} attacks {} but misses!'.format(self.name, enemy.name)

    def flee(self, enemy):
        # YOUR CODE HERE
        n = len(self.location.possible_moves())
        if self > enemy:
            self.location = self.location.possible_moves()[int(random.random() * n) - 1]
            return True
        else:
            return False

    def move(self, direction):
        # YOUR CODE HERE
        if direction == 'n':
            if self.location.north != None:
                self.location = self.location.north
                return True
            else:
                return False
        if direction == 's':
            if self.location.south != None:
                self.location = self.location.south
                return True
            else:
                return False
        if direction == 'e':
            if self.location.east != None:
                self.location = self.location.east
                return True
            else:
                return False
        if direction == 'w':
            if self.location.west != None:
                self.location = self.location.west
                return True
            else:
                return False

    def is_dead(self):
        # YOUR CODE HERE
        return self.hp <= 0

    def reset(self):
        # YOUR CODE HERE
        self.hp = self.total_hp




class Warrior(Character):
    def __init__(self, name, loc, sym):
        Character.__init__(self, name, loc, sym)
        self.role = 'Warrior'
        self.strength=10

    def __str__(self):
        l = len(self.name)
        return '#' * (l + 4) + '\n# ' + self.name + ' #\n' + '#' * (
                    l + 4) + '\n\nRole: {}\nHP: {} / {}\nSpeed: {}\nStrength: {}\nLocation: {}\n'.format(self.role,self.hp,self.total_hp,self.speed,self.strength,self.location.name)


class Goblin(Character):
    def __init__(self, name, loc, sym):
        Character.__init__(self, name, loc, sym)
        self.role = 'Goblin'
        self.hp = 35
        self.total_hp = 35
        self.strehgth = 5
        self.speed = 3

    def __str__(self):
        l = len(self.name)
        return '#' * (l + 4) + '\n# ' + self.name + ' #\n' + '#' * (l + 4) + '\n\nRole: {}\nHP: {} / {}\nSpeed: {}\nStrength: {}\nLocation: {}\n'.format(self.role,self.hp,self.total_hp,self.speed,self.strength,self.location.name)

    def move(self):
        ret=[]
        if self.location.north!=None:
            ret.append(self.location.north)
        if self.location.south!=None:
            ret.append(self.location.south)
        if self.location.east!=None:
            ret.append(self.location.east)
        if self.location.west!=None:
            ret.append(self.location.west)
        self.location=random.choice(ret)
random.seed(0)

daniel = Warrior('Daniel', water_pavilion, 'D')
uurlok = Goblin('Uur\'lok', bridge_north, 'U')

assert str(daniel) == '##########\n# Daniel #\n##########\n\nRole: Warrior\nHP: 50 / 50\nSpeed: 5\nStrength: 10\nLocation: Water Pavilion\n'
assert str(uurlok) == "###########\n# Uur'lok #\n###########\n\nRole: Goblin\nHP: 35 / 35\nSpeed: 3\nStrength: 5\nLocation: Bridge: North\n"

uurlok.move()
assert uurlok.location == bridge_center

uurlok.move()
assert uurlok.location in [bridge_north,water_pavilion,bridge_east,bridge_west]
assert uurlok.location == bridge_west

uurlok.move()
assert uurlok.location == bridge_center
class Map:
    def __init__(self, start):
        self.start = start
        self.bn = " "
        self.cee = " "
        self.bw = " "
        self.bc = " "
        self.be = " "
        self.wp = " "
        self.MAP = "---------\n|X|X|" + self.bn + "|X|\n---------\n|" + self.cee + "|" + self.bw + "|" + self.bc + "|" + self.be + "|\n---------\n|X|X|" + self.wp + "|X|\n---------\n"

    def str_w_chars(self, characters):
        for people in characters:
            if people.location==bridge_north:
                self.bn=people.sym
            if people.location==cc_east_ent:
                self.cee=people.sym
            if people.location==bridge_west:
                self.bw=people.sym
            if people.location==bridge_center:
                self.bc=people.sym
            if people.location==bridge_east:
                self.be=people.sym
            if people.location==water_pavilion:
                self.wp=people.sym
        self.AP = "---------\n|X|X|" + self.bn + "|X|\n---------\n|" + self.cee + "|" + self.bw + "|" + self.bc + "|" + self.be + "|\n---------\n|X|X|" + self.wp + "|X|\n---------\n"
        return self.AP

    def __str__(self):
        return '---------\n|X|X| |X|\n---------\n| | | | |\n---------\n|X|X| |X|\n---------\n'


m1 = Map(water_pavilion)
assert str(m1) == '---------\n|X|X| |X|\n---------\n| | | | |\n---------\n|X|X| |X|\n---------\n'
assert m1.str_w_chars([daniel,uurlok]) == '---------\n|X|X| |X|\n---------\n| | |U| |\n---------\n|X|X|D|X|\n---------\n'

m2 = Map(bridge_west)
assert str(m1) == str(m2)
assert m1.str_w_chars([daniel,uurlok]) == m2.str_w_chars([daniel,uurlok])

