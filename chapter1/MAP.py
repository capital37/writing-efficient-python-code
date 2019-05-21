# Map applies a function to each element in an object

nums = [1.5, 2.3, 3.4, 4.6, 5.0]

rnd_nums = map(round, nums)

print(nums)
print(list(rnd_nums))

# Map can also be used with lambda, or an anonymous function
nums = [1, 2, 3, 4, 5]
sqrd_nums = map(lambda x: x**2, nums)
print(list(sqrd_nums))

#----------------------------------------------------------------#
# Another way of making lists with map and unpacking with '*'

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Use map to apply str.upper to each element in names
names_map  = map(lambda x: x.upper(), names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
