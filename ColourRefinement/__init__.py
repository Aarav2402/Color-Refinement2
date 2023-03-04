from graph import *
from graph_io import load_graph, save_graph, write_dot

with open('colorref_smallexample_4_7.grl') as f:
    l = load_graph(f, read_list=True)

graph = Graph(False, 0, True)

for lists in l[0]:
    print(lists)
    graph = graph + lists
print(graph)


def color_refinement(l):
    # Initialize the partition with a single color class containing all nodes
    partition = [{node} for node in range(len(graph))]

    # Keep refining the partition until it no longer changes
    while True:
        # Create a new partition
        new_partition = []

        # Iterate over each color class in the current partition
        for color_class in partition:
            # Create a dictionary to count the number of neighbors in each color class
            neighbor_counts = {}
            for node in color_class:
                for neighbor in graph.vertices:
                    # Determine the color class of the neighbor
                    neighbor_color = None
                    for i, c in enumerate(partition):
                        if neighbor in c:
                            neighbor_color = i
                            break

                    # Increment the neighbor count for the corresponding color class
                    if neighbor_color in neighbor_counts:
                        neighbor_counts[neighbor_color] += 1
                    else:
                        neighbor_counts[neighbor_color] = 1

            # Partition the color class based on the neighbor counts
            for color, count in neighbor_counts.items():
                new_color_class = {node for node in color_class if
                                   color_class_neighbor_count(node, partition[color]) == count}
                new_partition.append(new_color_class)

        # Check if the partition has changed
        if new_partition == partition:
            break

        # Update the partition
        partition = new_partition


    # Return the final partition
    return partition


# Helper function to count the number of neighbors of a node in a color class
def color_class_neighbor_count(node, color_class):
    count = 0
    for neighbor in graph[node]:
        if neighbor in color_class:
            count += 1
    return count


with open('colourful3.dot', 'w') as f: write_dot(color_refinement(l), f)

# # Define a function for color refinement
# def color_refinement(graph):
#     """
#     Input: a graph G represented as an adjacency matrix
#     Output: a list of color classes of G after applying color refinement
#     """
#     colors = {}  # dictionary to store the colors of vertices
#     color_classes = []  # list to store the color classes
#     n = len(graph)
#
#     # Initialize the color of each vertex to its degree
#     for i in graph.vertices:
#         colors[i] = i.degree
#
#     # Repeat until there are no more color changes
#     while True:
#         # Create a new dictionary to store the updated colors
#         new_colors = {}
#
#         # Assign new colors to each vertex based on its neighbors' colors
#         for i in range(len(graph)):
#             neighbors = [i.neighbours for i in graph.vertices]
#             neighbor_colors = [colors[j] for j in neighbors[i]]
#             new_color = tuple(sorted(neighbor_colors))
#             new_colors[i] = new_color
#
#         # If there are no more color changes, break out of the loop
#         if new_colors == colors:
#             break
#
#         # Update the colors dictionary and color classes list
#         colors = new_colors
#         color_classes = []
#         for color in set(colors.values()):
#             vertices = [v for v in colors if colors[v] == color]
#             color_classes.append(vertices)
#
#     print(graph.vertices)
#     return color_classes
#
#
# color_refinement(G)


# def color_refinement():
#     colors = {}
#     for vertex in G.vertices:
#         vertex.color = 1
#     vertex.color = vertex.degree
#
#     while True:
#         neighbour = [vertex.neighbours]
#         for n in neighbour:
#             if n.degree == vertex.degree and n.neigbhour.color == vertex.neighbour.color:
#                 n.color = vertex.color
#             n.color += n.color + 1
#             print(vertex.degree)
#
#
# color_refinement()


# while True:
#     identical = {}
#     for vertex, color in colors.items():
#         if color not in identical:
#             identical[color] = []
#         identical[color].append(vertex)

# def color_refinement(graph):
#     """
#     Given an input graph, performs color refinement algorithm and returns a refined graph.
#
#     Args:
#         graph: A graph represented as a dictionary where keys are nodes and values are lists of neighbors.
#
#     Returns:
#         A refined graph where nodes with the same color are merged into a single node.
#     """
#     # Assign initial colors to nodes
#     colors = {}
#     for node in graph:
#         colors[node] = 0
#
#     # Keep refining until colors no longer change
#     while True:
#         # Create a dictionary to store nodes with the same color
#         color_classes = {}
#         for node, color in colors.items():
#             if color not in color_classes:
#                 color_classes[color] = []
#             color_classes[color].append(node)
#
#         # Assign new colors to nodes based on their neighbors' colors
#         new_colors = {}
#         for node in graph:
#             neighbor_colors = [colors[neighbor] for neighbor in graph[node]]
#             new_colors[node] = min(neighbor_colors + [colors[node]])
#
#         # If colors no longer change, return the refined graph
#         if new_colors == colors:
#             return {color: set(nodes) for color, nodes in color_classes.items()}
#
#         colors = new_colors
