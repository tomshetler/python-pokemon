import pokemon
import trainer
import battle
import random


def team_selection(owner):
    print("Choose a fighter: ")
    count = 0
    for fighter in available_pokemon:
        print("{}: {}".format(count, fighter.name))
        count += 1
    poke_num = int(input())
    available_pokemon[poke_num].trainer = owner
    owner.pokemon_list.append(available_pokemon[poke_num])
    available_pokemon.pop(poke_num)


def simulate_team_selection(owner):
    com_poke_num = random.randint(0, len(available_pokemon))
    available_pokemon[com_poke_num].trainer = owner
    owner.pokemon_list.append(available_pokemon[com_poke_num])
    available_pokemon.pop(com_poke_num)

bulbasaur = pokemon.Pokemon("Bulbasaur", "Grass", 50, {1: {"Tackle": 10}, 2: {"Growl": 5}}, None)
charmander = pokemon.Pokemon("Charmander", "Fire", 50, {1: {"Scratch": 10}, 2: {"Tail-Whip": 5}}, None)
squirtle = pokemon.Pokemon("Squirtle", "Water", 50, {1: {"Tackle": 10}, 2: {"Growl": 5}}, None)
pikachu = pokemon.Pokemon("Pikachu", "Electric", 50, {1: {"Thundershock": 20}, 2: {"Tail-Whip": 5}}, None)

available_pokemon = [bulbasaur, charmander, squirtle, pikachu]

red = trainer.Trainer("Red", [], {"Potions": 3})
blue = trainer.Trainer("Blue", [], {"Potions": 3})

print("WELCOME TO POKEMON!")
print()

team_selection(red)
simulate_team_selection(blue)


print()

red_choice = red.choose_pokemon()
blue_choice = blue.simulate_choose_pokemon()
print()
red_choice.display_stats()
print()
blue_choice.display_stats()
print()
new_battle = battle.Battle(red_choice, blue_choice)
new_battle.display_fight()
print()

turn = 0

result = new_battle.determine_winner(red_choice, blue_choice)

while not result:
    if turn % 2 == 0:
        new_battle.battle_options(red_choice, blue_choice)
    else:
        new_battle.simulate_battle_options(blue_choice, red_choice)
    result = new_battle.determine_winner(red_choice, blue_choice)
    turn += 1
