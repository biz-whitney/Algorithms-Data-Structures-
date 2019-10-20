public class ArrayDeque<T> {
    private T[] array;
    private int size;
    private int nextFirst;
    private int nextLast;

    /*constructor for the array list*/
    public ArrayDeque() {
        array = (T[]) new Object[8];
        size = 0;
        nextFirst = array.length - 1;
        nextLast = 0;

    }

    /*Returns the size of the array list*/
    public int size() {
        return size;
    }

    /*Returns True if the array list is empty*/
    public boolean isEmpty() {
        return size == 0;
    }

    private int minusOne(int x) {
        return (x - 1 + array.length) % array.length;
    }

    private int plusOne(int x) {
        return (x + 1) % array.length;
    }

    private int firstIndex() {
        return plusOne(nextFirst);
    }

    private int lastIndex() {
        return minusOne(nextLast);
    }

    /*Resizes the array list if the array runs out of space or if there are to0 many empty space*/
    private void resize(double capacity) {
        int newSize = (int) (capacity * array.length);
        T[] copyArray = (T[]) new Object[newSize];
        int sizeOfFirst = array.length - plusOne(nextFirst);
        int sizeOfLast = array.length - sizeOfFirst;
        System.arraycopy(array, nextLast, copyArray, 0, sizeOfFirst);
        System.arraycopy(array, 0, copyArray, sizeOfFirst, sizeOfLast);
        array = copyArray;
        nextFirst = array.length - 1;
        nextLast = size;


    }

    /*Reduces the array list size if there are too many empty space*/
    private void reducesize(double capacity) {
        int newSize = (int) (capacity * array.length);
        T[] copyArray = (T[]) new Object[newSize];
        int pointer = plusOne(nextFirst);
        int i = 0;
        while (pointer != nextLast) {
            copyArray[i] = array[pointer];
            i += 1;
            pointer = plusOne(pointer);
        }
        array = copyArray;
        nextFirst = array.length - 1;
        nextLast = size;

    }

    /*Adds an item to the front of the array list*/
    public void addFirst(T item) {
        if (size == array.length) {
            resize(2.0);
        }
        array[nextFirst] = item;
        nextFirst = minusOne(nextFirst);
        size += 1;
    }

    /*Adds an item to the back of the array list*/
    public void addLast(T item) {
        if (size == array.length) {
            resize(2.0);
        }
        array[nextLast] = item;
        nextLast = plusOne(nextLast);
        size += 1;
    }

    /* Prints the array list in order with space in between*/
    public void printDeque() {
        if (size == 0) {
            return;
        }
        int pointer = firstIndex();
        while (pointer != nextLast) {
            System.out.print(array[pointer] + " ");
            pointer = plusOne(pointer);
        }
    }

    /*Checks if there are too many empty spaces*/
    private boolean checkRatio() {
        final double least = 0.25;
        double ratio = (double) size / (double) array.length;
        return array.length > 16 && ratio < least;
    }

    /*Removes the first item in an array list*/
    public T removeFirst() {
        if (size == 0) {
            return null;
        }
        if (checkRatio()) {
            reducesize(0.5);
        }
        T itemToRemove = array[firstIndex()];
        array[firstIndex()] = null;
        nextFirst = firstIndex();
        size -= 1;
        return itemToRemove;
    }


    /*Removes the last item in an array list*/
    public T removeLast() {
        if (size == 0) {
            return null;
        }
        if (checkRatio()) {
            reducesize(0.5);
        }
        T itemToRemove = array[lastIndex()];
        array[lastIndex()] = null;
        nextLast = lastIndex();
        size -= 1;
        return itemToRemove;
    }

    /* Gets the index item of an array list using iteration */
    public T get(int index) {
        if (index < 0 || index > size) {
            return null;
        }
        return array[(firstIndex() + index) % array.length];
    }
}

