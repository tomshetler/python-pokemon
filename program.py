import pokemon
import trainer
import battle

bulbasaur = pokemon.Pokemon("Bulbasaur", "Grass", 50, {1: {"Tackle": 10}, 2: {"Growl": 5}}, None)
charmander = pokemon.Pokemon("Charmander", "Fire", 50, {1: {"Scratch": 10}, 2: {"Tail-Whip": 5}}, None)
squirtle = pokemon.Pokemon("Squirtle", "Water", 100, {"Tackle": 10, "Growl": 5}, None)
pikachu = pokemon.Pokemon("Pikachu", "Electric", 50, {"Thundershock": 20, "Tail-Whip": 5}, None)

available_pokemon = [bulbasaur, charmander, squirtle, pikachu]

red = trainer.Trainer("Red", [], [])
blue = trainer.Trainer("Blue", [], [])

print("WELCOME TO POKEMON!")
print("Choose a fighter: ")
count = 0
for pokemon in available_pokemon:
    print("{}: {}".format(count, pokemon.name))
    count += 1
poke_num = int(input())
red.pokemon_list.append(available_pokemon[poke_num])

for pokemon in red.pokemon_list:
    print(pokemon.name)

choice = red.choose_pokemon()

choice.display_stats()
print()
charmander.display_stats()
print()
battle = battle.Battle(choice, charmander)
battle.display_fight()
print()

turn = 0

result = battle.determine_winner(choice, charmander)

while not result:
    if turn % 2 == 0:
        battle.battle_options(choice, charmander)
    else:
        battle.simulate_battle_options(charmander, choice)
    result = battle.determine_winner(choice, charmander)
    turn += 1
