class Solution {
    public long gridGame(int[][] grid) {
        long tSumTot = 0;
        for (int i = 0; i < grid[0].length; i++) {
            tSumTot += grid[0][i];
        }
        long tSum = 0;
        long bSum = 0;
        long minScore = tSumTot - grid[0][0];
        // For each i, assume 1st robot moves down at the ith column,
        // compare 2nd robot score of the top path and the bottom path. 
        for (int i = 0; i < grid[0].length; i++) {
            tSum += grid[0][i];
            bSum += i > 0 ? grid[1][i-1] : 0;
            long score = tSumTot - tSum > bSum ? tSumTot - tSum : bSum;
            if (score < minScore) minScore = score;
        }
        return minScore;
    }
}
