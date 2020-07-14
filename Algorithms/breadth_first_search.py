"""
Implementation of Breath First Search
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

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value and \
               self.color == other.color and \
               self.distance == other.distance


class Queue:
    """
    Queue implementation for BFS algorithm
    """
    def __init__(self):
        self.array = list()

    def is_empty(self):
        """
        Checks if the queue is empty
        @return: true if empty otherwise false
        """
        if len(self.array) == 0:
            return True
        return False

    def enqueue(self, value):
        """
        Adds value into the queue
        @param value: the vale to add
        """
        self.array.append(value)

    def dequeue(self):
        """
        Removes the next item from the queue
        @return: the next value
        """
        return self.array.pop(0)

    def peek(self):
        """
        peek the next item in the queue
        @return: the value
        """
        return self.array[0]


def bfs(g, s):
    """
    Breath First Search Implementation
    @param g: the graph with edges and vertices
    @param s: the starting node
    """
    s.color = GRAY
    s.distance = 0
    queue = Queue()
    queue.enqueue(s)
    while not queue.is_empty():
        cur_node = queue.dequeue()
        for neighbor in g[cur_node.value]:
            if neighbor.color == WHITE:
                neighbor.color = GRAY
                neighbor.distance = cur_node.distance + 1
                neighbor.predecessor = cur_node
                queue.enqueue(neighbor)
            cur_node.color = BLACK


def find_path(g, s, t):
    """
    Prints the path from s to t
    @param g: the graph with edges and vertices
    @param s: the starting vertex
    @param t: the target vertex
    """
    if s == t:
        print(s.value)
    elif t.predecessor is None:
        print("No Path")
    else:
        find_path(g, s, t.predecessor)
        print(t.value)


def main():
    """
    Creates a graph and calls bfs
    @return:
    """
    g = list()
    node_0 = Node(0)
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    g.append([node_1, node_3, node_4])
    g.append([node_0, node_3])
    g.append([node_3, node_4, node_5])
    g.append([node_0, node_1, node_2])
    g.append([node_0, node_2])
    g.append([node_2])
    bfs(g, node_0)
    find_path(g, node_0, node_5)


main()
