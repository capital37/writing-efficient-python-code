# Combining with zip function
names = ['Bulbasaur', 'Charmander', 'Squirtle']
hps = [45, 39, 44]

combined_zip = zip(names, hps)
print(type(combined_zip))

combined_zip_list = [*combined_zip]
print(combined_zip_list)

# Combinations with itertools
from itertools import combinations

poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']
combos_obj = combinations(poke_types, 2)
print(type(combos_obj))

combos = [*combos_obj]
print(combos)

