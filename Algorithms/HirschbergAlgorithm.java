import java.util.*;
import java.lang.*;

/*
Implementation of the Hirschberg Algorithm to find the finds the optimal
sequence alignment between two strings. Takes O(mn) times and O(min{m,n})
space to find the optimal alignment.

Input:
    Enter first sequence:
    ACTACGCA
    Enter second sequence:
    TATGC
    Enter score for match:
    2
    Enter score for mismatch:
    -1
    Enter score for gaps:
    -2

output:
    ACTACGCA
      || ||
    --TATGC-
 */



public class HirschbergAlgorithm {
    int InsDels;
    int MisMatch;
    int Match;


    // Does the divide and conquer portion of the algorithm
    public String[] hirschberg(String X, String Y) {
        String[] result = new String[3];
        Needleman_Wunsch NW = new Needleman_Wunsch(Match, MisMatch, InsDels);
        String align_one = "";
        String align_two = "";
        String lines = "";
        if (X.length() == 0) {
            for (int i = 0; i < Y.length(); i++) {
                align_one = align_one + "-";
                lines = lines + " ";
                align_two = align_two + Y.charAt(i);
            }
        }
        else if ( Y.length() == 0) {
            for (int i = 0; i < X.length(); i++) {
                align_one = align_one + X.charAt(i);
                lines = lines + " ";
                align_two = align_two + "-";
            }
        }
        else if (X.length() == 1 || Y.length() == 1) {
            String[] nwResult = NW.alignSequences(X, Y);
            align_one = align_one + nwResult[0];
            lines = lines + nwResult[1];
            align_two = align_two + nwResult[2];
        }
        else {
            int xLen = X.length();
            int xMid = Math.floorDiv(xLen,2);
            int yLen = Y.length();

            String Ytemp = new StringBuilder(Y).reverse().toString();
            String Xrev = new StringBuilder(X.substring(xMid, xLen)).reverse().toString();

            int[] scoreL = NWScore(X.substring(0, xMid), Y);
            int[] scoreR = NWScore(Xrev, Ytemp);

            scoreR =reverseArray(scoreR);
            int yMid = argMax(scoreL, scoreR);

            String[] firstHalf = hirschberg(X.substring(0, xMid),Y.substring(0, yMid));
            String[] secondHalf = hirschberg(X.substring(xMid, xLen),Y.substring(yMid, yLen));
            result[0] = firstHalf[0] + secondHalf[0];
            result[1] = firstHalf[1] + secondHalf[1];
            result[2] = firstHalf[2] + secondHalf[2];
            return result;
        }
        result[0] = align_one;
        result[1] = lines;
        result[2] = align_two;
        return result;
    }


    // Finds the index with the highest score for an alignment
    public int argMax(int[] left, int[] right) {
        int index = 0;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < left.length; i++) {
            int val = left[i] + right[i];
            if (val > max) {
                index = i;
                max = val;
            }
        }
        return index;
    }


    // Reverses an int[] array
    public int[] reverseArray(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        int j = n;
        for(int i = 0; i < n; i++) {
            result[j - 1] = arr[i];
            j --;
        }
        return result;
    }


    // Returns the last line of the Needleman-Wunsch score matrix
    public int[] NWScore(String X, String Y) {
        int xLength = X.length() + 1;
        int yLength = Y.length() + 1;
        int[][] score = new int[2][yLength];
        int[] lastLine = new int[yLength];
        score[0][0] = 0;
        for (int j = 1; j < yLength; j++) {
            score[0][j] = score[0][j - 1] + InsDels;
        }
        for (int i = 1; i < xLength; i++) {
            score[1][0] = score[0][0] + InsDels;
            for (int j = 1; j < yLength; j++ ) {
                int scoreSub = score[0][j - 1] + Sim(X.charAt(i - 1), Y.charAt(j -1));
                int scoreDel = score[0][j] + InsDels;
                int scoreIns = score[1][j -1] + InsDels;
                score[1][j] = Math.max(scoreIns, Math.max(scoreDel, scoreSub));
            }
            System.arraycopy(score[1], 0, score[0], 0, yLength);
        }
        System.arraycopy(score[1], 0, lastLine, 0, yLength);
        return lastLine;
    }


    // checks if two characters match
    private int Sim(char one, char two) {
        if (one == two) {
            return Match;
        }
        return MisMatch;
    }


    private class Needleman_Wunsch {
        String seqOne;
        String seqTwo;
        int match;
        int mismatch;
        int gap;
        int matrix[][];
        int row;
        int col;
        StringBuffer align_one = new StringBuffer("");
        StringBuffer align_two = new StringBuffer("");
        StringBuffer lines = new StringBuffer("");

        // Constructor for the class
        public Needleman_Wunsch(int match, int mismatch, int gap) {
            this.match = match;
            this.mismatch = mismatch;
            this.gap = gap;
        }

        public String[] alignSequences(String X, String Y) {
            seqOne = X;
            seqTwo = Y;
            initializeMatrix();
            scoreMatrix();
            trackBack();
            String[] result = new String[3];
            result[0] = align_one.toString();
            result[1] = lines.toString();
            result[2] = align_two.toString();
            return result;
        }

        // initialization of the matrix for the algorithm
        public void initializeMatrix() {
            col = seqTwo.length() + 1;
            row = seqOne.length() + 1;
            matrix = new int[row][col];
            for (int i = 0; i < row; i++) {
                matrix[i][0] = i * gap;
            }
            for (int j = 0; j < col; j++) {
                matrix[0][j] = j * gap;
            }

        }


        // The scoring portion of the algorithm
        public void scoreMatrix() {
            for (int i = 1; i < row; i++) {
                char oneChar = seqOne.charAt(i - 1);
                for (int j = 1; j < col; j++) {
                    char twoChar = seqTwo.charAt(j - 1);
                    int matchSeq = matrix[i - 1][j - 1] + Sim(oneChar, twoChar);
                    int gapOne = matrix[i][j - 1] + gap;
                    int gapTwo = matrix[i - 1][j] + gap;
                    matrix[i][j] = Math.max(matchSeq, Math.max(gapOne, gapTwo));
                }
            }
        }


        // the trace back portion of the algorithm
        public void trackBack() {
            int i = seqOne.length();
            int j = seqTwo.length();
            while (i > 0 || j > 0) {
                if (i > 0 && j > 0 && matrix[i][j] == (matrix[i - 1][j - 1]
                        + Sim(seqOne.charAt(i - 1), seqTwo.charAt(j - 1)))) {
                    align_one.insert(0, seqOne.charAt(i - 1));
                    align_two.insert(0, seqTwo.charAt(j - 1));
                    if (seqOne.charAt(i - 1) == seqTwo.charAt(j - 1)) {
                        lines.insert(0, "|");
                    } else {
                        lines.insert(0, " ");
                    }
                    i--;
                    j--;
                } else if (i > 0 && matrix[i][j] == matrix[i - 1][j] + gap) {
                    align_one.insert(0, seqOne.charAt(i - 1));
                    align_two.insert(0, "-");
                    lines.insert(0, " ");
                    i--;
                } else {
                    align_one.insert(0, "-");
                    align_two.insert(0, seqTwo.charAt(j - 1));
                    lines.insert(0, " ");
                    j--;
                }
            }
        }
    }

    public static void main(String[] argv) {
        HirschbergAlgorithm HA = new HirschbergAlgorithm();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter first sequence: ");
        String seqOne = scanner.nextLine();
        System.out.println("Enter second sequence: ");
        String seqTwo = scanner.nextLine();
        System.out.println("Enter score for match: ");
        HA.Match = Integer.parseInt(scanner.nextLine());
        System.out.println("Enter score for mismatch: ");
        HA.MisMatch = Integer.parseInt(scanner.nextLine());
        System.out.println("Enter score for gaps: ");
        HA.InsDels = Integer.parseInt(scanner.nextLine());
        String[] result = HA.hirschberg(seqOne, seqTwo);
        System.out.println(result[0]);
        System.out.println(result[1]);
        System.out.println(result[2]);
    }
}
