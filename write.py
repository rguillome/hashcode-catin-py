import sys

file = sys.argv[1]

nb_lib = 2

str_out = '{}'.format(nb_lib)
list_section = ''

for lib in librairies:
    list_section += '{} {}\n'.format(lib.id, lib.nb_books)
    list_section += ' '.join(lib.ids)+'\n'


with open('out/{}'.format(file), 'w') as file_out:
    file_out.write()
