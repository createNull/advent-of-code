import networkx as nx


with open('input.txt') as f:
    puzzle_input = [obj.split(')') for obj in f.read().splitlines()]

start, end = "YOU", "SAN"


def get_result(array, option):
    graph = nx.DiGraph(array)
    if option == 1:
        return sum(len(nx.ancestors(graph, n)) for n in graph.nodes)
    elif option == 2:
        return len(nx.shortest_path(nx.Graph(array), start, end)) - 3


print('Part1: ', get_result(puzzle_input, 1))
print('Part2: ', get_result(puzzle_input, 2))
