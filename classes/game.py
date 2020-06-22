import random
from .magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\303[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

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

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.END_C)
        print(bcolors.OK_BLUE + bcolors.BOLD + "    Actions." + bcolors.END_C)
        for item in self.actions:
            print("        " + str(i) + ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OK_BLUE + bcolors.BOLD + "    Magic." + bcolors.END_C)
        for spell in self.magic:
            print("        " + str(i) + ':', spell.name, "(cost", str(spell.dmg) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OK_GREEN + bcolors.BOLD + "    Items." + bcolors.END_C)
        for item in self.items:
            name = item["item"].name
            description = item["item"].description
            quantity = str(item["quantity"])
            print("        " + str(i) + ".", name, ":", description, " (x" + quantity + ") ")
            i += 1

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 4

        mp_bar = ""
        mp_bar_ticks = (self.hp / self.max_hp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        print("                       ___________________________             ____________")
        print(bcolors.BOLD + self.name + "      " +
              str(self.hp) + "/" + str(self.max_hp) + "  " + bcolors.OK_GREEN + "|" + hp_bar + "|    "
              + str(self.mp) + "/" + str(self.max_mp) + "  " + bcolors.OK_BLUE + "|" + mp_bar + '|')

