l = 15

# row first ordering
def coordinates_to_index(x, y):
    return x + y * l

def index_to_coordinates(i):
    return i % l, i // l

def qubit_index_to_coordinates(qubit):
    coordinates = index_to_coordinates(qubit % (l*l))
    is_horizontal = qubit // (l*l)
    return coordinates, is_horizontal

def add_mod_two(list_1, list_2):
    result = list_1.copy()
    for element in list_2:
        # print(result)
        if element in list_1:
            result.remove(element)
        else:
            result.append(element)
    return result

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as f:
        for X_check in matrix:
            for q in X_check:
                f.write(str(q) + ' ')
            f.write('\n')

def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            check = [int(q) for q in line.split()]
            matrix.append(check)
    return matrix

def fill_mod_l(a, b, l):
    if  a==b :
        return []
    if b < a:
        return fill_mod_l(b, a, l)
    else: # a < b
        if (b - a) % l < (a - b) % l:
            return [i for i in range(a, b)]
        else:
            return ([i for i in range(b, l)] + [i for i in range(0, a)])

# fill = fill_mod_l(2, 6, 7)
# print(fill)
