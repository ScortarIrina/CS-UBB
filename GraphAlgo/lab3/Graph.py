import random
from copy import deepcopy

infinity = 99999999


class Graph:
    def __init__(self, vertices, edges):
        """
        Constructor for graph.
        :param vertices: a list of initial vertices (list of strings)
        :param edges: a list of tuples (a, b, c), meaning there is an edge from a to b with cost c (list of tuples)
        """
        self.__nin = {}
        self.__nout = {}
        self.__costs = {}

        if not isinstance(vertices, list) or not isinstance(edges, list):
            raise Exception("Invalid type of the arguments")

        for node in vertices:
            if not isinstance(node, str):
                raise Exception("Vertices are of invalid type")
            self.__nin[node] = []
            self.__nout[node] = []

        for edge in edges:
            if not isinstance(edge, tuple) or len(edge) != 3 or type(edge[2]) != int:
                raise Exception("Malformed edge")
            if edge[0] not in self.__nin or edge[1] not in self.__nout:
                raise Exception("Initial edges don't have both endpoints in the initial vertices")
            if (edge[0], edge[1]) in self.__costs:
                raise Exception("Edge already exists")
            self.__nin[edge[1]].append(edge[0])
            self.__nout[edge[0]].append(edge[1])
            self.__costs[(edge[0], edge[1])] = edge[2]

    def parse_vertices(self):
        """
        This function returns an iterable containing vertices
        The vertices are deep-copied, in order to avoid being modified from the outside
        :return: iterator through a list of deep-copied vertices
        """
        return deepcopy([node for node in self.__nin])

    def is_edge(self, x, y):
        """
        This function returns True if the edge x->y exists, false otherwise
        :param x: the first vertex
        :param y: the second vertex
        :return: True if an edge exists, false otherwise
        """

        if x not in self.__nout or y not in self.__nin:
            raise Exception("Vertices invalid")
        return (x, y) in self.__costs.keys()

    def get_in_degree(self, x):
        """
        This function returns the in degree of a vertex
        :param x: the vertex
        :return: the in degree of the vertex x
        """

        if x not in self.__nin:
            raise Exception("Vertex doesn't exist")

        return len(self.__nin[x])

    def get_out_degree(self, x):
        """
        This function returns the out degree of a vertex
        :param x: the vertex
        :return: the out degree of the vertex x
        """
        if x not in self.__nout:
            raise Exception("Vertex doesn't exist")

        return len(self.__nout[x])

    def parse_outbound_edges(self, x):
        """
        This function returns an iterable of deep-copied vertices
        :param x: the vertex for which to retrieve the iterator
        :return: iterator to a deep-copied list of outbound vertices
        """
        if x not in self.__nout:
            raise Exception("Vertex doesn't exist")
        return deepcopy(self.__nout[x])

    def parse_inbound_edges(self, x):
        """
        This function returns an iterable of deep-copied vertices
        :param x: the vertex for which to retrieve the iterator
        :return: iterator to a deep-copied list of inbound vertices
        """
        if x not in self.__nout:
            raise Exception("Vertex doesn't exist")
        return deepcopy(self.__nin[x])

    def get_cost_of_edge(self, x, y):
        """
        This function returns the cost of the edge from x to y
        :param x: the first vertex
        :param y: the second vertex
        :return: the cost of the edge from x to y
        """

        if (x, y) not in self.__costs:
            raise Exception("Edge doesn't exist")
        return self.__costs[(x, y)]

    def modify_cost_of_edge(self, x, y, z):
        """
        This function modifies the cost of the edge from x to y
        :param x: the first vertex (str)
        :param y: the second vertex (str)
        :param z: the new cost (int)
        """

        if (x, y) not in self.__costs:
            raise Exception("Edge doesn't exist")
        if type(z) != int:
            raise Exception("Cost isn't int")
        self.__costs[(x, y)] = z

    def copy(self):
        """
        This function returns a copy of the current graph
        :return: a Graph copy
        """
        return deepcopy(self)

    def add_vertex(self, x):
        """
        This function adds the vertex x to the graph
        :param x: the vertex to be added (str)
        """

        if not isinstance(x, str):
            raise Exception("Vertex doesn't have the required type")
        if x in self.__nout.keys():
            raise Exception("Vertex already exists")

        self.__nin[x] = []
        self.__nout[x] = []

    def remove_vertex(self, x):
        """
        This function removes the vertex x from the graph
        :param x: the vertex to be removed (str)
        :type x: str
        """

        if x not in self.__nout.keys():
            raise Exception("Vertex doesn't exist")

        for outbound in self.__nout[x]:
            del self.__costs[(x, outbound)]
            self.__nin[outbound].remove(x)
        for inbound in self.__nin[x]:
            del self.__costs[(inbound, x)]
            self.__nout[inbound].remove(x)

        del self.__nout[x]
        del self.__nin[x]

    def add_edge(self, x, y, z):
        """
        This function adds the edge from x to y to the graph
        :param x: the first vertex (str)
        :param y: the second vertex (str)
        :param z: the cost (int)
        """
        if not isinstance(x, str) or not isinstance(y, str) or not isinstance(z, int):
            raise Exception("Arguments do not have the correct types")

        if y not in self.__nin or x not in self.__nout:
            raise Exception("Vertices don't exist")

        if (x, y) in self.__costs:
            raise Exception("Edge already exists")

        self.__nin[y].append(x)
        self.__nout[x].append(y)
        self.__costs[(x, y)] = z

    def remove_edge(self, x, y):
        """
        This function removes the edge from x to y from the graph
        :param x: the first vertex (str)
        :param y: the second vertex (str)
        """

        if (x, y) not in self.__costs:
            raise Exception("Edge doesn't exist")

        self.__nin[y].remove(x)
        self.__nout[x].remove(y)
        del self.__costs[(x, y)]

    def __eq__(self, other):
        """
        This function return True if two graphs are the same, False otherwise
        :param other: the other graph
        :return: True if same graph, False otherwise
        """

        if sorted(self.__nin.keys()) != sorted(other.__nin.keys()) or \
                sorted(self.__nout.keys()) != sorted(other.__nout.keys()):
            return False

        if sorted(self.__costs.keys()) != sorted(other.__costs.keys()):
            return False

        for key in self.__costs.keys():
            if self.__costs[key] != other.__costs[key]:
                return False

        return True


def get_matrix(n):
    mat = []
    for i in range(n):
        col = []
        for j in range(n):
            col.append(infinity)
        mat.append(col)
    return deepcopy(mat)


def get_null_matrix(n):
    mat = []
    for i in range(n):
        col = []
        for j in range(n):
            col.append(None)
        mat.append(col)
    return deepcopy(mat)


def get_cost_matrix(graph):
    mat = get_matrix(len(graph.parse_vertices()))

    for v in graph.parse_vertices():
        for j in graph.parse_outbound_edges(v):
            mat[int(v)][int(j)] = graph.get_cost_of_edge(v, j)

    for v in graph.parse_vertices():
        mat[int(v)][int(v)] = 0

    return deepcopy(mat)


def floyd_warshall_with_path_reconstruction(graph):
    null_matrix = get_null_matrix(len(graph.parse_vertices()))
    dist_matrix = get_matrix(len(graph.parse_vertices()))

    vertices = graph.parse_vertices()
    edges = []
    for vertex in vertices:
        for outbound in graph.parse_outbound_edges(vertex):
            dist_matrix[int(vertex)][int(outbound)] = graph.get_cost_of_edge(vertex, outbound)
            null_matrix[int(vertex)][int(outbound)] = outbound
    for vertex in vertices:
        dist_matrix[int(vertex)][int(vertex)] = 0
        null_matrix[int(vertex)][int(vertex)] = vertex

    for k in range(1, len(vertices)):
        for i in range(1, len(vertices)):
            for j in range(1, len(vertices)):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    null_matrix[i][j] = null_matrix[i][k]

    return null_matrix


def shortest_path(graph, v1, v2):
    nxt = floyd_warshall_with_path_reconstruction(graph)
    if nxt[int(v1)][int(v2)] is None:
        return None
    path = [v1]
    while v1 is not v2:
        v1 = nxt[int(v1)][int(v2)]
        path.append(v1)
    return path


def read_graph(filename):
    """
    This function reads a graph from a file. It supports 2 formats:  .txt and  .modified.txt
    In case of .txt, the file is supposed to look like this:
        - On the first line, the number n of vertices and the number m of edges;
        - On each of the following m lines, three numbers, x, y and c, describing an edge: the origin, the target and
          the cost of that edge.
    In case of .modified.txt, the file is supposed to look like this:
        - On the first line, the number n of vertices and the number m of edges
        - On the second line, a list of the n vertices separated by space
        - On each of the following m lines, three numbers, x, y and c, describing an edge: the origin, the target and
          the cost of that edge.
    :param filename: the file from which to read(name, relative path or absolute path) (str)
    :return: Graph
    """

    if not isinstance(filename, str) or not filename.endswith(".txt"):
        raise Exception("invalid filename")

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
    return Graph(vertices, edges)


def write_graph(filename, graph):
    """
    This function writes a graph to a file.
    It supports 1 format: .modified.txt
    On the first line, the number n of vertices and the number m of edges
    On the second line, a list of the n vertices separated by space
    On each of the following m lines, three numbers, x, y and c, describing an edge:
                the origin, the target and the cost of that edge.
    :param filename: the filename to which to read, MUST end in .modified.txt (str)
    :param graph: the graph to be written
    """

    if not isinstance(filename, str) or not filename.endswith(".modified.txt"):
        raise Exception("invalid filename")

    if not isinstance(graph, Graph):
        raise Exception("Invalid arguments")

    with open(filename, "w") as f:
        vertices = graph.parse_vertices()
        edges = []
        for vertex in vertices:
            for outbound in graph.parse_outbound_edges(vertex):
                edges.append((vertex, outbound, graph.get_cost_of_edge(vertex, outbound)))
        f.write("%d %d\n" % (len(vertices), len(edges)))
        for vertex in vertices:
            f.write("%s " % vertex)
        f.write("\n")
        for edge in edges:
            f.write("%s %s %d\n" % (edge[0], edge[1], edge[2]))


def random_graph(n, m):
    """
    This function creates a random graph with specified number of vertices and edges
    :param n: the number of vertices (int)
    :param m: the number of edges (int)
    :return: a graph with specified parameters
    """

    if not isinstance(n, int) or not isinstance(m, int):
        raise Exception("Arguments have invalid types")

    if n < 0 or m < 0 or m > n * n:
        raise Exception("Bad arguments")

    graph = Graph([str(x) for x in range(0, n)], [])

    possible_edges = []
    for i in range(0, n):
        for j in range(0, n):
            possible_edges.append((i, j))

    random.shuffle(possible_edges)

    for i in range(0, m):
        graph.add_edge(str(possible_edges[i][0]), str(possible_edges[i][1]), random.randint(-10**9, 10**9))

    return graph
