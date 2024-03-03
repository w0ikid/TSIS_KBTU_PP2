my_list = ['KBTU', 'BANAN', 'NURIK']

with open('my_file.txt', 'w') as file:
    file.write(' '.join(my_list))