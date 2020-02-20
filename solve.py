import numpy as np
import sys

################### READ ######################
###############################################

file_in = sys.argv[1]
#A - example
with open(file_in+'.txt', 'r') as f:
    lines = f.readlines()
    book_nb, lib_nb, days = np.array([int(x) for x in lines[0].split()])
    scores = np.array([int(x) for x in lines[1].split()])
    print(book_nb, lib_nb, days, scores)

    lib_data = []
    for l in range(2, len(lines), 2):
        lib_para = np.array([int(x) for x in lines[l].split()])
        ids = np.array([int(x) for x in lines[l+1].split()])
        lib_data.append([lib_para, ids])
   
print(lib_data)
print("START")

lib_scores = np.array([])
for k in range(int(lib_nb)):
    nb_books = lib_data[k][0][0] #books in lib k
    signup = lib_data[k][0][1] 
    bookpday = lib_data[k][0][1]
    print("score", scores)
    print("books", lib_data[k][1])
    total_score = np.sum(scores[lib_data[k][1]])
    print(total_score)

################### SOLVE ######################
###############################################


nb_lib = 2

libs = [{
    'id': 0,
    'nb_books': 5,
    'ids': ["0", "1", "2", "3", "4"]
},
    {
    'id': 1,
    'nb_books': 1,
    'ids': ["5"]
}]


################### WRITE ######################
###############################################


str_out = '{}\n'.format(nb_lib)
list_section = ''

for lib in libs:
    print(lib)
    list_section += '{} {}\n'.format(lib["id"], lib["nb_books"])
    list_section += ' '.join(lib["ids"])+'\n'

str_out += list_section

with open('{}_out.txt'.format(file_in), 'w') as file_out:
    file_out.write(str_out)


print(lib_data)
