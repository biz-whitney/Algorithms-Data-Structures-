
class Node:
    """
    A Node object for BST
    """
    def __init__(self, key, left, right):
        """
        Constructor for the class
        @param key: the key
        @param left: left child
        @param right: right child
        """
        self.key = key
        self.left = left
        self.right = right
        self.parent = None

    def __str__(self):
        """
        String representation of the Node class
        @return: representation of the Node class
        """
        return 'Node: {key: ' + str(self.key) + \
               ' left: ' + str(self.left) + \
               ' right: ' + str(self.right) + '}'


def inorder_traversal(t):
    """
    In order traversal
    @param t: the tree to traverse
    """
    if t is not None:
        inorder_traversal(t.left)
        print(t.key)
        inorder_traversal(t.right)


def preord_traversal(t):
    """
    Pre order traversal
    @param t: the tree to traverse
    """
    if t is not None:
        print(t.key)
        preord_traversal(t.left)
        preord_traversal(t.right)


def postorder_traversal(t):
    """
    Post order traversal
    @param t: the tree to traverse
    """
    if t is not None:
        preord_traversal(t.left)
        preord_traversal(t.right)
        print(t.key)


def tree_search(t, k):
    """
    Search for k in Binary Search Tree
    @param t: the binary search tree
    @param k: item to search for
    @return: the node containing k otherwise None
    """
    if t is None or t.key == k:
        return t
    if k < t.key:
        return tree_search(t.left, k)
    else:
        return tree_search(t.right, k)


def tree_minimum(t):
    """
    Finds the max key
    @param t: bst tree to search
    @return: the node containing the min key
    """
    if t.left is None:
        return t
    return tree_minimum(t.left)


def tree_maximum(t):
    """
    Finds the max key
    @param t: bst tree to search
    @return: the node containing the max key
    """
    if t.right is None:
        return t
    return tree_maximum(t.right)


def tree_successor(t):
    """
    finds the successor node
    @param t: bst tree to search
    @return: the successor node
    """
    if t.right is not None:
        return tree_minimum(t.right)
    y = t.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


def tree_predecessor(t):
    """
     finds the predecessor node
     @param t: bst tree to search
     @return: the predecessor node
     """
    if t.left is not None:
        return tree_maximum(t.left)
    y = t.parent
    while y is not None and x == y.left:
        x = y
        y = y.parent
    return y


def tree_insert(t, value):
    """
    Inserts value into the BST
    @param t: BST to insert value into
    @param value: the item to insert into t
    """
    z = Node(value, None, None)
    if t is None:
        t = z
    y = None
    x = t
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        t = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def transplant(t, u, v):
    """
    Substitutes v into the position of u
    @param t: BST
    @param u: BST node to remove
    @param v: BST node to replace v
    """
    if u.parent is None:
        t = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v is not None:
        v.parent = u.parent


def tree_delete(t, z):
    """
    Deletes a node from BST
    @param t: BST to delete node from
    @param z: the node to delete from the BST
    """
    if z.left is None:
        transplant(t, z, z.right)
    elif z.right is None:
        transplant(t, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.parent != z:
            transplant(t, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(t, z, y)
        y.left = z.left
        y.left.parent = y


def height(t):
    """
    Finds the height for a BST
    @param t: the BST
    @return: the height of the BST
    """
    if t.left is None and t.right is None:
        return 1
    elif t.left is None:
        return height(t.right) + 1
    elif t.right is None:
        return height(t.left) + 1
    else:
        return max(height(t.left), height(t.right)) + 1


def bst_sort(array):
    t = Node(array[0], None, None)
    for i in range(1, len(array)):
        tree_insert(t, array[i])
    inorder_traversal(t)


# tree_insert(tree, 4)
# tree_insert(tree, 7)
# tree_insert(tree, 15)
# tree_insert(tree, 11)
# tree_insert(tree, 12)
# postorder_traversal(tree)
# inorder_traversal(tree)
# preord_traversal(tree)
# tree_delete(tree, tree_predecessor(tree))
# print(height(tree))
# inorder_traversal(tree)
lst = [21, 4, 5, 7, 26, 25, 20, 16, 90]
bst_sort(lst)
