import UndirectedGraph


def display_edges(edges):
    """
    This function displays a given list of edges
    :param edges: list of edges represented as tuples
    :return: None
    """
    for edge in edges:
        print("Edge from %s to %s with cost %d" % (edge[0], edge[1], edge[2]))


def display_vertices(vertices):
    """
    This function displays the given vertices
    :param vertices: list of the vertices
    :return: None
    """
    print("Vertices: ")
    for vertex in vertices:
        print(vertex, end=" ")
    print("")


def display_graph(graph):
    """
    This function displays a graph
    :param graph: the graph
    :return: None
    """
    display_vertices(graph.parse_vertices())
    edges = []
    for vertex in graph.parse_vertices():
        neighbor_list = list(filter(lambda x: x >= vertex, graph.parse_adjacent_edges(vertex)))
        for neighbor in neighbor_list:
            edges.append((vertex, neighbor, graph.get_edge_cost(vertex, neighbor)))
    print("And edges:")
    display_edges(edges)


def display_graph_msp(min_spanning_tree):
    display_vertices(min_spanning_tree.parse_vertices())
    edges = []
    for vertex in min_spanning_tree.parse_vertices():
        neighbor_list = list(filter(lambda x: x >= vertex, min_spanning_tree.parse_adjacent_edges(vertex)))
        for neighbor in neighbor_list:
            edges.append((vertex, neighbor, min_spanning_tree.get_edge_cost(vertex, neighbor)))
    print("And edges:")
    display_edges(edges)


def accessible(graph, start_vertex):
    acc = set()
    acc.add(start_vertex)
    bfs_list = [start_vertex]
    while len(bfs_list) > 0:
        x = bfs_list[0]
        bfs_list = bfs_list[1:]
        for y in graph.parse_adjacent_edges(x):
            if y not in acc:
                acc.add(y)
                bfs_list.append(y)
        return acc


def print_menu():
    """
    This function prints the menu options on the screen
    """
    print("\n\tMENU\n\n"
          "\t0. Exit\n"
          "\t1. Generate random graph\n"
          "\t2. Read graph from file\n"
          "\t3. Write the graph to a file\n"
          "\t4. Print vertices\n"
          "\t5. Print the truth value of 'the edge x-y exists'\n"
          "\t6. Print the degree of a vertex\n"
          "\t7. Print the adjacent edges of a vertex\n"
          "\t8. Print the cost of an edge\n"
          "\t9. Modify the cost of an edge\n"
          "\t10. Add vertex\n"
          "\t11. Remove vertex\n"
          "\t12. Add edge\n"
          "\t13. Remove edge\n"
          "\t14. Print connected components (BFS)\n"
          "\t15. Print the minimum spanning tree of the graph\n"
          "\t16. Find a Hamiltonian cycle of low cost\n")


def start():
    # Initializes graph with empty UndirectedGraph
    graph = UndirectedGraph.UndirectedGraph([], [])
    while True:
        print("\n\t******************************************************")
        print_menu()
        menu_option = input("\nChoose an option (0-16): ")
        if not menu_option.isnumeric():
            print("ERROR: Invalid input!")
        else:
            menu_option = int(menu_option)

            # exit program
            if menu_option == 0:
                return

            # generate random graph
            elif menu_option == 1:
                try:
                    number_of_vertices = input("\t-number of vertices: ")
                    number_of_edges = input("\t-number of edges: ")
                    if not number_of_edges.isnumeric() or not number_of_vertices.isnumeric():
                        print("ERROR: The number of vertices and the number of edges must be numbers!")
                    else:
                        graph = UndirectedGraph.random_graph(int(number_of_vertices), int(number_of_edges))
                except Exception as e:
                    print(str(e))

            # read graph from file
            elif menu_option == 2:
                try:
                    print("Text files options:  graph1.modified.txt / graph2.modified.txt")
                    filename = input("\t-file name: ")
                    graph = UndirectedGraph.read_graph(filename)
                except Exception as e:
                    print(str(e))

            # write graph to file
            elif menu_option == 3:
                try:
                    filename = input("\t-file name: ")
                    UndirectedGraph.write_graph(filename, graph)
                except Exception as e:
                    print(str(e))

            # print vertices
            elif menu_option == 4:
                try:
                    display_vertices(graph.parse_vertices())
                except Exception as e:
                    print(str(e))

            # print the truth value of 'the edge x-y exists'
            elif menu_option == 5:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric():
                        print("ERROR: The vertices must be numbers!")
                    else:
                        print(graph.is_edge(vertex1, vertex2))
                except Exception as e:
                    print(str(e))

            # print the degree of a vertex
            elif menu_option == 6:
                try:
                    vertex = input("\t-vertex: ")
                    if not vertex.isnumeric():
                        print("ERROR: The vertex must be a number!")
                    else:
                        print("The degree is:", graph.get_degree(vertex))
                except Exception as e:
                    print(str(e))

            # print the adjacent edges of a vertex
            elif menu_option == 7:
                try:
                    vertex = input("\t-vertex: ")
                    if not vertex.isnumeric():
                        print("ERROR: The vertex must be a number!")
                    else:
                        adjacent_vertices = graph.parse_adjacent_edges(vertex)
                        adjacent_edges = []
                        for adjacent in adjacent_vertices:
                            adjacent_edges.append((vertex, adjacent, graph.get_edge_cost(vertex, adjacent)))
                        display_edges(adjacent_edges)
                except Exception as e:
                    print(str(e))

            # print the cost of an edge
            elif menu_option == 8:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric():
                        print("ERROR: The vertices must be numbers!")
                    else:
                        print("THe cost is: " + str(graph.get_edge_cost(vertex1, vertex2)))
                except Exception as e:
                    print(str(e))

            # modify the cost of an edge
            elif menu_option == 9:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    new_cost = input("\t-new cost: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric() or not new_cost.isnumeric():
                        print("ERROR: The vertices and the new cost must be numbers!")
                    else:
                        graph.modify_edge_cost(vertex1, vertex2, int(new_cost))
                except Exception as e:
                    print(str(e))

            # add vertex
            elif menu_option == 10:
                try:
                    vertex = input("\t-vertex to add: ")
                    if not vertex.isnumeric():
                        print("ERROR: The vertex must be a number!")
                    else:
                        graph.add_vertex(vertex)
                except Exception as e:
                    print(str(e))

            # remove vertex
            elif menu_option == 11:
                try:
                    vertex = input("\t-vertex to remove: ")
                    if not vertex.isnumeric():
                        print("ERROR: The vertex must be a number!")
                    else:
                        graph.remove_vertex(vertex)
                except Exception as e:
                    print(str(e))

            # add edge
            elif menu_option == 12:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    cost = input("\t-cost: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric() or not cost.isnumeric():
                        print("ERROR: The vertices and the cost must be numbers!")
                    else:
                        graph.add_edge(vertex1, vertex2, int(cost))
                except Exception as e:
                    print(str(e))

            # remove edge
            elif menu_option == 13:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric():
                        print("ERROR: The vertices must be numbers!")
                    else:
                        graph.remove_edge(vertex1, vertex2)
                except Exception as e:
                    print(str(e))

            # print connected components (BFS)
            elif menu_option == 14:
                try:
                    all_connected = graph.find_connected_components()
                    for index in range(len(all_connected)):
                        print(str(all_connected[index]))
                except Exception as e:
                    print(str(e))

            # minimum spanning tree of the graph
            elif menu_option == 15:
                try:
                    display_graph_msp(graph.prims_mst(1))
                except Exception as e:
                    print(str(e))

            # Hamiltonian cycle of low cost
            elif menu_option == 16:
                try:
                    ham_cycle = UndirectedGraph.hamiltonian_cycle_low_cost(graph)
                    if ham_cycle[1] == []:
                        print("No hamiltonian cycle found!")
                    else:
                        cost = 0
                        ham_cycle[1].append(ham_cycle[1][0])
                        start_vertex = ham_cycle[1][0]
                        current_vertex = ham_cycle[1][1]
                        prev_vertex = ham_cycle[1][0]
                        cost += graph.get_edge_cost(current_vertex, prev_vertex)
                        i = 2
                        while start_vertex != current_vertex:
                            cost += graph.get_edge_cost(current_vertex, prev_vertex)
                            prev_vertex = current_vertex
                            current_vertex = ham_cycle[1][i]
                            i += 1

                        print("Found hamiltonian cycle of cost %d" % cost)
                        for vertex in ham_cycle[1]:
                            print(vertex, end=" ")
                        print()
                except Exception as e:
                    print(str(e))

            else:
                print("Invalid menu option!")
