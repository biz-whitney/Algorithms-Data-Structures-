import java.lang.*;
import java.util.*;


/* Implementation of Nussionov Algorithm for predicting secondary folds of RNA structures.

Input:
    Please enter RNA sequence:
    AAAUCCCAGGA

Output:
    AAAUCCCAGGA
    ...((....))

 */

public class NussinovAlgorithm {
    HashMap<Character, Character>  complement;
    String seq;
    int[][] matrix;
    int L;
    int minLoopLength = 4;
    Queue<int[]> queue = new LinkedList<>();
    char[] foldsArray;


    // Finds the secondary fold of the RNA structure
    public void findFold() {
        intitization();
        recursion();
        traceback();
        System.out.println(seq);
        System.out.println(foldsArray);
    }


    // Traces back to find the optimal folds
    public void traceback() {
        int[] itemToAdd = new int[]{1, L -1};
        queue.add(itemToAdd);
        foldsArray = new char[L];
        Arrays.fill(foldsArray, '.');
        while (!(queue.isEmpty())) {
            int[] itemPoped = queue.poll();
            int i = itemPoped[0];
            int j = itemPoped[1];
            if (i >= j) {
                //do nothing;
            }
            else if (computeOPT(i + 1, j) == computeOPT(i, j)) {
                itemToAdd = new int[]{i + 1, j};
                queue.add(itemToAdd);
            }
            else if (computeOPT(i, j - 1) == computeOPT(i, j)) {
                itemToAdd = new int[]{i, j - 1};
                queue.add(itemToAdd);
            }
            else if (computeOPT(i + 1, j - 1) + getComplement(i, j) == computeOPT(i, j)) {
                foldsArray[i] = '(';
                foldsArray[j] = ')';
                itemToAdd = new int[]{i + 1, j - 1};
                queue.add(itemToAdd);
            }
            else {
                for (int k = i + 1; k < j; k++) {
                    if (computeOPT(i, k) + computeOPT(k + 1, j) == computeOPT(i, j)) {
                        itemToAdd = new int[]{k + 1, j};
                        queue.add(itemToAdd);
                        itemToAdd = new int[]{i, k};
                        queue.add(itemToAdd);
                    }
                }
            }
        }
    }


    // Optional method to print out the matrix after the recursion
    public void printMatrix() {
        for (int i = 0; i < L; i++) {
            System.out.println();
            for (int j =0; j < L; j++) {
                System.out.print(matrix[i][j]);
            }
        }
    }


    // Recursion portion of the algorithm to find the optimal folds
    public void recursion() {
        for (int k = minLoopLength; k < L; k++) {
            for (int i = 0; i < L - k; i++) {
                int j = i + k;
                matrix[i][j] = computeOPT(i, j);
            }
        }
    }


    // Computes the optimal folds for each position
    public int computeOPT(int i, int j) {
        if (i >= j - minLoopLength) {
            return 0 ;
        }
        else {
            ArrayList<Integer> array = new ArrayList<>();
            for(int k = i; k < j; k++ ) {
                array.add(computeOPT(i, k) + computeOPT(k + 1, 1) );
            }
            int opFourFive = Collections.max(array);
            int opOne = computeOPT(i + 1, j);
            int opTwo = computeOPT(i, j - 1);
            int opThree = computeOPT(i + 1, j - 1) + getComplement(i, j);
            int result = Math.max(opOne, Math.max(opTwo, Math.max(opThree, opFourFive )));
            return result;
        }
    }


    // Initializes matrix
    public void intitization() {
        L = seq.length();
        matrix = new int[L][L];
        for (int i = 2; i < L; i++) {
            matrix[i][i - 1] = 0;
        }
        for (int i = 1; i < L; i++) {
            matrix[i][i] = 0;
        }
    }


    // Checks for complements
    public int getComplement(int i, int j) {
        if (complement.get(seq.charAt(i)) == seq.charAt(j)) {
            return 1;
        }
        return 0;
    }


    // Creates the complement set which is used to check complements
    public void setComplement() {
        complement = new HashMap<>();
        char[] key = new char[]{'A', 'U', 'C', 'G'};
        char[] value = new char[]{'U', 'A', 'G', 'C'};
        for (int i = 0; i < 4; i++) {
            complement.put(key[i], value[i]);
        }
    }


    public static void main(String[] argv) {
        Scanner scanner = new Scanner(System.in);
        NussinovAlgorithm NA = new NussinovAlgorithm();
        NA.setComplement();
        System.out.println("Please enter RNA sequence:");
        NA.seq = scanner.nextLine();
        NA.findFold();
    }
}
