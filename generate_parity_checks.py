

l = 3

# row first ordering
def coordinates_to_index(x, y):
    return x + y * l

def index_to_coordinates(i):
    return i % l, i // l 

# There are l^2 X-checks and l^2 Z-checks.
# There are l^2 vertical qubits and l^2 horizontal qubits.
# Vertical qubits are indexed from 0 to l^2 - 1.
# Horizontal qubits are indexed from l^2 to 2 * l^2 - 1.

def generate_Hx(l):
    Hx = []
    for x in range(l):
        for y in range(l):
            vertical_qubit_below = coordinates_to_index(x, (y - 1) % l)
            vertical_qubit_above = coordinates_to_index(x, y)
            horizontal_qubit_on_the_left = l*l + coordinates_to_index((x - 1) % l, y)
            horizontal_qubit_on_the_right = l*l + coordinates_to_index(x, y)
            X_check = [vertical_qubit_below, vertical_qubit_above, horizontal_qubit_on_the_left, horizontal_qubit_on_the_right]
            Hx.append(X_check)
    return Hx

# Hx = generate_Hx(l)
# print(Hx)

def generate_Hz(l):
    Hz = []
    for x in range(l):
        for y in range(l):
            vertical_qubit_on_the_left = coordinates_to_index(x, y)
            vertical_qubit_on_the_right = coordinates_to_index((x + 1) % l, y)
            horizontal_qubit_below = l*l + coordinates_to_index(x, y)
            horizontal_qubit_above = l*l + coordinates_to_index(x, (y + 1) % l)
            Z_check = [vertical_qubit_on_the_left, vertical_qubit_on_the_right, horizontal_qubit_below, horizontal_qubit_above]
            Hz.append(Z_check)
    return Hz

# Hz = generate_Hz(l)
# print(Hz)

# for X_check in Hx:
#     for Z_check in Hz:
#         w = 0
#         for q in X_check:
#             if q in Z_check:
#                 w += 1
#         print(w)


# Convert Hx and Hz to dense matrices.
# Compute their row echelon forms (Gaussion elimination).
# Generate a random error and visualize it.
# Visualize the syndrome.
# Visualize a recovery.
# Compute wether there was a logical error.
# 
# syndrome computation from parity check matrix
# total error operator is always a cycle (since it has zero syndrome)
# this operator is trivial iff it is a boundary.
# Possible to check its scalar product with the other logical operators.
# -> no need for Gaussian elimination.
# -> no need for dense parity check matrices.
# Give the two other logical operators explicitely manually   



