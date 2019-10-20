import java.util.*;
import java.lang.*;

/*
Implementation of the Needleman-Wunsch algorithm for global sequence alignment

Input:
    Enter first Sequence
    ACAGTACATA
    Enter second Sequence
    GTTATTACCAG
    Enter match score
    2
    Enter mismatch score
    -3
    Enter gap score
    -3

Output:
    -ACAGTA-CATA
     |||||| || |
    GTTATTACCA-G

 */

public class NeedlemanWunsch {
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


    public void alignSequences() {
        initializeMatrix();
        scoreMatrix();
        trackBack();
        System.out.println(align_one);
        System.out.println(lines);
        System.out.println(align_two);
    }

    // initialization of the matrix for the algorithm
    public void initializeMatrix() {
        col = seqTwo.length() + 1;
        row = seqOne.length() + 1;
        matrix = new int[row ][col ];
        for (int i = 0; i < row;  i++) {
            matrix[i][0] = i * gap;
        }
        for (int j = 0; j < col; j++) {
            matrix[0][j] = j * gap;
        }

    }

    // the trace back portion of the algorithm
    public void trackBack() {
        int i = seqOne.length();
        int j = seqTwo.length();
        while (i > 0 || j > 0) {
            if (i > 0 && j > 0 && matrix[i][j] == (matrix[i - 1][j - 1]
                    + Sim(seqOne.charAt(i-1), seqTwo.charAt(j-1)))  ) {
                align_one.insert(0, seqOne.charAt(i -1) );
                align_two.insert(0, seqTwo.charAt(j -1));
                lines.insert(0, "|");
                i--;
                j--;
            }
            else if(i > 0 && matrix[i][j] == matrix[i - 1][j] + gap) {
                align_one.insert(0, seqOne.charAt(i-1) );
                align_two.insert(0, "-");
                lines.insert(0, " ");
                i--;
            }
            else {
                align_one.insert(0, "-");
                align_two.insert(0, seqTwo.charAt(j-1) );
                lines.insert(0, " ");
                j--;
            }
        }

    }

    // The scoring portion of the algorithm
    public void scoreMatrix() {
        for (int i = 1; i < row; i++) {
            char oneChar = seqOne.charAt(i - 1);
            for (int j = 1; j < col; j++) {
                char twoChar = seqTwo.charAt(j - 1);
                int matchSeq = matrix[i-1][j-1] + Sim(oneChar, twoChar);
                int gapOne = matrix[i][j -1] + gap;
                int gapTwo = matrix[i -1][j] + gap;
                matrix[i][j] = Math.max(matchSeq, Math.max(gapOne, gapTwo));
            }
        }
    }

    // checks if two genes are the same
    private int Sim(char one, char two) {
        if (one == two) {
            return match;
        }
        return mismatch;
    }


    public static void main(String[] argv) {
        NeedlemanWunsch NW = new NeedlemanWunsch();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter first Sequence");
        NW.seqOne = scanner.nextLine();
        System.out.println("Enter second Sequence");
        NW.seqTwo = scanner.nextLine();
        System.out.println("Enter match score");
        NW.match  = Integer.parseInt(scanner.next());
        System.out.println("Enter mismatch score");
        NW.mismatch = Integer.parseInt(scanner.next());
        System.out.println("Enter gap score");
        NW.gap = Integer.parseInt(scanner.next());
        NW.alignSequences();
    }
}
