import random

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
                if defender.health <= 0:
                    print("{} has fainted!".format(defender.name))
                else:
                    print("{} now has {} health remaining".format(defender.name, defender.health))
                print()

    def battle_item(self, attacker):
        attacker.trainer.items_list["Potions"] -= 1
        attacker.health += 10
        print("{} uses a potion".format(attacker.trainer.name))
        print("{}'s health has now risen to {}".format(attacker.name, attacker.health))
        print("{} now has {} items left".format(attacker.trainer.name, attacker.trainer.items_list["Potions"]))
        print()

    def battle_options(self, attacker, defender):
        print("Your turn {}".format(attacker.trainer.name))
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
            self.battle_attack(attack_method, attacker, defender)
        elif option == "B":
            if attacker.trainer.items_list["Potions"] > 0:
                self.battle_item(attacker)
            else:
                print("Not an option!")
                self.battle_options(attacker, defender)

    def simulate_battle_options(self, attacker, defender):
        choice = random.randint(1, 2)
        option = ''
        if choice == 1:
            option = "A"
        elif choice == 2:
            option = "B"
        if option == "A":
            attack_method = random.randint(1, 2)
            self.battle_attack(attack_method, attacker, defender)
        elif option == "B":
            if attacker.trainer.items_list["Potions"] > 0:
                self.battle_item(attacker)
            else:
                print("Not an option!")
                self.simulate_battle_options(attacker, defender)


    def determine_winner(self, fighter_A, fighter_B):
        if fighter_A.health <= 0:
            print("{} WINS!".format(fighter_B.name))
            return True
        elif fighter_B.health <= 0:
            print("{} WINS!".format(fighter_A.name))
            return True
        else:
            return False