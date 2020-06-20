import random


class Colors:
    HEADER = '\033[95m',
    OK_BLUE = '\033[94n',
    OK_GREEN = '\033[92n',
    WARNING = '\033[93n',
    FAIL = '\033[91n',
    END_C = '\033[0m',
    BOLD = '\033[1m',
    UNDERLINE = '\303[4n'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']

    def choose_action(self):
        i = 1
        print('Actions.')
        for item in self.actions:
            print(str(i) + ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print('Magic.')
        for spell in self.magic:
            print(str(i) + ':', spell['name'], "(cost", str(spell['mp']) + ')')
            i += 1
