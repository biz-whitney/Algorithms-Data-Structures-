public class LinkedListDeque<T>  {

    /* class to build a node list*/
    private class NodeList {
        private T item;
        private NodeList next;
        private NodeList prev;

        /* the constructor for the node list*/
        private NodeList(T i, NodeList p, NodeList n) {
            prev = p;
            item = i;
            next = n;
        }
    }

    private NodeList sentinelFront;
    private NodeList sentinelBack;
    private int size;

    /*Creates the two sentinel nodes*/
    public LinkedListDeque() {
        sentinelFront = new NodeList(null, null, null);
        sentinelBack = new NodeList(null, sentinelFront, null);
        sentinelFront.next = sentinelBack;
        size = 0;
    }


    /*Adds an item to the front of the list*/
    public void addFirst(T item) {
        NodeList itemsToAdd = new NodeList(item, sentinelFront, sentinelFront.next);
        sentinelFront.next.prev = itemsToAdd;
        sentinelFront.next = itemsToAdd;
        size += 1;
    }

    /*Adds an item to the back of the list*/
    public void addLast(T item) {
        NodeList itemsToAdd = new NodeList(item, sentinelBack.prev, sentinelBack);
        sentinelBack.prev.next = itemsToAdd;
        sentinelBack.prev = itemsToAdd;
        size += 1;
    }

    /* Returns the size of the list*/
    public int size() {
        return size;
    }

    /* Returns whether a list is empty or not*/
    public boolean isEmpty() {
        return size == 0;
    }

    /*Removes the first item in a linked list*/
    public T removeFirst() {
        if (size == 0) {
            return null;
        } else {
            NodeList itemToRemove = new NodeList(sentinelFront.next.item, null, null);
            sentinelFront.next = sentinelFront.next.next;
            sentinelFront.next.prev = sentinelFront;
            size -= 1;
            return itemToRemove.item;
        }
    }

    /*Removes the last item in a linked list*/
    public T removeLast() {
        if (size == 0) {
            return null;
        } else {
            NodeList itemToRemove = new NodeList(sentinelBack.prev.item, null, null);
            sentinelBack.prev = sentinelBack.prev.prev;
            sentinelBack.prev.next = sentinelBack;
            size -= 1;
            return itemToRemove.item;
        }
    }

    /*Gets the index item of a linked list*/
    public T get(int index) {
        NodeList pointer = new NodeList(sentinelFront.next.item, sentinelFront.next.prev,
                sentinelFront.next.next);
        int counter = 0;
        while (counter < index) {
            pointer = pointer.next;
            counter += 1;
        }
        return pointer.item;
    }

    /*Prints the list in order with space in between*/
    public void printDeque() {
        if (size == 0) {
            return;
        }
        NodeList pointer = new NodeList(sentinelFront.next.item, sentinelFront.next.prev,
                sentinelFront.next.next);
        while (pointer.next.item != null) {
            System.out.print(pointer.item + " ");
            pointer = pointer.next;
        }
    }

    /*Gets the index item of a linked list using recursion*/
    public T getRecursive(int index) {
        NodeList pointer = new NodeList(sentinelFront.next.item, sentinelFront.next.prev,
                sentinelFront.next.next);
        return helper(index, pointer);
    }

    /*Helper method for getRecursive that takes in an index and a pointer node*/
    private T helper(int index, NodeList pointer) {
        if (pointer.item == null) {
            return null;
        }
        if (index == 0) {
            return pointer.item;
        } else {
            index -= 1;
            return helper(index, pointer.next);
        }
    }
}
