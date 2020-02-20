import numpy as np

#A - example
with open('a_example.txt', 'r') as f:
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