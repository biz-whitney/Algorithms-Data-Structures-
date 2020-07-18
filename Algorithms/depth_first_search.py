"""
Implementation of Depth First Search
"""

BLACK = "Black"
WHITE = "White"
GRAY = "Gray"

global time
time = 0


class Node:
    """
    Node class to represent graph vertices
    """

    def __init__(self, value):
        self.value = value
        self.color = WHITE
        self.predecessor = None
        self.d = None
        self.f = None
        self.visited = False
        self.neighbors = list()
        self.reversedNeighbors = list()

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value and \
               self.color == other.color and \
               self.d == other.distance

    def __str__(self):
        return "Value: " + str(self.value) + \
               "\t Distance: " + str(self.d) + \
               "\t f:" + str(self.f) + \
               "\t predecessor: " + str(self.get_pred())

    def get_pred(self):
        if self.predecessor is None:
            return None
        return self.predecessor.value

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def remove_neighbor(self, node):
        self.neighbors.remove(node)


def dfs(adjList):
    """
    Runs DFS and checks if each node is visited
    @param adjList: Adjacency List of the graph
    """
    global time
    time = 0
    for node in adjList:
        if node.color == WHITE:
            dfs_visit(node)


def dfs_visit(node):
    """
    Recursively visits each neighbor of the node
    @param node: the current node to explore
    """
    global time
    time += 1
    node.d = time
    node.color = GRAY
    for neighbor in node.neighbors:
        if neighbor.color == WHITE:
            neighbor.predecessor = node
            dfs_visit(neighbor)
    node.color = BLACK
    time += 1
    node.f = time


def topological_sort(adjList):
    """
    Sorts the vertex in the graph
    @param adjList: Adjacency List of the graph
    """
    global time
    time = 0
    result = list()
    for node in adjList:
        if node.color == WHITE:
            topological_visit(node, result)
    for item in result:
        print(item)


def topological_visit(node, result):
    """
    Recursively visits each neighbor of the node
    @param node: the current node to explore
    @param result: list with the nodes ordered
    """
    global time
    time += 1
    node.d = time
    node.color = GRAY
    for neighbor in node.neighbors:
        if neighbor.color == WHITE:
            neighbor.predecessor = node
            topological_visit(neighbor, result)
    node.color = BLACK
    time += 1
    node.f = time
    result.insert(0, node)


def strongly_connected_components(adjList):
    """
    Finds the strongly connected components of a graph
    @param adjList: Adjacency List of the graph
    """
    dfs(adjList)
    for node in adjList:
        for neighbor in node.neighbors:
            neighbor.reversedNeighbors.append(node)
    for node in adjList:
        node.neighbors = node.reversedNeighbors
    adjList = sorted(adjList, key=lambda x: x.f, reverse=True)
    for node in adjList:
        if not node.visited:
            result = list()
            scc_helper(node, result)
            print(result)


def scc_helper(node, result):
    """
    Helper function for strongly connected components
    @param node: node to start exploring
    @param result: list of the connected components to current node
    """
    node.visited = True
    for neighbor in node.neighbors:
        if not neighbor.visited:
            scc_helper(neighbor, result)
    result.append(node.value)


def main():
    """
    Creates a graph and calls DFS
    @return:
    """
    print("####### DFS #######")
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
    print("\n\n####### Topological Sort #######")
    undershorts = Node("undershorts")
    pants = Node("pants")
    belt = Node("belt")
    shirt = Node("shirt")
    tie = Node("tie")
    jacket = Node("jacket")
    shoes = Node("shoes")
    socks = Node("socks")
    watch = Node("watch")
    undershorts.neighbors = [pants, shoes]
    pants.neighbors = [belt, shoes]
    belt.neighbors = [jacket]
    shirt.neighbors = [belt, tie]
    tie.neighbors = [jacket]
    socks.neighbors = [shoes]
    adjList = [shirt, tie, jacket, belt, watch, undershorts, pants, shoes, socks]
    topological_sort(adjList)
    print("\n\n####### Strongly Connected Components #######")
    node_a = Node("a")
    node_b = Node("b")
    node_c = Node("c")
    node_d = Node("d")
    node_e = Node("e")
    node_f = Node("f")
    node_g = Node("g")
    node_h = Node("h")
    node_a.neighbors = [node_b]
    node_b.neighbors = [node_c, node_e, node_f]
    node_c.neighbors = [node_d, node_g]
    node_d.neighbors = [node_c, node_h]
    node_e.neighbors = [node_a, node_f]
    node_f.neighbors = [node_g]
    node_g.neighbors = [node_f, node_h]
    node_h.neighbors = [node_h]
    adjList = [node_a, node_b, node_c, node_d, node_e, node_f, node_g, node_h]
    strongly_connected_components(adjList)


main()
