class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        if (matrix.length == 1) return 1;
        int[] visited = new int[matrix.length];
        int res = 0;
        for (int i = 0; i < matrix.length; i++) {
            if (visited[i] > 0) continue;
            int count = 1;
            for (int j = i+1; j < matrix.length; j++) {
                if (isSameOrComplement(matrix[i], matrix[j])) {
                    count++;
                    visited[j] = 1;
                }
            }
            if (count > res) res = count;
            if (res >= matrix.length - i - 1) break;
        }
        return res;
    }
    private boolean isSameOrComplement(int[] a, int[] b) {
        boolean isSame = true;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                isSame = false;
                break;
            }
        }
        boolean isComplement = true;
        for (int i = 0; i < a.length; i++) {
            if (a[i] == b[i]) {
                isComplement = false;
                break;
            }
        }
        return isSame || isComplement;
    }
}
