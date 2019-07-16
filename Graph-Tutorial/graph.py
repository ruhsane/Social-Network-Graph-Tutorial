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

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # check if vertex is already a neighbor
        # if not, add vertex to neighbors and assign weight.
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
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

    def addVertex(self, key):
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

    def getVertex(self, key):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vertList:
            return self.vertList[key]

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        if f not in self.vertList:
        # add it
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].
        f_vert = self.getVertex(f)
        t_vert = self.getVertex(t)

        f_vert.addNeighbor(t_vert, cost)


    def getVertices(self):
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
    g.addVertex("Ruhsane")
    g.addVertex("Cherish")
    g.addVertex("Ryan")
    g.addVertex("Rinni")
    g.addVertex("Vincenzo")
    g.addVertex("Grace")
    g.addVertex("Tim")
    g.addVertex("My dad")
    g.addVertex("My mom")
    g.addVertex("Ariana Grande")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Ruhsane", "Cherish")
    g.addEdge("Ruhsane", "Ryan")
    g.addEdge("Ruhsane", "Vincenzo")
    g.addEdge("Ruhsane", "Rinni")
    g.addEdge("Ruhsane", "Grace")
    g.addEdge("Ruhsane", "Tim")
    g.addEdge("Ruhsane", "My dad")
    g.addEdge("Ruhsane", "My mom")
    g.addEdge("Ruhsane", "Ariana Grande")

    g.addEdge("Ryan", "Ruhsane")
    g.addEdge("Ryan", "Tim")
    g.addEdge("Ryan", "Vincenzo")
    g.addEdge("Ryan", "Cherish")
    g.addEdge("Ryan", "Rinni")

    g.addEdge("Vincenzo", "Ruhsane")
    g.addEdge("Vincenzo", "Tim")
    g.addEdge("Vincenzo", "Ryan")
    g.addEdge("Vincenzo", "Cherish")
    g.addEdge("Vincenzo", "Rinni")

    g.addEdge("Cherish", "Ruhsane")
    g.addEdge("Cherish", "Tim")
    g.addEdge("Cherish", "Ryan")
    g.addEdge("Cherish", "Vincenzo")
    g.addEdge("Cherish", "Rinni")

    g.addEdge("Rinni", "Ruhsane")
    g.addEdge("Rinni", "Tim")
    g.addEdge("Rinni", "Ryan")
    g.addEdge("Rinni", "Vincenzo")
    g.addEdge("Rinni", "Cherish")

    g.addEdge("Rinni", "Ruhsane")
    g.addEdge("Rinni", "Tim")
    g.addEdge("Rinni", "Ryan")
    g.addEdge("Rinni", "Vincenzo")
    g.addEdge("Rinni", "Cherish")

    g.addEdge("Tim", "Ruhsane")
    g.addEdge("Tim", "Tim")
    g.addEdge("Tim", "Ryan")
    g.addEdge("Tim", "Vincenzo")
    g.addEdge("Tim", "Rinni")

    g.addEdge("Grace", "Ruhsane")

    g.addEdge("My dad", "Ruhsane")
    g.addEdge("My dad", "My mom")

    g.addEdge("My mom", "Ruhsane")
    g.addEdge("My mom", "My dad")


    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
