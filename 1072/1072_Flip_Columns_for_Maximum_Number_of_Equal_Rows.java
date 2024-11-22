class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        return dp(matrix, 0);
    }
    private int dp(int[][] m, int r) {
        // For each row, we either give up or not give up.
        // If not give up, we either flip all 0 to 1 or all 1 to 0.
        // Whatever we choose to do, we have constraint for the subsequent rows.

        // Result of discarding the row.
        int giveUp;
        if (r == m.length-1) {
            giveUp = 0;
        } else {
            giveUp = dp(m, r+1);
        } 
        // Result of keeping the row as all 0.
        int zero = 1 + check(m, r+1, m[r]);
        int[] flipped = new int[m[0].length]; // Flipped cols. 0 - not flipped, 1 - flipped.
        for (int j = 0; j < m[0].length; j++) {
            flipped[j] = 1 - m[r][j];
        }
        // Result of keeping the row as all 1.
        int one = 1 + check(m, r+1, flipped);
        return Math.max(zero, Math.max(giveUp, one));
    }

    // Given flipped cols, return "number of equal rows"
    private int check(int[][] m, int r, int[] flipped) {
        if (r == m.length) return 0;
        int rest;
        if (r == m.length-1) {
            rest = 0;
        } else {
            rest = check(m, r+1, flipped);
        }
        boolean ok = true;
        int e = m[r][0];
        if (flipped[0] == 1) e = 1 - e;
        for (int j = 1; j < flipped.length; j++) {
            int v = m[r][j];
            if (flipped[j] == 1) v = 1 - v;
            if (v != e) {
                ok = false;
                break;
            }
        }
        return ok ? rest+1 : rest;
    }
}
