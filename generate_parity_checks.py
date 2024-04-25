from utilities import l, coordinates_to_index, index_to_coordinates, write_matrix_to_file

# There are l^2 X-checks and l^2 Z-checks.
# There are l^2 vertical qubits and l^2 horizontal qubits.
# Vertical qubits are indexed from 0 to l^2 - 1.
# Horizontal qubits are indexed from l^2 to 2 * l^2 - 1.

def generate_Hx(l):
    Hx = []
    for y in range(l):
        for x in range(l):
            vertical_qubit_below = coordinates_to_index(x, (y - 1) % l)
            vertical_qubit_above = coordinates_to_index(x, y)
            horizontal_qubit_on_the_left = l*l + coordinates_to_index((x - 1) % l, y)
            horizontal_qubit_on_the_right = l*l + coordinates_to_index(x, y)
            X_check = [vertical_qubit_below, vertical_qubit_above, horizontal_qubit_on_the_left, horizontal_qubit_on_the_right]
            Hx.append(X_check)
    return Hx

# Hx = generate_Hx(l)
# print(Hx)
# write_matrix_to_file(Hx, 'data/Hx_{}.txt'.format(l))

def generate_Hz(l):
    Hz = []
    for y in range(l):
        for x in range(l):
            vertical_qubit_on_the_left = coordinates_to_index(x, y)
            vertical_qubit_on_the_right = coordinates_to_index((x + 1) % l, y)
            horizontal_qubit_below = l*l + coordinates_to_index(x, y)
            horizontal_qubit_above = l*l + coordinates_to_index(x, (y + 1) % l)
            Z_check = [vertical_qubit_on_the_left, vertical_qubit_on_the_right, horizontal_qubit_below, horizontal_qubit_above]
            Hz.append(Z_check)
    return Hz

# Hz = generate_Hz(l)
# print(Hz)

# Verify that the two parity check matrices are orthogonal (i.e. the measurements corresponding to checks commute).
# for X_check in Hx:
#     for Z_check in Hz:
#         w = 0
#         for q in X_check:
#             if q in Z_check:
#                 w += 1
#         print(w)


