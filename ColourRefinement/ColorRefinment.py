from graph import *
from graph_io import load_graph, save_graph, write_dot
import time

with open('colorref_smallexample_4_16.grl') as f:
    l = load_graph(f, read_list=True)
for G in l[0]:

    vertexNeighbour = {}
    ListOfNeighbours = []
    neighbourColor = []
    vertexColors = []
    sortedNeighbourColors = []
    startTime = time.time()
    sortedFinalResult = []


    def color_refinement(l):
        for vertex in G.vertices:
            vertex.colornum = vertex.degree  # assigning vertex color with respect to its degree
            vertexNeighbour[vertex] = vertex.neighbours  # dictionary with key vertex has value of its neighbours
            vertexColors.append(vertex.colornum)  # adding the vertex color to a list

        ListOfNeighbours = list(vertexNeighbour.values())
        newResult = []
        finalResult = []
        oldResult = None

        while newResult != oldResult:
            oldResult = newResult

            for n in ListOfNeighbours:
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
            print(newResult)
            for i in range(0, len(G.vertices)):
                G.vertices[i].colornum = newResult[i]

            for vertex in G.vertices:
                print(vertex.colornum)

            finalResult.append(newResult)

            print(finalResult)
            print(sortedNeighbourColors)


    with open('colourful2.dot', 'w') as f: write_dot(color_refinement(l[0]), f)

    print(time.time() - startTime)
