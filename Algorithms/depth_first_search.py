"""
Implementation of Depth First Search
"""

BLACK = "Black"
WHITE = "White"
GRAY = "Gray"


class Node:
    """
    Node class to represent graph vertices
    """
    def __init__(self, value):
        self.value = value
        self.color = WHITE
        self.predecessor = None
        self.distance = None
        self.f = None
        self.neighbors = list()

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value and \
               self.color == other.color and \
               self.distance == other.distance

    def __str__(self):
        return "Value: " + str(self.value) + \
               "\t Distance: " + str(self.distance) + \
               "\t f:" + str(self.f)

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def remove_neighbor(self, node):
        self.neighbors.remove(node)


def dfs(adjList):
    """
    Runs DFS and checks if each node is visited
    @param adjList: Adjacency List of the graph
    """
    time = -1
    for node in adjList:
        if node.color == WHITE:
            dfs_visit( node, time)


def dfs_visit(node, time):
    """
    Recursively visits each neighbor of the node
    @param node: the current node to explore
    @param time: the time the node is visited
    """
    time += 1
    node.distance = time
    node.color = GRAY
    for neighbor in node.neighbors:
        if neighbor.color == WHITE:
            neighbor.predecessor = node
            dfs_visit(neighbor, time)
    node.color = BLACK
    time += 1
    node.f = time



def main():
    """
    Creates a graph and calls DFS
    @return:
    """
    adjList = list()
    node_0 = Node(0)
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_0.neighbors = [node_1, node_3, node_4]
    node_1.neighbors = [node_0, node_3]
    node_2.neighbors = [node_3, node_4, node_5]
    node_3.neighbors = [node_0, node_1, node_2]
    node_4.neighbors = [node_0, node_2]
    node_5.neighbors = [node_2]
    adjList = [node_0, node_1, node_2, node_3, node_4, node_5]
    dfs(adjList)
    for node in adjList:
        print(node)


main()


