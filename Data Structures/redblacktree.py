RED = 'red'
BLACK = 'black'


class Node:
    """
    A Node object for BST
    """
    def __init__(self, key, left, right, color):
        """
        Constructor for the class
        @param key: the key
        @param left: left child
        @param color: the color of the node
        @param right: right child
        """
        self.key = key
        self.left = left
        self.right = right
        self.color = color
        self.parent = None

    def __str__(self):
        """
        String representation of the Node class
        @return: representation of the Node class
        """
        return 'Node: {key: '+ str(self.key) + \
               ' left: ' + str(self.left) + \
               ' right: ' + str(self.right) + '}'


nil = Node(None, None, None, BLACK)


def left_rotate(t, x):
    y = x.right
    x.right = y.left
    if y.left != nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == nil:
        t = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
        y.left = x
        x.parent = y


def right_rotate(t, x):
    y = x.left
    x.left = y.right
    if y.right != nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == nil:
        t = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
        y.right = x
        x.parent = y


def rb_insert(t, z):
    y = nil
    x = t
    while x != nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent  = y
    if y == nil:
        t = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = nil
    z.right = nil
    z.color = RED
    rb_insert_fixup(t, z)


def rb_insert_fixup(t, z):
    while z.parent.color == RED:
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == RED:
                z.parent.color = BLACK
                y.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    left_rotate(t, z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                right_rotate(t, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == RED:
                z.parent.color = BLACK
                y.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    left_rotate(t, z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                right_rotate(t, z.parent.parent)
    t.color = BLACK


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

def rb_transplant(t, u, v):
    """
    Substitutes v into the position of u
    @param t: Red Black Tree
    @param u: Red Black Tree node to remove
    @param v: Red Black Tree node to replace v
    """
    if u.parent == nil:
        t = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent


def rb_delete(t, z):
    y = z
    y_original_color = y.color
    if z.left == nil:
        x = z.right
        rb_transplant(t, z, z.right)
    elif z.right == nil:
        x = z.left
        rb_transplant(t, z, z.left)
    else:
        y = tree_minimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.parent == z:
            x.parent = y
        else:
            rb_transplant(t, y, y.right)
            y.right = z.right
            y.right.parent = y
        rb_transplant(t, z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color
    if y_original_color == BLACK:
        rb_delete_fixup(t, x)


def rb_delete_fixup(t, x):
    while x != t and x.color == BLACK:
        if x == x.parent.left:
            w = x.parent.right
            if w.color == RED:
                w.color = BLACK
                x.parent.color = RED
                left_rotate(t, x.parent)
                w = x.parent.right
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.parent
            else:
                if w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    right_rotate(t, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = BLACK
                w.right.color = BLACK
                left_rotate(t, x.parent)
                x = t
        else:
            w = x.parent.left
            if w.color == RED:
                w.color = BLACK
                x.parent.color = RED
                left_rotate(t, x.parent)
                w = x.parent.left
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.parent
            else:
                if w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    right_rotate(t, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = BLACK
                w.right.color = BLACK
                left_rotate(t, x.parent)
                x = t
    x.color = BLACK





nil = Node(None, None, None, "black")
