import java.util.Arrays;

class Solution {
    public int countSquares(int[][] matrix) {
        if (matrix.length == 0) return 0;
        // Stores number of all-one square submatrices with top-left at memoi[r][c]
        int[][] memoi = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < memoi.length; i++) {
            Arrays.fill(memoi[i], -1);
        }
        int res = 0;
        for (int i = 0; i < memoi.length; i++) {
            for (int j = 0; j < memoi[i].length; j++) {
                res += dp(i, j, matrix, memoi);
            }
        }
        return res;
    }
    int dp(int r, int c, int[][] matrix, int[][]memoi) {
        // Handle out of bound
        if (r >= matrix.length || c >= matrix[0].length) {
            return 0;
        }
        if (memoi[r][c] >= 0) return memoi[r][c];
        if (matrix[r][c] == 0) {
            // If top-left is 0, there is no all-one submatrix starting here
            memoi[r][c] = 0;
            return 0;
        }
        // Out of bound will be handled within recursive call
        int down = dp(r+1, c, matrix, memoi);
        int right = dp(r, c+1, matrix, memoi);
        int diag = dp(r+1, c+1, matrix, memoi);
        // If matrix[r][c] is 1, then we have at least 1,
        // plus the minimum of results of down, right and diag.
        // Note the matrix has to be square,
        // So there is a 2x2 all-one iff all 3 results are 1 (all single-element matrix),
        // and so on so forth
        int res = 1 + Math.min(down, Math.min(right, diag));
        memoi[r][c] = res;
        return res;
    }
}
