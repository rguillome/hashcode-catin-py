#A - example
with open('a_example.txt', 'r') as f:
    lines = f.readlines()
    book_nb, lib_nb, days = lines[0].split()
    scores = lines[1].split()
    print(book_nb, lib_nb, days, scores)

    lib_data = []
    for l in range(2, len(lines), 2):
        lib_para = lines[l].split()
        ids = lines[l+1].split()
        lib_data.append([lib_para, ids])
   
print(lib_data)