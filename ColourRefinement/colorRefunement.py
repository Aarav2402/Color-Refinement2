from graph import *
from graph_io import load_graph, save_graph, write_dot

with open('colorref_smallexample_4_7.grl') as f:
    l = load_graph(f, read_list=True)

graph = Graph(False, 0, True)
for lists in l[0]:
    graph = graph + lists

vertexNeighbour = {}
ListOfNeighbours = []

vertexColors = []
sortedFinalResult = []
result = []
newList = []


def color_refinement(l):
    newResult = []
    length = len(graph.vertices)
    print(length)
    no_of_graphs = len(l)
    print(no_of_graphs)
    no_of_vertices = length // no_of_graphs
    print(no_of_vertices)



    for vertex in graph.vertices:
        vertex.colornum = vertex.degree  # assigning vertex color with respect to its degree
        vertexNeighbour[vertex] = vertex.neighbours  # dictionary with key vertex has value of its neighbours
        vertexColors.append(vertex.colornum)  # adding the vertex color to a list

    newResult.append(vertexColors)

    while True:
        sortedNeighbourColors = []
        neighbourColor = []
        listOfNeighbours = list(vertexNeighbour.values())

        for n in listOfNeighbours:
            Empty = []
            for j in n:
                Empty.append(j.colornum)
            neighbourColor.append(Empty)

        for lists in neighbourColor:
            temporary = sorted(lists)
            sortedNeighbourColors.append(temporary)

        unique_lst = {}
        count = 0
        result = []
        for l in sortedNeighbourColors:
            if tuple(l) not in unique_lst:
                unique_lst[tuple(l)] = count
                count += 1
            result.append([unique_lst[tuple(l)]])
        newResult = sum(result, [])

        if newResult in newList:
            break
        else:
            newList.append(newResult)
        print('jfpafjpjca', len(newList))
        print(newList)

        for i in range(0, len(graph.vertices)):
         graph.vertices[i].colornum = newResult[i]

    sublists = []
    for i in range(0, len(newResult), no_of_vertices):
        sublist = newResult[i:i + no_of_vertices]
        sublists.append(sublist)
    result = []
    for i, l1 in enumerate(sublists):
        matches = [i]
        for j, l2 in enumerate(sublists[i + 1:], start=i + 1):
            if set(l1) == set(l2):
                matches.append(j)
        if len(matches) > 1:
            result.append(matches)
    for lists in result:
        print(lists)
    #print("new result", newResult)

    return graph
color_refinement(l[0]), f

#with open('MyGraph.dot', 'w') as f: write_dot(color_refinement(l[0]), f)
