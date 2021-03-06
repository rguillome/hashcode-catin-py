import numpy as np
import sys

file_in = sys.argv[1]
################### READ ######################
###############################################

# A - example
with open(file_in+'.txt', 'r') as f:
    lines = f.readlines()
    book_nb, lib_nb, max_time = np.array(
        [int(x) for x in lines[0].split()])
    scores = np.array([int(x) for x in lines[1].split()])
    # print(book_nb, lib_nb, days, scores)

    lib_data = []
    for l in range(2, len(lines)-1, 2):
        lib_para = np.array([int(x) for x in lines[l].split()])
        ids = np.array([int(x) for x in lines[l+1].split()])
        lib_data.append([lib_para, ids])

# print(lib_data)
print("START")

lib_scores = np.zeros(lib_nb)
for k in range(int(lib_nb)):
    nb_books = lib_data[k][0][0]  # books in lib k
    signup = lib_data[k][0][1]
    bookpday = lib_data[k][0][2]
    # print("books", lib_data[k][1])
    total_score = np.sum(scores[lib_data[k][1]])
    print(nb_books, signup, bookpday)
    lib_score = total_score/nb_books*bookpday/signup
    lib_scores[k] = lib_score
print(lib_scores)

################### SOLVE ######################
###############################################

lib_ordered = np.argsort(lib_scores)
lib_ordered = lib_ordered[::-1]

current_time = 0
end_idx = 0
books_already_scanned = []

libs_final = []

print("begin out")
while current_time < max_time and end_idx < len(lib_ordered):

    index = lib_ordered[end_idx]
    print("dealing lib ", end_idx)
    current_time += lib_data[index][0][1]

    estimated_max_time = max_time - current_time - \
        int(lib_data[index][0][2]/lib_data[index][0][0])
    nb_books_allowed = min(lib_data[index][0][0], estimated_max_time)

    books_in_lib = lib_data[index][1]

    books_in_lib = sorted(books_in_lib, key=lambda elt: scores[elt], reverse=True)
    books_to_scan = []

    books_already_scanned = np.zeros((len(scores)))
    for book in books_in_lib:
        if books_already_scanned[book] == 0 and nb_books_allowed > 0:
            books_to_scan.append(book)
            books_already_scanned[book] = 1
            nb_books_allowed -= 1
        if nb_books_allowed <= 0:
            break

    libs_final.append({
        'id': index,
        'nb_books': len(books_to_scan),
        'ids': [str(x) for x in books_to_scan]
    })

    end_idx += 1

nb_lib = end_idx
# print(nb_lib)
# print(libs_final)

################### WRITE ######################
###############################################


list_section = ''

for lib in libs_final:
    print(lib)

    if lib["nb_books"] <= 0:
        nb_lib -= 1
    else:
        list_section += '{} {}\n'.format(lib["id"], lib["nb_books"])
        list_section += ' '.join(lib["ids"])+'\n'

str_out = '{}\n'.format(nb_lib)
str_out += list_section

with open('{}_out.txt'.format(file_in), 'w') as file_out:
    file_out.write(str_out)

print(lib_data)
