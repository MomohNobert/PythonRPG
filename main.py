from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 150, "black")
thunder = Spell("Thunder", 15, 175, "black")
blizzard = Spell("Blizzard", 20, 200, "black")
meteor = Spell("Meteor", 25, 250, "black")
quake = Spell("Quake", 30, 300, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "black")

# Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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
        print("You attacked for {} points of damage.".format(dmg))
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic : ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot Enough MP\n" + bcolors.END_C)
            continue

        player.reduce_mp(spell.cost)

        if spell.spell_type == "white":
            player.heal(magic_dmg)
            print(bcolors.OK_GREEN + "\n" + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.END_C)
        elif spell.spell_type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OK_BLUE + "\n" + spell.name + " deals", str(magic_dmg), " points of damage" + bcolors.END_C)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("You're attacked by the enemy. You take {} points of damage".format(enemy_dmg))

    print('------------------------------------')
    print("Enemy HP : ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.END_C + "\n")
    print("Your HP : ", bcolors.OK_GREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.END_C)
    print("Your MP : ", bcolors.OK_BLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.END_C + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OK_GREEN + "You win!" + bcolors.END_C)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lose!" + bcolors.END_C)
        running = False
