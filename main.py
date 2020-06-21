from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 150, "black")
thunder = Spell("Thunder", 15, 175, "black")
blizzard = Spell("Blizzard", 20, 200, "black")
meteor = Spell("Meteor", 25, 250, "black")
quake = Spell("Quake", 30, 300, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "black")

# Create Some Items.
potion = Item("Potion", "potion", "heals 50hp", 50)
high_potion = Item("High-Potion", "potion", "heals 100hp", 100)
super_potion = Item("Super-Potion", "potion", "heals 500hp", 500)
elixir = Item("Elixir", "elixir", "fully restores HP/MP of one party member", 9999)
high_elixir = Item("High-Elixir", "elixir", "fully restore party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "deals 500 damage", 500)

# Creating List Variables.
player_magic = [fire, thunder, blizzard, cure, cura]
player_items = [
    {"item": potion, "quantity": 5},
    {"item": high_potion, "quantity": 5},
    {"item": super_potion, "quantity": 5},
    {"item": elixir, "quantity": 2},
    {"item": high_elixir, "quantity": 2}
]

# Instantiate People
player = Person(460, 65, 60, 34, player_magic, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

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

        if magic_choice == -1:
            continue

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

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item : ")) - 1

        if item_choice == - 1:
            continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "This current item is no longer available." + bcolors.END_C)
            continue

        player.items[item_choice]["quantity"] -= 1

        if item.item_type == "potion":
            player.heal(item.prop)
            print(bcolors.OK_GREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.END_C)
        elif item.item_type == "elixir":
            player.hp = player.max_hp
            player.mp = player.max_mp
            print(bcolors.OK_GREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.END_C)
        elif item.item_type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.END_C)

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
