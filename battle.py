import random

# First, we need a class to create the fighters

class Pokemon:
    def __init__(self, name, type, health, attacks):
        self.name = name
        self.type = type
        self.health = health
        self.attacks = attacks

    def attack(self, attack_method):
        if attack_method in self.attacks:
            damage = self.attacks[attack_method]
        return damage

    def display_stats(self):
        print("Name: {}".format(self.name))
        print("Type: {}".format(self.type))
        print("Health: {}".format(self.health))
        for attack_num in self.attacks:
            for attack, damage in self.attacks[attack_num].items():
                print("{}: {}".format(attack, damage))


# Now we need a class to create the fight itself

class Battle:
    def __init__(self, pokemon_A, pokemon_B):
        self.pokemon_A = pokemon_A
        self.pokemon_B = pokemon_B

    def display_fight(self):
        print("{} is about to fight {}".format(self.pokemon_A.name, self.pokemon_B.name))

    # For general battle methods, use generic names for variables
    def battle_attack(self, attack_method, attacker, defender):
        if attack_method in attacker.attacks:
            for attack, damage in attacker.attacks[attack_method].items():
                defender.health -= damage
                print("{} uses {} on {}".format(attacker.name, attack, defender.name))
                print("{} now has {} health remaining".format(defender.name, defender.health))
                print()

    def battle_item(self, attacker):
        attacker.health += 10
        print("{} uses a potion".format(attacker.name))
        print("{}'s health has now risen to {}".format(attacker.name, attacker.health))
        print()

    def battle_options(self, attacker, defender):
        print("Your turn {}".format(attacker.name))
        print("""What will you do?
        A: Fight
        B: Item""")
        option = input().upper()
        if option == "A":
            print("Choose an attack method: ")
            for attack_num in attacker.attacks:
                for attack_name in attacker.attacks[attack_num]:
                    print("{}: {}".format(attack_num, attack_name))
            attack_method = int(input())
            battle.battle_attack(attack_method, attacker, defender)
        elif option == "B":
            battle.battle_item(attacker)

    def simulate_battle_options(self, attacker, defender):
        choice = random.randint(1, 2)
        option = ''
        if choice == 1:
            option = "A"
        elif choice == 2:
            option = "B"
        if option == "A":
            attack_method = random.randint(1, 2)
            battle.battle_attack(attack_method, attacker, defender)
        elif option == "B":
            battle.battle_item(attacker)


    def determine_winner(self, fighter_A, fighter_B):
        if fighter_A.health <= 0:
            print("{} WINS!".format(fighter_B.name))
            return True
        elif fighter_B.health <= 0:
            print("{} WINS!".format(fighter_A.name))
            return True
        else:
            return False

bulbasaur = Pokemon("Bulbasaur", "Grass", 50, {1: {"Tackle": 10}, 2: {"Growl": 5}})
charmander = Pokemon("Charmander", "Fire", 50, {1: {"Scratch": 10}, 2: {"Tail-Whip": 5}})
# squirtle = Pokemon("Squirtle", "Water", 100, {"Tackle": 10, "Growl": 5})

# available_pokemon = [bulbasaur, charmander, squirtle]

bulbasaur.display_stats()
print()
charmander.display_stats()
print()
battle = Battle(bulbasaur, charmander)
battle.display_fight()
print()

turn = 0

result = battle.determine_winner(bulbasaur, charmander)

while not result:
    if turn % 2 == 0:
        battle.battle_options(bulbasaur, charmander)
    else:
        battle.simulate_battle_options(charmander, bulbasaur)
    result = battle.determine_winner(bulbasaur, charmander)
    turn += 1
