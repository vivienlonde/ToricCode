import random as rd

l = 3
p = 0.1

def simulate_noise(l, p_error):
    error = []
    for q in range(2 * l * l):
        if rd.random() < p_error:
            error.append(q)
    return error

def compute_syndrome(error, H):
    syndrome = []
    for check in H:
        w = 0
        for q in check:
            if q in error:
                w += 1
        syndrome.append(w % 2)
    return syndrome

def decode(syndrome):
    return error # for now: perfect decoder ;)

# error = simulate_noise(l, p)
# print(error)
# syndrome = compute_syndrome(error, Hx, Hz)
# recovery = decode(syndrome)
# total_error = error + recovery

def generate_X_logicals(l):
    horizontal_X_logical = [i for i in range(l)]
    vertical_X_logical = [l*i for i in range(l*l, l*l + l)]
    X_logicals = [horizontal_X_logical, vertical_X_logical]
    return X_logicals

X_logicals = generate_X_logicals(l)
print(X_logicals)

def generate_Z_logicals(l):
    horizontal_Z_logical = [i for i in range(l*l, l*l + l)]
    vertical_Z_logical = [l*i for i in range(l)]
    Z_logicals = [horizontal_Z_logical, vertical_Z_logical]
    return Z_logicals

Z_logicals = generate_Z_logicals(l)
print(Z_logicals)
