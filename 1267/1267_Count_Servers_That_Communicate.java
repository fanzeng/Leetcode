class Solution {
    public int countServers(int[][] grid) {
        int totalCount = 0;
        int[] rowCount = new int[grid.length];
        int[] colCount = new int[grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    totalCount++;
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }
        int alone = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    if (rowCount[i] == 1 && colCount[j] == 1) alone++;
                }
            }
        }
        return totalCount - alone;
    }
}
