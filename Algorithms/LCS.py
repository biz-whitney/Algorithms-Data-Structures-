# Implementation of Longest common subsequence


def print_matrix(matrix):
    """
    Prints the result matrix after running LCS
    @param matrix: result matrix after running LCS
    """
    row = len(matrix)
    for i in range(row):
        print(matrix[i])


def trace_lcs(X, Y, C, i, j):
    """
    Traces for the LCS
    @param X: Sequence 1
    @param Y: Sequence 2
    @param C: the result matrix from running LCS
    @param i: row index
    @param j: column index
    @return: the longest common subsequence
    """
    if i == 0 or j == 0:
        return ""
    elif X[i - 1] == Y[j - 1]:
        return trace_lcs(X, Y, C, i - 1, j - 1) + X[i - 1]
    else:
        if C[i][j - 1] > C[i - 1][j]:
            return trace_lcs(X, Y, C, i, j - 1)
        else:
            return trace_lcs(X, Y, C, i - 1, j)


def trace_all_lcs(X, Y, C, i, j):
    """
    A set of all possible LCS
    @param X: Sequence 1
    @param Y: Sequence 2
    @param C: the result matrix from running LCS
    @param i: row index
    @param j: column index
    @return: the longest common subsequence
    @return: set of all possible LCS
    """
    if i == 0 or j == 0:
        return set([""])
    elif X[i - 1] == Y[j - 1]:
        return set([Z + X[i - 1] for Z in trace_all_lcs(X, Y, C, i - 1, j - 1)])
    else:
        R = set()
        if C[i][j - 1] >= C[i - 1][j]:
            R.update(trace_all_lcs(X, Y, C, i, j - 1))
        if C[i - 1][j] >= C[i][j - 1]:
            R.update(trace_all_lcs(X, Y, C, i - 1, j))
        return R


def LCS(X, Y):
    """
    Finds the longest common subsequence
    @param X: Sequence 1
    @param Y: Sequence 2
    @return: the longest common subsequence
    """
    m = len(X) + 1
    n = len(Y) + 1
    b = [[0] * n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                b[i][j] = b[i - 1][j - 1] + 1
            elif b[i - 1][j] >= b[i][j - 1]:
                b[i][j] = b[i - 1][j]
            else:
                b[i][j] = b[i][j - 1]
    print(trace_lcs(X, Y, b, m - 1, n - 1))
    print(trace_all_lcs(X, Y, b, m - 1, n - 1))



def main():
    str1 = "10010101"
    str2 = "010110110"
    LCS(str1, str2)


main()
