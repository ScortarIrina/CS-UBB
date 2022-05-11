import Graph


def display_edges(edges):
    """
    This function displays a given list of edges

    :param edges: list of edges represented as tuples (list)
    :return: None
    """
    for edge in edges:
        print("Edge from %s to %s with cost %d" % (edge[0], edge[1], edge[2]))


def display_vertices(vertices):
    """
    This function displays the given vertices

    :param vertices: the vertices (list)
    :return: None
    """
    print("Vertexes: ")
    for vertex in vertices:
        print(vertex, end=" ")
    print("")


def print_menu():
    """
    Prints on the screen the menu options

    :return: None
    """
    print("\n\t MENU\n")
    print("\t0. Exit\n"
          "\t1. Print vertices\n"
          "\t2. Print truth value of 'the edge x->y exists'\n"
          "\t3. Print the in degree of a vertex\n"
          "\t4. Print the out degree of a vertex\n"
          "\t5. Print the inbound edges of a vertex\n"
          "\t6. Print the outbound edges of a vertex\n"
          "\t7. Print the cost between 2 given vertices\n"
          "\t8. Modify the cost of the edge between 2 given vertices\n"
          "\t9. Add vertex\n"
          "\t10. Remove vertex\n"
          "\t11. Add edge\n"
          "\t12. Remove edge\n"
          "\t13. Read graph from a given file\n"
          "\t14. Write the graph to a file\n"
          "\t15. Generate random graph\n")


def main():
    """
    The main function of the program

    :return: None
    """
    # Initializes graph with empty graph
    graph = Graph.Graph([], [])
    while True:
        print("\n\t***************************************************************")
        print_menu()
        menu_option = input("\nChoose your option (0-15): ")
        if not menu_option.isnumeric():
            print("Invalid input!")
        else:
            menu_option = int(menu_option)

            # exit program
            if menu_option == 0:
                return

            # print vertices
            elif menu_option == 1:
                try:
                    display_vertices(graph.parse_vertices())
                except Exception as ve:
                    print(str(ve))

            # print truth value of 'the edge x->y exists
            elif menu_option == 2:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric():
                        print("The vertices must be numbers!")
                    else:
                        print(graph.is_edge(vertex1, vertex2))
                except Exception as ve:
                    print(str(ve))

            # Print the in degree of a vertex
            elif menu_option == 3:
                try:
                    vertex = input("\t-vertex: ")
                    if not vertex.isnumeric():
                        print("The vertex must be a number!")
                    else:
                        print(graph.get_in_degree(vertex))
                except Exception as ve:
                    print(str(ve))

            # Print the out degree of a vertex
            elif menu_option == 4:
                try:
                    vertex = input("\t-vertex: ")
                    if not vertex.isnumeric():
                        print("The vertex must be a number!")
                    else:
                        print(graph.get_out_degree(vertex))
                except Exception as ve:
                    print(str(ve))

            # Print the inbound edges of a vertex
            elif menu_option == 5:
                try:
                    vertex = input("\t-vertex: ")
                    if not vertex.isnumeric():
                        print("The vertex must be a number!")
                    else:
                        inbound_vertices = graph.parse_inbound_edges(vertex)
                        inbound_edges = []
                        for outbound in inbound_vertices:
                            inbound_edges.append((outbound, vertex, graph.get_cost_of_edge(outbound, vertex)))
                        display_edges(inbound_edges)
                except Exception as ve:
                    print(str(ve))

            # Print the outbound edges of a vertex
            elif menu_option == 6:
                try:
                    vertex = input("\t-vertex: ")
                    if not vertex.isnumeric():
                        print("The vertex must be a number!")
                    else:
                        outbound_vertices = graph.parse_outbound_edges(vertex)
                        outbound_edges = []
                        for inbound in outbound_vertices:
                            outbound_edges.append((inbound, vertex, graph.get_cost_of_edge(inbound, vertex)))
                        display_edges(outbound_edges)
                except Exception as ve:
                    print(str(ve))

            # Print the cost between 2 given vertices
            elif menu_option == 7:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric():
                        print("The vertices must be numbers!")
                    else:
                        print(graph.get_cost_of_edge(vertex1, vertex2))
                except Exception as ve:
                    print(str(ve))

            # Modify the cost of the edge between 2 given vertices
            elif menu_option == 8:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    updated_cost = input("\t-updated cost: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric() or not updated_cost.isnumeric():
                        print("The vertices and the cost must be numbers!")
                    else:
                        graph.modify_cost_of_edge(vertex1, vertex2, int(updated_cost))
                except Exception as ve:
                    print(str(ve))

            # Add vertex
            elif menu_option == 9:
                try:
                    vertex = input("\t-vertex to add: ")
                    if not vertex.isnumeric():
                        print("The vertex must be a number!")
                    else:
                        graph.add_vertex(vertex)
                except Exception as ve:
                    print(str(ve))

            # Remove vertex
            elif menu_option == 10:
                try:
                    vertex = input("\t-vertex to remove: ")
                    if not vertex.isnumeric():
                        print("The vertex must be a number!")
                    else:
                        graph.remove_vertex(vertex)
                except Exception as ve:
                    print(str(ve))

            # Add edge
            elif menu_option == 11:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    cost = input("\t-cost: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric() or not cost.isnumeric():
                        print("The vertices and the cost must be numbers!")
                    else:
                        graph.add_edge(vertex1, vertex2, int(cost))
                except Exception as ve:
                    print(str(ve))

            # Remove edge
            elif menu_option == 12:
                try:
                    vertex1 = input("\t-first vertex: ")
                    vertex2 = input("\t-second vertex: ")
                    if not vertex1.isnumeric() or not vertex2.isnumeric():
                        print("The vertices must be numbers!")
                    else:
                        graph.remove_edge(vertex1, vertex2)
                except Exception as ve:
                    print(str(ve))

            # Read graph from a given file
            elif menu_option == 13:
                try:
                    file_name = input("\t-file name: ")
                    graph = Graph.read_graph(file_name)
                except Exception as ve:
                    print(str(ve))

            # Write the graph to a file
            elif menu_option == 14:
                try:
                    file_name = input("\t-file name: ")
                    Graph.write_graph(file_name, graph)
                except Exception as ve:
                    print(str(ve))

            # Generate random graph
            elif menu_option == 15:
                try:
                    vertices = input("\t-number of vertices: ")
                    edges = input("\t-number of edges: ")
                    if not vertices.isnumeric() or not edges.isnumeric():
                        print("The number of vertices and the number of edges must me numbers!")
                    else:
                        graph = Graph.random_graph(int(vertices), int(edges))
                except Exception as ve:
                    print(str(ve))

            else:
                print("Invalid input")


if __name__ == "__main__":
    main()
