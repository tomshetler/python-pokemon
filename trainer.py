import random

class Trainer:
    def __init__(self, name, pokemon_list, items_list):
        self.name = name
        self.pokemon_list = pokemon_list
        self.items_list = items_list

    def choose_pokemon(self):
        print("Please choose an available pokemon: ")
        count = 0
        for item in self.pokemon_list:
            print("{}: {}".format(count, item.name))
            count += 1
        pokemon_choice = int(input())
        selection = self.pokemon_list[pokemon_choice]
        print("{} has chosen: {}".format(self.name, selection.name))
        return selection

    def simulate_choose_pokemon(self):
        # pokemon_choice = random.randint(0, len(self.pokemon_list))
        pokemon_choice = 0
        selection = self.pokemon_list[pokemon_choice]
        print("{} has chosen: {}".format(self.name, selection.name))
        return selection

