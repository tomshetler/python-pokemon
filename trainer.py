class Trainer:
    def __init__(self, name, pokemon_list, items):
        self.name = name
        self.pokemon_list = pokemon_list
        self.items = items

    def choose_pokemon(self):
        print("Please choose an available pokemon: ")
        count = 0
        for item in self.pokemon_list:
            print("{}: {}".format(count, item.name))
            count += 1
        pokemon_choice = int(input())
        selection = self.pokemon_list[pokemon_choice]
        return selection