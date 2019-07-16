#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # check if vertex is already a neighbor
        # if not, add vertex to neighbors and assign weight.
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        # TODO return the weight of the edge from this
        # vertext to the given vertex.
        if vertex in self.neighbors:
            return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # increment the number of vertices
        self.numVertices += 1
        # create a new vertex
        vert = Vertex(key)
        # add the new vertex to the vertex list
        self.vertList[key] = vert
        # return the new vertex
        return vert

    def get_vertex(self, key):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vertList:
            return self.vertList[key]

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        if f not in self.vertList:
        # add it
            self.add_vertex(f)
        if t not in self.vertList:
            self.add_vertex(t)

        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].
        f_vert = self.get_vertex(f)
        t_vert = self.get_vertex(t)

        f_vert.add_neighbor(t_vert, cost)


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Ruhsane")
    g.add_vertex("Cherish")
    g.add_vertex("Ryan")
    g.add_vertex("Rinni")
    g.add_vertex("Vincenzo")
    g.add_vertex("Grace")
    g.add_vertex("Tim")
    g.add_vertex("My dad")
    g.add_vertex("My mom")
    g.add_vertex("Ariana Grande")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Ruhsane", "Cherish")
    g.add_edge("Ruhsane", "Ryan")
    g.add_edge("Ruhsane", "Vincenzo")
    g.add_edge("Ruhsane", "Rinni")
    g.add_edge("Ruhsane", "Grace")
    g.add_edge("Ruhsane", "Tim")
    g.add_edge("Ruhsane", "My dad")
    g.add_edge("Ruhsane", "My mom")
    g.add_edge("Ruhsane", "Ariana Grande")

    g.add_edge("Ryan", "Ruhsane")
    g.add_edge("Ryan", "Tim")
    g.add_edge("Ryan", "Vincenzo")
    g.add_edge("Ryan", "Cherish")
    g.add_edge("Ryan", "Rinni")

    g.add_edge("Vincenzo", "Ruhsane")
    g.add_edge("Vincenzo", "Tim")
    g.add_edge("Vincenzo", "Ryan")
    g.add_edge("Vincenzo", "Cherish")
    g.add_edge("Vincenzo", "Rinni")

    g.add_edge("Cherish", "Ruhsane")
    g.add_edge("Cherish", "Tim")
    g.add_edge("Cherish", "Ryan")
    g.add_edge("Cherish", "Vincenzo")
    g.add_edge("Cherish", "Rinni")

    g.add_edge("Rinni", "Ruhsane")
    g.add_edge("Rinni", "Tim")
    g.add_edge("Rinni", "Ryan")
    g.add_edge("Rinni", "Vincenzo")
    g.add_edge("Rinni", "Cherish")

    g.add_edge("Rinni", "Ruhsane")
    g.add_edge("Rinni", "Tim")
    g.add_edge("Rinni", "Ryan")
    g.add_edge("Rinni", "Vincenzo")
    g.add_edge("Rinni", "Cherish")

    g.add_edge("Tim", "Ruhsane")
    g.add_edge("Tim", "Tim")
    g.add_edge("Tim", "Ryan")
    g.add_edge("Tim", "Vincenzo")
    g.add_edge("Tim", "Rinni")

    g.add_edge("Grace", "Ruhsane")

    g.add_edge("My dad", "Ruhsane")
    g.add_edge("My dad", "My mom")

    g.add_edge("My mom", "Ruhsane")
    g.add_edge("My mom", "My dad")


    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
