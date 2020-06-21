from classes.game import Person, bcolors


magic = [
    {"name": "Fire", "cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 15, "dmg": 75},
    {"name": "Blizzard", "cost": 20, "dmg": 90},
]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'An Enemy Attacks!' + bcolors.END_C)

while running:
    print("===============================")
    player.choose_action()
    choice = input("Choose Action : ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for {} points of damage. Enemy HP: {}".format(dmg, enemy.get_hp()))

    # running = False

