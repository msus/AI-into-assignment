nodes = ('A', 'B', 'C', 'D', 'F')
edges = (('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'F'),
         ('B', 'C'), ('C', 'D'), ('C', 'F'), ('D', 'F'))
colored = {}
number_of_colors = 4


def is_correct_neighbors(edge: tuple[str, str]) -> bool:
    nodeA, nodeB = edge
    if nodeA not in colored.keys() or nodeB not in colored.keys():
        return True
    return colored[nodeA] != colored[nodeB]


def is_colored_correctly():
    for edge in edges:
        if not is_correct_neighbors(edge):
            return False
    return True


def change_color(node: str):
    if node not in colored.keys():
        colored[node] = 0
    else:
        colored[node] += 1
        if colored[node] >= number_of_colors:
            return False
    return True


index = 0
while True:                                 # Go over all nodes
    if index < 0 or index >= len(nodes):
        break
    if not change_color(nodes[index]):      # Ran out of colors for node
        colored.pop(nodes[index])
        index -= 1
        continue
    if is_colored_correctly():              # Coloring is incorrect
        index += 1
print(colored)  # empty dictionary => can't color with N colors
