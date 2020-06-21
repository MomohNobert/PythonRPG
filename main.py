from classes.game import Person, bcolors


magic = [
    {"name": "Fire", "cost": 10, "dmg": 160},
    {"name": "Thunder", "cost": 15, "dmg": 175},
    {"name": "Blizzard", "cost": 20, "dmg": 190},
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

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("You're attacked by the enemy. You take {} points of damage. Your HP: {}".format(enemy_dmg, player.get_hp()))

    if enemy.get_hp() == 0:
        print(bcolors.OK_GREEN + "You win!" + bcolors.END_C)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lose!" + bcolors.END_C)
        running = False



