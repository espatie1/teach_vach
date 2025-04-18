import itertools

letter_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'F', 'D'],
    'C': ['A', 'B', 'E', 'G'],
    'D': ['B','F'],
    'F': ['D', 'B','G'],
    'E': ['C', 'G'],
    'G': ['E', 'C', 'F']
}

table_graph = {
    '1': ['3','4','5'],
    '2': ['5', '6'],
    '3': ['1', '4', '6', '7'],
    '4': ['1', '3'],
    '5': ['1', '2', '6'],
    '6': ['2', '3', '5', '7'],
    '7': ['3', '6']
}


def is_matching(letter_graph, table_graph, mapping):
    for l_node, l_neighbors in letter_graph.items():
        mapped_l = mapping[l_node]
        mapped_l_neighbors = set(mapping[n] for n in l_neighbors)
        if set(table_graph[mapped_l]) != mapped_l_neighbors:
            return False
    return True

letters = list(letter_graph.keys())
points = list(table_graph.keys())

for perm in itertools.permutations(points):
    mapping = dict(zip(letters, perm))
    if is_matching(letter_graph, table_graph, mapping):
        print("Done: ")
        for k, v in mapping.items():
            print(f"{k} -> {v}")
        break
