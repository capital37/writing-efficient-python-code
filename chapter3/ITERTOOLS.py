# Create combinations with itertools

from itertools import combinations

# Create a combination object with pairs of Pokémon
pokemon = ['poke1', 'poke2', 'poke3', 'poke4', 'poke5']
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)
