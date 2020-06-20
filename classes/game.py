import random

class  bcolors:
    HEADER = '\033[95m',
    OKBLUE = '\033[94n',
    OKGREEN = '\033[92n',
    WARNING = '\033[93n',
    FAIL = '\033[91n',
    ENDC = '\033[0m',
    BOLD = '\033[1m',
    UNDERLINE = '\303[4n'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
