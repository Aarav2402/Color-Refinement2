from graph import *
from graph_io import load_graph, save_graph, write_dot

with open('colorref_smallexample_4_16.grl') as f:
    l = load_graph(f, read_list=True)

graphA = Graph(False, 0, True)
print(l[0])
for lists in l[0]:
    print(lists)
    graphA = graphA + lists
print(graphA)


def color_refinement(graphA):
    # Step 1: Initialize empty dictionary of color classes for each graph
    color_classes = {}
    for i, graph in enumerate(graphA):
        color_classes[i] = {v: i for v in graph}

    # Step 2: Assign unique color to each vertex in each graph
    for i, graph in enumerate(graphA):
        colors = set()
        for v in graph:
            color = color_classes[i][v]
            while color in colors:
                color += len(graphA)
            color_classes[i][v] = color
            colors.add(color)

    # Step 3: Refinement loop
    while True:
        # Initialize new dictionaries of color classes
        new_color_classes = {}
        for i, graph in enumerate(graphA):
            new_color_classes[i] = {}

        # Determine color classes of each vertex in each graph
        for i, graph in enumerate(graphA):
            for v in graph:
                color_class = tuple(sorted(
                    color_classes[j][u] for j, neighbors in enumerate(graphA) for u in neighbors if u in graph[v]))
                new_color_classes[i][v] = color_class

        # Update color classes for each graph
        for i, graph in enumerate(graphA):
            if new_color_classes[i] != color_classes[i]:
                color_classes[i] = new_color_classes[i]
                break
        else:
            # Convergence achieved
            break

    # Step 4: Output final color classes for each graph
    return color_classes


with open('colourful4.dot', 'w') as f: write_dot(color_refinement(l[0]), f)
