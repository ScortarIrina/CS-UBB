import random
from copy import deepcopy
import PriorityDict

inf = 99999999


class UndirectedGraph:
    def __init__(self, vertices, edges):
        """
        Constructor for graph
        :param vertices: a list of initial vertices
        :param edges: a list of tuples (a, b, c), meaning there is an edge from a to b with cost c
        """
        self.__neighbours = {}
        self.__costs = {}

        if not isinstance(vertices, list) or not isinstance(edges, list):
            raise Exception("Arguments do not have the required type")

        for vertex in vertices:
            if not isinstance(vertex, str):
                raise Exception("Vertices do not have the required type")
            self.__neighbours[vertex] = []

        for edge in edges:
            if not isinstance(edge, tuple) or len(edge) != 3 or type(edge[2]) != int:
                raise Exception("Malformed edge")
            if edge[0] not in self.__neighbours or edge[1] not in self.__neighbours:
                raise Exception("Initial edges don't have both endpoints in the initial vertices")
            if (edge[0], edge[1]) in self.__costs:
                raise Exception("Edge already exists")
            self.__neighbours[edge[1]].append(edge[0])
            self.__costs[(edge[0], edge[1])] = edge[2]
            if edge[0] != edge[1]:
                self.__neighbours[edge[0]].append(edge[1])
                self.__costs[(edge[1], edge[0])] = edge[2]

    def has_vertex(self, vertex):
        """
        This function checks if the provided vertex exists
        :param vertex: the vertex
        :return: True = the vertex exists
                 False = it doesn't
        """
        if not isinstance(vertex, str):
            raise Exception("Vertex should be str")
        return vertex in self.__neighbours

    def parse_vertices(self):
        """
        This function returns an iterable containing vertices
        The vertices are deep-copied, in order to avoid being modified from the outside
        :return: iterator through a list of deep-copied vertices
        """
        for vertex in self.__neighbours:
            yield deepcopy(vertex)

    def parse_edges(self):
        for i in range(len(self.__costs)):
            for edge in self.__neighbours[str(i)]:
                yield deepcopy(i, edge)

    def is_edge(self, x, y):
        """
        This function checks if edge x-y exists
        :param x: the first vertex
        :param y: the second vertex
        :return: True = the edge exists
                 False = otherwise
        """
        if x not in self.__neighbours or y not in self.__neighbours:
            raise Exception("Vertices invalid")
        return (x, y) in self.__costs.keys()

    def get_degree(self, x):
        """
        This function returns the degree of a vertex
        :param x: the vertex
        :return: the in degree of the vertex x
        """
        if x not in self.__neighbours:
            raise Exception("Vertex doesn't exist")

        return len(self.__neighbours[x])

    def parse_adjacent_edges(self, x):
        """
        This function returns an iterable of deep-copied edges
        :param x: the vertex for which to retrieve the iterator
        :return: iterator to a deep-copied list of vertices
        """
        if x not in self.__neighbours:
            raise Exception("Vertex doesn't exist")
        for node in self.__neighbours[x]:
            yield deepcopy(node)

    def get_adjacent_vertices(self, v):
        return self.__neighbours[str(v)]

    def get_edge_cost(self, x, y):
        """
        This function returns the cost of the edge between x and y
        :param x: the first vertex
        :param y: the second vertex
        :return: the cost of the edge from x to y
        """
        if (x, y) not in self.__costs:
            raise Exception("Edge doesn't exist")
        return self.__costs[(x, y)]

    def modify_edge_cost(self, x, y, z):
        """
        This function modifies the cost of the edge from x to y
        :param x: the first vertex
        :param y: the second vertex
        :param z: the new cost
        """
        if (x, y) not in self.__costs:
            raise Exception("Edge doesn't exist")
        if type(z) != int:
            raise Exception("Cost isn't an integer")
        self.__costs[(x, y)] = z
        self.__costs[(y, x)] = z

    def copy(self):
        """
        This function retrieves a copy of the current graph
        :return: a Graph copy
        """
        return deepcopy(self)

    def add_vertex(self, x):
        """
        This function adds the vertex x to the graph
        :param x: the vertex to be added
        """
        if not isinstance(x, str):
            raise Exception("Vertex doesn't have the required type")
        if x in self.__neighbours.keys():
            raise Exception("Vertex already exists")

        self.__neighbours[x] = []

    def remove_vertex(self, x):
        """
        This function removes the vertex x from the graph
        :param x: the vertex to be removed
        """
        if x not in self.__neighbours.keys():
            raise Exception("Vertex doesn't exist")

        for neighbor in self.__neighbours[x]:
            del self.__costs[(x, neighbor)]
            if neighbor != x:
                del self.__costs[(neighbor, x)]
                self.__neighbours[neighbor].remove(x)

        del self.__neighbours[x]

    def add_edge(self, x, y, z):
        """
        This function adds the edge from x to y to the graph
        :param x: the first vertex
        :param y: the second vertex
        :param z: the cost
        """
        if not isinstance(x, str) or not isinstance(y, str) or not isinstance(z, int):
            raise Exception("Arguments do not have the correct types")
        if y not in self.__neighbours or x not in self.__neighbours:
            raise Exception("Vertices don't exist")
        if (x, y) in self.__costs:
            raise Exception("Edge already exists")

        self.__neighbours[y].append(x)
        self.__costs[(x, y)] = z
        if x != y:
            self.__neighbours[x].append(y)
            self.__costs[(y, x)] = z

    def remove_edge(self, x, y):
        """
        This function removes the edge from x to y from the graph
        :param x: the first vertex
        :param y: the second vertex
        """
        if (x, y) not in self.__costs:
            raise Exception("Edge doesn't exist")

        self.__neighbours[y].remove(x)
        del self.__costs[(x, y)]
        if x != y:
            self.__neighbours[x].remove(y)
            del self.__costs[(y, x)]

    def __eq__(self, other):
        """
        This function return True if two graphs are the same, False otherwise
        :param other: the other graph
        :return: True if same graph, False otherwise
        """
        if sorted(self.__neighbours.keys()) != sorted(other.__neighbours.keys()):
            return False
        if sorted(self.__costs.keys()) != sorted(other.__costs.keys()):
            return False
        for key in self.__costs.keys():
            if self.__costs[key] != other.__costs[key]:
                return False
        return True

    def breadth_first_traversal(self, vertex, visited):
        """
        Traverse the graph with a breath-first algorithm for a given vertex
        :param vertex: the starting vertex
        :param visited: a map to mark the visited vertices
        :return: the connected component with the given vertex as a starting vertex
        """
        bfs_queue = []
        connected_component = []  # list for connected components
        bfs_queue.append(vertex)  # add the starting vertex to the queue
        visited[vertex] = True  # mark the starting vertex as visited
        while bfs_queue:
            first_elem = bfs_queue.pop(0)  # pop the first elem from the queue and add it to the connected components
            connected_component.append(first_elem)
            # get all the adjacent vertices of the vertex first_elem that are not visited yet
            # mark them and add them to the queue
            for i in self.__neighbours[first_elem]:
                if visited[i] is False:
                    bfs_queue.append(i)
                    visited[i] = True
        return connected_component  # return the connected components

    def find_connected_components(self):
        visited = {}
        connected_component = []
        all_connected_components = []
        for vertex in self.__neighbours:
            visited[vertex] = False
        for vertex in self.__neighbours:
            if visited[vertex] is False:
                connected_component = self.breadth_first_traversal(vertex, visited)
                all_connected_components.append(connected_component)
        return all_connected_components

    def build_adjacency_matrix(self):
        nr_vertices = len(self.__costs)
        matrix = [[0 for column in range(nr_vertices)]
                  for row in range(nr_vertices)]
        for row in range(len(matrix)):
            if row in self.__neighbours:
                for column in range(len(matrix)):
                    if column in self.__neighbours:
                        matrix[row][column] = self.get_edge_cost(row, column)
        return matrix

    def prims_mst(self, start_vertex):
        distance_table = {}
        nr_vertices = len(self.__costs)

        for i in range(nr_vertices):
            distance_table[i] = (None, None)
        distance_table[start_vertex] = (0, start_vertex)

        priority_queue = PriorityDict.PriorityDict()
        # start with a single tree consisting in a single vertex and mark it as visited
        priority_queue[start_vertex] = 0

        visited_vertices = set()
        msp = UndirectedGraph(list(self.parse_vertices()), [])

        # At each step, an edge is added, connecting an exterior vertex to the tree.
        while len(priority_queue.keys()) > 0:
            # remove item with the lowest priority and add it to the set of visited vertices
            current_vertex = priority_queue.pop_smallest()
            # if the current vertex was already visited, we do nothing
            if current_vertex in visited_vertices:
                continue
            visited_vertices.add(current_vertex)

            if current_vertex != start_vertex:
                last_vertex = distance_table[current_vertex][1]
                edge = (
                    str(last_vertex), str(current_vertex), self.get_edge_cost(str(last_vertex), str(current_vertex)))
                # if the edge formed by the current and last vertex is not in the MSP, we add the edge to the solution
                if edge not in msp.parse_vertices():
                    msp.add_edge(edge[0], edge[1], edge[2])

            # we look for the local minimum cost edge
            for neighbour in self.get_adjacent_vertices(current_vertex):
                distance = self.get_edge_cost(str(current_vertex), str(neighbour))
                neighbour_distance = distance_table[int(neighbour)][0]

                if neighbour_distance is None or neighbour_distance > distance:
                    distance_table[neighbour] = (distance, current_vertex)
                    priority_queue[neighbour] = distance

        return msp


def iterator_len(x):
    n = 0
    try:
        while True:
            next(x)
            n += 1
    except StopIteration:
        pass
    return n


def hamiltonian_cycle_low_cost(graph):
    """
    This function get a hamiltonian path in the graph
    :param graph: the graph
    :return: tuple of (the cost, a list of nodes which represents the path)
    """

    def backtracking(node, path, cost):
        """
        This function gets a low cost hamiltonian path using backtracking
        :param node: the current_node
        :param path: the path of the nodes so far
        :param cost: the current cost
        """
        if len(path) >= len(list(graph.parse_vertices())):
            # if the current vertex is adjacent to the previously added vertex,
            # we update the cost and add the vertex to the path
            if path[0] in graph.parse_adjacent_edges(path[-1]):
                return cost + graph.get_edge_cost(path[-1], path[0]), deepcopy(path)

            return (0, [])  # tuple of cost 0 and empty path

        # we keep the adjacent edges of the current vertex in a list
        # and parse through it, updating the cost at each step
        neighbours = list(graph.parse_adjacent_edges(node))
        for i in range(len(neighbours)):
            neighbours[i] = (graph.get_edge_cost(node, neighbours[i]), neighbours[i])
        neighbours = sorted(neighbours)
        for neighbour_cost, neighbour in neighbours:
            if neighbour in path:
                continue
            # if we find such a vertex, we add the vertex as part of the solution
            path.append(neighbour)
            tmp = backtracking(neighbour, path, cost + neighbour_cost)
            if tmp != (0, []):
                return tmp
            path.pop()
        return (0, [])

    if len(list(graph.parse_vertices())) == 0:
        return (0, [])

    # Create an empty path array and add vertex 0 to it
    # The starting path has length 0
    # The starting cost is also 0
    return backtracking(list(graph.parse_vertices())[0], [list(graph.parse_vertices())[0]], 0)


def read_graph(filename):
    """
    This function reads a graph from a file
    :param filename: the file from which to read(name, relative path or absolute path)
    :return: Graph
    """
    if not isinstance(filename, str) or not filename.endswith(".txt"):
        raise Exception("Invalid filename")

    n = m = 0
    vertices = []
    edges = []

    with open(filename, "r") as f:
        lines = list(f.readlines())
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()
        lines = list(filter(lambda x: len(x) > 0, lines))
        metadata = lines[0].strip().split(" ")
        if len(metadata) != 2:
            raise Exception("invalid format")
        n, m = int(metadata[0]), int(metadata[1])

        if filename.endswith(".modified.txt"):
            if len(lines) != m + 2:
                raise Exception("invalid format")
            if len(lines[1].strip().split(" ")) != n:
                raise Exception("invalid format")

            for i in range(0, n):
                vertices.append(lines[1].strip().split(" ")[i])

            for i in range(2, len(lines)):
                line_data = lines[i].strip().split(" ")
                if len(line_data) != 3:
                    raise Exception("invalid format")
                edges.append((line_data[0], line_data[1], int(line_data[2])))
        else:
            if len(lines) != m + 1:
                raise Exception("invalid format")
            for i in range(0, n):
                vertices.append(str(i))
            for i in range(1, len(lines)):
                line_data = lines[i].strip().split(" ")
                if len(line_data) != 3:
                    raise Exception("invalid format")
                edges.append((line_data[0], line_data[1], int(line_data[2])))

    return UndirectedGraph(vertices, edges)


def write_graph(filename, graph):
    """
    This function writes a graph from a file
    :param filename: the filename to which to read(name, relative path or absolute path)
    :param graph: the graph to be written
    """
    if not isinstance(filename, str) or not filename.endswith(".txt"):
        raise Exception("invalid filename")
    if not isinstance(graph, UndirectedGraph):
        raise Exception("Invalid arguments")

    with open(filename, "w") as f:
        vertices = list(graph.parse_vertices())
        edges = []
        for vertex in vertices:
            for neighbor in graph.parse_adjacent_edges(vertex):
                if neighbor >= vertex:
                    edges.append((vertex, neighbor, graph.get_edge_cost(vertex, neighbor)))
        f.write("%d %d\n" % (len(vertices), len(edges)))
        for vertex in vertices:
            f.write("%s " % vertex)
        f.write("\n")
        for edge in edges:
            f.write("%s %s %d\n" % (edge[0], edge[1], edge[2]))


def random_graph(n, m):
    """
    This function creates a random graph with specified number of vertices and edges
    :param n: the number of vertices
    :param m: the number of edges
    :return: a graph with specified parameters
    """

    if not isinstance(n, int) or not isinstance(m, int):
        raise Exception("Arguments have invalid types")
    if n < 0 or m < 0 or m > n * (n + 1) // 2:
        raise Exception("Bad arguments")

    graph = UndirectedGraph([str(x) for x in range(0, n)], [])
    possible_edges = []
    for i in range(0, n):
        for j in range(i, n):
            possible_edges.append((i, j))

    # we shuffle the generated edges, so that they are not ordered
    random.shuffle(possible_edges)

    for i in range(0, m):
        graph.add_edge(str(possible_edges[i][0]), str(possible_edges[i][1]), random.randint(1, 90))

    return graph
