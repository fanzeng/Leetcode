class Solution {
    public long maxMatrixSum(int[][] matrix) {
        return sumMatrixAbs(matrix);
    }
    private long sumMatrixAbs(int[][] matrix) {
        long sum = 0;
        int minPos = 100000;
        int maxNeg = -100000;
        boolean even = true;
        boolean existsZero = false;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] > 0) {
                    sum += matrix[i][j];
                    if (matrix[i][j] < minPos) minPos = matrix[i][j];
                } else if (matrix[i][j] < 0) {
                    sum -= matrix[i][j];
                    if (matrix[i][j] > maxNeg) maxNeg = matrix[i][j];
                    even = !even;
                }
                if (matrix[i][j] == 0) existsZero = true;
            }
        }
        int remain = -maxNeg > minPos ? -minPos : maxNeg;
        return sum + (even || existsZero ? 0 : 2*remain);
    }
}
