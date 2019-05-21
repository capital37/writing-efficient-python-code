# Creates an indexed list of objects:

# Enumerate creates an index item pair for each item in the object provided

letters = ['a', 'b', 'c', 'd']

index_letters = enumerate(letters) # or: index_letters_list = [*enumerate(letters)]

index_letters_list = list(index_letters)
print(index_letters_list)

# indexing a list in a for loop
for index, letter in enumerate(letters):
    print(f'index:{index}, value:{letter}')
