from utilities import l, index_to_coordinates, add_mod_two, fill_mod_l

import networkx as nx

def compute_path_lengths(syndrome, l):
    """calculate the path lenghts between the unsatisfied checks 
    Input:
            syndrome: list of unsatisfied checks
    Output:
            path_lengths: array with for each element:
            [checkA, checkB, path_length]
    """
    path_lengths = []
    # for each stabilizer pair, calculate the minimum path length
    for i, checkA in enumerate(syndrome):
        xA, yA = index_to_coordinates(checkA) 
        for checkB in syndrome[i+1:]:
            xB, yB = index_to_coordinates(checkB)
            min_row_dif = min((xA - xB) % l, (xB- xA) % l)
            min_col_dif = min((yA - yB) % l, (yB - yA) % l)
            path_length = min_row_dif + min_col_dif
            path_lengths.append((checkA, checkB, path_length))
    return path_lengths

def compute_matching(syndrome, l):
    path_lengths = compute_path_lengths(syndrome, l)
    G = nx.Graph()
    for edge in path_lengths:
        G.add_edge(edge[0], edge[1], weight=-edge[2])
    matching = nx.algorithms.matching.max_weight_matching(G, maxcardinality=True)
    return matching

def compute_path(checkA, checkB, l):
    xA, yA = index_to_coordinates(checkA)
    # print('xA', xA, 'yA', yA)
    xB, yB = index_to_coordinates(checkB)
    # print('xB', xB, 'yB', yB)
    path = [l*l + yA*l + i for i in fill_mod_l(xA, xB, l)]
    # print('path after x', path)
    path += [xB + i*l for i in fill_mod_l(yA, yB, l)]
    # print('path after y', path)
    return path

def decode(syndrome):

    matching = compute_matching(syndrome, l)
    # print('matching:', matching)

    total_path = []
    for checkA, checkB in matching:
        # print(checkA, checkB)
        new_path = compute_path(checkA, checkB, l)
        # print('new_path:', new_path)
        total_path = add_mod_two(total_path, new_path)
        # print('total_path:', total_path)
    # print('total_path:', total_path)
    return total_path



